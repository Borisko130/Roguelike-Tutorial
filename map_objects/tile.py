class Tile:
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight.
    """

    ### From where coordinates for tile are taken
    ### EXPLANATION
    ### 1. Tiles are placed in 2d array
    ### 2. Their coords in array are their coords on map

    def __init__(self, blocked, block_sight = None):

        ### !!! Seems like all tiles should be blocked
        ### EXPLANATION
        ### 1. It is simply an assignment of 'blocked' variable value to the tile
        self.blocked = blocked

        #By default, if a tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
