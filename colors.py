import random


class UniqueColorGenerator:
    def __init__(self):
        self.used_colors = set()

    def generate_hex_color(self, length=6):
        """Generate a random hex color code."""
        return "#" + "".join(random.choices("0123456789ABCDEF", k=length))

    def get_unique_color(self):
        """Get a unique hex color code that hasn't been used before.

        Returns:
            str: A unique hex color code.
        """
        while True:
            # Generate a random color. Adjust length for different formats.
            color = self.generate_hex_color(length=random.choice([3, 4, 6, 8]))
            if color not in self.used_colors:
                self.used_colors.add(color)
                return color

    def add_color(self, color):
        """Add a color to the used_colors set.

        Args:
            color (str): The color to be added.
        """
        self.used_colors.add(color)


# Example usage
color_generator = UniqueColorGenerator()
# Get a new unique color
# It is added to used_colors set in
# color_generator
sample_a_color = color_generator.get_unique_color()
orangish_color = "#EF4A26"
# Add the color to the used_colors set
# so it won't be used again
color_generator.add_color(orangish_color)
# other analogous colors to the orangish color
burnt_orange = "#EFAF26"
color_generator.add_color(burnt_orange)
yellowish = "#CBEF26"
color_generator.add_color(yellowish)
bright_lime = "#26EF4A"
color_generator.add_color(bright_lime)
sea_foam = "#26EFAF"
color_generator.add_color(sea_foam)
