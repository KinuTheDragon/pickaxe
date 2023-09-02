from constants import *
from block import Block
from item import Item
from enchantment import Enchantment
from artifact import Artifact

class MyDDict(dict):
    def __init__(self, factory, data):
        self.factory = factory
        for k, v in data.items():
            self[k] = v
    def __missing__(self, key):
        self[key] = self.factory(key)
        return self[key]

blocks = MyDDict(Block.new, {b: Block.new(b) for b in BLOCKS.keys()})
items = MyDDict(Item.new, {
    i: Item.new(i)
    for i in list(ITEMS.keys()) + [ii.name for ii in Item.all_items]
})
artifacts = {a: Artifact.new(a) for a in ARTIFACTS.keys()}

for b, block in list(blocks.items()):
    block_data = BLOCKS[b]
    for drop in block_data["drops"] or []:
        if len(drop) == 2: drop += (1,)
        if isinstance(drop, tuple):
            block.add_drop((items[drop[0]], drop[1], drop[2]))
        else:
            block.add_drop((items[drop], None, None))
    if block_data["drops"] is None: block.set_no_drops()
    if "dew" in block_data.keys():
        block.dew_to = block_data["dew"]
        blocks[block_data["dew"]] # Ensure it exists
    if "hardness" in block_data.keys():
        block.hardness = block_data["hardness"]
    if "rbp" in block_data.keys():
        block.required_breaking_power = block_data["rbp"]
    if "layers" in block_data.keys():
        block.layers = block_data["layers"]
    if "id" in block_data.keys():
        block.id = block_data["id"]

for i, item in list(items.items()):
    item_data = ITEMS.get(i, {})
    if "forge" in item_data.keys():
        item.forge_result = items[item_data["forge"]]
    if "obtain" in item_data.keys():
        item.special_obtain = item_data["obtain"]
    if "use" in item_data.keys():
        item.special_uses = item_data["use"]
    if "craft" in item_data.keys():
        if "recipe" in item_data["craft"].keys():
            item.set_crafting_recipe(item_data["craft"]["tier"],
                                     item_data["craft"]["recipe"])
        elif "recipes" in item_data["craft"].keys():
            item.set_crafting_recipes(item_data["craft"]["tier"],
                                      item_data["craft"]["recipes"])
    if "museum" in item_data.keys():
        item.museum_position = item_data["museum"]
    if "sell" in item_data.keys():
        item.sell_price = item_data["sell"]
    if "rarity" in item_data.keys():
        item.rarity = item_data["rarity"]
    if "rads" in item_data.keys():
        item.radiation = item_data["rads"]
    if "mining speed" in item_data.keys():
        item.mining_speed = item_data["mining speed"]
    if "breaking power" in item_data.keys():
        item.breaking_power = item_data["breaking power"]
    if "accessory" in item_data.keys():
        item.accessory_use = item_data["accessory"]["use"]
        item.accessory_slots = item_data["accessory"]["slots"]
    if "module" in item_data.keys():
        item.module_use = item_data["module"]["use"]
        item.module_slots = item_data["module"]["slots"]
    if "depth" in item_data.keys():
        item.max_depth = item_data["depth"]
    if "oxygen" in item_data.keys():
        item.oxygen_capacity = item_data["oxygen"]
    if "lore" in item_data.keys():
        item.lore = item_data["lore"]
    if "audio" in item_data.keys():
        item.audio = f"instruments/{item_data['audio']}.ogg"
    if "modular" in item_data.keys():
        item.modular_armor_slots = item_data["modular"]["slots"]
        item.modular_armor_capacity = item_data["modular"]["capacity"]
    if "potion" in item_data.keys():
        item.potion_effect = item_data["potion"]["effect"]
        item.potion_level = item_data["potion"]["level"]
        item.potion_duration = item_data["potion"]["duration"]
    item.item_data = item_data["item"]

for block in blocks.values():
    if block.name in items.keys():
        items[block.name].disambiguate()
        block.disambiguate()

enchants = {e: Enchantment.new(e) for e in ENCHANTMENTS.keys()}
for e in enchants.values(): e.requirements # Load items

communist_items = [(items[i], g) for i, g in COMMUNIST]

# for item in Item.all_items:
#     if item.default_image_href.endswith("unknown.png"):
#         print(item.name)

GENERATE_REPORT = False

if GENERATE_REPORT:
    not_used = []
    not_obtainable = []
    for i in Item.all_items:
        if not (
            i.forge_result or
            i.museum_position or
            i.sell_price or
            i.mining_speed or
            i.breaking_power or
            i.crafting_uses or
            i.enchantment_uses
        ): not_used.append(i)
        if not (
            i.crafting_tier or
            i.special_obtain or
            i.forged_from or
            i.dropped_from
        ): not_obtainable.append(i)
    
    output = "Unusable:\n* " + "\n* ".join(i.name for i in not_used) + "\n\nUnobtainable:\n* " + "\n* ".join(i.name for i in not_obtainable)
    with open("unused.txt", "w") as f:
        f.write(output)