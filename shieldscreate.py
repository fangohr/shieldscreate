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


if __name__ == "__main__":
    if len(sys.args) == 2:
        path = sys.args[1]
    else:
        path = '.'
    meta_data = parse(path)
    # shields = get_shields_url(meta_data)
    # output = shields.export('md')
    # print(output)
