import sys
from pathlib import Path
parent = str(Path(__file__).absolute().parent.parent)
sys.path.append(parent)

from sblgntparser import parser, tools

import pytest
import logging
log = logging.getLogger(__name__)

def test_tools():
    particles = tools.particles()
    assert particles is not None
    assert len(particles.keys()) is 3
    particles = tools.particles(category='negation')
    assert len(particles) is 4