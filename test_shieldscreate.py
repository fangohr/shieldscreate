import os.path
from shieldscreate import parse, get_shields_url, export, main, \
    search_for_travis


def test_is_testdata_present():
    if os.path.exists('testdata'):
        print("testdata is present")
    else:
        print("cloning testdata repo(s)")
        os.system('make setup-testdata')


def test_parse_this_git():
    meta_data = parse('.', None)
    assert 'repo-type' in meta_data
    assert meta_data['repo-type'] == 'git'
    assert meta_data['repo-url'] == \
        'git@github.com:fangohr/shieldscreate.git'
    assert meta_data['travis-url'] == \
        'https://travis-ci.org/fangohr/shieldscreate'


def test_parse_git():
    meta_data = parse('testdata/createshieldstestrepo1', None)
    assert 'repo-type' in meta_data
    assert meta_data['repo-type'] == 'git'
    assert meta_data['repo-url'] == \
        'https://github.com/fangohr/createshieldstestrepo1.git'
    assert 'travis-url' not in meta_data


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
    github_root_only = expected_result.split('fangohr')[1]
    computed_result = main('.', 'html', 'createshields')['repo-url']
    github_root_only_computed = computed_result.split('fangohr')[1]
    assert github_root_only == github_root_only_computed

    # write into file for convenience
    open('tmp-test-output.html', 'w').write(computed_result)


def test_search_for_travis():
    assert search_for_travis('.') == '.travis.yml'

    #    https://img.shields.io/travis/fangohr/shieldscreate.svg

#    shields = get_shields_url(meta_data)
#    output = shields.export('md')
#    print(output)
