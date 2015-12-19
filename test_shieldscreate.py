from shieldscreate import parse


def test_parse():
    meta_data = parse('testdata/createshieldstestrepo1')
    assert 'github-url' in meta_data
    assert meta_data['github-url'] == \
        'https://github.com/fangohr/createshieldstestrepo1.git'


#    shields = get_shields_url(meta_data)
#    output = shields.export('md')
#    print(output)
