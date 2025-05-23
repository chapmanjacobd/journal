# PhotoPrism, LibrePhotos, and Damselfly

I chose to compare PhotoPrism, LibrePhotos, and Damselfly, because they seemed like the strongest freely available candidates for a large library of photographs.

I am mostly interested in face clustering (DBSCAN) and other "AI" capabilities like auto-categorization. Import speed is not as important to me as "playback" speed. I don't mind if it takes a few days but once everything is indexed and processed then it should be fast to explore everything.

The dataset that I used for this comparison was under 22GiB but over 750,000 images. Mostly AVIF files but some PNG and some JPEG.

- PhotoPrism
- LibrePhotos
- Damselfly

## Ease of installation

All three were pretty easy to get started. I liked that damselfly automatically started scanning. But I don't like that it starts a bunch of folder watchers (inotify, etc) and there doesn't seem to be an option to disable that.

So far, I have the most to complain about PhotoPrism:

I disliked that PhotoPrism creates a sidecar YAML file for each image--though it does save this in the PhotoPrism Storage folder rather than mucking up your Originals folder--so I know it could be worse! However, this can be disabled with `PHOTOPRISM_SIDECAR_YAML="false"`. But it is enabled by default!

It also seems weird that PHOTOPRISM_DISABLE_CHOWN is enabled by default, or even an option at all. LibrePhotos is more sane in this regard where there are a couple chmod commands [in the LibrePhotos documentation](https://docs.librephotos.com/docs/user-guide/faq#videos-are-not-playing-and-showing-a-404-error) that you can run _if_ it is a problem.

Enabling WAL mode for the PhotoPrism SQLite DB sped up the import process a bit but it did seem to be the slowest of the three. However, they do recommend to use MariaDB for larger collections so I will delete everything and rescan with that for a more fair evaluation of playback performance.

However, PhotoPrism's documentation is a lot more well-written than LibrePhotos--both in terms of detail and terseness. And Damselfly doesn't even have a proper documentation site... nothing wrong with a bunch of markdown files but what exists is pretty sparse. So PhotoPrism is definitely winning on the documentation front!

The only other complaint that I have at this point is that LibrePhotos requires docker-compose--although the happy path is well-trod and things _just work_. If anything, infrastructure seems the most robust for LibrePhotos because more of the moving parts seem to be separated cleanly (by HTTP). So my complaint here is really just a complaint against YAML: 127.0.0.1:3000:80 is not the same as "127.0.0.1:3000:80".

## Metadata space used

PhotoPrism makes 8 JPEG thumbnails with different crop/aspect ratio: center, left, right, fit, etc. This can add up but mostly in terms of file counts.

LibrePhotos generates 3 WebP thumbnails for each original: big, square, and square_small. In theory, these should be smaller in file size; however, the thumbnail size was about 3x the size of my original photos: 58 GiB in my case.

LibrePhotos also dumps all the photos into the same folder which is a big no-no. To contrast, PhotoPrism puts the thumbnails in three nested folders based on the first three chars of the hash used for the filename of the thumbnail. Damselfly retains the path of the original photos relative to the `/pictures` folder.

Damselfly generates, or at least saves, only one thumbnail per photo, as JPEG. Damselfly has the smallest cache so I would say that it won this round!

## Metadata extraction and features

PhotoPrism automatic object detection labeling is not very good but better than nothing. Face clustering is great but face _detection_ is terrible.

LibrePhotos has much better face detection! It found 10x as many faces than PhotoPrism. It also has a really neat Face Clusters scatter plot. But LibrePhotos didn't use EXIF or file modified date when indexing the photos :/

Damselfly has more advanced filtering options like the ability to see photos that don't have faces, portrait or landscape orientation, etc. The LibrePhotos interface is a bit cleaner but Damselfly has more core functionality.

Right now, I'd only recommend Damselfly.
