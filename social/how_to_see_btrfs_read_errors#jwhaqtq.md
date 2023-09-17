Well... you could do something like 

    printf "loop1\t%s" (journalctl | grep -c 'device loop1): read error corrected')

But I agree with the other commenter. SMART is likely better to track this:

    for dev in /dev/sd*
        echo $dev
        sudo smartctl -A $dev | grep -E 'Reallocated_Sector_Ct|Reallocated_Event_Count|Current_Pending_Sector|Offline_Uncorrectable'
    end
