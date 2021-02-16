#!/usr/bin/python3
import sys, os, re, time, markdown, htmlmin


def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def process_css(path):
    css = read_file(path)
    if len(css) < 1024:
        return '<style>' + css + '</style>'
    return '<link rel="stylesheet" href="' + os.path.normpath(path) + '" type="text/css">'


file_rules = {
    '.txt': { 
        'tag': '${CONTENT}',
        'preprocess': lambda path: read_file(path)
    },
    '.css': { 
        'tag': '${STYLES}',
        'preprocess': lambda path: process_css(path)
    },
    '.md': {
        'tag': '${CONTENT}', 
        'preprocess': lambda path: markdown.markdown(read_file(path))
    }
}


start = time.time()
template = None
address = None
sitemap = []

if len(sys.argv) > 1:
    protocol = 'https://'
    if len(sys.argv) > 2:
        protocol = sys.argv[2]
    address = protocol + sys.argv[1] + '/'

if address is not None:
    print('Processing', address)

with open(os.path.join('./', 'base', 'template.html')) as template_src:
    template = template_src.read()

for root, dirs, files in os.walk("./"):
    for filename in files:
        # Skip useless for us files
        if '.conf' not in filename:
            continue
        print('found', os.path.normpath(os.path.join(root, filename)))

        # Initialize and read the config file
        config = {}
        with open(os.path.join(root, filename), 'r') as src:
            for line in src.read().splitlines():
                if '=' not in line:
                    continue
                tokens = line.split('=')
                config[tokens[0]] = tokens[1]

        # Create a page from the template
        page = template
        # Config variables
        for var in config:
            page = page.replace("${{{:s}}}".format(var.upper()), config[var])
        # File rules
        for ext in file_rules:
            path = os.path.join(root, filename.replace('.conf', ext))
            if os.path.exists(path):
                page = page.replace(file_rules[ext]['tag'], file_rules[ext]['preprocess'](path))
        # Leftovers, unused tags
        for tag in re.findall('\$\{(.*?)\}', page):
            page = page.replace('${' + tag + '}', '');
            
        with open(os.path.join(root, filename.replace('.conf', '.html')), "w") as dest:
            dest.write(htmlmin.minify(page))
        
        # Add a link to the sitemap
        if address is not None:
            rel_link = root if 'index.' in filename else os.path.join(root, filename.replace('.conf', '.html'))
            link = address + os.path.normpath(rel_link)
            if link[len(link)-1] == '.':
                link = link[:len(link)-2]
            sitemap.append(link)

with open(os.path.join('.', 'sitemap.txt'), 'w') as sitemap_file:
    sitemap_file.writelines(addr + '\n' for addr in sitemap)

print('Done')