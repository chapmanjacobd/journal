I use this [ffprobe class](https://gist.github.com/chapmanjacobd/e8282dbc1d54a49950b1faeab645f9ae) and then compare with the input:

    assert original.duration == output.duration
    assert original.has_video == output.has_video
    assert original.has_audio == output.has_audio

But this won't catch everything. If you are paranoid, you could also scan the output file like this: https://gist.github.com/chapmanjacobd/7333baa69f0d271560ad11b4d8ab43f1 but it will be slow
