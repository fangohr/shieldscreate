import configparser
import os
import sys


def parse_dot_git_config(path):
    c = configparser.ConfigParser()
    r = {}  # Results
    with open('testdata/createshieldstestrepo1/.git/config') as f:
        c.read_file(f)

    r['github-url'] = c.get('''remote "origin"''', 'url')
    return r


def parse(path):
    """Given a path, return metadata about repository found
    at that location"""
    entries = os.listdir(path)
    if '.git' in entries:
        return parse_dot_git_config(os.path.join(path, '.git', 'config'))


def get_shields_url(metadata):
    shields = {}
    # https://img.shields.io/badge/github-finmag-green.svg
    for key, url in metadata.items():
        if key == 'github-url':
            # github_shield_url =\
                shieldvalue = 'https://img.shields.io/badge/github-finmag-green.svg'
        shields[key] = shieldvalue
    return shields


if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = '.'
    meta_data = parse(path)
    shields = get_shields_url(meta_data)
    print(shields)
    # output = shields.export('md')
    # print(output)
