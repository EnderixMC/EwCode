from argparse import ArgumentParser
from ewcode_lib import Execute
from ewcode_lexer import Lex
from zipfile import ZipFile
import tempfile
import shutil
import pickle
import sys
import os

version = "0.1"

def compile(name):
    with open(name+".ecr", "r") as f:
        raw = f.read()
    data = Lex(raw)
    with ZipFile(name+".ewc", "w") as zipfile:
        with zipfile.open("main", "w") as f:
            pickle.dump(data, f)
        with zipfile.open("code.properties", "w") as f:
            f.write(f"version={version}".encode("utf"))

def run(name):
    path = os.path.join(tempfile.gettempdir(),name+"_ecode")
    with ZipFile(name+".ewc", "r") as zipfile:
        zipfile.extractall(path)
    has_ver = False
    with open(os.path.join(path,"code.properties"), "r") as f:
        for l in f.readlines():
            if l.startswith("version="):
                if l[8:] == version:
                    has_ver = True
                    break
                else:
                    raise Exception(f"Incorrect version!\nEwCode version: {version}\nFile version: {l[8:]}")
    with open(os.path.join(path,"main"), "rb") as f:
        if not has_ver:
            print("[Warning]: This file contains no version. The code inside might be incompatible")
        Execute(pickle.load(f))
    shutil.rmtree(path)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("-c", "--compile", action="store_true")
    args = parser.parse_args()
    if args.compile:
        try:
            compile(args.file.replace(".ecr",""))
        except Exception as e:
            print("[Error]:", e)
            raise e #REMOVE LATER
            sys.exit()
    else:
        try:
            run(args.file.replace(".ewc",""))
        except Exception as e:
            print("[Error]:", e)
            raise e # REMOVE LATER
            sys.exit()
