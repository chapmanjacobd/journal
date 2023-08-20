I made something that will do this. I don't record `title` because that metadata is not very common in my experience but maybe I should add it... 

edit: I added `title` in the latest release. 

https://github.com/chapmanjacobd/lb/

It will create a SQLITE database and you would want to mount each drive onto a different path. 

- You don't need to have all drives attached at once but if you have a hard drive at `D:\` and then swap out the drive to the same mount point, `lb` will recognize that those files from the other drive as gone and mark them as deleted. this might be fine for your case since it is only soft deleting the metadata via a time_deleted column. 
- Or create a different database file per drive and it won't matter if they are all the same mount point.

Then you can run `sqlite-utils rows`  to get a CSV output https://sqlite-utils.datasette.io/en/stable/cli-reference.html#rows

Also you may want to look into Git Annex https://git-annex.branchable.com/not/

Here's an example of the output CSV (you can select fewer columns via sqlite3, sqlite-utils, dbeaver, etc):

    sqlite-utils rows test.db media --csv
    play_count,time_played,size,time_created,time_modified,time_downloaded,time_deleted,video_count,audio_count,chapter_count,width,height,fps,duration,subtitle_count,attachment_count,path,webpath,ie_key,sparseness,language,title,description
    0,0,224749150,1424844000,1541997172,1666806245,0,1,1,0,640,272,23,5757,2,0,/mnt/d/71_Mealtime_Videos/YouthOnScreen/The_Naked_Island_1960_-_English_Subtitles_[watGzwZ6S-c].webm,https://www.youtube.com/watch?v=watGzwZ6S-c,Local,1.0000109722328205,eng,The Naked Island (1960) - English Subtitles,A study in the constant struggle of agrarian life;this dialogue-free;black-and-white film depicts one family's difficult existence. The sole inhabitants of an island in Japan's Seto Inland Sea;the impoverished family sees their tough life as farmers become even more challenging when the oldest son falls deathly ill while his parents are away gathering water. Confronted with this tragedy;the family must work even harder to survive. Nobuko Otowa - Toyo (the mother) Taiji Tonoyama - Senta (the father) Shinji Tanaka - Tarô (the elder son) Masanori Horimoto - Jirô (the younger son) This is an unofficial recording for promotional use only and not for profit. Please visit the official sites and show your support! http://www.kindaieikyo.com http://www.imdb.com/title/tt0056049 http://www.imdb.com/name/nm0793881 Please get in contact if there are any problems with this video. Thank you.;YouthOnScreen
