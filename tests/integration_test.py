import os

def test_docs_directory_exists():
	# For the docs action, just assert that the docs directory exists.
	# TODO: Can we make this check a bit more stringent?
	assert os.path.exists("docs")
