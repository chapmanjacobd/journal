if you have to do this frequently and if it was a legitimate resource problem somehow then a creative option would be to have a small separate table which would switch how the application interprets isActive. If 300,000,000 users suddenly sign on then you could switch isActiveNegate from 0 to 1 in the small table and then update the much smaller number of rows needed to make the data valid (200,000,000 or less) within the same transaction.

I don't see this as something that would be a legitimate problem though so my answer is somewhat non-legitimate.
