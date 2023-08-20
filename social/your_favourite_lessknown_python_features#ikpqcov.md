> character_count.get(character, 0) + 1

be careful with this. If character or the value of the dict under the key "character" is explicitly None then you'll get None + 1

Instead you'll want to do:

    (character_count.get(character) or 0) + 1

or

    (character_count.get("character") or 0) + 1

Also shoutout to `.pop` which is similar

    (character_count.pop(character, None) or 0) + 1
