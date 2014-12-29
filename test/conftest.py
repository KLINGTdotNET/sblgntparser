import pytest
import os.path
import os

from sblgntparser import parser

import logging
log = logging.getLogger(__name__)

@pytest.fixture
def testfiles(scope='module'):
    testdatapath = os.path.join(os.path.dirname(__file__), 'data', 'sblgnt')
    testfilepaths = []
    for f in os.listdir(testdatapath):
        name, ext = os.path.splitext(f)
        if ext == '.txt':
            testfilepaths.append(os.path.join(testdatapath, f))
    if not testfilepaths:
        log.warn('testfilepaths are empty!')
    return testfilepaths

@pytest.fixture
def load_textfile():
    def parse_textfile(filename):
        return parser.parse(filename)
    return parse_textfile