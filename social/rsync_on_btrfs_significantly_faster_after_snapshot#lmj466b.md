It's either that rsync was updated and got faster somehow, or the file list was already cached in RAM, or your rsync configuration was such that it was skipping folders that weren't modified since last time.

The Linux Kernel uses a native caching mechanism called the page cache. If you ran `find` or `grep` prior to rsync the file list is almost certainly already in RAM. But note that this could be from a background utility (like mlocate or baloo) scanning soon prior to you running rsync--so maybe you are not aware of it...

Somewhat related, this article is about preserving the page cache by telling the OS to _not_ cache rsync reads/writes: https://insights.oetiker.ch/linux/fadvise.html It will still _read_ from the page cache though. The benefit here is that existing information in the page cache (which could include file trees) won't be evicted from the cache as quickly
