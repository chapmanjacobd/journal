I wonder if this could be used with Git for resolving merge conflicts?

ie. you can currently use the following to view diffs between SQLite DBs:

.gitconfig

    [diff "sqlite3"]
        textconv = "echo .dump | sqlite3"

.gitattributes

    *.db       diff=sqlite3
