floor_side=int(input("Enter Floor Side: "))
tile_side=int(input("Enter Tile side: "))
cost=int(input("Enter Cost per Tile: "))
no_oftile=floor_side*floor_side/tile_side*tile_side
print("Total cost of tile is ",cost*no_oftile,"Rs.")
