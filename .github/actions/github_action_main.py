#!/usr/local/bin/python
"""
Driver file for the vocabularies GitHub Action.  

the github workflow needs to copy output files to the docs directory
in the public github, else they disappear with the docker container when workflow
completes
original code by Dave Vieglais for iSamples project
modified by SM Richard 2023-12-14

input arguments are grabbed from environmental variables that are defined in actions.yml
and have values assigned in /.github/workflows/ {workflow def.yaml}.
"""

import logging
import os
import subprocess
import sys


PATH_PREFIX = "/app/"
VOCAB_PY = f"{PATH_PREFIX}/tools/vocab.py"
VOCABULARY_CACHE_PATH = f"{PATH_PREFIX}cache/vocabularies.db"

def main():
    print(f"environment variables are {os.environ}")

    command = os.environ["INPUT_ACTION"]
    print("github_action_main: INPUT_ACTION: ", command)
    path = os.environ["INPUT_PATH"]
    path = os.path.join(path, "docs")
    input = os.environ["INPUT_INPUTTTL"]
    print(f"inputttl string: {input}")
    inputttl = input.split('|')
    # inputttl is a list of skos rdf vocabulary filenames with Turtle serialization
    # vocab_source_dir is the path to the directory that contains the source files
    for filename in inputttl:
            print(f"files to load: {filename}")

    input = os.environ["INPUT_INPUTVOCABURI"]
    print(f"inputvocaburi string: {input}")
    inputvocaburi = input.split('|')
    for auri in inputvocaburi:
            print(f"vocab URIs: {auri}")

    
    # this is the directory that holds the source SKOS ttl files.
    sourcevocabdir = f"{PATH_PREFIX}vocabulary"


    print("github_action_main: target path for output: ", path)
    if path is None:
        print("Did not receive a valid path argument so we cannot run.")
        sys.exit(-1)
    if not os.path.exists(path):
        os.makedirs(path)
        # Change to 777 so subsequent steps that deal with the directory don't run into permissions issues
        os.chmod(path, 777)
        print(f"Created {path} since it didn't exist.")

    # do function of original Makefile here
  
#    for inputf in inputttl:
#        result=load_cachedb(sourcevocabdir + "/" + inputf + ".ttl", VOCABULARY_CACHE_PATH)
#        if (result == 0):
#            print(f"load_cachedb call successful for: {inputf}")
#        else:
#            print(f"load_cachedb had problem processing: {inputf}.  Exiting.")
#            sys.exit(-1)

    index = 0
    while index < len(inputttl):
        # for inputf in inputttl:
        result = load_cachedb(sourcevocabdir + "/" + inputttl[index] + ".ttl", inputvocaburi[index], VOCABULARY_CACHE_PATH)
        if (result == 0):
            print(f"load_cachedb call successful for: {inputttl[index]}")
        else:
            print(f"load_cachedb had problem processing: {inputttl[index]}")
        index += 1
        # ***********************

    if command == "uijson":
        print("uijson action has been removed.  json is now fetched dynamically at page load.")
        sys.exit(-1)
    elif command == "docs":
        print("Generating markdown and html docs")
        index = 0
        print(f"input markdown file: {inputttl[index]}, vocab uri: {inputvocaburi[index]}")
        while index < len(inputttl):
            result = _run_docs_in_container(os.path.join(path, inputttl[index]+".md"), inputvocaburi[index])
            if result == 0:
                _quarto_render_html((os.path.join(path, inputttl[index]+".md")),path)
            else:
                print(f"problem with {inputttl[index]}, don't call quarto")
            index += 1
    else:
        print(f"Unknown command {command}.  Exiting.")
        sys.exit(-1)

# update to add inputuri argument so works with vocab.py SMR 2024-08-14
def load_cachedb(inputf, inputuri, cachepath):
    # tools/vocab.py --verbosity ERROR -s $(CACHE) load $(SRC)/$@
    print(f"cachdb file to load: {inputf}")
    load_args = ["--verbosity", "ERROR", "-s", cachepath, "load", inputf, inputuri]
    result = _run_python_in_container(VOCAB_PY, load_args, f="")
    if (result == 0):
        print(f"vocab.py call successful for {inputf}")
        return 0
    else:
        print(f"vocab.py had problem processing {inputf}")
        return 1
    

def _quarto_render_html(markdown_in:str, output_path:str):
#     print("In githubActionMain: Quarto render: ",markdown_in,  output_path)
#     result = subprocess.run(["/opt/quarto/bin/quarto", "check"])
#     print("Quarto check result ", result.returncode)
#  NOTE update quarto location for your local install...
     result = subprocess.run(["/opt/quarto/bin/quarto", "render", markdown_in, "-t", "html"])
#     print("Quarto call result ", result.returncode)
     if (result.returncode == 0):
         print(f"Quarto call successful for {markdown_in}")
         return 0
     else:
         print(f"Quarto had problem processing {markdown_in}")
         return 1


def _run_make_in_container(target: str):
    print("In githubActionMain: make in container, target: ", target)
    subprocess.run(["/usr/bin/make", "-C", "/app", "-f", "/app/Makefile", target])


def _run_docs_in_container(output_path: str, vocab_uri: str):
    with open(output_path, "w") as f:
        docs_args = [VOCABULARY_CACHE_PATH, vocab_uri]
        testflag = _run_python_in_container("/app/tools/vocab2mdCacheV2.py", docs_args, f)
        if (testflag == 0):
            print(f"Docs in container: Successfully wrote doc file {vocab_uri} to {output_path}")
            return 0
        else:
            print(f"vocab2mdCacheV2. problem processing {vocab_uri}")
            return 1

def _run_python_in_container(path_to_python_script: str, args: list[str], f):
    subprocess_args = [sys.executable, path_to_python_script]
    subprocess_args.extend(args)
    if f=="":
        result = subprocess.run(subprocess_args)
    else:
        result = subprocess.run(subprocess_args, stdout=f)
#    print("container call result ", result.returncode)
    return result.returncode




if __name__ == "__main__":
    main()
