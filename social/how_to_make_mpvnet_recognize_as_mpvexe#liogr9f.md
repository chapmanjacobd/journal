It looks like you could set `ANI_CLI_PLAYER` to `mpvnet` 

    setx ANI_CLI_PLAYER "mpvnet"

or replace the `case "$(uname -a)" in ... esac` with `player_function=mpvnet`

https://github.com/pystardust/ani-cli/blob/master/ani-cli
