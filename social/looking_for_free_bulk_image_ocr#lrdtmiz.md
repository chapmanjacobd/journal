If the scans are very aligned it might be worth it to write a script to crop and OCR the specific fields into fields but honestly 500 images isn't that much. It might be faster to just do it semi-manually:

I recommend ocrmypdf. You can use it like this:

    pip install ocrmypdf
    ocrmypdf input.pdf output.pdf

> If OCRmyPDF is given an image file as input, it will attempt to convert the
image to a PDF before processing.  For more control over the conversion of
images to PDF, use the Python package img2pdf or other image to PDF software.

> For example, this command uses img2pdf to convert all .png files beginning
with the 'page' prefix to a PDF, fitting each image on A4-sized paper, and
sending the result to OCRmyPDF through a pipe.

>     img2pdf --pagesize A4 page*.png | ocrmypdf - myfile.pdf

Once you have that, you should be able to use something like [camelot](https://github.com/py-pdf/pypdf_table_extraction/) to extract table-like data from the pages

If all the post-OCR pages are append-able data for the same "table" then you can use this command to combine the data without writing any scripts. This uses camelot under the hood:

    pip install xklb
    library tables ocr_pages.pdf --start-row 1 --concat --to-json > output.jsonl
