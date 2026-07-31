from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base for a character with a name and a life status."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize the character with a first name and an alive flag."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Mark the character as no longer alive."""
        self.is_alive = False


class Stark(Character):
    """Concrete character belonging to House Stark."""

    def __init__(self, first_name, is_alive=True):
        """Initialize the Stark by delegating to the base character."""
        Character.__init__(self, first_name, is_alive)
