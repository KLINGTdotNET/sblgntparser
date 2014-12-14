import os.path
import re
import logging
log = logging.getLogger(__name__)

import grarticle

'''
    A python module that parses texts in the format the SBLGNT uses

    http://morphgnt.org/sblgnt/
'''

class Text():
    def __init__(self, words):
        self.words = words

    def len(self):
        return len(self.words)

    def find(self, sought):
        for word in self.words:
            if sought in word.views['norm']:
                return word

    def read(self, view='text'):
        for word in self.words:
            yield word.views[view]

    def neighbors(self, word):
        pos = word.textpos
        if pos > 0 and pos < self.len():
            return [ self.words[pos-1], self.words[pos+1]]
        elif pos == 0:
            return [ self.words[1] ]
        elif pos == self.len():
            return [ self.words[self.len()-1] ]
        else:
            log.warn('Word position not inside text! "{}":"{}"'.format(pos, word.views['text']))

class Word():
    def __init__(self, word):
        self.textpos = word['text_position']
        self.book = word['book']
        self.chapter = word['chapter']
        self.verse = word['verse']
        self.part_of_speech = word['part_of_speech']
        self.codes = word['codes']
        self.views = word['views']

def parse(filepath):
    if os.path.exists(filepath):
        raw_text = ''
        try:
            with open(filepath) as f:
                raw_text = f.readlines()
        except IOError as e:
            log.exception(e)
        else:
            if raw_text:
                parsed_words = [ parse_line(index, line) for index, line in enumerate(raw_text) ]
                return Text(parsed_words)
            else:
                log.error('"{}" is empty!'.format(filepath))
    else:
        log.warn('Could not find file "{}"!'.format(filepath))

def parse_line(index, line):
    parts = line.split()
    if len(parts) is not 7:
        log.warn('Malformed line: "{}"'.format(line))
    else:
        book, chapter, verse = parse_index(parts[0])
        parse_part_of_speech(parts[1])
        codes = parse_parsing_code(parts[2])
        text, word, normalised, lemma = tuple(parts[3:])
        return Word({
            'text_position': index,
            'book': int(book),
            'chapter': int(chapter),
            'verse': int(verse),
            'part_of_speech': None,
            'codes': codes,
            'views': {
                'text': text,
                'word': word,
                'norm': normalised,
                'lemma': lemma
                }
            })

def parse_index(part):
    matcher = re.compile(r'(\d{2})(\d{2})(\d{2})')
    res = matcher.match(part)
    return res.groups()

def parse_part_of_speech(part):
    # todo, because the codes are currently unknown
    pass

def parse_parsing_code(part):
    if len(part) is not 8:
        log.warn('bad parsing code: "{}"!'.format(part))
    else:
        # see https://github.com/morphgnt/tischendorf/blob/master/code/rptag.py
        # person, tense, voice, mood, case, number, gender, degree
        codes = [ _ for _ in part ]
        person = grarticle.codes.person(codes[0])
        tense = grarticle.codes.tense(codes[1])
        voice = grarticle.codes.voice(codes[2])
        mood = grarticle.codes.mood(codes[3])
        case = grarticle.codes.case(codes[4])
        number = grarticle.codes.number(codes[5])
        gender = grarticle.codes.gender(codes[6])
        degree = grarticle.codes.degree(codes[7])
        return {
            'person': person,
            'tense': tense,
            'voice': voice,
            'mood': mood,
            'case': case,
            'number': number,
            'gender': gender,
            'degree': degree
        }

