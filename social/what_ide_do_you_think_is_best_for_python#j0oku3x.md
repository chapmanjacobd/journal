I like VS Code but I'm a big fan of overwriting `sys.excepthook`:

    try:
        import ipdb
        from IPython.core import ultratb
        from IPython.terminal.debugger import TerminalPdb
    except ModuleNotFoundError:
        pass
    else:
        sys.breakpointhook = ipdb.set_trace
        sys.excepthook = ultratb.FormattedTB(
            mode="Context",
            color_scheme="Neutral",
            call_pdb=True,
            debugger_cls=TerminalPdb,
        )
