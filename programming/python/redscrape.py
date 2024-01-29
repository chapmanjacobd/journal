#!/usr/bin/env python3
# https://gist.github.com/Krazybug/2ab91232b3ecf120a394ef28f380526c

'''
Fetch and decode the links from a subreddit when they are encoded in base64 (until 3 pass)

Installation:
    You need python 3.8 installed

    Save the pastebin as a file i.e "redscrape.py" and open a terminal where the file is located
    > python3 -m venv . # On Mac
    > python -m venv . # On Windows/Linux
    > . bin/activate
    > pip install psaw fire
    > python redscrape.py --help

Usage examples :
    > python redscrape.py my_sub --after="2021-11-01"  # All the links in r/my_sub from 2021-11-01 to now
    > python redscrape.py my_sub --after="2021-07-01" --before="2021-08-01" --domains="drive.google.com, mega.nz"
    # All the links in r/my_sub on July 2021 containing the domains drive.google.com and mega.nz

Behaviour:
    A "links.json" file is generated, so that you can easily visualize links or process them with 'jq' program (See below).
    This file contains a list ("by_date") of the matching posts (submissions and comments) sorted by date, with the title and the links related.
    Another field ("by_id) contains more details as text content and, for comments, the root post title and its body.
    You can run the program with different params to complete your collection as the json file is reused on startup.


CAUTION: You should not run the program without parameters on a complete sub as you will hammer the pushshift API

Params:
    --sub=<string>                          :   Name of subreddit
    --after=<string>                        :   Start date (ex: --start="2021-09-15" ). By default it's the beginning of the sub
    --before=<string>                       :   Stop date (ex: --stop=="2021-06-03"). By default it's now
    --domains=<string>                      :   A list of domains to filter the links separated by commas. It overrides the default list
                                                (ex: --domains="drive.google.com, mega.nz")

JQ Examples: jq allows you to smartly grep in a json file and has many other features:

    # Search Schubert in the titles of the "by_date" index
    > jq -r '.by_date[] | select(.title | match("schubert"; "i"))' links.json
    # Search Mozart in the body the the posts.
    > jq -r '.by_id[] | select (.body != null) | select(.body | match("mozart"; "i"))' links.json

'''

import base64
import datetime
import json
import os
import re
from urllib.parse import urlparse

import fire
from psaw import PushshiftAPI

# cf. https://stackoverflow.com/questions/475074/regex-to-parse-or-validate-base64-data/475217#475217
BASE64_REGEX = '(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})'
# URL_REGEX = r'(https?:\/\/[A-Za-z0-9+\/\.\-_#?=!]+)'
URL_REGEX = r'(https?:\/\/[^\s)\]]+)'
URL_MARKDOWN_REGEX = r'\[.+?\]\((.+?)\)'
OUTPUT_FILE = 'links.json'
MAX_PASS = 3
ACCEPTED_DOMAINS = [
    'drive.google.com',
    'mega.nz',
    'web.archive.org',
    'filecat.org',
    'dropbox.com',
    'terabox.com',
    '1fichier.com',
    'youtube.com',
    'youtu.be',
    'transferfile.io',
    'udrop.com',
    'odrive.com',
    'mirrored.to',
    'mediafire.com',
    'file-upload',
    'dropbox.com',
    'uptobox.com',
    'ulozto.net',
    'ufile.io',
    'turbobit.net',
    'udl.to',
    'store.tidal.com',
    'krakenfiles.com',
    'gofile.io',
    'filetransfer.io',
    'dropapk.to',
    'drop.download',
    'easyupload.io',
    'dbree.org',
]


# Ugly globals
api = PushshiftAPI()
base64_pattern = re.compile(BASE64_REGEX)
url_pattern = re.compile(URL_REGEX)
md_pattern = re.compile(URL_MARKDOWN_REGEX)


def is_url(string):
    try:
        result = urlparse(string)
        return all([result.scheme, result.netloc])
    except:
        return False


def fetch_links(candidates, nb_pass=MAX_PASS, domains=ACCEPTED_DOMAINS):
    """Analyse a list of tuples and return valid links as a new list of tuples.
    The strings are decoded recursively in base 64 in "nb_pass".
    The returned list is filtered and should only contains links matching the accepted domains."""

    nb_pass -= 1
    candidate_list = candidates

    # print("level", nb_pass)
    # print('candidates', candidates)

    for candidate in candidates:
        # print('candidate:', candidate)

        matches = url_pattern.findall(candidate)
        # print("url matches:", matches)
        candidate_list.extend([c.rstrip('\n') for c in matches])
        # print("candidate list:", candidate_list)

        matches = base64_pattern.findall(candidate)
        candidate_list.extend(
            [base64.b64decode(c).decode('utf-8', errors='ignore').rstrip('\n') for c in matches if len(c) >= 12]
        )
        # print("base64 matches:", matches)
        candidate_list = list(set(candidate_list))
        # print("base64 candidates:", candidate_list)

    new_list = []
    new_list = [c for c in candidate_list if c]

    if not new_list:
        return []

    if nb_pass == 0:
        # new_list=[c for c in candidate_list if is_url(c[0])]

        # filter urls by domain
        tmp_list = []
        for c in new_list:
            for accepted in domains:
                if c.find(accepted) >= 0:
                    tmp_list.append(c)
                    break
        new_list = tmp_list

        return list(set(new_list))

    else:
        return list(set(fetch_links(new_list, nb_pass=nb_pass, domains=domains)))


def compute_sub(sub, after=None, before=None, domains=None):
    """
    Fetch links matching domains between 2 dates
    """

    print()
    print("Sub:", sub)

    print(f"From {after} to {before}")
    after = int(datetime.datetime.strptime(after, "%Y-%m-%d").timestamp()) if after else 0
    before = (
        int(datetime.datetime.strptime(before, "%Y-%m-%d").timestamp())
        if before
        else int(datetime.datetime.now().timestamp())
    )

    accepted = domains.split(',') if domains else ACCEPTED_DOMAINS
    accepted = [s.strip() for s in accepted]

    print("Domains :", ",".join(accepted))
    print()

    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r') as f:
            by_id = json.load(f)['by_id']
    else:
        by_id = {}
    posts_dict = {}

    print("Processing submissions. Please wait!")
    print()
    submissions = api.search_submissions(subreddit=sub, before=before, after=after)
    posts = (
        dict(
            id=post.id,
            url=post.full_link,
            title=post.title,
            date=datetime.datetime.fromtimestamp(post.created_utc).isoformat(),
            body=post.selftext if hasattr(post, 'selftext') else '',
        )
        for post in submissions
    )

    for p in posts:
        # Cache the submissions for future use
        posts_dict[p['id']] = p

        # Analyse the submissions
        # links =  fetch_links([(p['body'], p['body'])], nb_pass=MAX_PASS, domains=accepted)
        links = fetch_links([p['body']], nb_pass=MAX_PASS, domains=accepted)
        if links:
            print("\n", p['url'])
            print("links", links)
            p['links'] = links
            by_id[p["id"]] = p

    # print()
    # print("Waiting 10s ...") # To avoid some errors 429
    # print()
    # time.sleep(10)

    print("Processing comments. Please wait!")
    comments = api.search_comments(subreddit=sub, before=before, after=after)

    posts = (
        dict(
            id=post.id,
            url="http://reddit.com" + post.permalink,
            date=datetime.date.fromtimestamp(post.created_utc).isoformat(),
            body=post.body,
            parent_id=post.parent_id,
        )
        for post in comments
    )

    # Cache the comments for future use
    comments = []
    for p in posts:
        posts_dict[p['id']] = p
        comments.append(p['id'])

    for c in comments:
        p = posts_dict.get(c)
        links = fetch_links([p['body']], nb_pass=MAX_PASS, domains=accepted)
        if links:
            p['links'] = links

            # Retrieve submission info for this comment
            root_id = p['url'].split('/')[6]
            root = posts_dict.get(root_id, None)  # Data may be inconsistent or network errors
            title = root.get('title', '<Unknown Title>') if root else '<Unknown root submission>'
            body = root.get('body', '<Unknown Body>') if root else '<Unknown root submission>'
            p['submission_id'] = root_id
            p['title'] = title
            p['submission_body'] = body

            # Retrieve parent info for this comment
            parent_id = p['parent_id']
            if parent_id != root_id:
                parent = posts_dict.get(parent_id, None)
                body = parent.get('body', '<Unknown Body>') if parent else '<Unknown parent>'
                p['parent_body'] = body

            by_id[p["id"]] = p

            print("\n", p['url'])
            print("links", links)

    # Let's build the list sorted by date
    by_date = [{'id': p['id'], 'title': p['title'], 'date': p['date'], 'links': p['links']} for p in by_id.values()]
    by_date.sort(key=lambda x: x.get('date'), reverse=True)

    final_list = {"by_date": by_date, "by_id": by_id}
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(final_list, f, indent=4)

    print()
    print("Total :", len(by_date))


if __name__ == "__main__":
    fire.Fire(compute_sub)
