wget2 works very well for simple sites: https://github.com/rockdaboot/wget2

> My dream would be something that can handle (mostly) everything, including website-specific handlers like yt-dlp. Just a web interface where I can put in a link, set whether to do recursive grabbing and if it can follow outside links.

> But ideally I'd like something that can make WARCs

I doubt something exists which does everything you want _the way that you want it_. Not that WARCs or singlefiles are bad--they are just somewhat opinionated. I think you would be happy with a small site or script that you wrote yourself which would then call yt-dlp, gallery-dl, wget2, [single-file CLI](https://github.com/gildas-lormeau/single-file-cli) etc. 

I've done something similar [here](https://github.com/chapmanjacobd/library) but not too interested at the moment in adding support for singlefile, WARC, etc. And it's not a 100% automated tool, it takes time to learn how to look at a website and decide what content you want from it. But it is faster for me to use on a new site which has weird navigation or behavior than it is to try a bunch of different tools until I find one that works. 

You can also use my spider to feed a [list of URLs into ArchiveBox](https://github.com/ArchiveBox/ArchiveBox/wiki/Quickstart#3-add-your-urls-to-the-archive)--or [just use wget directly](https://github.com/ArchiveBox/ArchiveBox/issues/191#issuecomment-475834386)

ArchiveBox actually maintains a pretty substantial list of [similar projects](https://github.com/ArchiveBox/ArchiveBox/wiki/Web-Archiving-Community#Web-Archiving-Projects) and [alternatives](https://github.com/ArchiveBox/ArchiveBox/wiki/Web-Archiving-Community#other-archivebox-alternatives). You might have luck there
