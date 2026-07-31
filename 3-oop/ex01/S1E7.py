from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __init__(self, first_name, is_alive=True,
                 family_name="Baratheon", eyes="brown", hairs="dark"):
        """Initialize a Baratheon with the family's default traits."""
        Character.__init__(self, first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs


class Lannister(Character):
    """Representing the Lannister family."""

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __init__(self, first_name, is_alive=True,
                 family_name="Lannister", eyes="blue", hairs="light"):
        """Initialize a Lannister with the family's default traits."""
        Character.__init__(self, first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Build and return a new Lannister from a name and life status."""
        return cls(first_name, is_alive)
