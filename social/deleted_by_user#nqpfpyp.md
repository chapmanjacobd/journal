> [youtube] [jsc:deno] Solving JS challenges using deno

Means that it is using deno successfully but next time use -vv. The earlier lines reveal more information: 

    ...
    [debug] yt-dlp version nightly@2025.11.03.233024 from yt-dlp/yt-dlp-nightly-builds [ffb7b7f44] (pip)
    ...
    [debug] Optional libraries: ..., yt_dlp_ejs-0.3.0
    ...
    [debug] JS runtimes: deno-2.5.6
    ...
    [debug] [youtube] [jsc] JS Challenge Providers: bun (unavailable), deno, node (unavailable), quickjs (unavailable)
    ...
    [youtube] [jsc:deno] Solving JS challenges using deno
    [debug] [youtube] [jsc:deno] Using challenge solver lib script v0.3.0 (source: python package, variant: minified)
    [debug] [youtube] [jsc:deno] Using challenge solver core script v0.3.0 (source: python package, variant: minified)
    [debug] [youtube] [jsc:deno] Running deno: deno run --ext=js --no-code-cache --no-prompt --no-remote --no-lock --node-modules-dir=none --no-config --no-npm --cached-only -
    ...

https://github.com/openzim/python-scraperlib/issues/268#issuecomment-3491797329
