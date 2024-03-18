If you know a little bit of python it might not difficult to write a small extractor. 

Here's an example that downloads a video [directly from a site](https://github.com/chapmanjacobd/library/blob/main/xklb/scratch/javtiful.py). Here's another example that [passes a "master playlist" URL to ffmpeg](https://github.com/chapmanjacobd/library/blob/main/xklb/scratch/javguru.py)--you could pass it to yt-dlp instead. If you need cookies you can [re-use the yt-dlp code to get cookies from the browser](https://github.com/chapmanjacobd/library/blob/fc5cb5651fe2d1a3624ac85e21491cc9f3ceed5f/xklb/utils/web.py#L72) and inject them into `requests`.

You could create a [yt-dlp plugin](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#plugins), for example [ttuser](https://github.com/bashonly/yt-dlp-TTUser/tree/master)--but I think this is more difficult to get started
