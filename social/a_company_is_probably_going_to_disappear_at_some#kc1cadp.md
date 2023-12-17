cool! If you just want the JSON you can run this:

    xsv select id ~/Downloads/places.csv | 
      parallel --joblog ao_log --shuf --resume-failed \
      --timeout 800% -j2 --delay 1s \
      wget https://www.atlasobscura.com/places/{}.json
