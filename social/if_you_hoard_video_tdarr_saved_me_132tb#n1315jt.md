libsvtav1 on CPU is pretty fast at `-preset 7` but higher you lose a lot of potential compression. 

Quality is still pretty decent at that point if you use `-crf 40` or lower. Additional parameters like `-svtav1-params tune=0:enable-overlays=1` can also have a big difference in terms of visual quality.
