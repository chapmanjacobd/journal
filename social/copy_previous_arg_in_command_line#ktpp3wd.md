ahhh this makes great sense! although I think I would rather go with:

    bind \e, backward-kill-bigword yank yank

edit:  there seems to be a bug if I do `ctrl+backspace` (which I have bound to only `backward-kill-bigword`) and then `alt+,` right after it fish re-uses and resurrects the previously deleted word instead of killing the word that is to the left of the current cursor in the commandline but this shouldn't be a big deal in practice
