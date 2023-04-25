import griffe

previous = griffe.load_git("mypackage", ref="0.2.0")
current = griffe.load("mypackage")

for breakage in griffe.find_breaking_changes(previous, current):
    ...
