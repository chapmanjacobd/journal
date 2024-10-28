nushell can read excel files. I've found that to be pretty handy when searching across many excel files.

I've tried to use [ripgrep-all](https://github.com/phiresky/ripgrep-all) for something like this before, but it's a easier and faster to search when everything is converted to text beforehand.

I wrote a script that might help but I haven't tested the text extraction tools extensively because I haven't needed them. As long as you have the dependencies (tesseract, antiword, etc), it's all offline. Under the hood it uses `textract` which supports these formats: `xlsx`, `xls`, `doc`, `docx`, `csv`, `tab`, `tsv`, `eml`, `epub`, `json`, `htm`, `html`, `msg`, `odt`, `pdf`, `pptx`, `ps`, `rtf`, `txt`, `log`:

It's a CLI tool, but you can also use xklb to create a text index:

    pip install xklb textract-py3
    library fsadd --text usb.db E:\

You can also add `--ocr` to get text from image PDFs (or run `ocrmypdf` first), images, and `--speech-recognition` for audio files.

Then you can search files with `library fs data.db -p -s "tax evasion 2020"`. To get a file list only use `-pf` instead of just `-p`. To open the files remove `-p`... you can see all the options with `library fs --help`.

I have not tested this at all with network drives so I don't know if they work. If you have any crashes, let me know
