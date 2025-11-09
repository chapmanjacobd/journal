It depends what you want but generally, if you just want to apply normalization across many different files, use loudnorm:

    -af loudnorm=i=-18:tp=-3:lra=17

dynaudnorm is more useful for unmastered files like home video recordings, etc

    -af dynaudnorm=f=150:g=13
