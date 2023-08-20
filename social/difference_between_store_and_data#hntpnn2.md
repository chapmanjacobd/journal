Alpine.data is local like x-data but reusable. Each component wouldn't have access to other instances of that x-data but you only need to define it once

Store is like a global x-data. It doesn't have the local-reusable magic that Alpine.data has but you can do the same things with it

I've never used Alpine.data but I imagine that you could use Store inside of Alpine.data to talk between components but you will need to keep track of what component is what by passing data
