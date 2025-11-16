> load image in image manipulation library, do some basic manipulation (rotate, resize), don't save the result to disk, but made sure it actually did the manipulation

rotate, resize of images doesn't check much. I guess it's slightly more robust than checking the first few KB with exiftool but it doesn't really tell you if there are any errors.

https://photo.stackexchange.com/questions/46919/is-there-a-tool-to-check-the-file-integrity-of-a-series-of-images

maybe:

- https://github.com/ImpulseAdventure/JPEGsnoop
- https://coptr.digipres.org/index.php/ImageVerifier

It's not well-documented but exiftool [actually does have](https://old.reddit.com/r/DataHoarder/comments/f67v9x/finding_and_maybe_fixing_corruption_in_personal/firkupw/) a -validate flag which does do _something_:

      Warning = Missing required JPEG ExifIFD tag 0x9000 ExifVersion
      Warning = Missing required JPEG ExifIFD tag 0x9101 ComponentsConfiguration
      Warning = Missing required JPEG ExifIFD tag 0xa000 FlashpixVersion
      Warning = Missing required JPEG ExifIFD tag 0xa001 ColorSpace
      Warning = Missing required JPEG IFD0 tag 0x0213 YCbCrPositioning

But I think it is actually only validating the metadata and not the overall data structure nor validating that the image data looks intact.
