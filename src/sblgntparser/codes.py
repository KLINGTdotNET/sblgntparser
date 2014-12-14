import logging
log = logging.getLogger(__name__)

class Code():
    def __init__(self, codes, name):
        self.codes = codes
        self.name = name

    def get(self, code):
        clow = code.lower()
        if clow in self.codes:
            return self.codes[clow]
        elif code is '-':
            pass
        else:
            log.warn('Unknown {} code: "{}"'.format(self.name, code))

def person(code):
    p = Code({
        '1': '1st person',
        '2': '2nd person',
        '3': '3rd person'
    }, 'person')
    return p.get(code)

def tense(code):
    t = Code({
        "p" : "present",
        "i" : "imperfect",
        "f" : "future",
        "a" : "aorist",
        "r" : "perfect",
        "l" : "pluperfect",
        "x" : "no_tense_stated"
    }, 'tense')
    return t.get(code)

def voice(code):
    v = Code({
        "a" : "active",
        "m" : "middle",
        "p" : "passive",
        "e" : "middle_or_passive",
        "d" : "middle",
        "o" : "passive",
        "n" : "middle_or_passive",
        "q" : "active",
        "x" : "no_voice"
    }, 'voice')
    return v.get(code)

def mood(code):
    m = Code({
        "i" : "indicative",
        "s" : "subjunctive",
        "o" : "optative",
        "m" : "imperative",
        "n" : "infinitive",
        "p" : "participle",
        "r" : "imperative_participle"
    }, 'mood')
    return m.get(code)

def case(code):
    c = Code({
        "n" : "nominative",
        "v" : "vocative",
        "g" : "genitive",
        "d" : "dative",
        "a" : "accusative"
    }, 'case')
    return c.get(code)

def number(code):
    n = Code({
        's': 'singular',
        'p': 'plural'
    }, 'numbers')
    return n.get(code)

def gender(code):
    g = Code({
        'f': 'feminine',
        'm': 'masculine',
        'n': 'neuter'
    }, 'gender')
    return g.get(code)

def degree(code):
    # no codes known
    return None