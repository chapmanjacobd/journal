The reason why we don't see a lot of bit-shifting hacks is that the CPU itself is plenty fast.

One gap that I see right now (and thus a good area for experimental time-saving algorithms) is in everything between the user and RAM. CPU to RAM is heavily optimized. The software between RAM and everything else is much more generic and thus under-optimized (especially in terms of utilization) in comparison.

Data queuing, pre-fetching, or streaming isn't anything new but application developers generally let the operating system handle virtual memory, file caching. It does a pretty good job but there are often cases where the application knows more about what it *could* load next which the OS cannot know. Video games often optimize the data loading pipeline which makes other software like [Via](https://www.youtube.com/watch?v=e5wAn-4e5hQ) possible.

My point is not about the real world constraints like mechanical arms of hard drives--I'm not talking about the hardware at all. Software between the user and RAM is often generic (perhaps for the purposes of compatibility) but this also makes it under-optimized. There are interesting hacks in this space. I would argue custom file systems like how [S3 works](https://www.allthingsdistributed.com/2023/07/building-and-operating-a-pretty-big-storage-system.html) is along the same lines.

If we can make the feedback loop between humans and RAM faster then people can compute more (as long as the human brain can keep up).
