Use `fd-find`:

    fd --changed-within "3 days"

or if you use `xklb`

    library watch videos.db --created-within '3 days'
    library watch videos.db --downloaded-within '3 days'

    library watch videos.db --downloaded-within '3 days' -pa
    library watch videos.db --downloaded-within '3 days' -p
    library watch videos.db --downloaded-within '3 days' -pf

Or more generally to see download statistics

    library history videos.db downloaded

Or download status

    library download-status videos.db
