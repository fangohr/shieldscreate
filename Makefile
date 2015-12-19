test:
	py.test -v test_*.py

testdata:
	mkdir -p testdata

testdata/createshieldtestrepo1: testdata
	cd testdata && git clone https://github.com/fangohr/createshieldstestrepo1.git
