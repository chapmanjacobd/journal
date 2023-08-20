I like it. One thing I added recently was showing from reporoot when in a VCS directory.

    function prompt_git_pwd
        set -q argv[1]
        or set argv (pwd -P)

        set -l reporoot (git rev-parse --show-toplevel 2>/dev/null)
        string replace // / (string replace -r '^'"$reporoot"'($|/)' (basename "$reporoot")':$1/' $argv)
    end

https://github.com/chapmanjacobd/computer/blob/7d34d7b0179dd4f416f39fb5ae0eacf39bee2514/.config/fish/functions/fish_prompt.fish#L118-L135
