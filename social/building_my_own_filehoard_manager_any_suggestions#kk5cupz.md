Thanks :-)

For sure the license is here: https://github.com/chapmanjacobd/library/blob/main/.github/LICENSE although if you are just taking ideas there is really no need to include a copyright statement with my name in it.

Yes, I sometimes regret that postgres isn't quite as portable as SQLite. I really like that the user can create and swap out different databases without needing to do anything. If I could use postgres in a similar file-based way I would be interested in supporting that. Maybe I could use configuration files which reference the actual database... but there is something tactile which is lost in that. SQLite only uses one index per query so sometimes it is a bit slower than it needs to be for large databases.
