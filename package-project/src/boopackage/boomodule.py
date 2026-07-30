# Demonstrate absolute and relative imports as described by PEP 328.
from boopackage.barmodule import barfunc

from .barmodule import barfunc as barfunc_relative


def boofunc():
    print('boofunc')

    print('testing barfunc via absolute/normal import...')
    barfunc()
    print('testing barfunc via absolute import complete.')

    print('testing barfunc via relative import...')
    barfunc_relative()
    print('testing barfunc via relative import complete.')
