#!/usr/bin/python3
import os, re, markdown


def read_file(path):
    if not os.path.exists(path):
        return ''
    with open(path, 'r') as file:
        return file.read()


file_rules = {
    '.txt': { 
        'tag': '${CONTENT}',
        'preprocess': lambda path: read_file(path)
    },
    '.css': { 
        'tag': '${STYLES}',
        'preprocess': lambda path: '<link rel="stylesheet" href="' + os.path.normpath(path) + '" type="text/css">'
    },
    '.md': {
        'tag': '${CONTENT}', 
        'preprocess': lambda path: markdown.markdown(read_file(path))
    }
}


template = None
with open(os.path.join('./', 'base', 'template.html')) as template_src:
    template = template_src.read()

for root, dirs, files in os.walk("./"):
    for filename in files:
        if '.conf' not in filename:
            continue
        print('Found "{:s}"'.format(os.path.join(root, filename)))

        config = {}
        with open(os.path.join(root, filename), 'r') as src:
            for line in src.read().splitlines():
                if '=' not in line:
                    continue

                tokens = line.split('=')
                config[tokens[0]] = tokens[1]


        page = template
        for var in config:
            page = page.replace("${{{:s}}}".format(var.upper()), config[var])
        for ext in file_rules:
            page = page.replace(file_rules[ext]['tag'], file_rules[ext]['preprocess'](os.path.join(root, filename.replace('.conf', ext))))
        for tag in re.findall('\$\{(.*?)\}', page):
            page = page.replace('${' + tag + '}', '');

        with open(os.path.join(root, filename.replace('.conf', '.html')), "w") as dest:
            dest.write(page)
