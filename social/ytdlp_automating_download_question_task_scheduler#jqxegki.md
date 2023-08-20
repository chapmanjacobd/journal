Here is one option that you can consider. It is how I do it

one time setup:

    pip install xklb
    lb tubeadd educational.db $(cat list_of_educational_channel_or_playlist_URLs)

Then schedule a batch or powershell script:

    lb tubeupdate educational.db && lb download educational.db --video --prefix ./my_edu_videos/

Since you don't see the error. Try running the command manually before copy/pasting it into Task Scheduler or run the above with `-vv` and it should keep the terminal window open when there is an error:

    lb download educational.db --video --prefix ./my_edu_videos/ -vv
