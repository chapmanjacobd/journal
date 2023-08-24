I have a few AutoHotKey tips which I found very useful but have seldom seen people use: mouse button combinations. 

I use linux almost completely now and haven't found a replacement for it. I miss it sometimes so I'm sharing it with you guys

1. Hold down the right mouse button and left-click to fast-scroll down the page:

        RButton::Send {RButton}
            RButton & XButton1::
            Send, {PGUP}
            Sleep, 20
            return
            
            RButton & LButton::
            Send, {PGDN}
            Sleep, 20
            return
        return

2. Hold down the right button and scroll the wheel to fast-scroll up and down the page

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

3. Using the middle mouse button to switch tabs. This only works if your mouse supports mousewheel-left/right (instead of clicking down the middle button (mousewheel), swipe it left or right). You might be surprised how many mice actually support this but some don't
    
        WheelLeft::^PgUp
        WheelRight::^PgDn
    
3. same thing for the Logitech Marble Mouse

            XButton2alt:
            XButton2 & XButton1::
                 Send, ^{PGUP}
                 Sleep, 10
                 return
                 
                 XButton2 & RButton::
                 return
                 
                 XButton2 & LButton::
                 Send, ^{PGDN}
                 Sleep, 10
                 return
                 
            return
        
4. adjust volume
        
        XButton1::Send {MButton}
        
            XButton1 & XButton2::
            soundset, +5
            return
            
            XButton1 & LButton::
            return
            
            XButton1 & RButton::
            soundset, -5
            return
            
        return

BONUS: you can combine mouse combinations in other code

    #If WinActive("ahk_class SUMATRA_PDF_FRAME") || WinActive("ahk_class MediaPlayerClassicW")
    
    *W::Send, !{F4}
    
    RButton::Send {RButton}
    
        RButton & XButton2::
        Send, !{F4}
        Sleep, 10
        return
        
    return
    
    #If
