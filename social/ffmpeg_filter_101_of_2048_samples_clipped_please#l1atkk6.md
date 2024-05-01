As far as I understand you can only have one `af=` the rest need to be `af-add=` but yes. It makes sense that blindly increasing gain ie `:gain` or `volume=` past 0db (100%) would cause clipping..

I think `loudnorm` is better in general (and better to use in this specific case: after spatializing) than `dynaudnorm` but they are very different things and it ultimately depends on your preference. Though you shouldn't need both of them at the same time. Try playing around with it and see what sounds better for your setup.

For consistency between audio files it might help to have `af=volume=replaygain-track` before the sofalizer but I don't think this will affect video files because it's not common to have that metadata
