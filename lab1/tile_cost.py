tile_side=int(input(" enter tile side : "))
floor_side=int(input(" enter floor side length in multiple of tile sid efor perfect number of tilr :"))
cost=int(input(" enter cost per tile : "))
no_oftile=floor_side*floor_side/tile_side*tile_side
print("total cost of tiles is ",cost*no_oftile,"rs")
