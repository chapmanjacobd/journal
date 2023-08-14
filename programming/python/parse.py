from parse import parse

githubs = [
    "https://github.com/koaning/justcharts/",
    "https://github.com/koaning/human-learn/",
    "https://github.com/r1chardj0n3s/parse/",
]

[parse("https://github.com/{owner}/{repo}/", url).named for url in githubs]

[
    {"owner": "koaning", "repo": "justcharts"},
    {"owner": "koaning", "repo": "human-learn"},
    {"owner": "r1chardj0n3s", "repo": "parse"},
]


## Use search for substrings:

# ie. prefix foo
search("https://github.com/{account}/{project}/", "foo https://github.com/koaning/scikit-lego/")


from parse import findall

fmt = "https://github.com/{account}/{project}/"
txt = "https://github.com/koaning/human-learn/ https://github.com/koaning/scikit-lego/"
res = findall(fmt, txt)
