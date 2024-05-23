Debugger driven development: 

    pytest --ipdb --pdbcls=IPython.terminal.debugger:TerminalPdb \
       --ignore=tests/data --capture=tee-sys --log-cli-level=ERROR

I have it set to launch into debugger on an error if [any level of verbosity has been passed as command-line arguments](https://github.com/chapmanjacobd/library/blob/3bc71f0b7adf6b30bf89a09e96f254d7588e6c0a/xklb/utils/log_utils.py#L31)

Linting

    pycln --all && ssort && isort --profile black --line-length=120 && 
       black --line-length=120 --skip-string-normalization
