import sys
python_version = sys.version_info[0]
if python_version == 2:
    raise NotImplementedError("This programme needs python 3")
    # Configparser has trouble reading .git/config in python 2

import configparser
import os
import sys

default_badge_colour = 'green'


def create_metadata(name, colour=default_badge_colour):
    metadata = {'name': name}
    metadata['colour'] = colour
    return metadata


def parse_dot_git_config(path, name):
    c = configparser.ConfigParser()
    r = create_metadata(name)
    r['repo-type'] = 'git'
    with open(path) as f:
        c.read_file(f)

    r['repo-url'] = c.get('''remote "origin"''', 'url')
    return r


def parse_dot_hg_config(path, name):
    c = configparser.ConfigParser()
    r = create_metadata(name)
    r['repo-type'] = 'hg'

    with open(path) as f:
        c.read_file(f)

    r['repo-url'] = c.get('paths', 'default')
    return r


def parse(path, name):
    """Given a path, return metadata about repository found
    at that location"""
    entries = os.listdir(path)
    if '.git' in entries:
        return parse_dot_git_config(os.path.join(path, '.git', 'config'), name)
    if '.hg' in entries:
        return parse_dot_hg_config(os.path.join(path, '.hg', 'hgrc'), name)


def get_shields_url(metadata):
    shields = {}
    # https://img.shields.io/badge/github-finmag-green.svg
    shieldvalue = "{}/{}-{}-{}.svg".format(
        'https://img.shields.io/badge',
        metadata['repo-type'],
        metadata['name'],
        metadata['colour'])
    shields['repo-url'] = shieldvalue
    return shields


def export(shielddata, urldata, target='html'):
    htmls = {}
    if target == 'html':
        for key in shielddata:
            url = urldata[key]
            shield = shielddata[key]
            html = '<a href="{}"><img src="{}"></a>'.format(
                url, shield)
            htmls[key] = html
    return htmls


def search_for_travis(path):
    return '.travis.yml'   # XXX fake it till you make it


def main(path, format, name):
    assert format in ['html', 'rest', 'md']
    meta_data = parse(path, name)
    shields = get_shields_url(meta_data)
    output = export(shields, meta_data, format)
    return " ".join(output.values())


if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
        name = None
    elif len(sys.argv) == 3:
        path = sys.argv[1]
        name = sys.argv[2]
    else:
        raise ValueError("Need at least path as command line argument")

    output = main(path, 'html', name)
    open('test.html', 'w').write(output)
