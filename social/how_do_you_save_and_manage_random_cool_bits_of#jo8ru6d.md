Here is what I do and it has made my web surfing experience 100% better:

Every week on Sunday I append all the tabs that I haven't read into a line-delimited text file (this hasn't happened to me for several months as I've gotten good at organizing tab reads more efficiently).

Then I set up a schedule on my computer to open up 7 tabs at 9:30am, 14 tabs at 5:00pm. This helps me start my work day by feeding my brain something interesting without going overboard. It also helps me to stop working around 5pm.

There is an automated program that sorts and dedupes my tabs by TfidfVectorizer:

    pip install xklb
    sort --unique tabs.txt | lb clustersort | sponge tabs.txt

So similar tabs are grouped together and it helps me to close similar tabs faster.

Recurring tabs like, this subreddit, are opened on a schedule also but it is a different mechanism:

https://github.com/chapmanjacobd/library#getting-started
