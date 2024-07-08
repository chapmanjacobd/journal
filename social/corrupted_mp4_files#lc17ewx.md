You could try ffmpeg:

    ffmpeg -err_detect ignore_err -i video.mkv -c copy video_fixed.mkv

https://www.stellarinfo.com/blog/repair-corrupt-videos-using-ffmpeg/

But if the video isn't even playing a little bit in mpv or MPC-HC it is probably not decodable--but you could still try the above ffmpeg command and see
