Yes, always try to find the hidden API

It was actually using `requests`, no browser, but the other parts of the architecture was super-over-complex like saving each indicator to a bucket and then writing a record in BigQuery about the JSON that was just saved. Everything was abstracted away with OOP so it was hard to tell just how inefficient it was actually being 

I'm not sure how the original container took so long but I got it down to 15 minutes just by batching the different steps one at a time (save all, write to BQ once).
