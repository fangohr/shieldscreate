# run the tests
test:
	py.test -v test_*.py


# create testdata subdirectory
testdata:
	mkdir -p testdata

# clone test repositories
setup-testdata: testdata
	@echo "Cloning test repos (will happen only once)"
	cd testdata && git clone https://github.com/fangohr/createshieldstestrepo1.git
	cd testdata && hg clone https://bitbucket.org/fangohr/shieldscreate_test_repo2

# for development only (removes testdata)
clean-testdata:
	rm -rf testdata
