I have two and they work good. Not too loud.

If you order on Amazon be aware that some sellers sell drives with no warranty. HyperHawk was good. 5 years warranty with Seagate. Tech on Tech did not have a Seagate warranty but they said they would provide 2-year seller warranty. ANYHDD did not provide any seller warranty and no Seagate warranty. So I returned the drive from ANYHDD. 

When you get the drive do a two minute conveyance test and make sure TLER is enabled:


    cd bin/SeaChestUtilities/Non-RAID/
    sudo ./SeaChest_SMART_x86_64-redhat-linux -d /dev/sdX --conveyanceDST
    sudo ./SeaChest_SMART_x86_64-redhat-linux -d /dev/sdX --progress dst

    sudo ./SeaChest_GenericTests_x86_64-redhat-linux -d /dev/sdX --twoMinuteGeneric


    for d in /dev/sd?
        echo $d
        sudo smartctl -l scterc $d
    end

ENABLE if not enabled with sudo smartctl -l scterc,100,100 /dev/sdX


check that the firmware is up to date. if not follow the instructions on Seagate's website to update the FW

    sudo ./SeaChest_Firmware_x86_64-redhat-linux -d /dev/sdX --fwdlInfo

    sudo ./SeaChest_Basics_x86_64-redhat-linux -d /dev/sdX --smartCheck
    sudo ./SeaChest_Info_x86_64-redhat-linux -d /dev/sdX --deviceStatistics
    sudo ./SeaChest_Basics_x86_64-redhat-linux -d /dev/sdX --smartAttributes analyzed

    sudo ./SeaChest_Format_x86_64-redhat-linux -d /dev/sdX --seagateQuickFormat --setSectorSize 4096
    sudo ./SeaChest_Configure_x86_64-redhat-linux -d /dev/sdX --lowCurrentSpinup low

    sudo ./SeaChest_Configure_x86_64-redhat-linux -d /dev/sdX --puisFeature enable

With that much data in a single disk I would recommend doing RAID1. If you only have the 8TB and a recent kernel, you can use BTRFS with both drives and it can run RAID1 for the 8TB portion of the 18TB exos with your 8TB Barracuda. The remaining 10TB will be treated as degraded RAID and you wouldn't be able to recover it if your Exos failed. If you are on windows you can use SnapRAID or FreeFileSync
