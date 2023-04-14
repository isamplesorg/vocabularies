#!/usr/local/bin/python

import os
import subprocess
import sys


def main():
    # my_input = os.environ["INPUT_MYINPUT"]
    print(f"environment variables are {os.environ}")
    # my_output = f"Hello {my_input}"
    print(f"::set-output name=myOutput::foo")
    command = os.environ["INPUT_ACTION"]
    if command == "uijson":
        print("Generating uijson for inclusion in webUI build")
        path = os.environ["INPUT_PATH"]
        if path is None:
            print("Did not receive a valid path argument so we cannot run.")
            sys.exit(-1)
        subprocess.run("make cache")
        material_json = os.path.join(path, "material_hierarchy.json")
        subprocess.run(f"python tools/vocab.py -s cache/vocabularies.db uijson mat:materialsvocabulary -e >& {material_json}")
        material_json = os.path.join(path, "sampledFeature_hierarchy.json")
        subprocess.run(f"python tools/vocab.py -s cache/vocabularies.db uijson sf:sampledfeaturevocabulary -e >& {material_json}")
        material_json = os.path.join(path, "specimenType_hierarchy.json")
        subprocess.run(f"python tools/vocab.py -s cache/vocabularies.db uijson spec:specimentypevocabulary -e >& {material_json}")


if __name__ == "__main__":
    print("Hello there")
    main()
