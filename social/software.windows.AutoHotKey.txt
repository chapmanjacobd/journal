    #NoEnv
    #SingleInstance force
    #installkeybdhook
    #MaxHotkeysPerInterval 120
    SendMode Input
    Process, Priority, , H
    SetWorkingDir %A_ScriptDir%
    SetTitleMatchMode 3
    SetNumLockState,On
    SetNumLockState,AlwaysOn
    SetScrollLockState,Off
    SetScrollLockState,AlwaysOff
    return

    ;;keys

    Backspace::F13
    CapsLock::Backspace

    ;make media keys work
    Volume_Up::
    soundset, +1
    return

    Volume_Down::
    soundset, -1
    return

    +Volume_Up::
    soundset, +20
    return

    +Volume_Down::
    soundset, -20
    return

    Volume_Mute::
    SoundSet, +1, , mute
    return

    F12::Media_Next
    Media_Next::F12

    F10::Media_Prev
    Media_Prev::F10

    F11::Media_Play_Pause
    Media_Play_Pause::F11

    F9::Media_Stop
    Media_Stop::F9

    ;adjust mediamonkey volume

    ;enable AppsKey functionality
    AppsKey & [::Send #[
    AppsKey::Send, {AppsKey}

    AppsKey & Volume_Up::
    Send, ^!+{F8}
    sleep, 80
    Send, ^!+{F8}
    sleep, 80
    Send, ^!+{F8}
    return

    AppsKey & Volume_Down::
    Send, ^!+{F7}
    sleep, 80
    Send, ^!+{F7}
    sleep, 80
    Send, ^!+{F7}
    sleep, 80
    Send, ^!+{F7}
    return

    ;;colemak

    ;`::`
    ;1::1
    ;2::2
    ;3::3
    ;4::4
    ;5::5
    ;6::6
    ;7::7
    ;8::8
    ;9::9
    ;0::0
    ;-::-
    ;=::=

    ;q::q
    ;w::w
    e::f
    r::p
    t::b
    y::j
    u::l
    i::u
    o::y
    p::`;
    ;[::[
    ;]::]
    ;\::\

    ;a::a
    s::r
    d::s
    f::t
    g::g
    h::m
    j::n
    k::e
    l::i
    `;::o
    ;'::'

    ;z::z
    ;x::x
    ;c::c
    v::d
    b::v
    n::k
    m::h
    ;,::,
    ;.::.
    ;/::/

    ;RELEASE KEYS FROM REMAP WHEN MODIFIER DOWN

    *Ctrl::
    SetKeyDelay -1
    Send {Blind}{Ctrl DownTemp}
    Suspend On
    return
    *Ctrl up::
    Suspend Off
    SetKeyDelay -1
    Send {Blind}{Ctrl Up}
    return

    *Alt::
    SetKeyDelay -1
    Send {Blind}{Alt DownTemp}
    Suspend On
    return
    *Alt up::
    Suspend Off
    SetKeyDelay -1
    Send {Blind}{Alt Up}
    return

    *LWin::
    SetKeyDelay -1
    Send {Blind}{LWin DownTemp}
    Suspend On
    return
    *LWin up::
    Suspend Off
    SetKeyDelay -1
    Send {Blind}{LWin Up}
    return


    ;;mouse

    ; Accelerated Scrolling
    ; V1.3
    ; By BoffinbraiN

    ; Show scroll velocity as a tooltip while scrolling. 1 or 0.
    tooltips := 0

    ; The length of a scrolling session.
    ; Keep scrolling within this time to accumulate boost.
    ; Default: 500. Recommended between 400 and 1000.
    timeout := 600

    ; If you scroll a long distance in one session, apply additional boost factor.
    ; The higher the value, the longer it takes to activate, and the slower it accumulates.
    ; Set to zero to disable completely. Default: 30.
    boost := 70

    ; Spamming applications with hundreds of individual scroll events can slow them down.
    ; This sets the maximum number of scrolls sent per click, i.e. max velocity. Default: 60.
    limit := 100

    ; Runtime variables. Do not modify.
    distance := 0
    vmax := 1

    ; Key bindings
    WheelUp::    Goto Scroll
    WheelDown::  Goto Scroll

    Scroll:
        t := A_TimeSincePriorHotkey
        if (A_PriorHotkey = A_ThisHotkey && t < timeout)
        {
            ; Remember how many times we've scrolled in the current direction
            distance++

            ; Calculate acceleration factor using a 1/x curve
            v := (t < 80 && t > 1) ? (250.0 / t) - 1 : 1

            ; Apply boost
            if (boost > 1 && distance > boost)
            {
                ; Hold onto the highest speed we've achieved during this boost
                if (v > vmax)
                    vmax := v
                else
                    v := vmax

                v *= distance / boost
            }

            ; Validate
            v := (v > 1) ? ((v > limit) ? limit : Floor(v)) : 1

            if (v > 1 && tooltips)
                QuickToolTip("×"v, timeout)
            
            

            MouseClick, %A_ThisHotkey%, , , v
            }
            else
            {
                ; Combo broken, so reset session variables
                distance := 0
                vmax := 1

                MouseClick %A_ThisHotkey%
            }
        return

    QuickToolTip(text, delay)
    {
        ToolTip, %text%
        SetTimer ToolTipOff, %delay%
        return

        ToolTipOff:
        SetTimer ToolTipOff, Off
        ToolTip
        return
    }

    ; Accelerated Scrolling End


    ;windows shortcuts

    #e::
    run, explorer /n`,/e`,a:\working
    return

    ;;extend

    Lalt::
      KeyWait, Lalt
    Return

    #If, GetKeyState("Lalt", "P")

        *Tab::Send {Alt Down}{Tab}{Alt Up}
        
        *s::Send {Alt Down}{Enter}{Alt Up}
        *d::Send {Del}
        *r::Send {F2}
        
        *i::Up
        *j::Left
        *k::Down
        *l::Right
        
        *+i::Send {Alt Down}{Up}{Alt Up}
        *+j::Send {Alt Down}{Left}{Alt Up}
        *+k::Send {Alt Down}{Down}{Alt Up}
        *+l::Send {Alt Down}{Right}{Alt Up}

        *y::Send {Blind}{PgUp}
        *h::Send {Blind}{PgDn}
        *+y::Send ^{Home}
        *+h::Send ^{End}

        *Space::Send {Return}

        *0::Send {PgUp}
        *1::6
        *2::7
        *3::8
        *4::9
        *5::

        *WheelLeft::^PgUp
        *WheelRight::^PgDn

        *\::Capslock

    return


    ;firefox_mod

    #IfWinActive, ahk_class MozillaWindowClass
    RButton::Send {RButton}

        RButton & WheelUp::
        Send, ^{PGUP}
        Sleep, 10
        return

        RButton & WheelDown::
        Send, ^{PGDN}
        Sleep, 10
        return
        
    return
