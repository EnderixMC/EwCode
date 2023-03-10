"""
    EwCode - The most disgusting programming language (https://github.com/EnderixMC/EwCode)
    Copyright (C) 2022-2023  EnderixMC

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from argparse import ArgumentParser
from ewcode_lib import Execute
from ewcode_lexer import Lex
from zipfile import ZipFile
import tempfile
import shutil
import pickle
import sys
import os

__version__ = "0.5.0"
credits = f"Ewcode v{__version__} by EnderixMC (https://github.com/EnderixMC/EwCode)"

def compile(name):
    with open(name+".ecr", "r") as f:
        raw = f.read()
    data = Lex(raw)
    with ZipFile(name+".ewc", "w") as zipfile:
        with zipfile.open("main", "w") as f:
            pickle.dump(data, f)
        with zipfile.open("code.properties", "w") as f:
            f.write(f"version={__version__}".encode("utf"))

def run(name):
    path = os.path.join(tempfile.gettempdir(),name+"_ecode")
    with ZipFile(name+".ewc", "r") as zipfile:
        zipfile.extractall(path)
    has_ver = False
    with open(os.path.join(path,"code.properties"), "r") as f:
        for l in f.readlines():
            if l.startswith("version="):
                if l[8:] == __version__:
                    has_ver = True
                    break
                else:
                    raise Exception(f"Incorrect version!\nEwCode version: {__version__}\nFile version: {l[8:]}")
    with open(os.path.join(path,"main"), "rb") as f:
        if not has_ver:
            print("[Warning]: This file contains no version. The code inside might be incompatible")
        #for i in pickle.load(f):
        #    print(i)
        Execute(pickle.load(f))
    shutil.rmtree(path)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version=f"EwCode {__version__}")
    parser.add_argument('--credits', action='version', version=credits)
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
        except KeyboardInterrupt:
            sys.exit()
