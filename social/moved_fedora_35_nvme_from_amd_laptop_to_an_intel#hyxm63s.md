the system seems a lot more responsive after running:

    sudo dracut -v -f

after reinstalling pipewire audio started working again in firefox

    dnf erase pulseaudio
    dnf install --allowerasing wireplumber pipewire-pulseaudio pipewire-plugin-jack
                                                                                                                                      
  set -e PULSE_SERVER                                                                                                                                                        
  set -eg PULSE_SERVER                                                                                                                                                        
  set -eU PULSE_SERVER

Do you know if `nvme_core.default_ps_max_latency_us=0` causes excessive wear? Maybe I don't need to disable APST after all. I don't mind wasting some electricity but not if the SSD will last longer if I give it some e-cig breaks
