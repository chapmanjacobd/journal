import os
import sys

import pexpect

env = dict(os.environ)
env["NO_COLOR"] = "1"
env["PYTHON_COLORS"] = "0"
env["PYTHONBREAKPOINT"] = "pdb.set_trace"

child = pexpect.spawn(
    "python3",
    ["run_pdb.py"],
    timeout=180,
    encoding="utf-8",
    env=env,
)
child.logfile_read = sys.stdout

commands = [
    "p args.driver.current_url",
    "p args.driver.title",
    "p len(args.driver.page_source)",
    "!open('test.html','w').write(args.driver.page_source)",
    "!from bs4 import BeautifulSoup as BS",
    "!soup = BS(args.driver.page_source, 'html.parser')",
    "!print('WRAPPER COUNT', len(soup.select('#acf-content-wrapper')))",
    "!print(soup.select_one('#acf-content-wrapper').prettify()[:12000])",
    "c",
]

child.expect(r"\(Pdb\) ")
for command in commands:
    child.sendline(command)
    if command == "c":
        break
    child.expect(r"\(Pdb\) ")

child.expect(pexpect.EOF)
print("\n=== EXIT ===", child.exitstatus, child.signalstatus)
