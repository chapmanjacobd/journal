ffmpeg is probably the best option. You can use the concat filter to merge multiple files together. I've never sped up videos but you'll want to use something like rubberband so that it doesn't sound like Alvin and the Chipmunks when speeding up:

    for video in "${videos[@]}"; do
        # Apply 2x speed with rubberband filter to reduce pitch
        processed_video="${video%.mp4}_processed.mp4"
        ffmpeg -i "$video" -filter_complex \
        "[0:v]setpts=0.5*PTS[v]; \
         [0:a]rubberband=pitch=2.0[a]" \
        -map "[v]" -map "[a]" -c:v libx264 -c:a aac "$processed_video"
        
        # Add the processed video to the list
        echo "file '$processed_video'" >> $temp_list
    done
    
    # Concatenate the processed videos
    ffmpeg -f concat -safe 0 -i $temp_list -c copy "final_output.mp4"

Also, if it's something like a bunch of talking heads, you might consider using [Auto-Editor](https://auto-editor.com/). Easily trims out the silence of boring presentations. It's pretty easy to use. Took my brother's funeral video from 2 hours to 30 minutes and it didn't seem unnatural at all. Less umms and awkward silence.
