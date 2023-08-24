how do I accomplish this functionality in linux? Would this work? https://github.com/nikolavp/configs/blob/master/_xbindkeysrc.scm

**Hold down the right button and scroll the wheel to page up and down**  
  
    RButton::Send {RButton}
    
        # with {blind} you can hold down ctrl and modify the send so that you are switching tabs instead of scrolling the page
        RButton & WheelUp::
        Send, {blind}{PGUP}
        Sleep, 10
        return
    
        RButton & WheelDown::
        Send, {blind}{PGDN}
        Sleep, 10
        return
    
        # close tab with right button+middle click  
        RButton & MButton::
        Send, ^w
        Sleep, 200
        return
    return
    
