#!/usr/bin/env python3

import os
import argparse
import hashlib

TEAM_NFT_START = 9983
IMAGE_EXT = ".svg"

def main():
    parser = argparse.ArgumentParser(
        description="Get a consistent md5 hash for the directory of images.")
    parser.add_argument(
        "-d",
        "--directory",
        metavar="DIR",
        type=str,
        required=True,
        help="the directory to hash",
    )
    args = parser.parse_args()

    assert os.path.exists(args.directory), f"Directory does not exist: {args.directory}."

    h = hashlib.sha3_224()
    for i in range(1,TEAM_NFT_START):
        path = os.path.join(args.directory, str(i) + IMAGE_EXT)
        with open(path, "rb") as f:
            h.update(f.read())

    print(f"SHA3_224({args.directory}) = {h.hexdigest()}")
        

    





if __name__ == "__main__":
    main()
