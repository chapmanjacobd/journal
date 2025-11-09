I upgraded three machines last night and it went mostly smooth as butter:

Along with wine\\\* I had to remove LabPlot to be able to successfully run `sudo dnf system-upgrade download --releasever=43` and `sudo dnf5 offline reboot`

On my laptop I saw the offline update screen start so I closed the lid but several hours later I went to check on it and realized that it was sleeping so I left it lid open and it continued updating. My user's display manager settings is Do Nothing on lid close but maybe that's not a system-wide setting.

On one headless machine I think it was hanging at shutdown. I plugged in a HDMI to USB-C cable to check the display on my phone via nExt Camera but didn't see any image output. After I force powered it off, waited 20 seconds, and powered it back on I saw the BIOS load and then the "Installing Updates" offline update screen so I went to bed. When I woke up the next morning everything is running fine and it is on Fedora 43. It looks like updating took 20~30 mins based on the uptime now.

Ah yes, `journalctl -b -2 -r`

    Oct 31 01:29:39 backup kernel: nouveau 0000:01:00.0: [drm] fb0: nouveaudrmfb frame buffer device
    Oct 31 01:29:39 backup kernel: Console: switching to colour frame buffer device 160x45
    Oct 31 01:29:39 backup kernel: fbcon: nouveaudrmfb (fb0) is primary device
    Oct 31 01:29:29 backup kernel: nouveau 0000:01:00.0: drm: DDC responded, but no EDID for HDMI-A-1
    Oct 31 01:25:34 backup kernel: e1000e 0000:00:1f.6 eno1: NIC Link is Up 1000 Mbps Full Duplex, Flow Control: Rx/Tx
    Oct 31 01:25:20 backup kernel: e1000e 0000:00:1f.6 eno1: NIC Link is Down
    Oct 30 23:45:26 backup systemd-udevd[3414503]: 0:42: Worker [1428214] processing SEQNUM=12813 killed
    Oct 30 23:44:32 backup kernel: audit: type=1334 audit(1761885872.198:200700): prog-id=8914 op=UNLOAD
    Oct 30 23:44:32 backup kernel: audit: type=1334 audit(1761885872.193:200699): prog-id=8915 op=UNLOAD
    Oct 30 23:44:32 backup kernel: audit: type=1334 audit(1761885872.193:200698): prog-id=8916 op=UNLOAD
    Oct 30 23:44:32 backup kernel: audit: type=1334 audit(1761885872.192:200697): prog-id=8904 op=UNLOAD
    Oct 30 23:44:32 backup kernel: audit: type=1334 audit(1761885872.192:200696): prog-id=8905 op=UNLOAD
    Oct 30 23:44:32 backup kernel: audit: type=1334 audit(1761885872.191:200695): prog-id=8900 op=UNLOAD
    Oct 30 23:44:32 backup kernel: audit: type=1334 audit(1761885872.191:200694): prog-id=8901 op=UNLOAD
    Oct 30 23:44:32 backup kernel: audit: type=1131 audit(1761885872.181:200693): pid=1 uid=0 auid=4294967295 ses=42949672>
    Oct 30 23:44:32 backup kernel: audit: type=1130 audit(1761885872.181:200692): pid=1 uid=0 auid=4294967295 ses=42949672>
    Oct 30 23:44:32 backup systemd[1]: Shutting down.
    Oct 30 23:44:32 backup systemd[1]: Reached target reboot.target - System Reboot.

Slightly interesting snippets from `journalctl -b -1`

    Oct 31 01:49:17 backup dnf5[918]: [8183/8184] Removing ncurses-base-0:6.5 100% |   7.3 KiB/s | 179.0   B |  00m00s
    Oct 31 01:49:17 backup dnf5[918]: /usr/sbin cannot be merged yet, found /usr/sbin/capsh
    Oct 31 01:49:19 backup systemd[1]: Reexecution requested from client PID 37507 ('systemctl') (unit dnf5-offline-
    ...
    Oct 31 01:50:46 backup systemd[1]: Reloaded user@1000.service - User Manager for UID 1000.
    Oct 31 01:50:46 backup systemd[1]: Got disconnect on API bus.
    Oct 31 01:50:52 backup systemd[1]: man-db-cache-update.service: Deactivated successfully.
    Oct 31 01:50:52 backup systemd[1]: Finished man-db-cache-update.service.
    Oct 31 01:50:52 backup systemd[1]: man-db-cache-update.service: Consumed 6.738s CPU time, 226.2M memory peak.
    Oct 31 01:50:52 backup systemd[1]: run-p52817-i52818.service: Deactivated successfully.
    Oct 31 01:51:25 backup systemd[1]: Started run-p54247-i54248.service - [systemd-run] /usr/bin/systemctl start man-db-c>
    Oct 31 01:51:25 backup systemd[1]: Starting man-db-cache-update.service...
    Oct 31 01:51:26 backup systemd[1]: man-db-cache-update.service: Deactivated successfully.
    Oct 31 01:51:26 backup systemd[1]: Finished man-db-cache-update.service.
    Oct 31 01:51:26 backup systemd[1]: run-p54247-i54248.service: Deactivated successfully.
    Oct 31 01:51:28 backup dnf5[918]: [8184/8184] Removing libgcc-0:15.2.1-3. 100% |   0.0   B/s |  11.0   B |  02m11s
    Oct 31 01:51:28 backup dnf5[918]: Warning: skipped OpenPGP checks for 4130 packages from repositories: fedora, fedora->
    Oct 31 01:51:28 backup dnf5[918]: Transaction complete! Cleaning up and rebooting...
