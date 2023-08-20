There is also `convmv`. I've used `detox` before and while it works okay (if you carefully configure it), I wasn't satisfied with either and wrote my own using the [ftfy](https://github.com/rspeer/python-ftfy) python library.

Mind you, my script does not go as far as removing diacritical markers--so you would need to modify it to do that, but it should work on Windows.

In Linux there are a lot more f'd up filenames than on Windows because [pretty much anything that is data](https://dwheeler.com/essays/fixing-unix-linux-filenames.html) can be a filename in linux except for path separators.

I highly recommend taking a filesystem snapshot before running this so that you can easily revert in case it [does something](https://github.com/chapmanjacobd/library/blob/main/xklb/utils.py#L291) that you did not anticipate.

    pip install xklb
    library christen -v --dry-run ./folder ./paths*

The script is designed to rename machine generated and OCR filenames for media like videos and music. DO NOT run this against your operating system folder or program files because it will break stuff.
