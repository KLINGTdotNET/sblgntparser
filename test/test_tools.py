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
    assert tools.bookname(17) is 'Titus'
    for part, indices in tools.parts().items():
        assert part is not None
        for index in indices:
            assert tools.bookname(index) is not None