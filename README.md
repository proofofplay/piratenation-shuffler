# Pirate Nation Shuffle Script

This repo contains two scripts, one to shuffle the public NFTs based on a given seed and another to hash a directory of images.

We're going to publicly choose our seed value that's used to shuffle the NFTs before reveal. To choose our seed, we're going to rely on Ethereum's block hash for a future block which we will announce in our Discord.

We will use the block hash for block 15949475 listed here: [https://etherscan.io/block/15949475](https://etherscan.io/block/15949475)

# How To Verify

## Calculate hash of image folder before shuffle:
```
python3 ./hash-image-dir.py -d before/images 
```
SHA3-224 hash of directory before shuffling: ```7a551c6885716748816a213692d7bde4bff4ad8b7f3f21f176d12f4b```


## Calculate hash of image folder after shuffle:
```
python3 ./hash-image-dir.py -d after/images 
```
SHA3-224 hash of directory after shuffling: ```34edba058fa418af07c115d060936e20441f2c6d833daffe81b68ae8```


## Appendix
Built using Python 3.10.8 on MacOS 13.0.


