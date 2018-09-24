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
    GIT_URL = "git@github.com:kbaseapps/hayai_annotation.git"
    GIT_COMMIT_HASH = "243ad5b58534ece437eaf9413c12509092eb8811"

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
        :returns: instance of type "AnnotatePlantGenomeResults" (Here we
           define the output, which, for the purposes of the UI, will always
           be a report. The contents of the report are shown, in HTML, in the
           output widget.) -> structure: parameter "report_name" of String,
           parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN annotate_plant_genome
        #END annotate_plant_genome

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method annotate_plant_genome return value ' +
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
