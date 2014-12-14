import logging
log = logging.getLogger(__name__)

class Code():
    '''
    All codes are derived from `http://jtauber.com/2010/07/parse-helper/demo.html`
    '''
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
        "x" : "perfect",
        "y" : "pluperfect"
        }, 'tense')
    return t.get(code)

def voice(code):
    v = Code({
        "a" : "active",
        "m" : "middle",
        "p" : "passive"
        }, 'voice')
    return v.get(code)

def mood(code):
    m = Code({
        "i" : "indicative",
        "s" : "subjunctive",
        "o" : "optative",
        "d" : "imperative",
        "n" : "infinitive",
        "p" : "participle"
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
    d = Code({
        'c': 'comparative',
        's': 'superlative'
        }, 'degree')
    return d.get(code)

def part_of_speech(code):
    wordtype = Code({
        'a': 'adjective',
        'c': 'conjunction',
        'd': 'adverb',
        'n': 'noun',
        'p': 'pronoun',
        'r': 'preposition',
        's': 'suffix',
        't': 'particle',
        'v': 'verb',
        'x': 'exclamation',
        'i': 'interjection'
        }, 'word-type')
    wt = wordtype.get(code[0])
    if wt:
        # sblgnt only has 2 position codes for part of speech
        if wt == 'adjective':
            adjective = Code({
                'c': 'cardinal number',
                'o': 'ordinal number'
                }, 'adjective')
            return [wt, adjective.get(code[1])]
        elif wt == 'conjunction':
            conjunction = Code({
                'v': 'vav consecutive'
                }, 'conjunction')
            return [wt, conjunction.get(code[1])]
        elif wt == 'adverb':
            return [wt]
        elif wt == 'noun':
            noun = Code({
                # type
                'c': 'common',
                'g': 'gentilic',
                'p': 'proper name'
                }, 'noun')
            return [wt, noun.get(code[1])]
        elif wt == 'pronoun':
            pronoun = Code({
                'd': 'demonstrative',
                'f': 'indefinite',
                'i': 'interrogative',
                'p': 'personal',
                'r': 'relative'
                }, 'pronoun')
            return [wt, pronoun.get(code[1])]
        elif wt == 'preposition':
            preposition = Code({
                'i': 'independent',
                'b': 'bet inseparable',
                'k': 'kaf inseparable',
                'l': 'lamed inseparable',
                'm': 'mem inseparable',
                # seperate?
                'a': 'article',
                'd': 'demonstrative',
                'i': 'interrogative',
                'p': 'personal pronoun',
                'r': 'relative pronoun'
                }, 'preposition')
            return [wt, preposition.get(code[1])]
        elif wt == 'suffix':
            suffix = Code({
                'd': 'directional he',
                'h': 'paragogic he',
                'n': 'paragogic num',
                'p': 'pronomial'
                }, 'suffix')
            return [wt, suffix.get(code[1])]
        elif wt == 'particle':
            particle = Code({
                'a': 'affirmation',
                'd': 'definite article',
                'e': 'exhortation',
                'i': 'interrogative',
                'j': 'interjectioin',
                'm': 'demonstrative',
                'n': 'negative',
                'o': 'direct object marker',
                'r': 'relative',
                's': 'prefixed relateive (shin)'
                }, 'particle')
            return [wt, particle.get(code[1])]
        elif wt == 'verb':
            verb = Code({
                'p': 'perfect',
                'q': 'sequential perfect',
                'i': 'imperfect',
                'w': 'sequential imperfect',
                'a': 'infinitive absolute',
                'c': 'infinitive construct',
                'h': 'cohortative',
                'v': 'imperative',
                'j': 'jussive',
                'r': 'participle active',
                's': 'participle passive'
                }, 'verb')
            return [wt, verb.get(code[1])]
        else:
            return [wt]
