Here is how you can setup the car music thing in Tasker:

    State BT Connected (set the bluetooth address of your car)
    => Termux:Tasker path to a script with the music command*, uncheck the box that says "Wait for result of commands"

*my config here is a little complicated because I use the same [function](https://github.com/chapmanjacobd/phone/blob/main/.config/fish/functions/randmusic.fish) for starting and stopping my house speakers but you could keep it as simple as `mpv --shuffle --no-video ~/Music`.

I also set my Media Volume right after that in Tasker so it is loud 

When the car turns off you could turn the Media Volume back down and run `pkill mpv` via an **Exit Task** to that same Tasker profile

The Termux Android API does [not yet have support to detect Media Key](https://github.com/termux/termux-api/issues/61) buttons so if your car has the next song button and you want to use that you can setup another Tasker Profile likeso:

    State BT Connected (set the bluetooth address of your car)
    + State Media Button Next
    => Termux:Tasker path to a script with a next music command*

In this case you will need to start mpv with input-ipc-server configured but it is pretty easy to setup. It is just a file socket that needs to be the same when starting mpv and [when sending a command](https://github.com/chapmanjacobd/phone/blob/main/.config/fish/functions/nextSong.fish). The command in this case being `playlist-next force`
