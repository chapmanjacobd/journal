# Directory for sockets
set -x KTERM_DIR /run/user/$(uid)/terminals

# fish doesn't have PROMPT_COMMAND; use fish_prompt or fish_preexec/postexec
functions -q kcompletions; and functions -e kcompletions
function fish_prompt --description "Wrap default prompt with kcompletions"
    kcompletions
    # call default prompt
    fish_default_prompt
end

# Ensure directory exists
if not test -d $KTERM_DIR
    mkdir -p $KTERM_DIR
end

function kbash
    set T (kphrase)
    env KTERM_NAME=$T dtach -n $KTERM_DIR/$T bash
    echo $T
end

function klist
    for t in (find $KTERM_DIR -type s)
        echo (basename $t)
    end
end

function kcompletions
    complete -c kattach   -a "(klist)"
    complete -c kterm     -a "(klist)"
    complete -c ktermsize -a "(klist)"
    set -gx HN $KTERM_NAME
end

function kattach
    dtach -a $KTERM_DIR/$argv[1] -r winch -z
end

function kescape
    echo -en "\033P@kitty-cmd"
    cat
    echo -en "\033\\"
end

function ktermsize
    set T (count $argv) ? $argv[1] : $KTERM_NAME
    set matches (ls $KTERM_DIR/size*$T 2>/dev/null)
    if test -f $matches[1]
        cat $matches[1]
    else
        echo "-o initial_window_height=30c -o initial_window_width=80c"
    end
end

function kterm
    set TERMINAL (count $argv) ? $argv[1] : (kbash)
    cat - <<SEND | kescape
{"cmd":"new-window","version":[0,18,2],"no_response":true,"payload":{"window_type":"os","args":["(echo "/usr/local/bin/kitty -1 (ktermsize $TERMINAL) ssh -A -t devcon dtach -a $KTERM_DIR/$TERMINAL -r winch -z" | sed -re 's/ /", "/g')"]}}
SEND
end

function ksizing
    echo "-o initial_window_width=${COLUMNS}c -o initial_window_height=${LINES}c" > $KTERM_DIR/size.$$.$KTERM_NAME
end

function kcleanup
    rm -f $KTERM_DIR/size.$$.$KTERM_NAME
end

# fish has no trap; use events for signals
function __ksizing_trap --on-signal WINCH
    ksizing
end

function __kcleanup_trap --on-process-exit %self
    kcleanup
end
