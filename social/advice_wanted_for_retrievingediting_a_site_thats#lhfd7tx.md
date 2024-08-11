I usually use textract and bs4 for extracting and cleaning up text from old sites

I wrote a little CLI tool to make it easy: 

    pip install xklb
    lb text $URL  # or  lb text --local-html $local_path.htm

You can also use `lb webadd` to collect links but it might be easier to run something like `wget` first
