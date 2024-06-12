I think the best solution here is to automatically open the pages in cron. If you see something you like, grab it while it is fresh.

Or use something like this:

    library tabsadd tabs.db --frequency monthly --category fun \
      https://old.reddit.com/r/Showerthoughts/top/?sort=top&t=month \
      https://old.reddit.com/r/RedditDayOf/top/?sort=top&t=month

    45 9 * * * DISPLAY=:0 library tabs /home/my/tabs.db

> tabs is a way to organize your visits to URLs that you want to remember every once in a while.

> The main benefit of tabs is that you can have a large amount of tabs saved (say 500 monthly tabs) and only the smallest amount of tabs to satisfy that goal (500/30) tabs will open each day. 17 tabs per day seems manageable--500 all at once does not.

> The use-case of tabs are websites that you know are going to change: subreddits, games, or tools that you want to use for a few minutes daily, weekly, monthly, quarterly, or yearly.

> https://github.com/chapmanjacobd/library?tab=readme-ov-file#browser-tabs
