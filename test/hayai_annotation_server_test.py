# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests
import shutil

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from GenomeFileUtil.GenomeFileUtilClient import GenomeFileUtil
from hayai_annotation.hayai_annotationImpl import hayai_annotation
from hayai_annotation.hayai_annotationServer import MethodContext
from hayai_annotation.authclient import KBaseAuth as _KBaseAuth


class hayai_annotationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('hayai_annotation'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'hayai_annotation',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = hayai_annotation(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

        #Instantiate GenomeFileUtil class for loading test genome
        cls.gfu = GenomeFileUtil(cls.callback_url)

        cls.genome = "Test_Genome"
        cls.prepare_data()

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_hayai_annotation_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    @classmethod
    def prepare_data(cls):

        #Here the test genome files are copied into the container's scratch directory
        cls.gff_filename = 'Test_v1.0.gene.gff3.gz'
        cls.gff_path = os.path.join(cls.scratch, cls.gff_filename)
        shutil.copy(os.path.join("/kb", "module", "data", cls.gff_filename), cls.gff_path)

        cls.fa_filename = 'Test_v1.0.fa.gz'
        cls.fa_path = os.path.join(cls.scratch, cls.fa_filename)
        shutil.copy(os.path.join("/kb", "module", "data", cls.fa_filename), cls.fa_path)

    def loadFakeGenome(cls):
        
        input_params = {
            'fasta_file': {'path': cls.fa_path},
            'gff_file': {'path': cls.gff_path},
            'genome_name': cls.genome,
            'workspace_name': cls.getWsName(),
            'source': 'Phytozome',
            'type': 'Reference',
            'scientific_name': 'Populus trichocarpa'
        }

        result = cls.gfu.fasta_gff_to_genome(input_params)

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_your_method(self):

        # Loading test genome
        self.loadFakeGenome()

        # Running your parent method
        ret = self.getImpl().hayai_annotation(self.getContext(), {'input_ws' : self.getWsName(),
                                                                  'input_genome' : self.genome,
                                                                  'alignment_type' : 'local',
                                                                  'organism_type' : 'model',
                                                                  'max_hits_per_query' : 5,
                                                                  'max_seq_id' : 0.5})
        self.assertEqual(ret[0]['number_annotations'],1)
        pass
