Yeah this is working on my machine. I'm using 6.1.1 but it should work with ffmpeg v5, etc too:

    ffmpeg -i SC1ATK4.mov -c:v copy -filter_complex "[0:a:0][0:a:1]join=inputs=2:channel_layout=stereo" test.mov
    [aist#0:0/pcm_s24le @ 0x55db29aaa0c0] Guessed Channel Layout: mono
    [aist#0:1/pcm_s24le @ 0x55db29aaab40] Guessed Channel Layout: mono
    size=    8770kB time=00:00:01.74 bitrate=41069.6kbits/s speed=21.2x    

    ffprobe test.mov
    Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'test.mov':
      Metadata:
        major_brand     : qt  
        minor_version   : 512
        compatible_brands: qt  
        encoder         : Lavf60.16.100
      Duration: 00:00:01.76, start: 0.000000, bitrate: 40911 kb/s
      Stream #0:0[0x1]: Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 128 kb/s (default)
        Metadata:
          handler_name    : SoundHandler
          vendor_id       : [0][0][0][0]
      Stream #0:1[0x2](eng): Video: prores (Standard) (apcn / 0x6E637061), yuv422p10le(bottom coded first (swapped)), 720x486, 40765 kb/s, 30.18 fps, 29.97 tbr, 11988 tbn (default)
        Metadata:
          handler_name    : Core Media Video
          vendor_id       : FFMP
          encoder         : Apple ProRes 422
          timecode        : 03:13:34:02
      Stream #0:2[0x3](eng): Data: none (tmcd / 0x64636D74), 0 kb/s
        Metadata:
          handler_name    : Core Media Video
          timecode        : 03:13:34:02
    Unsupported codec with id 0 for input stream 2

Although, ffmpeg chooses AAC 128kbps for the output in this case. I'm not sure why it does that. 

Making the audio format explicit is necessary here to get the highest quality:

    ffmpeg -i SC1ATK4.mov -c:v copy -filter_complex "[0:a:0][0:a:1]join=inputs=2:channel_layout=stereo" -c:a pcm_s24le test.mov

then the audio stream in the output file looks like this:

      Stream #0:0[0x1]: Audio: pcm_s24le (in24 / 0x34326E69), 48000 Hz, stereo, s32 (24 bit), 2304 kb/s (default)
        Metadata:
          handler_name    : SoundHandler
          vendor_id       : [0][0][0][0]

These files should work fine but I do think it is abnormal(but maybe not too uncommon) for the audio track to be the first stream. To "fix" this you can map explicitly in the order that you want, which is usually video, audio, subtitles, and then extra data like timecode. But it looks like ffmpeg preserves the timecode whether or not you explicitly map it (`-map 0:d`):

    ffmpeg -i SC1ATK4.mov -c:v copy -filter_complex "[0:a:0][0:a:1]join=inputs=2:channel_layout=stereo[a]" -c:a pcm_s24le -map 0:v -map [a] test.mov
    [aist#0:0/pcm_s24le @ 0x560d8a0c71c0] Guessed Channel Layout: mono
    [aist#0:1/pcm_s24le @ 0x560d8a0c7c40] Guessed Channel Layout: mono
    File 'test.mov' already exists. Overwrite? [y/N] y
    size=    9236kB time=00:00:01.74 bitrate=43315.9kbits/s speed=75.1x    
    1266 0.9s ~/Downloads 🌍 ffprobe test.mov
    Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'test.mov':
      Metadata:
        major_brand     : qt  
        minor_version   : 512
        compatible_brands: qt  
        encoder         : Lavf60.16.100
      Duration: 00:00:01.76, start: 0.000000, bitrate: 43083 kb/s
      Stream #0:0[0x1](eng): Video: prores (Standard) (apcn / 0x6E637061), yuv422p10le(bottom coded first (swapped)), 720x486, 40765 kb/s, 30.18 fps, 29.97 tbr, 11988 tbn (default)
        Metadata:
          handler_name    : Core Media Video
          vendor_id       : FFMP
          encoder         : Apple ProRes 422
          timecode        : 03:13:34:02
      Stream #0:1[0x2]: Audio: pcm_s24le (in24 / 0x34326E69), 48000 Hz, stereo, s32 (24 bit), 2304 kb/s (default)
        Metadata:
          handler_name    : SoundHandler
          vendor_id       : [0][0][0][0]
      Stream #0:2[0x3](eng): Data: none (tmcd / 0x64636D74), 0 kb/s
        Metadata:
          handler_name    : Core Media Video
          timecode        : 03:13:34:02

edit:

Also, one final thing to be aware of is I'm assuming that the first audio stream is left channel. If it is actually right channel you would want to use `[0:a:1][0:a:0]` instead of `[0:a:0][0:a:1]`
