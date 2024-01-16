Yes. if you enable both `recursive` and `manual` mode.

But qbittorrent will still delete the torrent file when it loads it. However, you could create a folder of torrents that mirrors the download file tree and then rsync or rclone copy that folder of torrents into the qbittorrent watch folder. It will ignore torrents already loaded
