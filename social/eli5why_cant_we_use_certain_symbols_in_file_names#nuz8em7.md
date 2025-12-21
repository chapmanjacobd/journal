One of the consequences of being too permissive, like in Linux, is that you can have files which have line breaks in filenames which many scripts and programs are not written to correctly handle. You can even write filenames using arbitrary bytes (excluding the path seperator and ascii null which denotes the end of the filename internally) so it isn't possible to type or display without escaping it somehow and even more programs fail to handle files like that:

https://dwheeler.com/essays/fixing-unix-linux-filenames.html

From that perspective the Windows requirement of UTF-16 paths is very much a blessing.

But most of the restrictions you are thinking of are likely due to esoteric OS design (eg. Windows) which won't let you make `CON` or `PRN` files or folders...
