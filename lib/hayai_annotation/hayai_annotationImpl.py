# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import uuid
import shutil
import subprocess
import time

from KBaseReport.KBaseReportClient import KBaseReport
from GenomeFileUtil.GenomeFileUtilClient import GenomeFileUtil
from DataFileUtil.DataFileUtilClient import DataFileUtil
from Workspace.WorkspaceClient import Workspace as workspaceService
#END_HEADER


class hayai_annotation:
    '''
    Module Name:
    hayai_annotation

    Module Description:
    A KBase module: hayai_annotation
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER

    def log(self,message, prefix_newline=False):
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))
        print(('\n' if prefix_newline else '') + time_str + ': ' + message)

    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR

        self.workspaceURL = config['workspace-url']
        self.token = os.environ['KB_AUTH_TOKEN']
        self.scratch = os.path.abspath(config['scratch'])
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.dfu = DataFileUtil(self.callback_url)
        self.gfu = GenomeFileUtil(self.callback_url)

        #END_CONSTRUCTOR
        pass


    def annotate_plant_genome(self, ctx, input):
        """
        Here we define an actual function.
        :param input: instance of type "AnnotatePlantGenomeParams" (Here we
           define the parameters that are passed from the UI The same
           parameters need to be defined in ui/narrative/methods/) ->
           structure: parameter "input_ws" of String, parameter
           "input_genome" of String, parameter "output_genome" of String,
           parameter "alignment_type" of String, parameter "organism_type" of
           String, parameter "max_hits_per_query" of Long, parameter
           "max_seq_id" of Double, parameter "max_e_value" of Double,
           parameter "query_coverage" of Double, parameter "target_coverage"
           of Double
        :returns: instance of type "AnnotatePlantGenomeResults" (Here we define
           the output, which, for the purposes of the UI, will always be a
           report. The contents of the report are shown, in HTML, in the
           output widget.) -> structure: parameter "report_name" of String,
           parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN hayai_annotation

        output = dict()

        # Retrieve input genome object
        self.log("Fetching plant genome: "+input['input_ws']+'/'+input['input_genome'])
        plant_genome = self.dfu.get_objects({'object_refs': [input['input_ws']+'/'+input['input_genome']]})['data'][0]

        # Collecting sequences
        self.log("Collecting sequences")
        sequences_dict=dict()
        for ftr in plant_genome['data']['features']:
            sequences_dict[ftr['id']]=ftr['protein_translation']

        if(len(sequences_dict)==0):
            raise Exception("The genome does not contain any protein sequences!")

        # Create random directory in scratch for storing new fasta file
        uuid_string = str(uuid.uuid4())
        fasta_file_path=os.path.join(self.scratch,uuid_string)
        os.mkdir(fasta_file_path)

        # Printing sequences to file
        self.log("Printing protein sequences to file")

        temp_genome_name = input['input_genome']
        # The fasta file could have a random name to avoid _any_ clashes
        # temp_genome_name = str(uuid.uuid4())
        fasta_file = os.path.join(fasta_file_path,temp_genome_name+".fa")
        with open(fasta_file,'w') as fasta_handle:

            #Code plagarized from https://github.com/biopython/biopython/blob/master/Bio/SeqIO/FastaIO.py

            for seq_id in sequences_dict:
                fasta_handle.write(">"+seq_id+"\n")
                for i in range(0, len(sequences_dict[seq_id]), 80):
                    fasta_handle.write(sequences_dict[seq_id][i:i+80]+"\n")
                    
        # File where results will be saved
        annotation_file = os.path.join(fasta_file_path,"annotation.txt")

        # Building and running command that runs on fasta file
        command = "echo `head -n1 "+fasta_file+" | cut -f1 | perl -lne 'print substr($_,1)'`\"\tHello World\" > "+annotation_file

        self.log("Running command: "+command)
        pipe = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

        command_output_file='Command_Output.txt'
        cof_fh=open(os.path.join(fasta_file_path,command_output_file),'w')

        # It's useful to "poll" the output of long-running scripts and print them 
        # as it'll appear in the widget's log, as well as the final output file
        while pipe.poll() is None:
            stdout_line = pipe.stdout.readline()
            print stdout_line.rstrip()
            cof_fh.write(stdout_line)

        # Capture last piece of text if any
        stdout_line=pipe.stdout.read()
        print stdout_line.rstrip()
        cof_fh.write(stdout_line)
        cof_fh.close()

        annotation_dict = dict()
        annotation_handle = open(annotation_file)
        for line in annotation_handle.readlines():
            line=line.strip()
            (ftr,term)=line.split('\t')
            annotation_dict[ftr]=term

        # Add annotation to protein-coding genes in genome object
        for ftr in plant_genome['data']['features']:
            ftr['functions']=["Uncurated"]
            if(ftr['id'] in annotation_dict):
                ftr['functions']=[annotation_dict[ftr['id']]]

        output['number_annotations']=len(annotation_dict.keys())

        # Saving genome
        if('output_genome' not in input):
            input['output_genome']=input['input_genome']

        save_result = self.gfu.save_one_genome({'workspace' : input['input_ws'],
                                                'name' : input['output_genome'],
                                                'data' : plant_genome['data']});
        
        # Prepare output report
        # Write HTML string for report
        html_string="<html><head><title>Hayai-Annotation Report</title></head><body>"
        html_string+="<p>The Hayai-Annotation  app has finished running. "
        html_string+=str(len(annotation_dict.keys()))+" protein sequences were annotated.</p></body></html>"

        saved_genome = "{}/{}/{}".format(save_result['info'][6],save_result['info'][0],save_result['info'][4])
        description = "Plant genome "+plant_genome['data']['id']+" annotated"

        # Save command output as file, accessible from within report
        output_files=list()
        output_files.append({'path' : os.path.join(fasta_file_path,command_output_file),
                             'name' : command_output_file,
                             'label' : "Command Output",
                             'description' : 'Output text generated by Command'})

        # Prepare report object, use random string as part of report name
        uuid_string = str(uuid.uuid4())
        report_params = { 'objects_created' : \
                          [{"ref":saved_genome,"description":description}],
                          'file_links' : output_files,
                          'direct_html' : html_string,
                          'workspace_name' : input['input_ws'],
                          'report_object_name' : 'kb_plant_rast_report_' + uuid_string }
        kbase_report_client = KBaseReport(self.callback_url, token=self.token)
        report_client_output = kbase_report_client.create_extended_report(report_params)
        output['report_name']=report_client_output['name']
        output['report_ref']=report_client_output['ref']

        #END hayai_annotation

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method hayai_annotation return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
