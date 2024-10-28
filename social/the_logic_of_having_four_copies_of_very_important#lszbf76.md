While more copies is always better, the problem of knowing which copy is corrupted is solved pretty well with metadata. 

I don't think that specific problem scenario truly justifies the cost of an additional copy as opposed to additional programmatic robustness (ie. running `cmp` across two servers instead of comparing the result of local hashing processes)

I would say having 5 or more copies of metadata is warranted because it is usually small and easy to do. Having one offline or read-only copy is easily justified by ransomware and other attacks--that's a better reason than content consensus
