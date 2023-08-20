you can catch errors and drop into a REPL (but be careful of this code running in a headless context because ipdb will run forever waiting for your input commands):

    import sys
    from IPython.core import ultratb
    from IPython.terminal.debugger import TerminalPdb

    sys.excepthook = ultratb.FormattedTB(
        mode="Context",
        color_scheme="Neutral",
        call_pdb=True,
        debugger_cls=TerminalPdb,
    )
