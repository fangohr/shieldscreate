
def test_parse():
    meta_data = parse('testdata/repo1')
    assert 'github' in meta_data
    assert metada_data['github'] == {'github' : 'https://github.com/fangohr/createshieldstestrepo1'}


#    shields = get_shields_url(meta_data)
#    output = shields.export('md')
#    print(output)
