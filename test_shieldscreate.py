import os.path
from shieldscreate import parse, get_shields_url, export, main


def test_is_testdata_present():
    if os.path.exists('testdata'):
        print("testdata is present")
    else:
        print("cloning testdata repo(s)")
        os.system('make setup-testdata')


def test_parse_git():
    meta_data = parse('testdata/createshieldstestrepo1', None)
    assert 'repo-type' in meta_data
    assert meta_data['repo-type'] == 'git'
    assert meta_data['repo-url'] == \
        'https://github.com/fangohr/createshieldstestrepo1.git'


def test_parse_hg():
    meta_data = parse('testdata/shieldscreate_test_repo2', None)
    assert meta_data['repo-type'] == 'hg'
    assert meta_data['repo-url'] == \
        'https://bitbucket.org/fangohr/shieldscreate_test_repo2'


def test_get_shields_urls():
    githuburl = 'https://github.com/fangohr/createshieldstestrepo1.git'
    meta_data = {'github-url': githuburl, 'repo-type': 'git', 'name': 'finmag',
                 'colour': 'green'}
    shields = get_shields_url(meta_data)
    assert shields['repo-url'] == \
        'https://img.shields.io/badge/git-finmag-green.svg'


def test_export_html():
    urls = {'github-url':
            'https://github.com/fangohr/createshieldstestrepo1.git'}
    shields = {'github-url':
               'https://img.shields.io/badge/github-finmag-green.svg'}
    html = export(shields, urls, 'html')
    assert html['github-url'] == '''<a href="https://github.com/fangohr/''' + \
        '''createshieldstestrepo1.git"><img src="https://img.shields.io/badge''' + \
        '''/github-finmag-green.svg"></a>'''


def test_end_to_end_this_repo():
    expected_result = """<a href="git@github.com:fangohr/shieldscreate.git">""" + \
        """<img src="https://img.shields.io/badge/git-create""" + \
        """shields-green.svg"></a>"""
    assert main('.', 'html', 'createshields') == expected_result

#    shields = get_shields_url(meta_data)
#    output = shields.export('md')
#    print(output)
