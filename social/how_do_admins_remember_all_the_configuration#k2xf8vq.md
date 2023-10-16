Etckeeper exists.

For servers the age of managing everything from containers is already in the mainstream. So ideally you would not edit any live systems. Integrate changes by replacing everything.

For desktop it's pretty easy to make your whole home folder into a git repo: 

https://github.com/chapmanjacobd/computer/

I do that for my phone too: 

https://github.com/chapmanjacobd/phone/

And if you don't use etckeeper you can programmatically edit system files such that they are still copied into a version control system; like this fish shell function:

    function edit
        set sp (path normalize ~/.github/"$argv")
    
        sudo nano "$argv"
    
        mkdir -p (path dirname "$sp")
        sudo rsync --chown=(stat -c '%U:%G' (path dirname "$sp")) "$argv" "$sp"
    end
