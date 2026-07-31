from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The false king, Baratheon in name only."""

    def __init__(self, first_name, is_alive=True):
        """Initialize the king through the first branch of the MRO."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """Set the king's eye color."""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set the king's hair color."""
        self.hairs = hairs

    def get_eyes(self):
        """Return the king's eye color."""
        return self.eyes

    def get_hairs(self):
        """Return the king's hair color."""
        return self.hairs
