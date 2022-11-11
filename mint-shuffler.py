#!/usr/bin/env python3

import os
import shutil
import argparse
import random
from typing import Mapping
from pprint import pprint

# from IPython import embed

BEFORE_IMAGES = "./before/images"
BEFORE_METADATA = "./before/metadata"
AFTER_IMAGES = "./after/images"
AFTER_METADATA = "./after/metadata"

TEAM_NFT_START = 9983
TOTAL_COUNT = 9999
IMAGE_EXT = ".svg"

def main():
    parser = argparse.ArgumentParser(
        description="Shuffle NFTs based on a seed.")
    parser.add_argument(
        "--seed",
        metavar="SEED",
        type=str,
        default="PIRATE",
        help="random seed to be used for the shuffling",
    )
    args = parser.parse_args()

    random.seed(args.seed)

    for path in (BEFORE_IMAGES, BEFORE_METADATA):
        assert os.path.exists(path), f"Directory does not exist: {path}."

    for path in (AFTER_IMAGES, AFTER_METADATA):
        if os.path.isdir(path):
            print(f"Found {path}, deleting.")
            shutil.rmtree(path)
        os.makedirs(path)
        print(f"Creating {path}.")

    # Copy public NFTs in a random position.
    shuffled_nft_ids = list(range(1,TEAM_NFT_START))
    random.shuffle(shuffled_nft_ids)
    for i in range(len(shuffled_nft_ids)):
        copy_nft_to_new_position(str(i+1), str(shuffled_nft_ids[i]))

    # Copy team NFTs to the same position.
    for i in range(TEAM_NFT_START, TOTAL_COUNT+1):
        copy_nft_to_new_position(str(i), str(i))
        

def copy_nft_to_new_position(before, after):
    print(f"{before} -> {after}")
    shutil.copy(os.path.join(BEFORE_IMAGES, before + IMAGE_EXT), os.path.join(AFTER_IMAGES, after + IMAGE_EXT))
    shutil.copy(os.path.join(BEFORE_METADATA, before), os.path.join(AFTER_METADATA, after))


    





if __name__ == "__main__":
    main()
