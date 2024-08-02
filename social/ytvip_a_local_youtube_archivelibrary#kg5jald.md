ytvip/ytcl might be preferable for viewing the downloaded videos in a browser but if you are downloading many playlists/channels I wrote something that helps with that. 

- [xklb](https://github.com/chapmanjacobd/library) separates the playlists iterating part from the actual downloading part so it might be more robust than other downloading options. 
- It also manages yt-dlp errors based on if something is permanently unavailable or temporarily / geolocked. If something can be retried it will be queued up to retry every two weeks. You can modify this via `lb dl --retry-delay '1 month'`
- It will also check playlists less often when there are no new videos, and it will check more frequently when there are new videos.
