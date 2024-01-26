import json
import os

def _assert_file_exists_and_is_json(file_path: str):
	"""For the UIJSON action, assert that we wrote out the specified file, and it's valid JSON"""
	exists = os.path.exists(file_path)
	assert exists is True
	with open(file_path, "r") as file:
		json.load(file)


def test_uijson_sample_type_exists():
	_assert_file_exists_and_is_json("CVJSON/docs/material_sample_type.json")

def test_uijson_material_type_exists():
	_assert_file_exists_and_is_json("CVJSON/docs/material_type.json")

def test_uijson_samples_feature_type_exists():
	_assert_file_exists_and_is_json("CVJSON/docs/sampled_feature_type.json")

def test_docs_directory_exists():
	# For the docs action, just assert that the docs directory exists.
	# TODO: Can we make this check a bit more stringent?
	assert os.path.exists("docs")
