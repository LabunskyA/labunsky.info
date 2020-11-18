#!/usr/bin/python3
import os

IN_EXT, OUT_EXT, RULES, TXT = ".tmpl", ".html", os.path.join(os.path.dirname(__file__), "rules.txt"), []

with open(RULES, "r") as rules:
    tokens = rules.read().split("\n\n")
    for token in tokens:
        token = [x for x in [x.strip() for x in token.split("\n")] if len(x) > 0 and x[0] != '#']

        if len(token) != 2:
            print("Ignoring tokens:\n{:s}".format(token))
            continue

        TXT.append((token[0], token[1]))

for root, dirs, files in os.walk("./"):
    for filename in files:
        if IN_EXT not in filename:
            continue

        print("Found \"{:s}\", processing...".format(os.path.join(root, filename)))
        with open(os.path.join(root, filename), "r") as src:
            result = src.read()

        changed = False
        while True:
            replaced = False
            for token in TXT:
                if token[0] not in result:
                    continue
                replaced, changed = True, True

                cmd = token[1].format(root, filename.replace(IN_EXT, ""))
                result = result.replace(token[0], os.popen(cmd).read())

            if not replaced:
                break

        if changed:
            with open(os.path.join(root, filename.replace(IN_EXT, OUT_EXT)), "w") as dest:
                dest.write(result)
