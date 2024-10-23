It's a CLI tool, but you can also use xklb to create a text index:

    pip install xklb
    library fsadd --text usb.db E:\

You can also add `--ocr` or `--speech-recognition` to get text from image PDFs (or run `ocrmypdf` first), images, and audio files.

Then you can search files with `library fs usb.db -p -s`
