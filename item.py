from constants import *
from block import Block
from enchantment import Enchantment
from flask import request
import os

class Item:
    all_items = []

    @classmethod
    def new(cls, name):
        self = cls()
        self.__name = name
        if self in cls.all_items:
            return [x for x in cls.all_items if x == self][0]
        href = name.lower()
        for c in href:
            if c not in ALLOWED_URL_CHARS:
                href = href.replace(c, "-")
        while "--" in href: href = href.replace("--", "-")
        self.__href = f"/item/{href}"
        self.update_href()
        self.forge_result = None
        self.__crafting_tier = None
        self.__crafting_recipes = []
        self.audio = None
        self.special_obtain = []
        self.special_uses = []
        self.museum_position = None
        self.sell_price = None
        self.rarity = None
        self.radiation = None
        self.mining_speed = None
        self.breaking_power = None
        self.accessory_use = None
        self.accessory_slots = None
        self.module_effect = None
        self.module_slots = None
        self.potion_effect = None
        self.potion_level = None
        self.potion_duration = None
        self.modular_armor_slots = None
        self.modular_armor_capacity = None
        self.max_depth = None
        self.oxygen_capacity = None
        self.lore = None
        self.item_data = {}
        cls.all_items.append(self)
        return self

    @property
    def name(self):
        return self.__name

    @property
    def href(self):
        return self.__href

    @property
    def default_image_href(self):
        return self.__image_href

    @property
    def spore_image_href(self):
        return self.__spore_href

    @property
    def image_href(self):
        return self.spore_image_href if request.cookies.get("sporetex") else self.default_image_href

    @property
    def forged_from(self):
        for item in self.__class__.all_items:
            if item.forge_result is self:
                return item

    @property
    def dropped_from(self):
        dropped_from = []
        for block in Block.all_blocks:
            if block.drops:
                for drop in block.drops:
                    if drop[0] == self:
                        dropped_from.append((block, drop[1], drop[2]))
        return dropped_from

    def set_crafting_recipe(self, tier, recipe):
        self.set_crafting_recipes(tier, [recipe])

    def set_crafting_recipes(self, tier, recipes):
        self.__crafting_tier = tier
        self.__crafting_recipes = [[
            [Item.new(x) if x else None for x in r]
            for r in recipe
        ] for recipe in recipes]

    @property
    def crafting_tier(self):
        return self.__crafting_tier

    @property
    def crafting_recipes(self):
        return self.__crafting_recipes

    @property
    def crafting_uses(self):
        uses = []
        for item in self.__class__.all_items:
            for recipe in item.crafting_recipes:
                if self in sum(recipe, []):
                    uses.append(item)
                    break
        return uses

    @property
    def enchantment_uses(self):
        uses = []
        for ench in Enchantment.all_enchantments:
            for level, req in enumerate(ench.requirements):
                if self in req:
                    uses.append((ench, level + 1))
        return uses

    def __repr__(self):
        return f"Item({repr(self.name)})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name

    def disambiguate(self):
        self.__name += " (Item)"
        self.__href += "--item"
        self.update_href()

    def update_href(self):
        href = os.path.basename(self.__href)
        for file_extension in FILE_EXTENSIONS:
            self.__image_href = f"images/default/{href}.{file_extension}"
            if os.path.exists("static/" + self.__image_href): break
        else:
            self.__image_href = f"images/default/unknown.png"
        for file_extension in FILE_EXTENSIONS:
            self.__spore_href = f"images/sporefreak/{href}.{file_extension}"
            if os.path.exists("static/" + self.__spore_href): break
        else:
            self.__spore_href = self.__image_href

    @property
    def item_id(self):
        return self.item_data["id"]

    @property
    def item_enchanted(self):
        return bool(self.item_data.get("enchanted"))

    @property
    def color(self):
        return RARITY_COLORS.get(self.rarity, "")

    @property
    def sage_rarity(self):
        return next_rarity(self.rarity)

    @property
    def sage_color(self):
        return RARITY_COLORS.get(self.sage_rarity, "")

    @property
    def overclocked_rarity(self):
        return next_rarity(self.sage_rarity)

    @property
    def overclocked_color(self):
        return RARITY_COLORS.get(self.overclocked_rarity, "")

    @property
    def potion_effect_text(self):
        return POTION_EFFECTS[self.potion_effect](self.potion_level)

    @property
    def potion_duration_text(self):
        return "{0}h{1}m{2}s".format(*self.potion_duration)

    def icon(self, url_for):
        return f"""<a href="{self.href}" style="color:{self.color}"><img src="{url_for("static", filename=self.image_href)}" width=50 height=50 />{self.name}</a>"""

    def json(self):
        opt = lambda f, x: f(x) if x else None
        hopt = lambda x: opt(lambda i: i.href, x)
        vopt = lambda x: opt(lambda e: e.value, x)
        return {
            "name": self.name,
            "forge_result": hopt(self.forge_result),
            "forged_from": hopt(self.forged_from),
            "crafting_tier": opt(
                lambda e: (e.value[0] if isinstance(e.value, tuple)
                           else e.value), self.crafting_tier),
            "crafting_recipes": [
                [[hopt(i) for i in r] for r in recipe]
                 for recipe in self.crafting_recipes
            ],
            "special_obtain": self.special_obtain,
            "special_uses": self.special_uses,
            "museum_position": opt(list, self.museum_position),
            "sell_price": self.sell_price,
            "rarity": vopt(self.rarity),
            "radiation": self.radiation,
            "mining_speed": self.mining_speed,
            "breaking_power": self.breaking_power,
            "accessory_use": self.accessory_use,
            "accessory_slots": self.accessory_slots,
            "module_effect": self.module_effect,
            "module_slots": self.module_slots,
            "potion_effect": self.potion_effect.value,
            "potion_level": self.potion_level,
            "potion_duration": self.potion_duration,
            "modular_armor_slots": self.modular_armor_slots,
            "modular_armor_capacity": self.modular_armor_capacity,
            "max_depth": self.max_depth,
            "oxygen_capacity": self.oxygen_capacity,
            "lore": self.lore or [],
            "item": self.item_data,
            "dropped_from": [
                (b[0].href, b[1]) if isinstance(b, tuple)
                else (b.href, None)
                for b in self.dropped_from
            ],
            "crafting_uses": [i.href for i in self.crafting_uses],
            "enchantment_uses": [[e.href, lvl]
                                 for e, lvl in self.enchantment_uses]
        }