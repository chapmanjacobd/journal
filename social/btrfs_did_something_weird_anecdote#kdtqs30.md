Damaged RAM will cause problems by silently corrupting everything regardless of what filesystem you use. 

The filesystem cannot know if you didn't mean to write a file in the wrong way. For example, you open a text file which is read from disk (passing checksum verify) then it exists in RAM and you type a line of text but suddenly many bits are flipped by the damaged RAM and so when the text editor saves the file, it gets sent to disk as the wrong letters. The new data is saved with a new checksum.

The same thing can happen when writing any data like binary blob save files.
