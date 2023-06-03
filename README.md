# Remote Sensing Instance Segmentation Algorithms (RSISA)

## Installation

## Tutorial

## Test


## Updates
Added two methods to improve space complexity:
1. if an instance is in the middle of a tile, only global mask will be kept in the instances list.
2. the tile manager dynamically save instances to a shapefile when an tile's adjacent tiles have been registered. At the same time, the saved instances will be deleted in mememory. steps: 1) sort tile indices; 2) given a tile index, check if each of its adjacent tile has already been registered; 3) if no, continue to check next adjacent tile; if yes, check if all adjacent tiles of the adjacent tile have been registered; 4) if yes, save the adjacent tile. 