#!/usr/bin/python3
import os, sys, subprocess

IN_EXT, OUT_EXT = ".tmpl", ".html"
RULES, LOCAL = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None

TXT = []
with open(RULES, "r") as rules:
    tokens = rules.read().split("\n\n")
    for token in tokens:
        token = [x.strip() for x in token.split("\n") if len(x) > 0 and x[0] != '#']

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
                replacement = subprocess.check_output(cmd, shell=True)
                result = result.replace(token[0], replacement.decode("UTF-8"))

            if not replaced:
                break

        if changed:
            with open(os.path.join(root, filename.replace(IN_EXT, OUT_EXT)), "w") as dest:
                dest.write(result)
