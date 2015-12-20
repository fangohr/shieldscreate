import os.path
from shieldscreate import parse, get_shields_url, export


def test_is_testdata_present():
    if os.path.exists('testdata'):
        print("testdata is present")
    else:
        print("cloning testdata repo(s)")
        os.system('make setup-testdata')


def test_parse():
    meta_data = parse('testdata/createshieldstestrepo1')
    assert 'github-url' in meta_data
    assert meta_data['github-url'] == \
        'https://github.com/fangohr/createshieldstestrepo1.git'


def test_get_shields_urls():
    githuburl = 'https://github.com/fangohr/createshieldstestrepo1.git'
    meta_data = {'github-url': githuburl}
    shields = get_shields_url(meta_data)
    assert shields['github-url'] == \
        'https://img.shields.io/badge/github-finmag-green.svg'


def test_export_html():
    urls = {'github-url':
            'https://github.com/fangohr/createshieldstestrepo1.git'}
    shields = {'github-url':
               'https://img.shields.io/badge/github-finmag-green.svg'}
    html = export(shields, urls, 'html')
    assert html['github-url'] == '''<a href="https://github.com/fangohr/''' + \
        '''createshieldstestrepo1.git"><img src="https://img.shields.io/badge''' + \
        '''/github-finmag-green.svg"></a>'''


#    shields = get_shields_url(meta_data)
#    output = shields.export('md')
#    print(output)
