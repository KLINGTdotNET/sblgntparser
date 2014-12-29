# import sys
# from pathlib import Path
# parent = str(Path(__file__).absolute().parent.parent)
# sys.path.append(parent)

from sblgntparser import parser, tools

import pytest
import logging
log = logging.getLogger(__name__)

def test_parse(testfiles):
    for testpath in testfiles:
        text = parser.parse(testpath)
        assert text is not None
        assert len(text) > 0
        for sentence in text.sentences():
            assert sentence is not None
            assert len(sentence) > 0

def test_text(testfiles, load_textfile):
    filepaths = testfiles
    for filepath in filepaths:
        text = load_textfile(filepath)
        assert text is not None
        assert text.bookindex() > 0
        for word in text.words():
            assert str(word) == str(word.sentence().word(word.position()))
        for sentence in text.sentences():
            for index, word in enumerate(sentence.words()):
                n = word.neighbors()
                if len(sentence) == 1:
                    assert n['left'] is None and n['right'] is None
                else:
                    if index == 0:
                        assert n['left'] is None
                    elif index == len(sentence) - 1:
                        assert n['right'] is None
                    else:
                        assert n['left'] is not None and n['right'] is not None
        hits = text.find(u'καί')
        # "καί" is in every book
        assert hits is not None and len(hits) > 0

# def test_sentence(sentence):
#     for index, word in enumerate(sentence.words()):
#         n = word.neighbors()
#         if index == 0:
#             assert n['left'] is None
#         elif index == len(sentence) - 1:
#             assert n['right'] is None
#         else:
#             assert n['left'] is not None and n['right'] is not None
