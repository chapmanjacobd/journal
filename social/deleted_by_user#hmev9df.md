I am a frequent abuser of tools. 

I've used Alpine to make a somewhat complex app and it isn't too slow. I would say it's more responsive than something which uses the virtual DOM since all components in my app are native browser HTML5 tags. In my application Alpine handles all the data binding and state.

I think 100 rows should be fine--if you need more or lots of complex rendering in columns I might recommend something like react-window or maybe there is a way to get similar functionality in alpine by only rendering 10 rows at a time and make the next, previous buttons instant so it's not annoying or allow people to download CSV
