> LOCKSS makes better use of the copies it manages, by enlisting them to validate integrity against each other, rather than relying uncritically on comparisons against a centralized fixity store

For fixity specifically, there is nothing special provided by having additional copies of data over additional copies of metadata (checksums). You can still have a simple or complex consensus system around this metadata.

It's conflating the problem of verification with the problem of preservation. Having additional copies is good and helps with preservation but it doesn't automatically help with fixity. I don't think fixity is a good enough justification for additional blind copies. 

For example, you can have many more copies of metadata for the same amount of resources and, if fixity is the goal, having many more copies of metadata can be a greater sum-of-diminishing-returns than one additional copy of the content.
