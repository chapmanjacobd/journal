Most online tools will probably call ghostscript under the hood:

    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress -dNOPAUSE -dQUIET -dBATCH -sOutputFile=out.pdf file.pdf

black and white only can make a very small PDF

    gs -q -dNOPAUSE -dBATCH -dSAFER -sProcessColorModel=DeviceGray -sColorConversionStrategy=Gray -dDownsampleColorImages=true -dOverrideICC -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dColorImageDownsampleType=/Bicubic -dColorImageResolution=120 -dGrayImageDownsampleType=/Bicubic -dGrayImageResolution=120 -dMonoImageDownsampleType=/Bicubic -dMonoImageResolution=120 -sOutputFile=out.pdf file.pdf

Personally, I like Calibre's `ebook-convert`. You can get down to really nice sizes by also encoding the images to avif or webp afterwards but it will also mangle the layout so that doesn't sound like what you want !
