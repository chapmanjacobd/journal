> so yt-dlp.exe --cookies-from-browser firefox then the link should work?

yes. If you are using the default profile in firefox and are signed in to the site it will grab the cookies from firefox.

> --cookies-from-browser BROWSER[+KEYRING][:PROFILE][::CONTAINER]
                                The name of the browser to load cookies
                                from. Currently supported browsers are:
                                brave, chrome, chromium, edge, firefox,
                                opera, safari, vivaldi, whale. Optionally, the
                                KEYRING used for decrypting Chromium cookies
                                on Linux, the name/path of the PROFILE to
                                load cookies from, and the CONTAINER name
                                (if Firefox) ("none" for no container) can
                                be given with their respective seperators.
                                By default, all containers of the most
                                recently accessed profile are used.
