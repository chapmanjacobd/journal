> [HM-SMR] offers vastly better performance [over DM-SMR]

Yes this is true but only because zoned devices force you to tailor your application to the behavior of the device. 

Using TAR on DM-SMR can provide a similar level of performance (vs storing a lot of small files on HM-SMR) and it is a lot easier to use. There's really no good reason for _an individual_ to seek out HM-SMR (even while zoned Btrfs is a bit easier to use than F2FS...)

That is not to say that zoned devices cannot be a good fit for enterprise scenarios where there is enough support (ie. people to spend time optimizing device usage patterns)--they can be a great value (price/performance) in the right scenario
