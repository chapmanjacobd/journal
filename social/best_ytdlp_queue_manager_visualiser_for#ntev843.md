> using pueue

GNU Parallel is often a better alternative to pueue for various reasons that I won't get into. If you haven't heard of it, check it out!

For your other questions, I will suggest that you check out my wrapper, [library](https://github.com/chapmanjacobd/library). It supports yt-dlp, gallery-dl, generic http, and generic webpage parsing.

I personally only run one yt-dlp process at a time but you can run multiple `library download` processes concurrently on the same database with no trouble--and you can add more URLs/playlists to the database while you are downloading. I track 20,000 YouTube playlists and channels daily with my wrapper and it will check less frequently for channels/playlists that don't update often--from hourly up to a year between checks.

The only problem you might encounter is storing the database on a network share--don't do that. It requires `mmap` so keep the database somewhere local. The download destination can be anywhere though
