Use `duration_string` instead of `duration`: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#output-template

But you can also do this

    pip install xklb
    lb tubeadd videos.db https://www.youtube.com/playlist?list=PLkpvfd3IhdOccc8ybisPqLW-Phi68HqN1

    lb watch videos.db -p -u duration
    path                                         title                                      duration                    play_count
    -------------------------------------------  -----------------------------------------  ------------------------  ------------
    https://www.youtube.com/watch?v=wyHwVY8N9og  Villains falling to their deaths part 15   5 minutes and 59 seconds             0
    https://www.youtube.com/watch?v=tFoYr7DOG28  villains falling to their deaths part 14   5 minutes and 2 seconds              0
    https://www.youtube.com/watch?v=ip3_EoxfDpc  villains falling to their deaths part 17   4 minutes and 45 seconds             0
    https://www.youtube.com/watch?v=OcatHvpxiOE  Villain's falling to their deaths part 24  4 minutes and 3 seconds              0
    https://www.youtube.com/watch?v=mSW7x_7U_B8  Villains falling to their deaths part 2    3 minutes and 53 seconds             0
    https://www.youtube.com/watch?v=q9anfLCzV9c  Villains Falling To Their Deaths Part 27   3 minutes and 41 seconds             0
    https://www.youtube.com/watch?v=c7Ym4Xn7a9U  Villains falling to their deaths part 8    3 minutes and 39 seconds             0
    https://www.youtube.com/watch?v=gT3VjvkwUCY  Villains Falling To Their Deaths Part 28   3 minutes and 13 seconds             0
    https://www.youtube.com/watch?v=vQKXAR1E4ug  Villains falling to their deaths part 6    3 minutes and 4 seconds              0
    https://www.youtube.com/watch?v=s35Wc9BhJJk  villains falling to their deaths part 9    2 minutes and 59 seconds             0
    https://www.youtube.com/watch?v=M_SSCbwMLA4  Villains falling to their deaths part 23   2 minutes and 58 seconds             0
    https://www.youtube.com/watch?v=s-gfutFmVKg  villains falling to their deaths part 4    2 minutes and 57 seconds             0
    https://www.youtube.com/watch?v=xJ-ypG3iIfI  Villains falling to their death part 19    2 minutes and 55 seconds             0
    https://www.youtube.com/watch?v=z3K88up7e5Y  villains falling to their deaths part 12   2 minutes and 53 seconds             0
    https://www.youtube.com/watch?v=D0gkydn6lqc  Villains Falling To Their Deaths Part 30   2 minutes and 48 seconds             0
    https://www.youtube.com/watch?v=E0R1R5gAAb4  Villains falling to their deaths part 21   2 minutes and 45 seconds             0
    https://www.youtube.com/watch?v=2x5kWhhuSj0  Villains falling to their death part 20    2 minutes and 45 seconds             0
    https://www.youtube.com/watch?v=DWyV_InKw2Y  Villains falling to their deaths part 16   2 minutes and 42 seconds             0
    https://www.youtube.com/watch?v=yEcg4ESigHQ  Villains falling to their deaths part 7    2 minutes and 38 seconds             0
    https://www.youtube.com/watch?v=v49oUiKr7U0  Villains Falling To Their Deaths Part 29   2 minutes and 33 seconds             0
    https://www.youtube.com/watch?v=YMGHr-Qukk4  Villains Falling To Their Deaths Part 26   2 minutes and 26 seconds             0
    https://www.youtube.com/watch?v=pAxQ6aYp7Bw  villains falling to their deaths part 10   2 minutes and 23 seconds             0
    https://www.youtube.com/watch?v=_v_GpqH1ymI  Villains Falling To Their Deaths Part 25   2 minutes and 19 seconds             0
    https://www.youtube.com/watch?v=wsje0WkybAQ  Villains falling to their deaths part 3    2 minutes and 18 seconds             0
    https://www.youtube.com/watch?v=YDjhoyHmlqo  villains falling to their deaths part 11   2 minutes and 18 seconds             0
    https://www.youtube.com/watch?v=IckDQIp9lkM  Villains falling to their deaths part 18   2 minutes and 18 seconds             0
    https://www.youtube.com/watch?v=pbwf07sJq-4  Villains falling to their deaths           2 minutes and 17 seconds             0
    https://www.youtube.com/watch?v=5Fi5MvYpTgc  villains falling to their deaths part 5    2 minutes and 17 seconds             0
    https://www.youtube.com/watch?v=pqlx5fR1Uxg  Villains falling to their deaths part 22   1 minute and 59 seconds              0
    https://www.youtube.com/watch?v=8zSn-KAuIaA  villains falling to their deaths part 13   1 minute and 45 seconds              0
    https://www.youtube.com/watch?v=7mKV8OyLZak                                                                                  0
    https://www.youtube.com/watch?v=4hKyOUiUS2o                                                                                  0
    32 media
    Total duration: 1 hour and 31 minutes

`-u duration` sorts by duration
