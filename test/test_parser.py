import sys
from pathlib import Path
parent = str(Path(__file__).absolute().parent.parent)
sys.path.append(parent)

from sblgntparser import parser, tools

import pytest
import logging
log = logging.getLogger(__name__)

def test_parse():
    for testpath in __get_testfiles():
        text = parser.parse(str(testpath))
        assert text is not None
        assert len(text) > 0
        for sentence in text.sentences():
            assert sentence is not None
            assert len(sentence) > 0

def test_text():
    filepaths = __get_testfiles()
    for fp in filepaths:
        if '84-2Jn-morphgnt.txt' in str(fp):
            text = parser.parse(str(fp))
            assert text is not None
            assert text.bookindex() is 24
            for word in text.words():
                assert str(word) == str(word.sentence().words()[word.position()])
            for sentence in text.sentences():
                for index, word in enumerate(sentence.words()):
                    n = word.neighbors()
                    if index == 0:
                        assert n['left'] is None
                    elif index == len(sentence) - 1:
                        assert n['right'] is None
                    else:
                        assert n['left'] is not None and n['right'] is not None
            hits = text.find(u'ἐν')
            assert hits is not None and len(hits) == 8

def __get_testfiles():
    testdata = Path(__file__).parent / 'data' / 'sblgnt'
    return testdata.glob('*.txt')
