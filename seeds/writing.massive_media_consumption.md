# Techniques for _Massive_ Media consumption:

Is this unconscious media consumption? I have experienced this jaded serendipity. Satiated serendipity.

A goal of consuming 1TB per week. 52TB per year. When I say this, I'm talking about 480p video and 96 vbr opus audio. If your eyes bleed when you see anything less than 4K please multiply the previous numbers by 10. The goal is not to just download a bunch of data but to also consume/delete a large quantity of data.

- Have high standards
- Skip as much as possible
  - boring scene? skip ahead
  - boring episode? go to the next one without delay
  - automate skipping with [sponsorblock](https://github.com/asakura42/sponsorblock-mpv-local) and the [power of subtitles](https://github.com/Ben-Kerman/mpv-sub-scripts/blob/master/sub-skip.lua)
- Automate consumption
  - Make bulk deletion easy (I didn't like that song so delete the whole album, or the whole discography)
  - Smart home: play music you never heard of as your alarm clock; turn on the TV at 5:00pm every day
  - Use machine learning to build a "cookie" of yourself. Have the computer watch TV for you. Download the highlights reel back into your brain.
  - Watch two, three, or four episodes [at the same time](https://github.com/chapmanjacobd/library/blob/48218744b440482536a2287347777426c087653f/xklb/player.py#L559https://github.com/chapmanjacobd/library/blob/main/xklb/player.py#L559). These could be sequential episodes of the same series or completely different genres. You will either uncover the pattern of patterns [or](https://www.computerhistory.org/collections/catalog/X39.81) go insane.
- Don't go outside
  - Live in a boring small town where there is usually nothing going on. This maximizes the amount of time that you can watch TV and not feel guilty.
  - Set up excercise equipment near your TV so you can "work your pecs at home".

My goal here isn't really to maximize the number of hours watched but rather to maximize curation.

If it takes you 30 seconds to find something to watch while you are eating then reducing that time to 5 seconds could save you about 4 hours per year (if you watch something twice per day, 6 days per week). But if you take 5 minutes to find something to watch, and you can bring that down to 5 seconds, by doing so you are effectively finding 1 hour per week that you didn't have before. You save over 2 extra days per year.

How do you even download a terabyte?

I hate spotify and I hate having to choose things based on a brief glance at a thumbnail or a 30 second preview. Marketing is a skill that many people don't have and the modern stance is to leave that element of 'chance' to a flick of the wrist or some machine learning algorithm. I have been pleasently surprised more often from pure long-tail randomness than from any personalized recommendation system. There is a lot of stuff out there but instagram and facebook just feed me the same stuff over and over (perhaps to save bandwidth?). I don't ever want to experience memoized-at-the-macro life.

```sh
wt --played-within '30 days' -w 'time_deleted>0' -pa
╒═══════════╤════════════╤════════════════╤═════════╤═════════╕
│ path      │ duration   │ avg_duration   │ size    │   count │
╞═══════════╪════════════╪════════════════╪═════════╪═════════╡
│ Aggregate │ 10 days, 1 │ 10.07 minutes  │ 99.9 GB │    1437 │
│           │ hour and   │                │         │         │
│           │ 14 minutes │                │         │         │
╘═══════════╧════════════╧════════════════╧═════════╧═════════╛

lb lt -w 'play_count>0' -pa
╒═══════════╤════════════╤════════════════╤═════════╤═════════╕
│ path      │ duration   │ avg_duration   │ size    │   count │
╞═══════════╪════════════╪════════════════╪═════════╪═════════╡
│ Aggregate │ 2 months,  │ 14.75 minutes  │ 31.9 GB │    7757 │
│           │ 18 days,   │                │         │         │
│           │ 11 hours   │                │         │         │
│           │ and 2      │                │         │         │
│           │ minutes    │                │         │         │
╘═══════════╧════════════╧════════════════╧═════════╧═════════╛
```
