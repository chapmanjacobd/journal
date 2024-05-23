You probably just need to set `-referrer` and/or other headers / cookies: https://stackoverflow.com/a/48101066/697964

The problem is that the server is redirecting to a random png file so ffmpeg is doing the correct thing and can't guess what the server wants in order to get the actual content
