from constants import *
import os

class Artifact:
    all_artifacts = []

    @classmethod
    def new(cls, number):
        self = cls()
        self.__number = number
        self.__name = f"#{number}: " + ARTIFACTS[number]["name"]
        self.__lore = ARTIFACTS[number]["lore"]
        self.__color = ARTIFACTS[number]["color"]
        if self in cls.all_artifacts:
            return [x for x in cls.all_artifacts if x == self][0]
        self.__audio = None
        if "audio" in ARTIFACTS[number].keys():
            self.__audio = f"instruments/{ARTIFACTS[number]['audio']}.ogg"
        href = str(number)
        self.__href = f"/artifact/{href}"
        self.update_href()
        cls.all_artifacts.append(self)
        return self

    @property
    def number(self):
        return self.__number
        
    @property
    def name(self):
        return self.__name

    @property
    def href(self):
        return self.__href

    @property
    def lore(self):
        return self.__lore

    @property
    def color(self):
        return self.__color

    @property
    def audio(self):
        return self.__audio

    @property
    def image_href(self):
        return self.__image_href

    def icon(self, url_for):
        return f"""<a href="{self.href}" style="color:{self.color}"><img src="{url_for("static", filename=self.image_href)}" width=50 height=50 />{self.name}</a>"""
        
    def update_href(self):
        href = os.path.basename(self.__href)
        for file_extension in FILE_EXTENSIONS:
            self.__image_href = f"images/default/{href}.{file_extension}"
            if os.path.exists("static/" + self.__image_href): break
        else:
            self.__image_href = f"images/default/unknown.png"

    def __repr__(self):
        return f"Artifact({self.number})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.number == other.number

    def json(self):
        return {
            "name": self.name,
            "number": self.number,
            "lore": self.lore,
            "color": self.color
        }