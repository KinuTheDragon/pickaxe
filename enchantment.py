from constants import *

class Enchantment:
    all_enchantments = []
    
    @classmethod
    def new(cls, name):
        self = cls()
        self.__name = name
        if self in cls.all_enchantments:
            return [x for x in cls.all_enchantments if x == self][0]
        href = name.lower()
        for c in href:
            if c not in ALLOWED_URL_CHARS:
                href = href.replace(c, "-")
        while "--" in href: href = href.replace("--", "-")
        self.__href = f"/enchant/{href}"
        cls.all_enchantments.append(self)
        return self
        
    @property
    def name(self):
        return self.__name

    @property
    def href(self):
        return self.__href

    @property
    def enchantment_data(self):
        return ENCHANTMENTS[self.name]

    @property
    def effect(self):
        return self.enchantment_data["effect"]

    @property
    def location(self):
        return self.enchantment_data["location"]

    @property
    def requirements(self):
        from item import Item
        req = self.enchantment_data["requirements"]
        item_req = [[Item.new(r) for r in s] for s in req]
        for s in item_req:
            s.extend([None] * (4 - len(s)))
        return item_req

    def __repr__(self):
        return f"Enchantment({repr(self.name)})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name

    def icon(self, url_for):
        return f"""<a href="{self.href}"><img src="{url_for('static', filename = 'images/default/enchantment.gif')}" width=50 height=50 />{self.name}</a>"""

    def json(self):
        return {
            "name": self.name,
            "effect": self.effect,
            "location": self.location,
            "requirements": [
                [i.href if i else None for i in r]
                for r in self.requirements
            ]
        }