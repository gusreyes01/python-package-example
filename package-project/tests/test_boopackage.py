from boopackage.barmodule import barfunc
from boopackage.boomodule import boofunc


def test_barfunc_prints_its_name(capsys):
    barfunc()
    assert capsys.readouterr().out == "barfunc\n"


def test_boofunc_demonstrates_absolute_and_relative_imports(capsys):
    boofunc()

    assert capsys.readouterr().out.splitlines() == [
        "boofunc",
        "testing barfunc via absolute/normal import...",
        "barfunc",
        "testing barfunc via absolute import complete.",
        "testing barfunc via relative import...",
        "barfunc",
        "testing barfunc via relative import complete.",
    ]
