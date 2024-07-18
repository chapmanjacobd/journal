Both this

    ENV = os.environ['UNSET_ENV']

and this

    assert os.environ['UNSET_ENV']

will raise KeyError when the env var isn't set. But the assert will also raise AssertionError if they set the env var to empty string. I guess that makes sense. Both ways are clear to me when they are at the top of the script
