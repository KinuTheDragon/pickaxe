from constants import *
from flask import request
import os

class Block:
    all_blocks = []

    @classmethod
    def new(cls, name):
        self = cls()
        self.__name = name
        if self in cls.all_blocks:
            return [x for x in cls.all_blocks if x == self][0]
        href = name.lower()
        for c in href:
            if c not in ALLOWED_URL_CHARS:
                href = href.replace(c, "-")
        while "--" in href: href = href.replace("--", "-")
        self.__href = f"/block/{href}"
        self.update_href()
        self.__drops = []
        self.__dew_to = None
        self.hardness = None
        self.required_breaking_power = None
        self.layers = []
        cls.all_blocks.append(self)
        self.id = self.name.lower().replace(" ", "_")
        return self

    @property
    def name(self):
        return self.__name

    @property
    def href(self):
        return self.__href

    @property
    def drops(self):
        return self.__drops

    @property
    def dew_to(self):
        return self.__dew_to

    @dew_to.setter
    def dew_to(self, dt):
        self.__dew_to = self.__class__.new(dt)

    @property
    def dewed_from(self):
        df_list = []
        for block in self.__class__.all_blocks:
            if block.dew_to == self:
                df_list.append(block)
        return df_list

    def add_drop(self, drop):
        self.__drops.append(drop)

    def set_no_drops(self):
        self.__drops = None

    @property
    def default_image_href(self):
        return self.__image_href

    @property
    def spore_image_href(self):
        out = self.default_image_href.replace("default", "sporefreak")
        if not os.path.exists("static/" + out):
            out = self.default_image_href
        return out

    @property
    def image_href(self):
        return self.spore_image_href if request.cookies.get("sporetex") else self.default_image_href

    def __repr__(self):
        return f"Block({repr(self.name)})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name

    def disambiguate(self):
        self.__name += " (Block)"
        self.__href += "--block"
        self.update_href()

    def update_href(self):
        href = os.path.basename(self.__href)
        for file_extension in FILE_EXTENSIONS:
            self.__image_href = f"images/default/{href}.{file_extension}"
            if os.path.exists("static/" + self.__image_href): break
        else:
            self.__image_href = f"images/default/unknown.png"
    
    def icon(self, url_for):
        return f"""<a href="{self.href}"><img src="{url_for("static", filename=self.image_href)}" width=50 height=50 />{self.name}</a>"""

    def json(self):
        return {
            "name": self.name,
            "drops": self.drops,
            "dew_to":
                self.dew_to.href if self.dew_to else None,
            "dewed_from": [
                block.href for block in self.dewed_from
            ],
            "hardness": self.hardness,
            "required_breaking_power": self.required_breaking_power,
            "id": self.id,
            "layers": [
                layer.value for layer in self.layers
            ]
        }