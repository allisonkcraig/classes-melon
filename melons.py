"""This file should have our melon-type classes in it."""
class Melon(object):

    def __init__(self, base_price= 5.00):
        self.base_price = base_price


class CantaloupeOrder(Melon):
    species = "Cantaloupe"
    rind_color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.imported == True:
            self.base_price = self.base_price * 1.5

        if self.shape == "square":
            self.base_price = self.base_price * 2

        if self.species == "Cantaloupe":
            self.base_price = self.base_price * 0.50

        total = float(self.base_price * qty)

        return total

class WatermelonOrder(Melon):
    species = "Watermelon"
    rind_color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.imported == True:
            self.base_price = self.base_price * 1.5

        if self.shape == "square":
            self.base_price = self.base_price * 2

        if self.species == "Watermelon" and qty >= 3:
            self.base_price = self.base_price * 0.75

        total = float(self.base_price * qty)

        return total

class CasabaOrder(Melon):
    species = "Casaba"
    rind_color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.imported == True:
            self.base_price = self.base_price * 1.5

        if self.shape == "square":
            self.base_price = self.base_price * 2

        self.base_price += 1

        total = float(self.base_price * qty)

        return total


class SharlynOrder(Melon):
    species = "Sharlyn"
    rind_color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.imported == True:
            self.base_price = self.base_price * 1.5

        if self.shape == "square":
            self.base_price = self.base_price * 2

        total = float(self.base_price * qty)

        return total

class SantaClausOrder(Melon):
    species = "Santa Claus"
    rind_color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.imported == True:
            self.base_price = self.base_price * 1.5

        if self.shape == "square":
            self.base_price = self.base_price * 2

        total = float(self.base_price * qty)

        return total

class ChristmasOrder(Melon):
    species = "Christmas"
    rind_color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.imported == True:
            self.base_price = self.base_price * 1.5

        if self.shape == "square":
            self.base_price = self.base_price * 2

        total = float(self.base_price * qty)

        return total

class HornedMelonOrder(Melon):
    species = "Horned Melon"
    rind_color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.imported == True:
            self.base_price = self.base_price * 1.5

        if self.shape == "square":
            self.base_price = self.base_price * 2

        total = float(self.base_price * qty)

        return total

class XiguaOrder(Melon):
    species = "Xigua"
    rind_color = "green"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.imported == True:
            self.base_price = self.base_price * 1.5

        if self.shape == "square":
            self.base_price = self.base_price * 2

        total = float(self.base_price * qty)

        return total

class OgenOrder(Melon):
    species = "Ogen"
    rind_color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.imported == True:
            self.base_price = self.base_price * 1.5

        if self.shape == "square":
            self.base_price = self.base_price * 2

        if self.species == "Ogens":
            self.base_price += 1

        total = float(self.base_price * qty)

        return total