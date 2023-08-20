if you use Fish shell you could likely do something like this (untested):

    function ffmpegToHEVC --argument input
        if test (ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 $input) != "hevc"
            ffmpeg -i "$input" -c:v libx265 -c:a copy -x265-params crf=25 "$input.x265.mkv" && rm "$input"
        end
    end

Then use fd-find or GNU Parallel to batch everything in one go
