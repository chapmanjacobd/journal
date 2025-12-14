I like integrating with systemd. Something like this is working well for me:

    $ tree -L 3 ~/.config/containers/
    .config/containers/
    ├── compose
    │  └── projects
    │      └── immich.env
    └── templates
        └── immich
            ├── data
            └── docker-compose.yml

    6 directories, 2 files

You can use `podman-compose systemd -a register` to set this up. Then when you run something like `systemctl --user enable --now podman-compose@immich` it will also start the docker-compose containers when you reboot
