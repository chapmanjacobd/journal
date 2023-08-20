hmmm


    ~ 🌛 journalctl -b | grep -E 'snd|hda|audio'
    Feb 28 22:33:51 fedora kernel: snd_hda_intel 0000:00:1f.3: enabling device (0004 -> 0006)
    Feb 28 22:33:51 fedora kernel: snd_hda_intel 0000:01:00.1: Force to non-snoop mode
    Feb 28 22:33:51 fedora kernel: snd_hda_intel 0000:01:00.1: bound 0000:01:00.0 (ops amdgpu_dm_audio_component_bind_ops [amdgpu])
    Feb 28 22:33:51 fedora kernel: snd_hda_codec_realtek hdaudioC0D0: ALCS1200A: SKU not ready 0x00000000
    Feb 28 22:33:51 fedora kernel: snd_hda_codec_realtek hdaudioC0D0: autoconfig for ALCS1200A: line_outs=1 (0x14/0x0/0x0/0x0/0x0) type:line
    Feb 28 22:33:51 fedora kernel: snd_hda_codec_realtek hdaudioC0D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
    Feb 28 22:33:51 fedora kernel: snd_hda_codec_realtek hdaudioC0D0:    hp_outs=1 (0x1b/0x0/0x0/0x0/0x0)
    Feb 28 22:33:51 fedora kernel: snd_hda_codec_realtek hdaudioC0D0:    mono: mono_out=0x0
    Feb 28 22:33:51 fedora kernel: snd_hda_codec_realtek hdaudioC0D0:    inputs:
    Feb 28 22:33:51 fedora kernel: snd_hda_codec_realtek hdaudioC0D0:      Front Mic=0x19
    Feb 28 22:33:51 fedora kernel: snd_hda_codec_realtek hdaudioC0D0:      Rear Mic=0x18
    Feb 28 22:33:51 fedora kernel: snd_hda_codec_realtek hdaudioC0D0:      Line=0x1a

    Feb 28 22:44:59 fedora plasmashell[1873]: org.kde.plasma.pulseaudio: context kaput
    Feb 28 22:45:05 fedora plasmashell[1873]: org.kde.plasma.pulseaudio: context kaput
    Feb 28 22:45:05 fedora systemsettings5[3835]: kf.coreaddons: "Could not load plugin from kcm_pulseaudio: The shared library was not found."
    Feb 28 22:45:05 fedora systemsettings5[3835]: org.kde.plasma.pulseaudio: Settings schema org.freedesktop.pulseaudio.module-group is not installed
    Feb 28 22:45:05 fedora systemsettings5[3835]: org.kde.plasma.pulseaudio: Settings schema org.freedesktop.pulseaudio.module-group is not installed
    Feb 28 22:45:05 fedora systemsettings5[3835]: org.kde.plasma.pulseaudio: Settings schema org.freedesktop.pulseaudio.module-group is not installed
    Feb 28 22:45:11 fedora plasmashell[1873]: org.kde.plasma.pulseaudio: context kaput
    Feb 28 22:45:17 fedora plasmashell[1873]: org.kde.plasma.pulseaudio: context kaput
    Feb 28 22:45:23 fedora plasmashell[1873]: org.kde.plasma.pulseaudio: context kaput
