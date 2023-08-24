in journalctl I get a lot of these logs:

    Feb 28 18:35:55 fedora plasmashell[2271]: org.kde.plasma.pulseaudio: context kaput
    Feb 28 18:36:01 fedora plasmashell[2271]: org.kde.plasma.pulseaudio: context kaput

here are my interrupts...


    CPU0       CPU1       CPU2       CPU3       CPU4       CPU5       CPU6       CPU7       CPU8       CPU9       CPU10      CPU11      
    0:         12          0          0          0          0          0          0          0          0          0          0          0  IR-IO-APIC    2-edge      timer
    8:          0          0          0          0          0          0          0          1          0          0          0          0  IR-IO-APIC    8-edge      rtc0
    9:          0          0          0          0          0          0          0          0          0          0          0          0  IR-IO-APIC    9-fasteoi   acpi
    16:          0          0          0          0          0          0          0          0          0          0          0          4  IR-IO-APIC   16-fasteoi   i801_smbus
    120:          0          0          0          0          0          0          0          0          0          0          0          0  DMAR-MSI    0-edge      dmar0
    124:          0          0          0          0          0        988     284393          0          0          0          0          0  IR-PCI-MSI 376832-edge      ahci[0000:00:17.0]
    125:          0    2208072          0          0          0          0       1313          0          0          0          0          0  IR-PCI-MSI 327680-edge      xhci_hcd
    126:          0          0          0          0          0          0          0          0         30          0         56          0  IR-PCI-MSI 1048576-edge      nvme0q0
    127:     184954          0          0          0          0          0          0          0          0          0          0          0  IR-PCI-MSI 1048577-edge      nvme0q1
    128:          0     171760          0          0          0          0          0          0          0          0          0          0  IR-PCI-MSI 1048578-edge      nvme0q2
    129:          0          0     154397          0          0          0          0          0          0          0          0          0  IR-PCI-MSI 1048579-edge      nvme0q3
    130:          0          0          0     159620          0          0          0          0          0          0          0          0  IR-PCI-MSI 1048580-edge      nvme0q4
    131:          0          0          0          0     153556          0          0          0          0          0          0          0  IR-PCI-MSI 1048581-edge      nvme0q5
    132:          0          0          0          0          0     175089          0          0          0          0          0          0  IR-PCI-MSI 1048582-edge      nvme0q6
    133:          0          0          0          0          0          0     166343          0          0          0          0          0  IR-PCI-MSI 1048583-edge      nvme0q7
    134:          0          0          0          0          0          0          0     173505          0          0          0          0  IR-PCI-MSI 1048584-edge      nvme0q8
    135:          0          0          0          0          0          0          0          0     166200          0          0          0  IR-PCI-MSI 1048585-edge      nvme0q9
    136:          0          0          0          0          0          0          0          0          0     162000          0          0  IR-PCI-MSI 1048586-edge      nvme0q10
    137:          0          0          0          0          0          0          0          0          0          0     144583          0  IR-PCI-MSI 1048587-edge      nvme0q11
    138:          0          0          0          0          0          0          0          0          0          0          0     163042  IR-PCI-MSI 1048588-edge      nvme0q12
    139:          0          0          0          0          0          0          0          0          0        447    3757193          0  IR-PCI-MSI 524288-edge      amdgpu
    140:          0          0          0          0          0          0          0          0          0          0         51          0  IR-PCI-MSI 360448-edge      mei_me
    141:          0        289          0          0    9372058          0          0          0          0          0          0          0  IR-PCI-MSI 520192-edge      eno1
    142:       5994          0        102          0          0          0          0          0          0          0          0          0  IR-PCI-MSI 1572864-edge      iwlwifi:default_queue
    143:          0          0          0          0          0          0          0          0          0          0        236          0  IR-PCI-MSI 1572865-edge      iwlwifi:queue_1
    144:          0          0          0          0          0          0          0          0          0        617          0          0  IR-PCI-MSI 1572866-edge      iwlwifi:queue_2
    145:          0          0          0          0          0          0        114          0          0          0          0          0  IR-PCI-MSI 1572867-edge      iwlwifi:queue_3
    146:          0          0          0          0          0          0          0          0          0          0          0        684  IR-PCI-MSI 1572868-edge      iwlwifi:queue_4
    147:          0          0          0        283          0          0          0          0          0          0          0          0  IR-PCI-MSI 1572869-edge      iwlwifi:queue_5
    148:          0          0          0          0          0          0          0          0          0        679          0          0  IR-PCI-MSI 1572870-edge      iwlwifi:queue_6
    149:          0       1017          0          0          0          0          0          0          0          0          0          0  IR-PCI-MSI 1572871-edge      iwlwifi:queue_7
    150:          0          0        905          0          0          0          0          0          0          0          0          0  IR-PCI-MSI 1572872-edge      iwlwifi:queue_8
    151:          0          0          0          0          0          0          0        674          0          0          0          0  IR-PCI-MSI 1572873-edge      iwlwifi:queue_9
    152:          0          0          0          0          0          0          0          0          0          0          0        261  IR-PCI-MSI 1572874-edge      iwlwifi:queue_10
    153:          0          0          0          0          0          0          0          0        174          0          0          0  IR-PCI-MSI 1572875-edge      iwlwifi:queue_11
    154:          0          0          0          0          0          0          0         89          0          0          0          0  IR-PCI-MSI 1572876-edge      iwlwifi:queue_12
    155:          0          0          0          5          0          1          0          0          0          0          0          0  IR-PCI-MSI 1572877-edge      iwlwifi:exception
    156:          0          0          0          0       3495          0          0          0          0          0          0          0  IR-PCI-MSI 514048-edge      snd_hda_intel:card0
    157:          0          0          0          0          0      14581          0          0          0          0          0          0  IR-PCI-MSI 526336-edge      snd_hda_intel:card1
    NMI:          0          0          0          0          0          0          0          0          0          0          0          0   Non-maskable interrupts
    LOC:    4614879    4206567    4001905    3668692    4024153    4380632    3085733    3133609    3180154    3229616    3295853    3491229   Local timer interrupts
    SPU:          0          0          0          0          0          0          0          0          0          0          0          0   Spurious interrupts
    PMI:          0          0          0          0          0          0          0          0          0          0          0          0   Performance monitoring interrupts
    IWI:    2192872    1761301    1605884    1413797    1443396    1662445    1156426    1170847    1211963    1214175    1924346    1298930   IRQ work interrupts
    RTR:          0          0          0          0          0          0          0          0          0          0          0          0   APIC ICR read retries
    RES:      86141      91554      78352      72190     246263     600266      76681      70599      70976      70603     128686     186120   Rescheduling interrupts
    CAL:    1619790    1313933    1153063    1073582    1112364    1058622    1035089    1026962     988165     965885     977815     937786   Function call interrupts
    TLB:     552957     572090     554364     546061     626770     565515     525963     523563     513685     499523     523999     499912   TLB shootdowns
    TRM:          0          0          0          0          0          0          0          0          0          0          0          0   Thermal event interrupts
    THR:          0          0          0          0          0          0          0          0          0          0          0          0   Threshold APIC interrupts
    DFR:          0          0          0          0          0          0          0          0          0          0          0          0   Deferred Error APIC interrupts
    MCE:          0          0          0          0          0          0          0          0          0          0          0          0   Machine check exceptions
    MCP:         29         30         30         30         30         30         30         30         30         30         30         30   Machine check polls
    ERR:          0
    MIS:          0
    PIN:          0          0          0          0          0          0          0          0          0          0          0          0   Posted-interrupt notification event
    NPI:          0          0          0          0          0          0          0          0          0          0          0          0   Nested posted-interrupt event
    PIW:          0          0          0          0          0          0          0          0          0          0          0          0   Posted-interrupt wakeup event
