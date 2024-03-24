I would try using SeaChest utils instead of `dd`

For example, you might try:

    cd SeaChestUtilities/Non-RAID/
    sudo ./SeaChest_Erase_x86_64-redhat-linux -d /dev/sdX --overwrite 0 --overwriteRange 4096
    sudo ./SeaChest_Format_x86_64-redhat-linux -d /dev/sdX --seagateQuickFormat --setSectorSize 4096

Run these one at a time and make sure they complete before trying to access the disk in any way, even SMART, etc otherwise it might end up broken like it is now

After or before doing that:

    sudo ./SeaChest_SMART_x86_64-redhat-linux -d /dev/sdX --conveyanceDST
    watch sudo ./SeaChest_SMART_x86_64-redhat-linux -d /dev/sdX --progress dst
    sudo ./SeaChest_GenericTests_x86_64-redhat-linux -d /dev/sdX --twoMinuteGeneric 
    sudo ./SeaChest_Firmware_x86_64-redhat-linux -d /dev/sdX --fwdlInfo     
    sudo ./SeaChest_Basics_x86_64-redhat-linux -d /dev/sdX --smartCheck  
    sudo ./SeaChest_Info_x86_64-redhat-linux -d /dev/sdX --deviceStatistics    
    sudo ./SeaChest_Basics_x86_64-redhat-linux -d /dev/sdX --smartAttributes analyzed
