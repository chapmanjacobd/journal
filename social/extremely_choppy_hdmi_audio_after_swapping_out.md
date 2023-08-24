I went from an Intel 10400 to a 13600K**F**. On the 10400 I never experienced issues with audio (maybe because I had intel hardware acceleration but don't now?).

I was running Fedora 36 and that has been working great for a year or so and I swapped the nvme drive into the new motherboard and everything works normally except for the audio out of the RX 570 HDMI port. 

Before moving to the new motherboard the audio was never choppy but now it plays for 400~1400ms then I don't hear any audio for 200~1200ms and it repeats kinda randomly like that and it doesn't stop chopping up the audio (like it thinks it is Iron Chef).

I'm out of ideas. I get the same behavior in Fedora 37 LiveUSB.

I will now describe some strange things that I've noticed: It's choppy when I play a YouTube video, but playing a local video in mpv does not sound choppy (95% of the time; depends on video codec)--BUT when playing local audio in mpv (opus codec), I get lots of choppyness. To make my troubleshooting even more confusing, I noticed that the audio is crystal clear without any choppiness if I play a local video file at the same time as the local audio file or the YouTube video! I've tested this several times: play local video in mpv--no choppiness in any HDMI audio (YouTube, local video, or local audio file)--pause the local video--choppiness in both YouTube and local audio file playback !!

I've tried resetting the settings in the UEFI, but it does not seem to have any affect. All audio playback is normal (not choppy) when playing through integrated 3.5mm jack.

If it helps, I also found out I had ALCS1200A before but now ALC897, but nothing else interesting in `sudo journalctl --grep="hda_codec"`

Earlier today I updated to Fedora 37 and that process was very smooth and uneventful. It only took twenty minutes with dnf system-upgrade but the behavior has not changed.

I did not test it extensively but audio playback through HDMI seemed fine in Windows 10, YouTube

Edit: 

- Set `intel_idle.max_cstate=0` (and rebooting, checked that it was there with `cat /proc/cmdline`); still choppy
- Set `snd_hda_intel` power_save to 0; still choppy
- I tried turning off snooping, power_save, and disabling msi but no dice.
- I tried setting dmic_detect=0, and position_fix=1
- I tried a bunch of different models and rebooting each time (including auto, basic, alc891-headset, clevo-p950, asrock-mobo, asus-mobo, ...)
- I tried this echo 1000000 | sudo tee /sys/module/snd_hda_intel/parameters/power_save
- I tried setting pcie_aspm.policy=performance
- Nothing has fixed the stuttering

        $ cat /etc/modprobe.d/hdmi_audio_fix.conf
        options snd_hda_intel enable_msi=0 power_save=0 power_save_controller="N" snoop=0

        $ systool -vm snd_hda_intel
        Module = "snd_hda_intel"

        Attributes:
            coresize            = "61440"
            initsize            = "0"
            initstate           = "live"
            refcnt              = "4"
            taint               = ""
            uevent              = <store method only>

        Parameters:
            align_buffer_size   = "-1"
            bdl_pos_adj         = "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1"
            beep_mode           = "N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N,N"
            dmic_detect         = "Y"
            enable_msi          = "0"
            enable              = "Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y,Y"
            id                  = "(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null)"
            index               = "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1"
            jackpoll_ms         = "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
            model               = "(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null)"
            patch               = "(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null),(null)"
            pm_blacklist        = "Y"
            position_fix        = "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1"
            power_save          = "0"
            power_save_controller= "N"
            probe_mask          = "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1"
            probe_only          = "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
            single_cmd          = "-1"
            snoop               = "0"

works referenced:

- [https://archive.vn/o/o4q3X/https://bbs.archlinux.org/viewtopic.php?id=181764](https://archive.vn/o4q3X)
- [kernel.org hd audio notes](https://www.kernel.org/doc/html/v4.16/sound/hd-audio/notes.html#hd-audio-controller)
