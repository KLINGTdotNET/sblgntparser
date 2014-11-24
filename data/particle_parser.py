#!/usr/bin/env python3

from pathlib import Path
import pprint
pp = pprint.PrettyPrinter()
import logging
log = logging.getLogger(__name__)

def main():
    p = Path('particles-python_project.txt')
    if p.exists() and  p.is_file():
        parse(str(p))

def parse(filepath):
    raw = ''
    try:
        with open(filepath) as f:
            raw = f.read()
    except IOError as e:
        log.exception(e)
        return 1
    else:
        parse_lines(raw.splitlines())

def parse_lines(lines):
    '''
    parser for particle list of stylianos
    '''
    data = {}
    category = ''
    particle = ''
    for line in lines:
        parts = line.split()
        if parts[0] == '*':
            category = ' '.join(parts[1:])
            if category not in data:
                data[category] = {}
            else:
                log.warn('Category "{}" already defined!'.format(category))
        elif parts[0] == '**':
            if category:
                if parts[1] not in data[category]:
                    particle = parts[1]
                    data[category][particle] = []
                else:
                    log.warn('Particle "{}" already contained in category: "{}"'.format(parts[1], category))
            else:
                log.warn('particle without previous category specification: "{}"'.format(parts[1]))
        elif parts[0] == '+':
            if category in data and particle in data[category]:
                data[category][particle].append(parts[1])
            else:
                log.warn('particle variation without previous category specification: "{}"'.format(parts[0]))
        else:
            log.error('malformed line: "{}"'.format(line))
    pp.pprint(data)

if __name__ == '__main__':
    main()
