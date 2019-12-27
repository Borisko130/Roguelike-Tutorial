from map_objects.tile import Tile

"""
Generates map
"""

class GameMap:
    def __init__(self, width, height):
        # Initializes map
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        # Initializes tiles on map

        ### Here seems to be backwards order.
        ### First x, then y, then tile's blocking property
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles
    
    def create_room(self, room):
        # Go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False


    def is_blocked(self, x, y,):
    # Checks whether tile is blocked
        if self.tiles[x][y].blocked:
            return True

        return False
