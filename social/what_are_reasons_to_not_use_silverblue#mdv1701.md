> Most of the threads I can find on this are 1+ year old

A lot of the "immutable" development work in the past year has been going toward bootc+dnf5 as an eventual replacement for rpm-ostree. Atomic is pretty cool and it is a bit annoying to have to reboot a lot more... I have two servers that I use it with but personally I don't see a lot of advantages to it other than greenboot (automatically reverting updates which break things. pretty cool but I've never had an update actually break something... I'm sure it is possible though)

It's definitely still relevant and things "just work" so just not a lot to talk about really... you can use `rpm-ostree apply-live` in a pinch if you don't want to reboot for installing a small package. If you don't update for a long time (months) then you'll get some weird rpm package caching issues but it will expire/fix itself after a day or two.
