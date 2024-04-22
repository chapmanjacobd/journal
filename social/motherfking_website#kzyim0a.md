Well even today most CSS frameworks start with "resetting" the minimal styles and browser style incompatibilities that already exist.

Any browser improvements would need to preserve the existing functionality. If any CSS is loaded or any JS adds/modifies style then it would need to unload the build-in style. 

But I imagine _if_ better (more cohesive, less ugly) defaults existed you would be able to easily download the defaults as CSS to include it and/or tweak it. This might seem like we are back to square 1 but I really don't think so. Defaults are powerful and if they are not painful defaults then they are sticky and help to anchor people's expectations. 

Instead of everything needing to have custom styles we could live in a world where it's just 20% or so and the people consuming content would have more accessible choices than they do now. Right now it is possible to override stylesheets with global userstyles but it's not common practice.

"Reader mode" is interesting because it makes the browser at least as configurable as an e-ink reader to the average user. I wonder if a browser addon exists to automatically enable reader mode when no stylesheets are loaded--or even better make it default enabled until a page loads CSS or runs JS or something like that. Without it being the default, this is a bit of a chicken and egg problem: there aren't a lot of CSS-less sites because the default has been "strictly unopinionated" for so long.

somewhat related: https://old.reddit.com/r/web_design/comments/tnn7ws/i_made_a_reader_mode_browser_extension_that_keeps/
