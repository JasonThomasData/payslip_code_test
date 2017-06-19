### Tests

You should be seeing these pass with TravisCI on Github, with all major versions of Python3.

To run the tests locally make sure this has program [installed](install.md) correctly, then do:

	nosetests test/integration test/unit

I've tested coverage - unit tests are at about 70%, because the controller doesn't have unit tests. Integration tests focus on the controller and that has 96% coverage.

This program was developed and tested locally on a Linux Mint environment.
