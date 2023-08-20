sorry for the late reply. I locked myself out via mdadm + /etc/fstab lol. now I'm back in:

Intel i5 10400

    ~ [5] 👮 sudo lspci 
    00:00.0 Host bridge: Intel Corporation Comet Lake-S 6c Host Bridge/DRAM Controller (rev 05)
    00:01.0 PCI bridge: Intel Corporation 6th-10th Gen Core Processor PCIe Controller (x16) (rev 05)
    00:12.0 Signal processing controller: Intel Corporation Comet Lake PCH Thermal Controller
    00:14.0 USB controller: Intel Corporation Comet Lake USB 3.1 xHCI Host Controller
    00:14.2 RAM memory: Intel Corporation Comet Lake PCH Shared SRAM
    00:16.0 Communication controller: Intel Corporation Comet Lake HECI Controller
    00:17.0 SATA controller: Intel Corporation Comet Lake SATA AHCI Controller
    00:1b.0 PCI bridge: Intel Corporation Comet Lake PCI Express Root Port #21 (rev f0)
    00:1d.0 PCI bridge: Intel Corporation Device 06b2 (rev f0)
    00:1f.0 ISA bridge: Intel Corporation H470 Chipset LPC/eSPI Controller
    00:1f.3 Audio device: Intel Corporation Comet Lake PCH cAVS
    00:1f.4 SMBus: Intel Corporation Comet Lake PCH SMBus Controller
    00:1f.5 Serial bus controller: Intel Corporation Comet Lake PCH SPI Controller
    00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection (11) I219-V
    01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X/590] (rev ef)
    01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere HDMI Audio [Radeon RX 470/480 / 570/580/590]
    02:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller SM981/PM981/PM983
    03:00.0 Network controller: Intel Corporation Wi-Fi 6 AX200 (rev 1a)
    ~ 🌭 sudo lsmod
    Module                  Size  Used by
    ib_core               421888  0
    ntfs3                 266240  0
    nft_objref             16384  1
    nf_conntrack_netbios_ns    16384  1
    nf_conntrack_broadcast    16384  1 nf_conntrack_netbios_ns
    nft_fib_inet           16384  1
    nft_fib_ipv4           16384  1 nft_fib_inet
    nft_fib_ipv6           16384  1 nft_fib_inet
    nft_fib                16384  3 nft_fib_ipv6,nft_fib_ipv4,nft_fib_inet
    nft_reject_inet        16384  6
    nf_reject_ipv4         16384  1 nft_reject_inet
    nf_reject_ipv6         20480  1 nft_reject_inet
    nft_reject             16384  1 nft_reject_inet
    nft_ct                 20480  16
    nft_chain_nat          16384  2
    nf_nat                 57344  1 nft_chain_nat
    nf_conntrack          163840  4 nf_nat,nft_ct,nf_conntrack_netbios_ns,nf_conntrack_broadcast
    nf_defrag_ipv6         24576  1 nf_conntrack
    nf_defrag_ipv4         16384  1 nf_conntrack
    ip_set                 61440  0
    nf_tables             258048  232 nft_ct,nft_reject_inet,nft_fib_ipv6,nft_objref,nft_fib_ipv4,nft_chain_nat,nft_reject,nft_fib,nft_fib_inet
    nfnetlink              20480  3 nf_tables,ip_set
    qrtr                   45056  4
    bnep                   28672  2
    sunrpc                659456  1
    binfmt_misc            24576  1
    snd_sof_pci_intel_cnl    16384  0
    snd_sof_intel_hda_common   106496  1 snd_sof_pci_intel_cnl
    intel_rapl_msr         20480  0
    intel_rapl_common      28672  1 intel_rapl_msr
    soundwire_intel        45056  1 snd_sof_intel_hda_common
    soundwire_generic_allocation    16384  1 soundwire_intel
    soundwire_cadence      40960  1 soundwire_intel
    snd_sof_intel_hda      20480  1 snd_sof_intel_hda_common
    snd_sof_pci            20480  2 snd_sof_intel_hda_common,snd_sof_pci_intel_cnl
    snd_sof_xtensa_dsp     16384  1 snd_sof_intel_hda_common
    iwlmvm                491520  0
    snd_sof               159744  2 snd_sof_pci,snd_sof_intel_hda_common
    soundwire_bus          94208  3 soundwire_intel,soundwire_generic_allocation,soundwire_cadence
    intel_tcc_cooling      16384  0
    snd_soc_skl           180224  0
    x86_pkg_temp_thermal    20480  0
    intel_powerclamp       20480  0
    mac80211             1175552  1 iwlmvm
    snd_soc_hdac_hda       24576  2 snd_sof_intel_hda_common,snd_soc_skl
    iTCO_wdt               16384  0
    snd_hda_ext_core       36864  4 snd_sof_intel_hda_common,snd_soc_hdac_hda,snd_soc_skl,snd_sof_intel_hda
    intel_pmc_bxt          16384  1 iTCO_wdt
    coretemp               20480  0
    ee1004                 20480  0
    iTCO_vendor_support    16384  1 iTCO_wdt
    mei_hdcp               24576  0
    mei_pxp                20480  0
    snd_soc_sst_ipc        20480  1 snd_soc_skl
    snd_soc_sst_dsp        36864  1 snd_soc_skl
    snd_soc_acpi_intel_match    61440  3 snd_sof_intel_hda_common,snd_soc_skl,snd_sof_pci_intel_cnl
    libarc4                16384  1 mac80211
    kvm_intel             360448  0
    raid1                  53248  1
    snd_soc_acpi           16384  3 snd_soc_acpi_intel_match,snd_sof_intel_hda_common,snd_soc_skl
    snd_soc_core          339968  5 soundwire_intel,snd_sof,snd_sof_intel_hda_common,snd_soc_hdac_hda,snd_soc_skl
    kvm                  1028096  1 kvm_intel
    snd_hda_codec_realtek   155648  1
    snd_compress           28672  1 snd_soc_core
    snd_hda_codec_generic    98304  1 snd_hda_codec_realtek
    ac97_bus               16384  1 snd_soc_core
    iwlwifi               380928  1 iwlmvm
    ledtrig_audio          16384  2 snd_hda_codec_generic,snd_sof
    snd_hda_codec_hdmi     73728  1
    snd_pcm_dmaengine      16384  1 snd_soc_core
    irqbypass              16384  1 kvm
    snd_hda_intel          57344  2
    btusb                  65536  0
    rapl                   20480  0
    intel_cstate           20480  0
    snd_intel_dspcfg       28672  3 snd_hda_intel,snd_sof_intel_hda_common,snd_soc_skl
    btrtl                  28672  1 btusb
    snd_intel_sdw_acpi     20480  2 snd_sof_intel_hda_common,snd_intel_dspcfg
    cfg80211             1036288  3 iwlmvm,iwlwifi,mac80211
    intel_uncore          204800  0
    btbcm                  20480  1 btusb
    snd_hda_codec         172032  5 snd_hda_codec_generic,snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec_realtek,snd_soc_hdac_hda
    btintel                45056  1 btusb
    snd_hda_core          110592  10 snd_hda_codec_generic,snd_hda_codec_hdmi,snd_hda_intel,snd_hda_ext_core,snd_hda_codec,snd_hda_codec_realtek,snd_sof_intel_hda_common,snd_soc_hdac_hda,snd_soc_skl,snd_sof_intel_hda
    snd_seq                86016  0
    i2c_i801               36864  0
    pcspkr                 16384  0
    wmi_bmof               16384  0
    intel_wmi_thunderbolt    20480  0
    snd_seq_device         16384  1 snd_seq
    snd_hwdep              16384  1 snd_hda_codec
    i2c_smbus              20480  1 i2c_i801
    bluetooth             692224  28 btrtl,btintel,btbcm,bnep,btusb
    snd_pcm               139264  11 snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec,soundwire_intel,snd_sof,snd_sof_intel_hda_common,snd_compress,snd_soc_core,snd_soc_skl,snd_hda_core,snd_pcm_dmaengine
    ses                    20480  0
    mei_me                 45056  2
    snd_timer              45056  2 snd_seq,snd_pcm
    enclosure              16384  1 ses
    mei                   151552  5 mei_hdcp,mei_pxp,mei_me
    scsi_transport_sas     49152  1 ses
    snd                   110592  17 snd_hda_codec_generic,snd_seq,snd_seq_device,snd_hda_codec_hdmi,snd_hwdep,snd_hda_intel,snd_hda_codec,snd_hda_codec_realtek,snd_sof,snd_timer,snd_compress,snd_soc_core,snd_pcm
    ecdh_generic           16384  2 bluetooth
    joydev                 28672  0
    rfkill                 28672  6 bluetooth,cfg80211
    soundcore              16384  1 snd
    intel_pch_thermal      20480  0
    i2c_multi_instantiate    20480  0
    acpi_pad              184320  0
    acpi_tad               16384  0
    zram                   28672  2
    ip_tables              36864  0
    dm_crypt               61440  1
    hid_logitech_hidpp     49152  0
    hid_logitech_dj        28672  0
    amdgpu               7909376  32
    uas                    32768  0
    usb_storage            81920  3 uas
    drm_ttm_helper         16384  1 amdgpu
    ttm                    81920  2 amdgpu,drm_ttm_helper
    iommu_v2               24576  1 amdgpu
    gpu_sched              49152  1 amdgpu
    i2c_algo_bit           16384  1 amdgpu
    drm_kms_helper        315392  1 amdgpu
    crct10dif_pclmul       16384  1
    crc32_pclmul           16384  0
    crc32c_intel           24576  5
    cec                    69632  1 drm_kms_helper
    nvme                   49152  3
    drm                   634880  16 gpu_sched,drm_kms_helper,amdgpu,drm_ttm_helper,ttm
    e1000e                311296  0
    nvme_core             139264  5 nvme
    ghash_clmulni_intel    16384  0
    wmi                    32768  2 intel_wmi_thunderbolt,wmi_bmof
    video                  57344  0
    i2c_dev                28672  0
    ipmi_devintf           20480  0
    ipmi_msghandler       118784  1 ipmi_devintf
    fuse                  167936  5

    ~ [1] 🃃 pulseaudio -k
    E: [pulseaudio] main.c: Failed to kill daemon: No such process
    ~ [1] 🃍 sudo systemctl start pulseaudio
    Failed to start pulseaudio.service: Unit pulseaudio.service not found.


I noticed that no audio devices were showing up in KDE sound settings--It's just a blank page.

sound works weirdly enough via mpv

    ~ [4] 🌜 mpv d/80_Now_Listening/00_Armful.opus
    Resuming playback. This behavior can be disabled with --no-resume-playback.
    (+) Audio --aid=1 'Armful' (opus 2ch 48000Hz)
    File tags:
    Artist: CASIOPEA 3rd
    Album: A・SO・BO
    Album_Artist: CASIOPEA 3rd
    Comment: http://www.alljpop.info Promo
    Date: 2015
    Genre: J-Pop
    Title: Armful
    [ao/pulse] Init failed: Invalid server
    ALSA lib pulse.c:242:(pulse_connect) PulseAudio: Unable to connect: Invalid server

    [ao/alsa] Playback open error: Connection refused
    AO: [jack] 48000Hz stereo 2ch floatp
