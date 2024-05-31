> still was perplexed as to what was going on

Yes, to clarify a bit more: xdg-open is opening the GUI program in the shell background and GUI programs are sometimes a bit log noisy. 

`setsid -f xdg-open` doesn't work because xdg-open looks for the shell process and opens a background process in there or something like that. It doesn't want to be a session leader process
