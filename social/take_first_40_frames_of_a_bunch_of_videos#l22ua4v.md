You could probably use fd-find:

    fd -eMP4 -x ffmpeg -i {} -frames:v 40 -c copy ../credits/{/}

or GNU Parallel:

    fd -eMP4 | parallel ffmpeg -i {} -frames:v 40 -c copy ../credits/{/}

- https://github.com/sharkdp/fd?tab=readme-ov-file#placeholder-syntax
- https://www.gnu.org/software/parallel/
- https://www.gnu.org/software/parallel/parallel_cheat.pdf
