I'd like to bind a shortcut `ALT+,` to duplicate the argument to the left of the cursor:

```
bind \e, something
```



For example, `command one two `

When the cursor is at `command one HERE two ` and `ALT+,` is pressed then the commandline should be transformed to `command one one HERE two `.

It didn't seem like this is possible given the current options but I could be wrong: 

https://fishshell.com/docs/current/cmds/bind.html
