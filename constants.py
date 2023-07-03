import string
from enum import Enum

ALLOWED_URL_CHARS = string.ascii_letters + string.digits + "-"

FILE_EXTENSIONS = "png gif".split()

class CraftTier(Enum):
    Crafting0 = "Tier 0 Crafting"
    Crafting1 = "Tier 1 Crafting", "Hat of Knowledge"
    Crafting2 = "Tier 2 Crafting", "Hat of Wisdom"
    Crafting3 = "Tier 3 Crafting", "Hat of Ominescence"
    Tech0 = "Tier 0 Tech"
    Tech1 = "Tier 1 Tech", "Tech Perception Gear"
    Tech2 = "Tier 2 Tech", "Extreme Insight Tech Helmet"
    Water = "Water Crafting"
    Walgo = "Walgo Altar Crafting"
    Brewing = "Brewing"
    Skin = "Skin Crafting"
    Pumpkin = "Pumpkin Crafting"

class Rarity(Enum):
    Mundane = "Mundane"
    Common = "Common"
    Uncommon = "Uncommon"
    Rare = "Rare"
    Epic = "Epic"
    Legendary = "Legendary"
    Mythic = "Mythic"
    Godly = "Godly"
    Exotic = "Exotic"
    Divine = "Divine"
    Surreal = "Surreal"
    Overclocked = "Overclocked"

RARITY_COLORS = {
    Rarity.Mundane: "#aaa",
    Rarity.Common: "#fff",
    Rarity.Uncommon: "#5ff",
    Rarity.Rare: "#5f5",
    Rarity.Epic: "#a0a",
    Rarity.Legendary: "#fa0",
    Rarity.Mythic: "#f5f",
    Rarity.Godly: "#a00",
    Rarity.Exotic: "#ccb18f",
    Rarity.Divine: "#007acc",
    Rarity.Surreal: "#555",
    Rarity.Overclocked: "#f55"
}

class Layer(Enum):
    Dirt = "Dirt", True, 0, 9
    Stone = "Stone", True, 10, 49
    Blackstone = "Blackstone", True, 50, 79
    Brimstone = "Brimstone", True, 80, 120
    NetherHub = "Nether Hub", True, 130, 165
    Breakfast = "Breakfast", True, 166, 189
    Void = "Void", True, 190, 200
    Sand = "Sand", False, 0, 9
    Sandstone = "Sandstone", False, 10, 39
    Clay = "Clay", False, 40, 69
    Ice = "Ice", False, 70, 119
    Cake = "Cake", False, 120, 180

ARTIFACTS = {
    1: {
        "color": "#FF5",
        "name": "Rubber Ducky",
        "lore": [
            "A relic from an unknown time where",
            "rubber duckies were worshipped as",
            "beings greater than or equal to gods."
        ]
    },
    2: {
        "color": "#F55",
        "name": "The Commusputt Manifesto",
        "lore": [
            "Contains various quotes from our glorious leader.",
            "Part of a balanced diet, according to unbiased researchers.",
            "",
            "CHAPTER 1",
            "Order and the rule of law creates the true bedrock of any",
            "great nation. The principle of democracy is nothing more than",
            "a stuffed ballot box, paid for by national security interest.",
            "I do not hide the truth from my nation. Freedom exists only",
            "when order is enforced.",
            "",
            "Look not upon me as a leader, but as a father doting on his",
            "children. Do not be fooled by the sirens of lost rebellions.",
            "Each day we build our nation together, our illustrious military,",
            "shining symbols of power, protecting us from the evil spawn of",
            "delusional rebels. These words, inspired by the tongues of great",
            "men before me, lift us all on our doctrine. Teach those, swallowed",
            "in the decay of the world, and let them be reborn.",
            "",
            "I am Sputt, I bring the new world order to all."
        ]
    },
    3: {
        "color": "#14CC00",
        "name": "101 Pages of Random Digits",
        "lore": [
            "One million industrial-grade random numbers",
            "for all your random number needs.",
            "Just look at our reviews:",
            "",
            "\u2605\u2605\u2605\u2605\u2605 by Moon Lord",
            "\"A very engrossing book with historical importance,",
            "it keeps you guessing until the end.\"",
            "",
            "\u2605\u2605\u2605\u2605\u2606 by Bingo Bongo",
            "\"Very interesting, starts off slow but picks up",
            "and is great until the end, which doesn\u2019t match up.\"",
            "",
            "\u2605\u2605\u2605\u2605\u2605 by Robert E. O. Speedwagon",
            "\"I laughed, I cried and I cheered, and then right near",
            "the end of the book, 05683! So what now? I have to buy",
            "in to a whole series to get closure?\"",
            "",
            "\u2605\u2605\u2605\u2605\u2605 by W. D. Gaster",
            "\"Still a better love story than Toradora\""
        ]
    },
    4: {
        "color": "#990000",
        "name": "How to Bombproof Your Horse",
        "lore": [
            "Although it\u2019s true that horses spook easily, \"bombproofing\"",
            "sounds a bit drastic, doesn't it? As if this book's techniques",
            "aren't enough for a worried horse owner, there's a sequel",
            "entitled \"Better Than Bombproof: New Ways to Make Your Horse",
            "a Solid Citizen and Keep You Safe on the Ground, in the Arena,",
            "and on the Trail.\" If there's ever a third book, it'll have to",
            "contain no less than the secret to eternal life.",
            "",
            "CHAPTER 1: Precautions",
            "Book Company Inc. is not responsible for any permanent",
            "damage inflicted upon you, your horse or your sanity."
        ]
    },
    5: {
        "color": "#EEFF00",
        "name": "The Joy of Chickens",
        "lore": [
            "A must-have for any chicken enthusiast."
        ]
    },
    6: {
        "color": "#00FFC4",
        "name": "The Miracles of Gsus",
        "lore": [
            "This book shows the true musical potential of the",
            "arguably uncommon Gsus chord. Legend has it, if you",
            "play it five times you'll summon Beethoven himself."
        ]
    },
    7: {
        "color": "#004166",
        "name": "Harry Potter and the Pit of Infinite Suffering",
        "lore": [
            "The long-awaited sequel to the bestseller book",
            "\"Harry Potter and the Cauldron of Excruciating Pain\"",
            "",
            "CHAPTER 1: ouch",
            "",
            "CHAPTER 2: oh god",
            "",
            "CHAPTER 3: OH MY GOD STOP IT AAAA",
            "",
            "CHAPTER 4: AOEIAOEIAOEIOEAAOEEIAOAEIOEA"
        ]
    },
    8: {
        "color": "#C8E6FA",
        "name": "Off-brand Newspapers",
        "lore": [
            "Dated 1985",
            "BREAKING NEWS - Advertisement -",
            "Top Sputtium Inc. Researchers have discovered a",
            "cure for aging! Just type in your credit card",
            "number and bank info to continue reading.",
            "",
            "- Advertisement -",
            "Are you interested in getting rid of your local Bob?",
            "Well, we got the perfect solution for you! The Sputtium Inc.",
            "Product Development Team proudly present to you:",
            "Ultra Effective Anti-Bob Spray!! Order now for 2% off",
            "on your first life-time supply order!",
            "(offer expires in 30 seconds)",
            "",
            "29th of February, 1985",
            "A man has fallen into the river in LEGO city! Start the new",
            "rescue helicopter! Build the helicopter and off to the",
            "rescue! Prepare the lifeline, lower the stretcher and",
            "make the rescue!",
            "",
            "- Weather Forecast -",
            "Apologies, our production budget ran out. We're taking a",
            "guess and saying it'll rain today. Don't sue us. Please.",
            "- Bingo Bongo, Head Writer",
            "",
            "This newspaper uses cookies to enhance your experience.",
            "By reading this, you support our use of cookies and are",
            "also legally required to pay us $300 in management fees."
        ]
    },
    9: {
        "color": "#0090FF",
        "name": "Stack of unpaid taxes",
        "lore": [
            "\"You owe us 5 million dollars. Please pay",
            "immediately or we will nuke your house.\"",
            "- The Government",
            "(Due March 19, 1997)"
        ]
    },
    10: {
        "color": "#E600FF",
        "name": "Boshimage Hira: A biography",
        "lore": [
            "My name is Boshimage Hira, i am 33 years old.",
            "My house is in the southwest section of the Mushroom",
            "Kingdom, where all the villas are, and I am not married.",
            "I work as an employee for the Yame Ku department",
            "stores, and I get home every day by 8 PM at the latest.",
            "I'm in bed by 11 PM, and make sure I get eight hours of",
            "sleep, no matter what. After getting a glass of warm milk",
            "and doing about twenty minutes of stretches before",
            "going to bed, I usually have no problems sleeping until",
            "morning. Just like a baby, I wake up without any fatigue",
            "or stress in the morning. I was told there were no issues",
            "at my last check-up. I'm trying to explain that I'm a person",
            "who wishes to live a very quiet life. I take care not to",
            "trouble myself with any enemies, like winning and losing,",
            "that would cause me to lose sleep at night. That is how I",
            "deal with society, and I know that is what brings me happiness."
        ]
    },
    11: {
        "color": "#9000FF",
        "name": "JaJa's Totally Normal (Nothing out of the ordinary) Adventure",
        "lore": [
            "A series of books where Janis J. Karen kills and dismembers",
            "various managers of different companies",
            "",
            "PART 1:",
            "Scam Tendency",
            "",
            "PART 2:",
            "Karen Blood",
            "",
            ". . . (It goes on for more 6 more parts)"
        ]
    },
    12: {
        "color": "#661100",
        "name": "Necronomicon",
        "lore": [
            "Once pertained to a master necromancer before",
            "spontaneousley combusting.",
            "",
            "Contains pages upon pages filled with ancient writings only",
            "masters of necromancy could understand.",
            "",
            "PAGE 1",
            "Glonginbing Skiblongle Glonbert Skalalalalsklingilingi glob",
            "blongu blongu bob"
        ]
    },
    13: {
        "color": "#FFF",
        "name": "a stack of dirt",
        "lore": [
            "its just dirt",
            "        a lot of it"
        ]
    },
    14: {
        "color": "#FA0",
        "name": "Metallic Artifact",
        "lore": [
            "Made of an unknown alloy."
        ]
    },
    15: {
        "color": "#FF5",
        "name": "Ancient device",
        "lore": [
            "Ancient fusions between keys",
            "and doorways. Appears to be",
            "an ancient puzzle cube??"
        ]
    },
    16: {
        "color": "#55F",
        "name": "Sputt Egg",
        "lore": [
            "It's just staring at you.",
            "Ominously."
        ]
    },
    17: {
        "color": "#5F5",
        "name": "Sputt Sushi",
        "lore": [
            "Not for human consumption.",
            "Pro tip: Wear it on your head",
            "and tilt it forward/backwards",
            "to look super wacky"
        ]
    },
    18: {
        "color": "#F5F",
        "name": "Mini Sputt Plush: Secret Service edition",
        "lore": [
            "May or may not nuke your house."
        ]
    },
    19: {
        "color": "#F5F",
        "name": "Mini Sputt Plush",
        "lore": [
            "owo cute",
            "must protect"
        ]
    },
    20: {
        "color": "#FA0",
        "name": "Sputt Chest",
        "lore": [
            "Something went wrong and the",
            "Sputt had fused with the chest :("
        ]
    },
    21: {
        "color": "#F55",
        "name": "Bob Relic",
        "lore": [
            "Once an object of worship.",
            "Now just another wacky artefact.",
            "Do not anger it."
        ]
    },
    22: {
        "color": "#FA0",
        "name": "Ancient Device",
        "lore": [
            "Unknown purpose, unknown origin.",
            "Filled with cogs and wheels.",
            "Surprisingly well-preserved."
        ]
    },
    23: {
        "color": "#5F5",
        "name": "Speed Artifact",
        "lore": [
            "Where have I seen this before?"
        ]
    },
    24: {
        "color": "#0AA",
        "name": "Water Relic",
        "lore": [
            "Emits a cool, refreshing aura."
        ]
    },
    25: {
        "color": "#0A0",
        "name": "Earth Relic",
        "lore": [
            "Reacts when exposed to sunlight."
        ]
    },
    26: {
        "color": "#FFF",
        "name": "Wind Relic",
        "lore": [
            "The velocity of the air around",
            "it is magnified greatly."
        ]
    },
    27: {
        "color": "#A00",
        "name": "Fire Relic",
        "lore": [
            "Scorches the ground around you,",
            "but leaves you unharmed."
        ]
    },
    28: {
        "color": "#FF5",
        "name": "Light Relic",
        "lore": [
            "Illuminates the surroundings but",
            "isn't visibly emitting any light."
        ]
    },
    29: {
        "color": "#A0A",
        "name": "Ender Relic",
        "lore": [
            "Shifts and warps itself as",
            "you hold it in your hand."
        ]
    },
    30: {
        "color": "#FF80E1",
        "name": "Big Brain",
        "lore": [
            "Yes. This is big brain time."
        ]
    },
    31: {
        "color": "#A0A",
        "name": "Ominous Bread",
        "lore": [
            "watching..."
        ]
    },
    32: {
        "color": "#7AC9CC",
        "name": "Victor's Debt Filled Adventure",
        "lore": [
            "A series of books that accompany the tale of Victor J. 1912, in his attempt",
            "to recover from absolute bankruptcy.",
            "",
            "Part 1 - Money Blood",
            "",
            "Part 2 - Loan Tendency",
            "",
            "Part 3 - Bank Crusaders",
            "",
            "Part 4 - Debt is Unpayable",
            "",
            "Part 5 - Golden Alloy"
        ]
    },
    33: {
        "color": "#F5F",
        "name": "Bob Dating Simulator",
        "lore": [
            "Sputtendo Switch Game Cartridge",
            "",
            "Experience an all-new realistic",
            "dating experience with the Bob you",
            "all know and love!",
            "",
            "Sputtendo does not endorse dating Bob"
        ]
    },
    34: {
        "color": "#FFF",
        "name": "Stone &fBall",
        "lore": [
            "The pinnacle of geometry."
        ]
    },
    35: {
        "color": "#0A0",
        "name": "Mossy Helmet",
        "lore": [
            "A helmet that looks ancient, however",
            "it is simply a trick, an act of foolery;",
            "the moss is infact purely decorative."
        ]
    },
    36: {
        "color": "#FF6600",
        "name": "Sentient Bobbo Nuggie",
        "lore": [
            "It's staring at you.",
            "Care to take a bite?"
        ]
    },
    37: {
        "color": "#0AA",
        "name": "Failed Experiment #53",
        "lore": [
            "Banished to the Sputtrooms,",
            "yet only managed to spread further.",
            "",
            "This decorational replica is a model",
            "of how mortal humans percieve it."
        ]
    },
    38: {
        "color": "#55F",
        "name": "Cobalt Corn",
        "lore": [
            "This corn was grown on top of a",
            "huge cobalt deposit and developed",
            "a blue color. Toxicity unkown."
        ]
    },
    39: {
        "color": "#F55",
        "name": "Nether Corn",
        "lore": [
            "Grown in the depths of nether,",
            "this corn has developed a red",
            "color. Eating it will most likely",
            "summon the demons of the",
            "underworld, or something."
        ]
    },
    40: {
        "color": "#5F5",
        "name": "Green Corn",
        "lore": [
            "Has an extremely high natural radioactivity",
            "from growing on an uranium deposit.",
            "It's a miracle it hasn't killed you already."
        ]
    },
    41: {
        "color": "#FF5",
        "name": "Can of off-brand soda",
        "lore": [
            "Shiny\u2122 Soda\u00ae, the only soda in",
            "this world that (probably\u2122) won't",
            "kill you and your family! \u00a9"
        ]
    },
    42: {
        "color": "#F55",
        "name": "Legendary Artifact (replica)",
        "lore": [
            "Highly soluble in dogs."
        ]
    },
    43: {
        "color": "#FA0",
        "name": "Accordion",
        "lore": [
            "Can be played!",
            "Left-click to play, change pitch by",
            "moving your head up and down."
        ]
    },
    44: {
        "color": "#FFF",
        "name": "Piano",
        "lore": [
            "Can be played!",
            "Left-click to play, change pitch by",
            "moving your head up and down."
        ],
        "audio": "harp"
    },
    45: {
        "color": "#FA0",
        "name": "Ancient Drum",
        "lore": [
            "Can be played!",
            "Left-click to play, change pitch by",
            "moving your head up and down."
        ]
    },
    46: {
        "color": "#FA0",
        "name": "Electronic Donkey",
        "lore": [
            "Can be played!",
            "Left-click to play, change pitch by",
            "moving your head up and down."
        ]
    },
    47: {
        "color": "#FA0",
        "name": "Banjo",
        "lore": [
            "Can be played!",
            "Left-click to play, change pitch by",
            "moving your head up and down."
        ],
        "audio": "banjo"
    },
    48: {
        "color": "#FFF",
        "name": "Vent",
        "lore": [
            "It's where the imposter went."
        ]
    },
    49: {
        "color": "#F55",
        "name": "Beetroot Replica",
        "lore": [
            "Used in those display fruit baskets",
            "found in furniture stores. Has since",
            "been retired and buried in a chest."
        ]
    },
    50: {
        "color": "#AAA",
        "name": "Olden Iron Helmet",
        "lore": [
            "Once donned for war, now lost",
            "only to be found again."
        ]
    },
    51: {
        "color": "#F5F",
        "name": "High-specs Graphics Card",
        "lore": [
            "Too bad you have no computer",
            "to actually use it in, rendering it",
            "completely and utterly useless.",
            "",
            "What a shame."
        ]
    },
    52: {
        "color": "#F55",
        "name": "Broken Sputtendo 64",
        "lore": [
            "Can be played!",
            "Left-click to play, change pitch by",
            "moving your head up and down."
        ],
        "audio": "bit"
    },
    53: {
        "color": "#F55",
        "name": "Flesh Monstrosity",
        "lore": [
            "Luckily, it doesn't seem to be alive.",
            "Not commonly sold in convenience stores."
        ]
    },
    54: {
        "color": "#F55",
        "name": "Fleshfruit",
        "lore": [
            "High in nutrients.",
            "",
            "The fleshy skin wraps its fleshy insides",
            "in an exotic display of fleshy flavor.",
            "These plants commonly grow from flesh trees."
        ]
    },
    55: {
        "color": "#FF5",
        "name": "Golden Seed",
        "lore": [
            "A golden seed, fount at the base of",
            "an illusory tree. Increases your maximum",
            "uses of bad references."
        ]
    },
    56: {
        "color": "#FA0",
        "name": "Old Lantern",
        "lore": [
            "Ran out of fuel years ago.",
            "Must've been left there by some",
            "long-gone miner."
        ]
    },
    57: {
        "color": "#FFF",
        "name": "Scale Cube",
        "lore": [
            "A cube made out of iron-clad scales.",
            "Too tough to open, though you might",
            "not want to know what's inside..."
        ]
    },
    58: {
        "color": "#F55",
        "name": "Plumber-shaped Object",
        "lore": []
    },
    59: {
        "color": "#F55",
        "name": "Unusually Large Heart",
        "lore": [
            "Slightly larger than your head.",
            "You should fear whoever once had this."
        ]
    },
    60: {
        "color": "#FA0",
        "name": "Respectable Pottery",
        "lore": [
            "1. Wipe Your Shoes",
            "2. Have Fun",
            "3. Respect The Pottery",
            "4. Have Fun",
            "5. List Entry Duplication Error"
        ]
    },
    61: {
        "color": "#0A0",
        "name": "Ancient Guacamole",
        "lore": [
            "Difficult to identify.",
            "Might possibly be acid."
        ]
    },
    62: {
        "color": "#0A0",
        "name": "Ancient Acid",
        "lore": [
            "Difficult to identify.",
            "Might possibly be guacamole."
        ]
    },
    63: {
        "color": "#F55",
        "name": "Krox Mask",
        "lore": [
            "Wear it to become krox's",
            "cooooooooooooool friend."
        ]
    },
    64: {
        "color": "#FFAA00",
        "name": "Archeologist's Trophy",
        "lore": [
            "Awe and respect is only for the few.",
            "This item, however, seems to be malfunctioning",
            "as you have not received any, despite having",
            "obtained a trophy.",
            "",
            "Yet such are the ways of the game."
        ]
    },
    65: {
        "color": "#97B9CC",
        "name": "Reassurance Bucket",
        "lore": [
            "Somehow, holding this bucket gives you",
            "a feeling of comfort and contentment."
        ]
    },
    66: {
        "color": "#CC7E18",
        "name": "Bucket of nuggets",
        "lore": [
            "Caution: may contain harpy."
        ]
    },
    67: {
        "color": "#A0A",
        "name": "Code Warp Block",
        "lore": [
            "Got a big line of code? Warp it somewhere!"
        ]
    },
    68: {
        "color": "#663700",
        "name": "Ancient Poop",
        "lore": []
    },
    69: {
        "color": "#F55",
        "name": "The Red Stone of Aaa",
        "lore": [
            "Said to be able to absorb screams and",
            "refract them a million times."
        ]
    },
    70: {
        "color": "#FA0",
        "name": "Lizard Cube #5",
        "lore": [
            "Supposedly, there's more... but who knows?"
        ]
    },
    71: {
        "color": "#998E17",
        "name": "Bucket of Decaying Slop",
        "lore": [
            "Truly the best treasure one",
            "could ever ask for."
        ]
    },
    72: {
        "color": "#CCB185",
        "name": "Dummy Box",
        "lore": [
            "Do you want to punch someone?",
            "Maybe try out a new killing move?",
            "Then this is the best simulation",
            "of a human body you can get!",
            "Just place it down and then make",
            "it go BOOM-PAUF-POW-BAM!!"
        ]
    },
    73: {
        "color": "#CC950A",
        "name": "World's 2nd Largest Potato",
        "lore": [
            "Once found by a german farmer, this",
            "45cm wide and 15cm tall potato has",
            "enough mass to produce 18 bags of",
            "standard-size bags of potato chips.",
            "Too bad the farmed decided to bury",
            "his produce in a chest underground."
        ]
    },
    74: {
        "color": "#4BCC71",
        "name": "World's Largest Bacteria",
        "lore": [
            "Measuring 2.5cm wide and 4cm tall, this",
            "now-dead bacteria was supposedly",
            "found floating like a balloon in the",
            "closet of a Sputtium Inc. researcher."
        ]
    },
    75: {
        "color": "#FFF68C",
        "name": "Mayonnaise Manual ",
        "lore": [
            "A book with seemingly never-ending yet",
            "thought-provoking ideas revolving around",
            "the intriguing subject of mayonnaise.",
            "",
            "CHAPTER 1",
            "How to avoid fake mayonnaise:",
            "1: Look at the package or bottle.",
            "2: Check if the container has images on it",
            "3: If it has images of eggs, then it's real",
            "4: If not, burn it and smash it to pieces."
        ]
    },
    76: {
        "color": "#5F5",
        "name": "Emerald Banana",
        "lore": [
            "An ancient fruit consumed traditionally",
            "by villagers. Has more potassium than",
            "a regular banana, yet its hard shell is",
            "difficult to peel off without proper tools."
        ]
    }
}

COMMUNIST = [(x, False) if isinstance(x, str) else x for x in [
    "Communist Flakes",
    "Potato",
    "Refined Ruby",
    ("Clover", True),
    "Present",
    "Netherite Ingot",
    "Soul",
    "Luxury Cheese",
    "Baked Potato",
    "Amber",
    "Amethyst",
    ("Onyx", True),
    "Lead Ingot",
    "Wood",
    "Cookie",
    "Aureate Grapes",
    "Void Orb",
    "Banana",
    ("Uranium", True),
    "Super Glue",
    "Clover Bag",
    "Magnesium",
    "Ancient Tooth",
    "Silica",
    "Communite",
    "Pig Steel",
    "Volcanic Ash",
    ("Sage Crystal", True),
    "Plutonium",
    "Refined Amethyst",
    "Copper Ingot",
    ("Wurtzite Boron Nitride", True),
    "Honey",
    "Banana",
    "Hypercompact Stone",
    "Aureate Grapes",
    "Meteorite Bar",
    "Gold Ingot",
    "Exquisite Pumpkin",
    "Flint Edge",
    "Mustache Polish",
    "Cookie",
    ("Plastic Sheet", True),
    "Lead Plate",
    "Graphene",
    "Soul",
    "Communite",
    ("Stalinium", True)
]]

ENCHANTMENTS = {
    "Autoforge": {
        "effect": "0.2% x level chance of automatically forging drop",
        "location": "Swim through the waterfalls by the Sand God in the mesa",
        "requirements": [
            ["Magma Orb", "Sage Crystal", "Steel", "Wurtzite Boron Nitride"],
            ["Magma Core", "Refined Onyx", "Sage Crystal", "Steel Plate"],
            ["Gold Block", "Perfect Amethyst", "Sage Crystal", "Steel Plate"],
            ["Antimatter", "Perfect Amber", "Sage Crystal", "Wurtzite Boron Nitride Compound Plate"],
            ["Perfect Topaz", "Potassium Ingot", "Sage Crystal", "Sand Pearl"]
        ]
    },
    "Drill": {
        "effect": "Chance to break blocks around mined block",
        "location": "In nether area mining towards the corner closest to the overworld forge",
        "requirements": [
            ["Bacon", "Cheese", "Gemstone Mixture", "Onyx"],
            ["Luxury Cheese", "Onyx", "Pig Steel", "Refined Ruby"],
            ["Pig Steel", "Refined Amethyst", "Refined Ruby", "Topaz"],
            ["Pig Steel", "Refined Amethyst", "Refined Onyx", "Topaz"],
            ["Adamantium", "Pig Steel", "Refined Amethyst", "Refined Topaz"],
            ["Bedrock Piece", "Omega Alloy", "Refined Onyx"]
        ]
    },
    "Efficiency": {
        "effect": "Increased mining speed",
        "location": "Behind Bob's Pickaxe Emporium on the left",
        "requirements": [
            ["Anthracite"],
            ["Amber", "Graphite"],
            ["Amber", "Graphite", "Graphite", "Graphite"],
            ["Amber Crystal", "Graphene"],
            ["Graphene", "Netherite Ingot", "Onyx"],
            ["Graphene", "Graphene", "Onyx", "Refined Amber"],
            ["Boron Nitride", "Onyx", "Refined Amber"],
            ["Steel Plate", "Wurtzite Boron Nitride"],
            ["Wurtzite Boron Nitride Compound Plate"],
            ["Adamantium", "Arkenstone Fragment", "Void Alloy", "Void Singularity"],
            ["Banana", "Perfect Diamond", "Void Alloy", "Void Singularity"],
            ["Banana", "Omega Shard"],
            ["Banana", "Omega Alloy", "Perfect Amber"],
            ["Antimatter", "Omega Alloy", "Sage Crystal", "Wurtzite Boron Nitride Compound Plate"],
            ["Omega Alloy", "Perfect Onyx", "Perfect Topaz", "Sage Crystal"]
        ]
    },
    "Festive": {
        "effect": "When mining, small chance to drop gifts",
        "location": "To right of mesa entrance",
        "requirements": [
            ["Snowball", "Snow Chunk", "Snow Chunk"],
            ["Snow Block (Item)", "Snow Block (Item)"],
            ["Compressed Snow", "Compressed Snow", "Present"],
            ["Black Present", "Compressed Snow", "Hypercompact Snow", "Present"],
            ["Gold Present", "Hypercompact Snow", "Hypercompact Snow", "Present"],
            ["Opal", "Gold Present", "Gold Present"],
            ["Perfect Opal"]
        ]
    },
    "Gills": {
        "effect": "Increases oxygen supply of armor piece by 10% of base + 2s x level",
        "location": "\"FREE WIFI\" tunnel when heading from the mesa to the water mine",
        "requirements": [
            ["Orichalcum Scrap", "Rockite Chunk", "Flint", "Oxycoral"],
            ["Orichalcum Shards", "Processed Rockite", "Impure Lead", "Oxygen Bottle"],
            ["Orichalcum Piece", "Compressed Rockite", "Plastic Sheet", "Oxygen Bottle"],
            ["Orichalcum Lump", "Hypercompact Rockite", "Uranium"],
            ["Impure Orichalcum", "Hematite", "Plutonium"]
        ]
    },
    "Luck": {
        "effect": "Increases chance of finding rare drops by 10% x level",
        "location": "2nd floor of backpack shop",
        "requirements": [
            ["Golden Grass"],
            ["Clover", "Golden Grass"],
            ["Clover", "Clover", "Golden Grass", "Golden Grass"],
            ["Clover Bag", "Golden Grass", "Golden Grass", "Golden Grass"],
            ["Diamond Grass"],
            ["Clover Bag", "Clover Bag"],
            ["Golden Clover Bag"],
            ["Diamond Grass", "Golden Clover Bag"],
            ["Clover Bag", "Diamond Grass"],
            ["The Arkengrass"],
            ["RNG Trophy"],
            ["Golden Clover Bag", "RNG Trophy", "The Arkengrass"],
            ["Potassium", "RNG Trophy", "RNG Trophy"],
            ["Potassium Ingot", "RNG Trophy", "RNG Trophy", "RNG Trophy"],
            ["Amogus"]
        ]
    },
    "Overclocked": {
        "effect": "2% x level chance to overclock an item when Sage activates",
        "location": "Go up the mossy hill in the mountain mine, then go through the cave on your right by the unlit candles",
        "requirements": [
            ["Perfect Ruby", "Crimson Sod", "Sage Crystal", "Sage Crystal"],
            ["Ruby Grass", "Overclocker", "Sage Crystal", "Orichalcum Ingots"],
            ["Crimsonbrand Grass", "Overclocker", "Perfect Aquamarine", "Engine"],
            ["Elusive Fossil", "Wurtzite Boron Nitride Compound Plate", "Overclocker", "Overclocker"],
            ["Flawless Gemstone Mesh Orb", "Overclocker", "Overclocker", "Overclocker"]
        ],
    },
    "Plated": {
        "effect": "Increases armor's radiation resistance",
        "location": "Tech crafting area in mesa",
        "requirements": [
            ["Impure Lead", "Impure Lead", "Impure Lead"],
            ["Impure Lead", "Lead Ingot", "Uranium Ore"],
            ["Electric Circuit", "Lead Ingot", "Lead Ingot", "Uranium"],
            ["Advanced Circuit", "Lead Ingot", "Lead Ingot", "Plutonium"],
            ["Battery", "Lead Plate", "Plutonium", "Processing Unit"]
        ]
    },
    "Pristine": {
        "effect": "When mining, small chance to drop amethysts",
        "location": "Blackstone layer facing moon door (chunk-relative: 11 ~ 15 on right side of mine)",
        "requirements": [
            ["Onyx", "Refined Amber", "Refined Ruby", "Synthetic Diamond"],
            ["Amethyst", "Starite", "Starite"],
            ["Amethyst", "Amethyst", "Amethyst", "Celestial Ingot"],
            ["Amethyst", "Celestial Ingot", "Celestial Ingot", "Refined Amethyst"],
            ["Amethyst", "Amethyst", "Refined Amethyst", "Refined Amethyst"],
            ["Perfect Amethyst"],
            ["Celestial Ingot", "Perfect Amethyst", "Refined Amethyst", "Refined Amethyst"],
            ["Celestial Ingot", "Perfect Amethyst", "Perfect Amethyst"],
            ["Perfect Amethyst", "Perfect Amethyst", "Refined Amethyst", "Refined Amethyst"],
            ["Celestial Artefact", "Perfect Amethyst", "Perfect Amethyst", "Perfect Amethyst"],
            ["Perfect Amethyst", "Perfect Amethyst", "Perfect Amethyst", "Perfect Amethyst"]
        ]
    },
    "Prosperity": {
        "effect": "When mining, 5% x level chance to get 2x drops",
        "location": "To right of overworld forge",
        "requirements": [
            ["Earth Crystal"],
            ["Compressed Stone", "Iron Ore"],
            ["Gold Ingot", "Graphite"],
            ["Magma Gem", "Netherite Ingot", "Ruby", "Silica"],
            ["Boron Nitride", "Onyx", "Salt", "Soul"],
            ["Amethyst", "Magma Orb", "Wurtzite Boron Nitride"],
            ["Adamantium", "Pig Steel", "Topaz"],
            ["Refined Topaz", "Void Alloy", "Void Singularity"],
            ["Arkenstone Fragment", "Banana", "Celestial Artefact", "Refined Onyx"],
            ["Perfect Amethyst", "Perfect Diamond", "Perfect Ruby", "Perfect Topaz"]
        ]
    },
    "Sage": {
        "effect": "1% x level chance of giving a Saged version of drop",
        "location": "Behind moon door",
        "requirements": [
            ["Refined Amber", "Void Shard"],
            ["Synthetic Diamond", "Void Matter"],
            ["Banana", "Graphene", "Graphene", "Void Orb"],
            ["Magnesium Ingot", "Perfect Ruby", "Silica", "Void Singularity"],
            ["Magma Core", "Void Singularity", "Void Singularity", "Wurtzite Boron Nitride"],
            ["Adamantium", "Antimatter", "Perfect Topaz", "Void Alloy"],
            ["Sand Pearl", "Lead Plate", "Refined Copper", "Oil Bucket"],
            ["Processing Unit", "Perfect Aquamarine", "Engine", "Cream"],
            ["Orichalcum Ingots", "Perfect Hematite", "Dried Kelp", "Flint Edge"]
        ]
    },
    "sans": {
        "effect": "Small chance to play a tune and drop items",
        "location": "Bob's shop in the Sputtrooms",
        "requirements": [
            ["Bedrock Piece", "Bone Block", "Bone Block", "Bone Block"]
        ]
    },
    "Stonks": {
        "effect": "Gives money when you break a block",
        "location": "Behind Nether door",
        "requirements": [
            ["Gold Ingot", "Ruby"],
            ["Gold Ingot", "Gold Ingot", "Gold Ingot", "Refined Ruby"],
            ["Bag of Gold", "Gold Block", "Refined Ruby"],
            ["Adamantium Scraps", "Gold Block", "Pot of Gold", "Refined Ruby"],
            ["Gold Block", "Gold Block", "Gold Trophy", "Perfect Ruby"]
        ]
    }
}

BLOCKS = {
    "Ancient Debris": {
        "drops": [
            "Netherite Scrap",
            "Netherite Ingot"
        ],
        "rbp": 4
    },
    "Andesite": {
        "drops": [
            "Andesite Chunk"
        ],
        "layers": [
            Layer.Stone,
            Layer.Blackstone
        ],
        "rbp": 1
    },
    "Basalt": {
        "drops": [
            "Basalt",
            "Compressed Stone",
            "Hypercompact Stone",
            "Volcanic Ash",
            "Salt",
            "Soul Fragments",
            "Soul Shard"
        ],
        "rbp": 4
    },
    "Beacon": {
        "drops": [
            "Present",
            "Black Present",
            "Gold Present"
        ]
    },
    "Bedrock": {
        "drops": [
            "Bedrock Piece"
        ],
        "dew": "Chiseled Deepslate",
        "rbp": 9
    },
    "Beehive": {
        "drops": [
            "Honeycomb",
            ("Honey", 108)
        ]
    },
    "Black Stained Glass": {
        "drops": [
            "Void Matter",
            "Void Shard",
            ("Void Orb", 1500),
            ("Void Alloy", 250)
        ],
        "dew": "Gray Stained Glass",
        "rbp": 7
    },
    "Black Terracotta": {
        "drops": [
            "Stupid Stone"
        ],
        "rbp": 10
    },
    "Blackstone": {
        "drops": [
            "Coal Piece",
            "Coal",
            "Anthracite",
            "Blackstone Chunk"
        ],
        "dew": "Block of Coal",
        "layers": [
            Layer.Blackstone,
            Layer.Brimstone
        ],
        "rbp": 3
    },
    "Block of Coal": {
        "drops": [
            "Coal",
            "Anthracite",
            "Graphite"
        ],
        "rbp": 3,
        "id": "coal_block"
    },
    "Block of Copper": {
        "id": "copper_block",
        "drops": None
    },
    "Block of Diamond": {
        "drops": [
            "Impure Orichalcum",
            "Orichalcum"
        ],
        "id": "diamond_block"
    },
    "Block of Emerald": {
        "drops": [
            "Uranium Ore",
            "Uranium"
        ],
        "id": "emerald_block"
    },
    "Block of Gold": {
        "drops": [
            "Gold Ore",
            "Gold Ingot"
        ],
        "rbp": 5,
        "id": "gold_block"
    },
    "Block of Iron": {
        "drops": [
            "Iron Ore",
            "Iron Ingot"
        ],
        "id": "iron_block"
    },
    "Block of Lapis Lazuli": {
        "drops": [
            "Water Orb"
        ],
        "id": "lapis_lazuli_block"
    },
    "Block of Netherite": {
        "drops": [
            "Graphene",
            "Adamantium Scraps"
        ],
        "dew": "Chiseled Nether Bricks",
        "id": "netherite_block"
    },
    "Block of Raw Copper": {
        "id": "raw_copper_block",
        "drops": None
    },
    "Blue Ice": {
        "drops": [
            "Ice",
            "Aquamarine"
        ],
        "dew": "Light Blue Stained Glass"
    },
    "Blue Stained Glass": {
        "drops": [
            "Sog Stone",
            "Sog Gem"
        ],
        "dew": "Block of Lapis Lazuli",
        "rbp": 0
    },
    "Brain Coral Block": {
        "drops": [
            "Bacon",
            "Pig Steel"
        ],
        "rbp": 3
    },
    "Brown Mushroom Block": {
        "drops": [
            "Meteorite Core"
        ]
    },
    "Brown Wool": {
        "drops": [
            "Chocolate Chips"
        ]
    },
    "Chiseled Deepslate": {
        "drops": [
            "Reinforced Bedrock"
        ]
    },
    "Chiseled Nether Bricks": {
        "drops": [
            "Adamantium"
        ]
    },
    "Chiseled Stone Bricks": {
        "drops": [
            "Hypercompact Stone"
        ]
    },
    "Clay": {
        "drops": [
            "Clay",
            "Sog Stone",
            "Aluminium Ore"
        ]
    },
    "Coal Ore": {
        "drops": [
            "Coal Piece",
            "Coal"
        ],
        "layers": [
            Layer.Stone,
            Layer.Blackstone
        ]
    },
    "Coarse Dirt": {
        "drops": [
            "Dirt",
            "Pebble",
            "Earth Crystal",
            "Bone",
            ("Amber", 900),
            "Ancient Tooth",
            "Ancient Skull",
            ("RNG Trophy", 200000),
            "Amogus"
        ],
        "layers": [Layer.Dirt],
        "rbp": 0
    },
    "Cobblestone": {
        "drops": [
            "Stone Chunk",
            "Cobblestone Chunk"
        ],
        "layers": [Layer.Stone],
        "rbp": 1
    },
    "Conduit": {
        "drops": [
            "Arkenstone Fragment"
        ]
    },
    "Crimson Hyphae": {
        "drops": [
            "Blood"
        ],
        "rbp": 4
    },
    "Crimson Nylium": {
        "drops": [
            "Crimson Sod",
            "Refined Ruby"
        ]
    },
    "Crying Obsidian": {
        "drops": [
            "Ender Ore",
            "Obsidian"
        ],
        "dew": "Bedrock",
        "rbp": 5
    },
    "Dark Prismarine": {
        "drops": [
            "Orichalcum Scrap"
        ]
    },
    "Dead Brain Coral Block": {
        "drops": [
            "Rockite",
            "Rockite Chunk",
            ("Water Amethyst", 400),
            "Cobblestone Chunk"
        ],
        "dew": "Dead Bubble Coral Block"
    },
    "Dead Horn Coral Block": {
        "drops": [
            "Lead Ore",
            "Impure Lead",
            "Lead Ingot"
        ],
        "dew": "Polished Blackstone"
    },
    "Diamond Ore": {
        "drops": [
            "Orichalcum Chips",
            "Orichalcum Scrap",
            "Orichalcum Shards"
        ]
    },
    "Diorite": {
        "drops": [
            "Aluminium Ore",
            "Impure Aluminium"
        ]
    },
    "Dirt": {
        "drops": [
            "Dirt",
            "Pebble",
            ("Earth Crystal", 100),
            ("Bone", 150),
            ("Amber", 2000),
            ("Ancient Tooth", 4000),
            ("Ancient Skull", 9000),
            ("Mosquito Amber", 15000),
            ("RNG Trophy", 200000),
            "Amogus"
        ],
        "dew": "Rooted Dirt",
        "hardness": 15,
        "rbp": 0,
        "layers": [Layer.Dirt]
    },
    "Dried Kelp Block": {
        "drops": [
            "Kelp"
        ]
    },
    "Emerald Ore": {
        "drops": [
            "Uranium Ore"
        ]
    },
    "End Stone": {
        "drops": [
            "Cheese",
            "Luxury Cheese",
            "Topaz"
        ],
        "dew": "End Stone Bricks",
        "rbp": 6
    },
    "End Stone Bricks": {
        "drops": [
            "Cheese",
            "Luxury Cheese",
            "Topaz"
        ],
        "dew": "Yellow Stained Glass",
        "rbp": 6
    },
    "Fire": {
        "drops": [
            "Stone"
        ]
    },
    "Flowering Azalea Leaves": {
        "drops": [
            "Flower"
        ]
    },
    "Gilded Blackstone": {
        "drops": [
            "Blackstone Chunk",
            "Gilded Chunk",
            "Banana"
        ],
        "layers": [
            Layer.Blackstone,
            Layer.Brimstone
        ],
        "rbp": 3
    },
    "Gold Ore": {
        "drops": [
            "Gold Ore"
        ],
        "dew": "Block of Gold",
        "layers": [Layer.Stone]
    },
    "Grass Block": {
        "drops": [
            "Dirt",
            "Grass",
            ("Golden Grass", 150),
            ("Diamond Grass", 10000),
            ("Clover", 1000),
            ("Potato", 1500)
        ],
        "dew": "Moss Block",
        "rbp": 0
    },
    "Gravel": {
        "drops": [
            "Pebble",
            "Clay",
            "Rough Flint",
            "Aquatic Pebble"
        ],
        "dew": "Dead Brain Coral Block"
    },
    "Gray Stained Glass": {
        "drops": [
            "Adamantium Scraps"
        ]
    },
    "Horn Coral Block": {
        "drops": [
            "Omega Shard"
        ]
    },
    "Ice": {
        "drops": [
            "Ice Fragments",
            "Ice Shard",
            ("Ice", 620)
        ],
        "dew": "Packed Ice"
    },
    "Iron Ore": {
        "drops": [
            "Iron Ore",
            "Stone Chunk"
        ],
        "dew": "Block of Iron",
        "layers": [
            Layer.Stone,
            Layer.Blackstone
        ],
        "rbp": 2
    },
    "Lapis Lazuli Ore": {
        "drops": [
            "Cobalt Ore"
        ]
    },
    "Light Blue Wool": {
        "drops": [
            "Orichalcum Lump",
            "Impure Orichalcum",
            "Orichalcum"
        ]
    },
    "Light Gray Glazed Terracotta": {
        "drops": [
            "Plutonium Ore"
        ]
    },
    "Magma Block": {
        "drops": [
            "Magma Stone"
        ],
        "dew": "Fire",
        "rbp": 5
    },
    "Moss Block": {
        "drops": [
            "Plant Fibre",
            "Clover",
            ("Clover Bag", 400),
            "Diamond Grass",
            ("Iridite Sod", 160)
        ],
        "rbp": 0
    },
    "Mycelium": {
        "drops": [
            "Meteorite"
        ],
        "dew": "Brown Mushroom Block"
    },
    "Nether Gold Ore": {
        "drops": [
            "Gold Ore",
            "Gold Ingot",
            "Sulfur"
        ],
        "dew": "Yellow Wool"
    },
    "Nether Quartz Ore": {
        "drops": [
            "Quartz",
            "Iron Ore",
            "Iron Ingot"
        ],
        "dew": "White Wool"
    },
    "Netherrack": {
        "drops": [
            "Brimstone",
            "Corundum",
            "Ruby",
            ("Refined Ruby", 5000),
            "Sulfur",
            "Magma Stone",
            "Quartz"
        ],
        "dew": "Nether Quartz Ore",
        "layers": [Layer.Brimstone]
    },
    "Oak Wood": {
        "drops": [
            "Wood"
        ],
        "layers": [Layer.Dirt]
    },
    "Obsidian": {
        "drops": [
            "Obsidian",
            "Anthracite"
        ],
        "dew": "Bedrock",
        "rbp": 5
    },
    "Orange Glazed Terracotta": {
        "drops": [
            "Copper Scraps",
            "Impure Copper",
            ("Copper Ingot", 400)
        ],
        "dew": "Polished Granite"
    },
    "Orange Terracotta": {
        "drops": [
            "Palladium Ore",
            "Impure Palladium"
        ]
    },
    "Packed Ice": {
        "drops": [
            "Ice Shard",
            ("Ice", 630)
        ],
        "dew": "Blue Ice",
        "layers": [Layer.Ice]
    },
    "Polished Andesite": {
        "drops": [
            "Andesite Chunk",
            "Stone Chunk",
            "Compressed Stone",
            "Stone Ball"
        ],
        "layers": [
            Layer.Stone,
            Layer.Blackstone
        ],
        "rbp": 3
    },
    "Polished Basalt": {
        "drops": [
            "Basalt",
            "Hypercompact Stone",
            "Volcanic Ash",
            "Salt",
            "Boron Nitride"
        ],
        "rbp": 5
    },
    "Polished Blackstone": {
        "drops": [
            "Impure Lead",
            "Lead Ingot"
        ],
        "dew": "Chiseled Polished Blackstone"
    },
    "Polished Blackstone Bricks": {
        "drops": [
            "Rockite Chunk",
            "Processed Rockite",
            "Compressed Rockite"
        ]
    },
    "Polished Granite": {
        "drops": [
            "Impure Copper",
            "Copper Ingot"
        ],
        "dew": "Block of Copper"
    },
    "Prismarine": {
        "drops": [
            "Orichalcum Shards",
            "Orichalcum Ore"
        ]
    },
    "Prismarine Bricks": {
        "drops": [
            "Orichalcum Shards",
            "Orichalcum Piece",
            "Orichalcum Lump",
            "Orichalcum Ore"
        ]
    },
    "Pumpkin": {
        "drops": [
            "Pumpkin",
            "Pumpkin Seeds"
        ]
    },
    "Red Glazed Terracotta": {
        "drops": [
            "Cherry"
        ]
    },
    "Red Sand": {
        "drops": [
            "Iron Sand",
            ("Red Herring", 2000)
        ],
        "dew": "Block of Raw Copper",
        "rbp": 0
    },
    "Redstone Ore": {
        "drops": [
            "Magma Stone",
            "Magma Gem",
            "Ruby"
        ],
        "layers": [Layer.Stone],
        "rbp": 4
    },
    "Rooted Dirt": {
        "drops": [
            "Earth Crystal",
            "Amber",
            "Amber Crystal",
            "Bone",
            "Ancient Tooth",
            "Ancient Skull",
            "Elusive Fossil",
            "Iridite Sod"
        ]
    },
    "Sand": {
        "drops": [
            "Sand",
            "Sandstone",
            ("Dense Sand", 3000),
            ("Sandfish", 800),
            ("Shell", 600),
            ("Fossil", 750),
            ("Ancient Tooth", 2000),
            ("Ancient Skull", 7000),
            ("Quartz", 400),
            "Clay",
            "Pebble",
            "Stone Chunk",
            "Copper Scraps",
            "Roots",
            "Earth Crystal",
            "Coal Piece",
            ("Kawaii Amogus", 2000000)
        ],
        "dew": "Red Sand",
        "rbp": 0
    },
    "Sandstone": {
        "drops": [
            "Sandstone",
            ("Dense Sand", 600),
            "Shell",
            ("Fossil", 700),
            "Roots"
        ],
        "dew": "Red Sandstone"
    },
    "Sea Lantern": {
        "drops": [
            "Celestial Ingot",
            "Starite"
        ],
        "dew": "Tinted Glass"
    },
    "Smooth Quartz Block": {
        "drops": None,
        "id": "smooth_quartz"
    },
    "Smooth Sandstone": {
        "drops": [
            "Egg"
        ]
    },
    "Smooth Stone": {
        "drops": [
            "Huge Compressed Stone",
            "Hypercompact Stone",
            "Synthetic Diamond"
        ],
        "dew": "Chiseled Stone Bricks"
    },
    "Snow": {
        "drops": [
            "Snowball",
            "Snow Chunk",
            "Snow Block",
            ("Compressed Snow", 10000),
            "Present",
            "Black Present",
            ("Gold Present", 45000),
            ("Arctic Amogus", 1000000)
        ]
    },
    "Snow Block": {
        "drops": [
            "Snowball",
            "Snow Chunk",
            "Snow Block",
            ("Compressed Snow", 10000),
            "Present",
            "Black Present",
            ("Gold Present", 45000),
            ("Arctic Amogus", 1000000)
        ],
        "dew": "Packed Ice"
    },
    "Soul Soil": {
        "drops": [
            "Salt",
            "Soul Fragments"
        ],
        "dew": "Soul Sand",
        "rbp": 0
    },
    "Spruce Wood": {
        "drops": [
            "Wood Ingot"
        ]
    },
    "Stone": {
        "drops": [
            "Pebble",
            "Stone Chunk",
            "Cobblestone Chunk"
        ],
        "dew": "Polished Andesite",
        "layers": [Layer.Stone],
        "rbp": 1
    },
    "Stripped Oak Wood": {
        "drops": [
            "Dough"
        ]
    },
    "Terracotta": {
        "drops": [
            "Clay",
            "Stone Chunk",
            "Palladium Ore"
        ]
    },
    "Tinted Glass": {
        "drops": [
            "Astral Ore"
        ]
    },
    "Tube Coral Block": {
        "drops": [
            "Oxycoral"
        ]
    },
    "Warped Hyphae": {
        "drops": [
            "Soul Shard"
        ],
        "rbp": 4
    },
    "Warped Nylium": {
        "drops": [
            "Soul Grass",
            "Soul Fragments"
        ],
        "dew": "Crimson Nylium",
        "rbp": 4
    },
    "White Concrete Powder": {
        "drops": [
            "Cake Frosting"
        ]
    },
    "White Wool": {
        "drops": [
            "Potassium",
            "Silica"
        ]
    },
    "Yellow Stained Glass": {
        "drops": [
            "Topaz"
        ]
    },
    "Yellow Wool": {
        "drops": [
            "Sulfuric Acid"
        ]
    }
}

ITEMS = {
    "Adamantium": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                [None, "Adamantium Scraps", None],
                ["Adamantium Scraps", "Netherite Ingot", "Adamantium Scraps"],
                [None, "Adamantium Scraps", None]
            ]
        },
        "sell": 40000,
        "museum": (3, 3, 1),
        "rarity": Rarity.Mythic,
        "lore": ["All its properties surpass those of diamond."],
        "item": {
            "id": "nether_brick",
            "cmd": 1473
        }
    },
    
    "Adamantium Scraps": {
        "sell": 8000,
        "museum": (3, 2, 9),
        "rarity": Rarity.Legendary,
        "lore": ["Can be combined into adamantium ingots."],
        "item": {
            "id": "melon_seeds",
            "cmd": 1475
        }
    },
    
    "Advanced Circuit": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Copper Wire"] * 3,
                ["Electric Circuit", "Plastic Sheet", "Electric Circuit"],
                [None, "Gold Ingot", None]
            ]
        },
        "rarity": Rarity.Legendary,
        "item": {
            "id": "filled_map",
            "color": "B40000",
            "cmd": 1612
        }
    },
    
    "Aeroboots": {
        "obtain": [
            "The overworld shop offers this for $25,000."
        ],
        "rarity": Rarity.Uncommon,
        "lore": [
            "These boots will make you",
            "fall more slowly while wearing."
        ],
        "item": {
            "id": "leather_boots",
            "color": "FAF0C8",
            "cmd": 1375
        }
    },
    
    "Aluminium Ore": {
        "forge": "Impure Aluminium",
        "sell": 300,
        "museum": (5, 4, 8),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "firework_star",
            "color": "F0F0F0",
            "cmd": 1630
        }
    },
    "Impure Aluminium": {
        "forge": "Aluminium Ingot",
        "museum": (5, 4, 9),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzI4NmE0NmIzODMzZmU4MDY5Nzg4OWZjNzBlNWY1NWM4NWYzODE1YjNlZmE4ZTY4MWQ0OTMwZjM3ZDNmN2U3In19fQ==",
            "cmd": 1631
        }
    },
    "Aluminium Ingot": {
        "sell": 8000,
        "museum": (6, 1, 1),
        "rarity": Rarity.Rare,
        "item": {
            "id": "iron_ingot",
            "cmd": 1632
        }
    },

    "Amethyst": {
        "forge": "Refined Amethyst",
        "obtain": [
            "Mining any block with the Pristine enchantment has a chance to drop Amethysts."
        ],
        "sell": 5000,
        "museum": (3, 4, 7),
        "rarity": Rarity.Epic,
        "lore": ["Magical violet quartz."],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTQ5M2M2ZjU0MGM3MDAxZmVkOTdiMDdmNmI0Yzg5MTI4ZTNhN2MzNzU2M2FhMjIzZjBhY2NhMzE0ZjE3NTUxNSJ9fX0=",
            "cmd": 1443
        }
    },
    "Refined Amethyst": {
        "forge": "Perfect Amethyst",
        "sell": 19000,
        "museum": (3, 4, 8),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzRmYzYyY2Y0Nzc3YWJmMzU2NWE3MDk4NTI3NzhlMjQ4YWFhZTkzNmZkNTE1N2MzMWRiMmEzYzI0NzBhNjY1YyJ9fX0=",
            "cmd": 1444
        }
    },
    "Perfect Amethyst": {
        "sell": 100000,
        "museum": (3, 4, 9),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDg4NmUwZjQxMTg1YjE4YTNhZmQ4OTQ4OGQyZWU0Y2FhMDczNTAwOTI0N2NjY2YwMzljZWQ2YWVkNzUyZmYxYSJ9fX0=",
            "cmd": 1445
        }
    },

    "Amogus": {
        "museum": (1, 1, 9),
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGM0ZDQ0YTBmZmUwMjM0OWU5OWRhMDYyOTIxMzA2MzExM2U2YmIzYWZjMjU5ZjQ2NjE4YzkwZWRjZTgzMDc4NiJ9fX0=",
            "cmd": 1522
        }
    },

    "Ancient Dentures": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Ancient Tooth"] * 3,
                ["Ancient Tooth", "Steel", "Ancient Tooth"],
                ["Ancient Tooth"] * 3
            ]
        },
        "accessory": {
            "use": "Gives +6% mining speed",
            "slots": 2
        },
        "rarity": Rarity.Rare,
        "lore": [
            "Chew your blocks slower!",
            "+6% Mining speed"
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmU1NjQyZGI4MTBlNjg5ZTBiNGE0NTU1YmYzMTA5M2U1YzQ3OWUzMWFlYTU5OTJhNGVmZWQzYWI0MTk3YTkyZSJ9fX0=",
            "cmd": 1801
        }
    },

    "Ancient Skull": {
        "sell": 8000,
        "museum": (1, 2, 2),
        "rarity": Rarity.Epic,
        "lore": ["A giant skull of an unknown creature"],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjdlODQ5MGMwZjk3ZTU5ZTJjNjA5MzI3MjVmMTAyMzVlOTdiNzQ0YmRhYjU5ODcwMmEwYjJlNzk5MGRlMzA0YyJ9fX0=",
            "cmd": 1432
        }
    },

    "Ancient Tooth": {
        "sell": 3000,
        "museum": (1, 2, 3),
        "rarity": Rarity.Rare,
        "lore": ["A huge tooth from an ancient creature."],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZjBjODQzMjBmNGIwZmNkODM5MWI4YTIwZjUzYmQ0MTYxMmNhNmE1MGU3NTgzMDk1MjU5NzFmNzdhY2UyZCJ9fX0=",
            "cmd": 1433
        }
    },

    "Antimatter Module": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Impure Lead", "Vacuum Tube", "Impure Lead"],
                ["Impure Palladium", "Antimatter", "Impure Palladium"],
                ["Impure Lead", "Advanced Circuit", "Impure Lead"]
            ]
        },
        "module": {
            "use": "No effect; increases module capacity by 2",
            "slots": -2
        },
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNGQ0MmJiMzM5MWIzOTY0ZGUyNjZkOWJlYmU3Y2NmN2VmM2MzOTA2MjZlYjdhODQ1NjEyYWQ5MGYzZmE0MmMxMiJ9fX0=",
            "cmd": 1604
        }
    },

    "Aquatic Crowbar": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Starite", "Water Core", "Starite"],
                ["Flint", "Empowered Crowbar", "Flint"],
                ["Starite", "Aluminium Ingot", "Starite"]
            ]
        },
        "rarity": Rarity.Uncommon,
        "mining speed": 10,
        "breaking power": 5,
        "item": {
            "id": "bone",
            "enchanted": True,
            "cmd": 1675
        }
    },

    "Aquatic Pebble": {
        "museum": (6, 4, 5),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "warped_button",
            "cmd": 1692
        }
    },

    "Arctic Amogus": {
        "museum": (7, 4, 5),
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDY0MDgwYTcyOWQyZWJhYzgwOGNkNGE4ZjkzNzFkMmZmZWY4MGM3MTIwODNhMzUyZGY4NjU3ZmM1OTU4MGUxMCJ9fX0=",
            "cmd": 1821
        }
    },
    
    "Arkenstone Fragment": {
        "forge": "Arkenstone",
        "museum": (4, 1, 1),
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTgyMjhjMjM0YzM5MDNjNTEyYTVhMGFhNDUyNjBlN2I1NjdlMGUyMGVlZmM3ZDU2MWNjZWM5N2IyOTU4NzFhZiJ9fX0=",
            "cmd": 1516
        }
    },
    "Arkenstone": {
        "museum": (4, 1, 2),
        "rarity": Rarity.Exotic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODZmMDZlYWEzMDA0YWVlZDA5YjNkNWI0NWQ5NzZkZTU4NGU2OTFjMGU5Y2FkZTEzMzYzNWRlOTNkMjNiOWVkYiJ9fX0=",
            "cmd": 1517
        }
    },

    "Astral Ore": {
        "lore": [
            "Dark, ominous ore that has entered the deepest",
            "layers of the earth during its formation through",
            "collision with incoming asteroids from outside the solar",
            "system. Can also be formed through corrupting starite."
        ],
        "sell": 10000,
        "museum": (7, 4, 7),
        "rarity": Rarity.Godly,
        "item": {
            "id": "black_dye",
            "enchanted": True,
            "cmd": 1755
        }
    },

    "Aureate Grapes": {
        "obtain": [
            "A random drop from chests."
        ],
        "sell": 10000,
        "museum": (7, 3, 6),
        "rarity": Rarity.Legendary,
        "lore": [
            "Legendary berries blessed with",
            "golden dew, can be consumed for",
            "a mining speed boost or crafted",
            "into valuable items."
        ],
        "item": {
            "id": "glow_berries",
            "cmd": 1744
        }
    },

    "Auto Seller": {
        "obtain": [
            "The nether shop offers this for $10,000."
        ],
        "use": [
            "Inserted items will be automatically sold when picked up."
        ],
        "rarity": Rarity.Epic,
        "lore": [
            "RIGHT CLICK to open. Put in items",
            "into the menu to automatically sell those",
            "items (with tax) when you pick them up."
        ],
        "item": {
            "id": "hopper_minecart",
            "cmd": 1435
        }
    },

    "Bacon": {
        "sell": 1000,
        "museum": (3, 2, 5),
        "rarity": Rarity.Legendary,
        "lore": ["A cube of salt-cured pork."],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTdiYTIyZDVkZjIxZTgyMWE2ZGU0YjhjOWQzNzNhM2FhMTg3ZDhhZTc0ZjI4OGE4MmQyYjYxZjI3MmU1In19fQ==",
            "cmd": 1471
        }
    },

    "Bacon Chestplate": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Bacon", None, "Bacon"],
                ["Bacon"] * 3,
                ["Bacon"] * 3
            ]
        },
        "use": [
            "Doubles your maximum health.",
            "Gives +5% mining speed.",
            "Gives +30% luck."
        ],
        "rarity": Rarity.Epic,
        "lore": ["Doubles your maximum health."],
        "item": {
            "id": "leather_chestplate",
            "color": "FF5A5A",
            "cmd": 1514
        }
    },

    "Bag of Gold": {
        "obtain": [
            "A random drop from presents."
        ],
        "sell": 2000,
        "museum": (3, 4, 2),
        "rarity": Rarity.Legendary,
        "lore": ["Sell this for coins."],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYTliOTA2YjIxNTVmMTkzNzg3MDQyMzM4ZDA1Zjg0MDM5MWMwNWE2ZDNlODE2MjM5MDFiMjk2YmVlM2ZmZGQyIn19fQ==",
            "cmd": 1501
        }
    },

    "Bag of Seeds": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Grass"] * 3,
                ["Fabric", "Grass", "Fabric"],
                ["Fabric"] * 3
            ]
        },
        "use": [
            "When right-clicked, spreads [Grass Block]s over [Dirt (Block)]."
        ],
        "rarity": Rarity.Rare,
        "lore": [
            "RIGHT CLICK to spread",
            "grass on nearby dirt blocks."
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzY3ZmU1ZTNlMmY3YmY5MmVhYTZmMjAyNzYxYzEwZWMzMmRhZjNhMmEyYWRlYzFkYmJhY2E4M2M1ZjcxNmRhNSJ9fX0=",
            "cmd": 1441
        }
    },

    "Bag of Seeds Deluxe": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Golden Grass"] * 3,
                ["Fabric", "Bag of Seeds", "Fabric"],
                ["Golden Grass"] * 3
            ]
        },
        "use": [
            "When right-clicked, spreads [Grass Block]s over [Dirt (Block)]."
        ],
        "rarity": Rarity.Rare,
        "lore": [
            "RIGHT CLICK to spread",
            "grass blocks faster than ever"
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzJkMDNjODc2YjllYTIwY2ExZWIzMGVhNjMxZDkwMTNiNWMzNDdkNDRlNjZjZTc3YmQ2OTUyNTkyMzVlMTg4YSJ9fX0=",
            "cmd": 1495
        }
    },

    "Banana": {
        "forge": "Potassium",
        "sell": 1000,
        "museum": (1, 4, 5),
        "rarity": Rarity.Rare,
        "lore": [
            "Stop everything!",
            "Get the banana!",
            "Potassium."
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjBhYWExNDI1ZDJiOTkzODM2OTdkNTcxOTNmMjdkODcyNDQyYmNiOTk1NTA4ZjQyZDE5ZGU0YWYxZjg2MTIifX19",
            "cmd": 1368
        }
    },
    "Potassium": {
        "forge": "Potassium Ingot",
        "sell": 100000,
        "museum": (4, 4, 1),
        "rarity": Rarity.Rare,
        "item": {
            "id": "sugar",
            "enchanted": True,
            "cmd": 1547
        }
    },
    "Potassium Ingot": {
        "museum": (4, 4, 2),
        "rarity": Rarity.Rare,
        "item": {
            "id": "iron_ingot",
            "enchanted": True,
            "cmd": 1548
        }
    },

    "Banana Leggings": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Banana", "Glue", "Banana"],
                ["Banana", None, "Banana"],
                ["Banana", None, "Banana"]
            ]
        },
        "use": [
            "Increases speed."
        ],
        "rarity": Rarity.Rare,
        "lore": [
            "Increases movement speed."
        ],
        "item": {
            "id": "golden_leggings",
            "cmd": 1430
        }
    },

    "Basalt": {
        "forge": "Magnesium",
        "sell": 250,
        "museum": (3, 1, 2),
        "rarity": Rarity.Rare,
        "lore": [
            "Fine-grained ingenious rock.",
            "Rich in magnesium and iron."
        ],
        "item": {
            "id": "gunpowder",
            "cmd": 1450
        }
    },
    "Magnesium": {
        "forge": "Magnesium Ingot",
        "sell": 1500,
        "museum": (2, 4, 5),
        "rarity": Rarity.Rare,
        "lore": [
            "Light, shiny gray metal.",
            "Burns brightly white."
        ],
        "item": {
            "id": "sugar",
            "cmd": 1453
        }
    },
    "Magnesium Ingot": {
        "museum": (2, 4, 6),
        "rarity": Rarity.Epic,
        "item": {
            "id": "iron_ingot",
            "cmd": 1454
        }
    },

    "Battery": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Iron Ingot", "Sulfuric Acid", "Copper Ingot"],
                [None] * 3,
                [None] * 3
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTYxZDNjNjU1ZmZlMjkxNTQ4OGNkNDE0YmMyMzc0NGZhZGQ2OTk4NmU3NTcxNTlkN2M5MTdjNjA0OGQ1ZmNjYyJ9fX0=",
            "cmd": 1623
        }
    },

    "Bedrock Piece": {
        "sell": 400000,
        "museum": (4, 3, 9),
        "rarity": Rarity.Divine,
        "lore": [
            "Thought to be unbreakable."
        ],
        "item": {
            "id": "blackstone_button",
            "cmd": 1546
        }
    },

    "Blackstone Chunk": {
        "sell": 40,
        "museum": (1, 3, 7),
        "rarity": Rarity.Uncommon,
        "lore": [
            "A hard, black stone found underground.",
            "Has gotten it's color from its high",
            "concentration of coal."
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMThmODJjNTRjOTdlNzFlZGFkZTY5MmQ0NzUzZGY1NjAxMzI5Nzk0ZWM1MGFmMWRmNWZmYmMxMDM0ZWM5YmIyNyJ9fX0=",
            "cmd": 1364
        }
    },

    "Blessed Gemstone Mixture": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                ["Lucky Gemstone Mixture", "Arkenstone", "Lucky Gemstone Mixture"],
                ["Aureate Grapes", "Omega Alloy", "Aureate Grapes"],
                ["Perfect Diamond", "Refined Onyx", "Perfect Ruby"]
            ]
        },
        "rarity": Rarity.Mythic,
        "lore": [
            "Can be applied to gear in an anvil to surpass",
            "the lucky gemstone mixture cap, up to 10."
        ],
        "use": [
            "Similar to [Lucky Gemstone Mixture]"
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZWRlMmNkZWRlNmE0YmQ2YzUxYmE5MDE0YTA5ZjRhYWM5Zjc2MWNiOGNjZDE5MmM4YzdhNjdhMzhkMTUzMmUzNiJ9fX0=",
            "cmd": 1870
        }
    },

    "Blood": {
        "sell": 500,
        "museum": (3, 1, 8),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZjBmNGNmYzg3MDU2MjQ3YThmZjJjODNiNjBmNTlmZGRlYzlmOGZkMjUzMTFlNmExYjcyNjE2YTBkYTk1NTZlOSJ9fX0=",
            "cmd": 1484
        }
    },

    "Bob Pickaxe": {
        "obtain": [
            "The Sputtrooms shop offers this for $200,000."
        ],
        "item": {
            "id": "golden_hoe",
            "cmd": 1552
        },
        "mining speed": 0.1,
        "breaking power": 9,
        "rarity": Rarity.Legendary
    },

    "Bob's Hot n' Spicy Outfit": {
        "obtain": [
            "The Sputtrooms shop offers this for $1,000,000."
        ],
        "item": {
            "id": "leather_chestplate",
            "color": "FF7800",
            "cmd": 1553
        },
        "use": [
            "Slightly increases speed."
        ],
        "rarity": Rarity.Legendary
    },
    
    "Bobbo Nuggies": {
        "forge": "Bob Macaroni",
        "obtain": [
            "The Sputtrooms shop offers this for $6,900."
        ],
        "museum": (4, 4, 3),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "potato",
            "enchanted": True,
            "cmd": 1549
        }
    },
    "Bob Macaroni": {
        "forge": "Bob's Big Bad Body Building Burrito",
        "museum": (4, 4, 4),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "rabbit_stew",
            "cmd": 1550
        }
    },
    "Bob's Big Bad Body Building Burrito": {
        "forge": "Bob's Big Banquet",
        "museum": (4, 4, 5),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "cooked_rabbit",
            "cmd": 1551
        }
    },
    "Bob's Big Banquet": {
        "forge": "Bob's Chef-D'oevre",
        "museum": (4, 4, 6),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "cooked_chicken",
            "cmd": 1554
        }
    },
    "Bob's Chef-D'oevre": {
        "museum": (4, 4, 7),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "pumpkin_pie",
            "enchanted": True,
            "cmd": 1555
        }
    },

    "Bomb": {
        "obtain": [
            "The overworld shop offers this for $38,000."
        ],
        "rarity": Rarity.Uncommon,
        "breaking power": 2,
        "lore": [
            "Throw it at the ground and it'll",
            "explode, breaking neaby blocks."
        ],
        "item": {
            "id": "fire_charge",
            "cmd": 1377
        }
    },

    "Bone": {
        "sell": 30,
        "museum": (1, 2, 1),
        "rarity": Rarity.Common,
        "lore": ["A bone from an unknown creature."],
        "item": {
            "id": "bone",
            "cmd": 1356
        }
    },

    "Boots of Growth": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                [None] * 3,
                ["Fabric", None, "Fabric"],
                ["Bag of Seeds", None, "Bag of Seeds"]
            ]
        },
        "use": [
            "Passively spreads [Grass Block]s over [Dirt (Block)] you walk on."
        ],
        "rarity": Rarity.Rare,
        "lore": [
            "Generates grass when you",
            "walk on dirt blocks."
        ],
        "item": {
            "id": "leather_boots",
            "color": "00B400",
            "cmd": 1535
        }
    },

    "Boots of Snow": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                [None] * 3,
                ["Fabric", None, "Fabric"],
                ["Magical Snowball", None, "Magical Snowball"]
            ]
        },
        "use": [
            "Passively spreads [Snow] over blocks you walk on."
        ],
        "rarity": Rarity.Common,
        "lore": [
            "Generates snow when you",
            "walk on blocks."
        ],
        "item": {
            "id": "leather_boots",
            "color": "FFFFFF",
            "cmd": 1536
        }
    },

    "Boron Nitride": {
        "forge": "Wurtzite Boron Nitride",
        "sell": 1500,
        "museum": (3, 1, 5),
        "rarity": Rarity.Epic,
        "lore": [
            "A highly refractory compound of",
            "boron and nitrogen. Very hard."
        ],
        "item": {
            "id": "flint",
            "cmd": 1451
        }
    },
    "Wurtzite Boron Nitride": {
        "sell": 10000,
        "museum": (3, 1, 6),
        "rarity": Rarity.Epic,
        "lore": [
            "Has a thermal and chemical stabilty",
            "superior than that of diamond."
        ],
        "item": {
            "id": "diamond",
            "cmd": 1452
        }
    },

    "Boron Nitride Pickaxe": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Netherite Pickaxe", "Super Glue", "Wurtzite Boron Nitride"],
                [None] * 3,
                [None] * 3
            ]
        },
        "rarity": Rarity.Epic,
        "mining speed": 6.5,
        "breaking power": 5,
        "lore": [
            "Reinforced with Wurtzite Boron Nitride."
        ],
        "item": {
            "id": "diamond_pickaxe",
            "cmd": 1460
        }
    },

    "Botanist Kit": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["String", "Roots", "String"],
                ["Diamond Grass", "Dirt", "Diamond Grass"],
                ["Fabric", "Wood", "Fabric"]
            ]
        },
        "accessory": {
            "use": "Boosts [Bag of Seeds]'s speed and size, plus allows [Flowering Azalea Leaves] to spawn when using it.",
            "slots": 4
        },
        "rarity": Rarity.Rare,
        "lore": [
            "Boosts the bag of seeds' speed and",
            "seed count, and adds a very small",
            "chance for a flower to grow on",
            "the grass it spreads."
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDU3Mjg4NTQ0ZmViYWQzM2Y0NWMwMjNjYTgxY2Y4YjU0MjM5ZTc2ZGMzNjZjMGJlZDU2MjUxMWU3YWQ5YTI0MCJ9fX0=",
            "cmd": 1741
        }
    },

    "Brimstone": {
        "forge": "Corundum",
        "sell": 120,
        "museum": (1, 4, 6),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjBkNjI2MTZkOTI5ZDNjZjIwOGQ1M2IxMzBjZGRiNjIwN2UzZGIwMDE3YjBhYzZlY2UyNWU2ZmE4NzlkMDZmMyJ9fX0=",
            "cmd": 1391
        }
    },
    "Corundum": {
        "forge": "Ruby",
        "sell": 650,
        "museum": (1, 4, 7),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvN2U4YWRhOWI3MTNmZGVlZDE0MmE4NmEwNjExYTM1OGRlYjRhNzdkZGM1NGQ0NWUyYjY4ZjI1NzdkZmFiYWI0In19fQ==",
            "cmd": 1394
        }
    },
    "Ruby": {
        "forge": "Refined Ruby",
        "obtain": [
            "The communist shop offers this for $6,000."
        ],
        "sell": 3500,
        "museum": (1, 4, 8),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDE1OWIwMzI0M2JlMThhMTRmM2VhZTc2M2M0NTY1Yzc4ZjFmMzM5YTg3NDJkMjZmZGU1NDFiZTU5YjdkZTA3In19fQ==",
            "cmd": 1395
        }
    },
    "Refined Ruby": {
        "forge": "Perfect Ruby",
        "sell": 19000,
        "museum": (1, 4, 9),
        "rarity": Rarity.Epic,
        "lore": ["A refined form of ruby with no noticable flaws."],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjFkYmUzMGIwMjdhY2JjZWI2MTI1NjNiZDg3N2NkN2ViYjcxOWVhNmVkMTM5OTAyN2RjZWU1OGJiOTA0OWQ0YSJ9fX0=",
            "cmd": 1396
        }
    },
    "Perfect Ruby": {
        "sell": 100000,
        "museum": (2, 1, 1),
        "rarity": Rarity.Legendary,
        "lore": ["Flawless."],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzliNmUwNDdkM2IyYmNhODVlOGNjNDllNTQ4MGY5Nzc0ZDhhMGVhZmU2ZGZhOTU1OTUzMDU5MDI4MzcxNTE0MiJ9fX0=",
            "cmd": 1397
        }
    },

    "Bronze Trophy": {
        "obtain": [
            "A rare drop from presents."
        ],
        "sell": 40000,
        "museum": (3, 3, 8),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZjk3ZTJjOGI4Mjc2Mjc2ZTM4ZGVjYTg4NTA4NzJkNTllY2M5YzFmMzhmMmFkY2U0MDg1OGVkYjllNjM0ZDdiYSJ9fX0=",
            "cmd": 1508
        }
    },

    "Bucket": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                [None] * 3,
                ["Iron Ingot", None, "Iron Ingot"],
                [None, "Iron Ingot", None]
            ]
        },
        "use": [
            "Used to make [Oil Bucket]s or [Milk Bucket]s."
        ],
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTE3ZDg2ZTNmODFjYzE4MzdjNzBmMTBiZTQ4ODk4MzRjMDRmNTdhN2U5OGUwZGQwYjRiMjIzYjUwYzdhOGY5MCJ9fX0=",
            "cmd": 1614
        }
    },

    "Budget Diamond Pickaxe": {
        "obtain": [
            "The overworld shop offers this for $9,500."
        ],
        "rarity": Rarity.Uncommon,
        "mining speed": 2,
        "breaking power": 3,
        "item": {
            "id": "diamond_hoe",
            "cmd": 1370
        }
    },

    "Cake Frosting": {
        "forge": "Sugar",
        "museum": (6, 3, 4),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzkyYjJiMDQxNGNlZTM2YjI0ZDgzZjVjZmEwNzFkODYzODUyNzI0OWMyZGNkZGZhNTgwYmUzN2UwN2M2MGUwOCJ9fX0=",
            "cmd": 1681
        }
    },
    "Sugar": {
        "museum": (6, 3, 5),
        "rarity": Rarity.Rare,
        "item": {
            "id": "sugar",
            "cmd": 1682
        }
    },

    "Calcium Potion": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipe": [
                ["Bone", "Water Bottle", None],
                [None] * 3,
                [None] * 3
            ]
        },
        "use": [
            "Gives immunity to fall damage."
        ],
        "rarity": Rarity.Common,
        "item": {
            "id": "potion",
            "color": "FFF0C8",
            "cmd": 1804
        }
    },

    "Caramel Candy": {
        "obtain": [
            "Mining blocks in the lower mesa mine after consuming [Grapes of Jonathan] has a chance of dropping this."
        ],
        "museum": (8, 3, 8),
        "rarity": Rarity.Epic,
        "lore": [
            "Right Click to consume.",
            "Gives +1 Autoforge level."
        ],
        "use": [
            "When consumed, gives +1 [Autoforge] level."
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzQzNmViZmU1MTQ2ZWY2YTIzMjVkYjZhNjJlNmI1NmVkM2E4OWE2MzBmYjIxOWQ3NDdjMTUyMzg4ZDdjYzgyOSJ9fX0=",
            "cmd": 1843
        }
    },

    "Celestial Boots": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                [None] * 3,
                [None, "Aeroboots", None],
                ["Celestial Ingot", None, "Celestial Ingot"]
            ]
        },
        "rarity": Rarity.Legendary,
        "item": {
            "id": "iron_boots",
            "enchanted": True,
            "cmd": 1389
        }
    },

    "Celestial Crowbar": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Starite", "Celestial Ingot", "Starite"],
                ["Celestial Ingot", "Empowered Crowbar", "Celestial Ingot"],
                ["Starite", "Celestial Ingot", "Starite"]
            ]
        },
        "rarity": Rarity.Legendary,
        "mining speed": 7,
        "breaking power": 4,
        "item": {
            "id": "bone",
            "enchanted": True,
            "cmd": 1419
        }
    },

    "Celestial Dew": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Honey", "Aureate Grapes", "Golden Grass"],
                ["Starite", None, None],
                [None] * 3
            ]
        },
        "obtain": [
            "The @waluigi shop offers this for 20 Waluigi Tokens."
        ],
        "museum": (7, 3, 7),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "honey",
            "enchanted": True,
            "cmd": 1747
        }
    },
    
    "Cheese": {
        "forge": "Luxury Cheese",
        "sell": 800,
        "museum": (3, 1, 9),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzZjMDFiZmZlY2ZkYWI2ZDNjMGYxYTdjNmRmNmFhMTkzNmYyYWE3YTUxYjU0YTRkMzIzZTFjYWNiYzUzOSJ9fX0=",
            "cmd": 1466
        }
    },
    "Luxury Cheese": {
        "forge": "Topaz",
        "sell": 2000,
        "museum": (3, 2, 1),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzRmZWJiYzE1ZDFkNGNjNjJiZWRjNWQ3YTJiNmYwZjQ2Y2Q1YjA2OTZhODg0ZGU3NWUyODllMzVjYmI1M2EwIn19fQ==",
            "cmd": 1467
        }
    },
    "Topaz": {
        "forge": "Refined Topaz",
        "sell": 9000,
        "museum": (3, 2, 2),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvM2ZkOTYwNzIyZWMyOWM2NjcxNmFlNWNhOTdiOWI2YjI2Mjg5ODRlMWQ2ZjlkMjU5MmNkMDg5OTE0MjA2YTFiIn19fQ==",
            "cmd": 1468
        }
    },
    "Refined Topaz": {
        "forge": "Perfect Topaz",
        "museum": (3, 2, 3),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDQ5YTZkMzMwNDY1YmM5NGQ1NzM3MTY0MjhkYzY2MmNjMTZhY2QzYjgwNTM1YjUyMDI4YzY2NWY0ZGFmNjgyZSJ9fX0=",
            "cmd": 1469
        }
    },
    "Perfect Topaz": {
        "sell": 200000,
        "museum": (3, 2, 4),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvM2RhNmVjZGNiYzNmZTM1NWNhMDYxMTE5MmEzZmJkMzVkZDU2MzVkNWZjZGYzZmJjNzllZDJiYzFmNGEwMTdmZSJ9fX0=",
            "cmd": 1470
        }
    },

    "Cherry": {
        "sell": 5000,
        "museum": (6, 3, 6),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYWU1M2EzYWVlYzk2NjJiZTUxM2M5NDA0OWE5ZWUwYWFkZTM1MTcwMTVhOTc2MzhkOWY4NmIyMWU4YjMxODJlYSJ9fX0=",
            "cmd": 1683
        }
    },

    "Child Smacker": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                ["Waluigi Ball", "Sage Crystal", "Waluigi Ball"],
                ["Waluigi Ball", "Perfect Diamond", "Waluigi Ball"],
                [None, "Gold Rod", None]
            ]
        },
        "use": [
            "Upon hitting a player, it removes their chat formatting and turns them invisible, thus fake-banning them."
        ],
        "rarity": Rarity.Divine,
        "item": {
            "id": "diamond_axe",
            "cmd": 1793
        }
    },

    "Chocolate Chips": {
        "forge": "Chocolate",
        "museum": (6, 3, 7),
        "rarity": Rarity.Rare,
        "item": {
            "id": "cocoa_beans",
            "cmd": 1684
        }
    },
    "Chocolate": {
        "forge": "Chocolate Bar",
        "museum": (6, 3, 8),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzJjMWMwMjA5YjEwZTFiOTk3YjQ2MTI4N2Y5ZDQyNmUzMTZhNGE2NjcyMjc4ZDRlNDYzYjE5OTI1ZmZmMjYifX19",
            "cmd": 1685
        }
    },
    "Chocolate Bar": {
        "forge": "Luxury Chocolate",
        "museum": (6, 3, 9),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODE5Zjk0OGQxNzcxOGFkYWNlNWRkNmUwNTBjNTg2MjI5NjUzZmVmNjQ1ZDcxMTNhYjk0ZDE3YjYzOWNjNDY2In19fQ==",
            "cmd": 1686
        }
    },
    "Luxury Chocolate": {
        "museum": (6, 4, 1),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmFjZmM3ODY0NjllNjM2YmY0ZWFhYzJlZDQ5ZDlhNmM1MjEyYWY2ZDkwNzFkOTYxOTQ0YmU4YTkzNWY0NzhlIn19fQ==",
            "cmd": 1687
        }
    },

    "Chromatic Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Refined Ruby", "Gold Block", "Refined Amethyst"],
                ["Refined Topaz", "Skin Core", "Synthetic Diamond"],
                ["Gold Ingot", "Refined Onyx", "Gold Ingot"]
            ]
        },
        "museum": (8, 4, 5),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmVmMWE1YWZhM2E1MTQxMzg4MGFlN2IyYWM5OWExMjg3NzU3M2RjNDA0NjQ2OTQyYmVmMmQ5MzJhMzg0NTk3NCJ9fX0=",
            "cmd": 1849
        }
    },

    "Clay": {
        "forge": "Brick",
        "sell": 100,
        "museum": (5, 2, 2),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "clay_ball",
            "cmd": 1567
        }
    },
    "Brick": {
        "sell": 1000,
        "museum": (5, 2, 3),
        "rarity": Rarity.Rare,
        "item": {
            "id": "brick",
            "cmd": 1568
        }
    },

    "Clover": {
        "forge": "Clover Bag",
        "obtain": [
            "The @waluigi shop offers this for 5 Waluigi Tokens."
        ],
        "sell": 10,
        "museum": (1, 1, 4),
        "rarity": Rarity.Rare,
        "item": {
            "id": "fern",
            "cmd": 1463
        }
    },
    "Clover Bag": {
        "forge": "Golden Clover Bag",
        "museum": (3, 2, 7),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzY3ZmU1ZTNlMmY3YmY5MmVhYTZmMjAyNzYxYzEwZWMzMmRhZjNhMmEyYWRlYzFkYmJhY2E4M2M1ZjcxNmRhNSJ9fX0=",
            "cmd": 1464
        }
    },
    "Golden Clover Bag": {
        "forge": "Diamond Clover Bag",
        "museum": (3, 2, 8),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDgxODgzNDVkYzZhMWJmMDg2NjMzODViOTlmMmJkMTU1MWE0OTI5MmE5M2I4NGUwYTk3YjkxN2I1NjViZjQxYSJ9fX0=",
            "cmd": 1465
        }
    },
    "Diamond Clover Bag": {
        "forge": "Arken Clover Bag",
        "museum": (7, 1, 9),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzYwYTA4ZGE4ZDNlNzNjNWFkZGNjMTAzODk1NjU2YWM0MDRmZjQyZjJkNWI1Yjc0NmNjZGU2MDdjZTkwNDQzYyJ9fX0=",
            "cmd": 1708
        }
    },
    "Arken Clover Bag": {
        "museum": (7, 2, 1),
        "rarity": Rarity.Exotic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjE3NmE0YzQ0NmI1NGQ1MGFlM2U1YmE4ZmU2ZjQxMzE3Njg5ZmY1YTc1MjMwMjgwOTdmNjExOTUzZDFkMTI5NyJ9fX0=",
            "cmd": 1709
        }
    },

    "Clover Talisman": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["String", None, "String"],
                ["Clover", "Gold Ingot", "Clover"],
                [None, "Clover", None]
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "ewogICJ0aW1lc3RhbXAiIDogMTY1MzY3NjIyNjU5MiwKICAicHJvZmlsZUlkIiA6ICI0M2NmNWJkNjUyMDM0YzU5ODVjMDIwYWI3NDE0OGQxYiIsCiAgInByb2ZpbGVOYW1lIiA6ICJrYW1pbDQ0NSIsCiAgInNpZ25hdHVyZVJlcXVpcmVkIiA6IHRydWUsCiAgInRleHR1cmVzIiA6IHsKICAgICJTS0lOIiA6IHsKICAgICAgInVybCIgOiAiaHR0cDovL3RleHR1cmVzLm1pbmVjcmFmdC5uZXQvdGV4dHVyZS8xNDBlYjQyNDdiNTk5MzkxMjQzN2NjZGZlNTM2YjU5NjU4ZmYzNGM4YWEwOGU0MWY0Y2JkMWZkNzgxYWY1ZmM3IgogICAgfQogIH0KfQ==",
            "cmd": 1734
        }
    },

    "Coal Piece": {
        "forge": "Coal",
        "sell": 45,
        "museum": (1, 3, 8),
        "rarity": Rarity.Common,
        "item": {
            "id": "blackstone_button",
            "cmd": 1353
        }
    },
    "Coal": {
        "forge": "Anthracite",
        "sell": 75,
        "museum": (1, 3, 9),
        "rarity": Rarity.Common,
        "obtain": [
            "The Jonathan shop (next to the beehive in the mesa) offers this for $400."
        ],
        "item": {
            "id": "coal",
            "cmd": 1354
        }
    },
    "Anthracite": {
        "forge": "Graphite",
        "sell": 550,
        "museum": (1, 4, 1),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "charcoal",
            "cmd": 1386
        }
    },
    "Graphite": {
        "forge": "Graphene",
        "sell": 4000,
        "museum": (1, 4, 2),
        "rarity": Rarity.Rare,
        "lore": ["Crystalline form of carbon."],
        "item": {
            "id": "flint",
            "cmd": 1387
        }
    },
    "Graphene": {
        "sell": 22000,
        "museum": (1, 4, 3),
        "rarity": Rarity.Epic,
        "item": {
            "id": "flint",
            "cmd": 1416
        }
    },
    
    "Cobalt Ore": {
        "forge": "Cobalt",
        "sell": 5000,
        "museum": (6, 1, 2),
        "rarity": Rarity.Epic,
        "item": {
            "id": "firework_star",
            "color": "6689D3",
            "cmd": 1659
        }
    },
    "Cobalt": {
        "sell": 30000,
        "museum": (6, 1, 3),
        "rarity": Rarity.Epic,
        "item": {
            "id": "cyan_dye",
            "cmd": 1660
        }
    },

    "Communist Blood Vow": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                ["Communite", "Blood", "Communite"],
                [None, "Fabric", None],
                ["Stalinium"] * 3
            ]
        },
        "accessory": {
            "use": "Increases the rate of transfer of the [Communist Cap].",
            "slots": 4
        },
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZjA4MGQwZjg5NzRkMjVkNjFjMjMxM2ExODJlNmE5YjFkMDQ4YzNmYTYxY2M5ODNlYTQ3N2E0ZmM4OTE5ZTZkZiJ9fX0=",
            "cmd": 1792
        }
    },

    "Communist Cap": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Communite", "Stalinium", "Communite"],
                ["Communite", "Miner's Helmet", "Communite"],
                [None] * 3
            ]
        },
        "use": [
            "Drains money from nearby players who have more than you, but gives money to nearby players who have less than you."
        ],
        "rarity": Rarity.Godly,
        "item": {
            "id": "leather_helmet",
            "color": "C80000",
            "cmd": 1581
        }
    },
    "Communist Coat": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Fabric", None, "Fabric"],
                ["Fabric", "Stalinium", "Fabric"],
                ["Communite", "Fabric", "Communite"]
            ]
        },
        "use": [
            "Increases the rate of transfer of the [Communist Cap].",
            "Gives +4.5% mining speed."
        ],
        "rarity": Rarity.Godly,
        "item": {
            "id": "leather_chestplate",
            "color": "4B6633",
            "cmd": 1583
        }
    },
    "Communist Pants": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Fabric", "Stalinium", "Fabric"],
                ["Communite", None, "Communite"],
                ["Fabric", None, "Fabric"]
            ]
        },
        "use": [
            "Increases the rate of transfer of the [Communist Cap].",
            "Gives +4.5% mining speed."
        ],
        "rarity": Rarity.Godly,
        "item": {
            "id": "leather_leggings",
            "color": "4B6633",
            "cmd": 1584
        }
    },
    "Boots of Labour": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Communite", None, "Communite"],
                [None, "Sturdy Boots", None],
                ["Communite", None, "Communite"]
            ]
        },
        "use": [
            "Gives +10% chance for double drops if you have less than $50,000.",
            "Increases the rate of transfer of the [Communist Cap].",
            "Gives +2% mining speed."
        ],
        "rarity": Rarity.Common,
        "item": {
            "id": "leather_boots",
            "color": "994200",
            "cmd": 1580
        }
    },
    "Italist Cap": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Bag of Gold"] * 3,
                ["Bag of Gold", "Miner's Helmet", "Bag of Gold"],
                ["Bag of Gold"] * 3
            ]
        },
        "use": [
            "Prevents other players' [Communist Cap]s from affecting you.",
            "Gives +4.5% mining speed."
        ],
        "rarity": Rarity.Rare,
        "item": {
            "id": "leather_helmet",
            "color": "00FF00",
            "cmd": 1582
        }
    },

    "Communist Flakes": {
        "obtain": [
            "The communist shop offers this for $200."
        ],
        "museum": (5, 2, 7),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYTFiYjlhMTk0NmFiZDhhYzI5YzNiOTVlZTg0NWYzNmQzNDhiZjc5NDUxNGFhZWFjNDdmOWIxNzgyZWRhIn19fQ==",
            "cmd": 1575
        }
    },

    "Communite": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Communist Flakes"] * 3,
                ["Communist Flakes", "Pebble", "Communist Flakes"],
                ["Communist Flakes"] * 3
            ]
        },
        "sell": 1500,
        "museum": (5, 2, 8),
        "rarity": Rarity.Godly,
        "item": {
            "id": "redstone",
            "cmd": 1576
        }
    },

    "Computerized Mining Support": {
        "craft": {
            "tier": CraftTier.Tech2,
            "recipe": [
                ["Battery", "Refined Copper", "Sulfuric Acid"],
                ["Engine", "Magnet", "Boron Nitride Pickaxe"],
                ["Battery", "Processing Unit", "Glass"]
            ]
        },
        "module": {
            "use": "Increases mining speed by +40% while sneaking. Consumes charge from the suit.",
            "slots": 2
        },
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNWE3YjNiMTZlNWQwYzRjZmQyMWM0ZWI5MTMzZTk2OWFhZDdjYzczMDNjY2RmMzE3NTEyZTI2YTQ4NzliNTEifX19",
            "cmd": 1649
        }
    },

    "Cookie": {
        "obtain": [
            "The @waluigi shop offers this for 2 Waluigi Tokens."
        ],
        "rarity": Rarity.Rare,
        "lore": ["Miner's treat."],
        "item": {
            "id": "cookie",
            "cmd": 1642
        }
    },

    "Cooling Module": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Ice", "Compressed Ice", "Ice"],
                ["Netherite Ingot", "Electric Circuit", "Netherite Ingot"],
                ["Fabric", "Compressed Ice", "Fabric"]
            ]
        },
        "module": {
            "use": "Gives immunity to damage from magma blocks.",
            "slots": 3
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDVjOGVkNDE3YmNkYjJiNjY1Y2NiZGJlMjlhY2JlNmEwNmY2Y2I3OWQ2Y2VmYzkwNzU0NjQ0ZGRkN2YxYzJhMyJ9fX0=",
            "cmd": 1646
        }
    },

    "Copper Coil": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                [None, "Copper Wire", None],
                ["Gold Ingot", "Copper Wire", "Gold Ingot"],
                [None, "Copper Wire", None]
            ]
        },
        "sell": 26000,
        "museum": (5, 3, 6),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGY1MTM2MWE4MGM3MmQ2ODUwN2E0YzVkY2I3ZDY3MWNmMGZmZGMzNTc3YmNlOWU3OWVmOWFmOTMxNTM2YmE1MyJ9fX0=",
            "cmd": 1610
        }
    },

    "Copper Drill": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Impure Copper"] * 3,
                [None, "Battery", None],
                [None, "Ender Dust", None]
            ]
        },
        "rarity": Rarity.Uncommon,
        "mining speed": 15,
        "breaking power": 5,
        "item": {
            "id": "leather_horse_armor",
            "color": "CC7400",
            "cmd": 1643
        }
    },

    "Copper Wire": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                [None] * 3,
                [None, "Copper Ingot", None],
                [None] * 3
            ]
        },
        "sell": 8500,
        "museum": (5, 3, 5),
        "rarity": Rarity.Rare,
        "item": {
            "id": "string",
            "cmd": 1609
        }
    },

    "Copper Scraps": {
        "forge": "Impure Copper",
        "sell": 250,
        "museum": (5, 3, 1),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "beetroot_seeds",
            "cmd": 1605
        }
    },
    "Impure Copper": {
        "forge": "Copper Ingot",
        "sell": 1500,
        "museum": (5, 3, 2),
        "rarity": Rarity.Uncommon,
        "obtain": [
            "The Jonathan shop (next to the beehive in the mesa) offers this for $19,000."
        ],
        "item": {
            "id": "raw_copper",
            "cmd": 1606
        }
    },
    "Copper Ingot": {
        "forge": "Refined Copper",
        "sell": 8000,
        "museum": (5, 3, 3),
        "rarity": Rarity.Rare,
        "item": {
            "id": "copper_ingot",
            "cmd": 1607
        }
    },
    "Refined Copper": {
        "sell": 30000,
        "museum": (5, 3, 4),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDBhNmU2YWE3Y2U5OWM4MWRhZjgxNmQ2OTYzOGQ1MmIyODgyYTI1NTg4ODAyMjJlOWE0NjZkY2VkYzg4MDE1YSJ9fX0=",
            "cmd": 1608
        }
    },

    "Cream": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Milk Bucket"] * 3,
                ["Milk Bucket", None, "Milk Bucket"],
                ["Milk Bucket"] * 3
            ]
        },
        "sell": 15000,
        "museum": (6, 4, 3),
        "rarity": Rarity.Common,
        "item": {
            "id": "white_dye",
            "cmd": 1689
        }
    },

    "Crewmate Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Communite", "Skin Core", "Communite"],
                ["Ruby", "Amogus", "Ruby"],
                ["Magma Gem", "Stalinium", "Magma Gem"]
            ]
        },
        "museum": (8, 4, 8),
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZjg5YmNlNzM2YTRmZDc5M2VlMmEzODI3NTZhMjUzZjkyY2E3ZDdlYWMwMzFlNDViYTk3YWQwNmNlODYzZGQ0YiJ9fX0=",
            "cmd": 1852
        }
    },

    "Crimson Sod": {
        "forge": "Ruby Grass",
        "sell": 1500,
        "museum": (7, 3, 8),
        "rarity": Rarity.Epic,
        "lore": [
            "Scarlet vegetation that doesn't grow",
            "naturally unless stimulated."
        ],
        "item": {
            "id": "fire_coral_fan",
            "enchanted": True,
            "cmd": 1749
        }
    },
    "Ruby Grass": {
        "forge": "Crimsonbrand Grass",
        "sell": 10000,
        "museum": (7, 3, 9),
        "rarity": Rarity.Epic,
        "lore": ["Scarlet-red strands of shining ruby."],
        "item": {
            "id": "fire_coral_fan",
            "enchanted": True,
            "cmd": 1750
        }
    },
    "Crimsonbrand Grass": {
        "museum": (7, 4, 1),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "fire_coral",
            "enchanted": True,
            "cmd": 1751
        }
    },

    "Crowbar": {
        "forge": "Empowered Crowbar",
        "obtain": [
            "The overworld shop offers this for $3,500."
        ],
        "rarity": Rarity.Common,
        "item": {
            "id": "bone",
            "cmd": 1363
        }
    },
    "Empowered Crowbar": {
        "rarity": Rarity.Uncommon,
        "mining speed": 3.5,
        "breaking power": 3,
        "item": {
            "id": "bone",
            "enchanted": True,
            "cmd": 1369
        }
    },

    "Cryonic Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Synthetic Diamond", "Plastic Sheet", "Synthetic Diamond"],
                ["Compressed Ice", "Skin Core", "Compressed Ice"],
                ["Synthetic Diamond", "Perfect Aquamarine", "Synthetic Diamond"]
            ]
        },
        "museum": (8, 4, 7),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTdhNDg3NDM1MmY4NzVjNzVlOTM2ZWI2ZGMyYTJlZjc3ZjU0ODlmODQyZWE3ZjAwYTRhNWM2YzI3Mzg3YWE3OSJ9fX0=",
            "cmd": 1851
        }
    },

    "Dark Crewmate Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Hypercompact Rockite", "Perfect Onyx", "Hypercompact Rockite"],
                ["Lead Plate", "Skin Core", "Lead Plate"],
                ["Hypercompact Rockite", "Astral Ore", "Hypercompact Rockite"]
            ]
        },
        "museum": (9, 1, 3),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMmZjYWQ3Mjc2NmYzODQ0NzhjZmU2MzlmMDIyMjZmYmU4MzYwMDNiMGRlOWFhNjUwZmJiNDljNzA1NDI5YjJhYyJ9fX0=",
            "cmd": 1856
        }
    },

    "Deluxe Bag Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Fabric", "Refined Amethyst", "Fabric"],
                ["Lead Ingot", "Skin Core", "Lead Ingot"],
                ["Fabric", "Onyx", "Fabric"]
            ]
        },
        "museum": (9, 1, 1),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzk0Yjc1OGNhNzU2NWFhYWVhMjcyZjkyNjExZjY0ODlmYzk3OGVhMTBlYzNhZTRkNmJlMjk4NWMxZjdjYTE3OCJ9fX0=",
            "cmd": 1854
        }
    },

    "Depth Talisman": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["String", "Grass", "String"],
                ["Hypercompact Stone", "Silica", "Graphite"],
                ["Gold Ingot", "Large Obsidian", "Wurtzite Boron Nitride"]
            ]
        },
        "accessory": {
            "use": "Increases mining speed by +0.1% x your depth in meters.",
            "slots": 5
        },
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "ewogICJ0aW1lc3RhbXAiIDogMTY1MzY3NjIzOTAyNiwKICAicHJvZmlsZUlkIiA6ICIzZmM3ZmRmOTM5NjM0YzQxOTExOTliYTNmN2NjM2ZlZCIsCiAgInByb2ZpbGVOYW1lIiA6ICJZZWxlaGEiLAogICJzaWduYXR1cmVSZXF1aXJlZCIgOiB0cnVlLAogICJ0ZXh0dXJlcyIgOiB7CiAgICAiU0tJTiIgOiB7CiAgICAgICJ1cmwiIDogImh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzQyMzY4YmUxZmFmZjc3N2E4NTIyODYzOTRhMTRjNDM2NjhlMzg1Y2M5YWQ4NGI1N2MyMDdlOTBkZTYxODU0ZiIKICAgIH0KICB9Cn0=",
            "cmd": 1736
        }
    },

    "Dew Dripper": {
        "craft": {
            "tier": CraftTier.Crafting3,
            "recipe": [
                ["Celestial Dew", "Honeycomb", "Celestial Dew"],
                ["Gold Ingot", "Refined Topaz", "Gold Ingot"],
                ["Celestial Dew", "Honeycomb", "Celestial Dew"]
            ]
        },
        "accessory": {
            "use": "Can apply [Celestial Dew] to blocks that you walk on.",
            "slots": 5
        },
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMmM2ODAxNDlhZDE3ZTQ2ZmJiZjc2MDZiMjg0Y2M4M2EwM2IxYTY3Y2Q4YTUyNzE3YjQ0YmZhM2FkNTkxNGYxNCJ9fX0=",
            "cmd": 1761
        }
    },

    "Diamond Grass": {
        "forge": "The Arkengrass",
        "sell": 20000,
        "museum": (1, 1, 6),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "tube_coral_fan",
            "cmd": 1420
        }
    },
    "The Arkengrass": {
        "museum": (1, 1, 7),
        "rarity": Rarity.Mythic,
        "lore": [
            "Its strands have a thousand facets, it shone",
            "like silver in the firelight, like water in the",
            "sun, like snow under the stars, like rain",
            "upon the Moon"
        ],
        "item": {
            "id": "dead_horn_coral_fan",
            "enchanted": True,
            "cmd": 1462
        }
    },

    "Diamond Pickaxe": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Budget Diamond Pickaxe", "Glue", "Budget Diamond Pickaxe"],
                [None] * 3,
                [None] * 3
            ]
        },
        "obtain": [
            "The overworld shop offers this for $21,500."
        ],
        "rarity": Rarity.Uncommon,
        "mining speed": 2.7,
        "breaking power": 4,
        "item": {
            "id": "diamond_pickaxe",
            "cmd": 1371
        }
    },

    "Dinosaur Omelette": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                [None, "Luxury Cheese", None],
                ["Bacon", "Ominous Egg", "Bacon"],
                [None, "Banana", None]
            ]
        },
        "use": [
            "Spawns [Smooth Sandstone] when used."
        ],
        "museum": (4, 2, 6),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmY4YmI3NDgzYzFlMzEyNjVjZmI5MTE3OGQ0Mzk5ODY5ZWEyMDllZDgwNjBmMTI2OTlhMTZlZTE4MWI0MmZiMCJ9fX0=",
            "cmd": 1485
        }
    },

    "Dirt": {
        "forge": "Earth Crystal",
        "sell": 3,
        "museum": (1, 1, 2),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "dirt",
            "cmd": 1337
        }
    },
    "Earth Crystal": {
        "forge": "Amber",
        "sell": 35,
        "museum": (1, 2, 5),
        "rarity": Rarity.Common,
        "item": {
            "id": "orange_dye",
            "cmd": 1342
        }
    },
    "Amber": {
        "forge": "Amber Crystal",
        "sell": 450,
        "museum": (1, 2, 6),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZWY3ODM1ZmM5ZTZkYWY2MzIxNjBlOWI3ZmYzNzg3ODhhNDA4MDY0Y2M3NWViZjlmNTE1OGU2MTViZGQ1OTYwMyJ9fX0=",
            "cmd": 1379
        }
    },
    "Amber Crystal": {
        "forge": "Refined Amber",
        "sell": 3000,
        "museum": (1, 2, 7),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZGExOTQzNmY2MTUxYTdiNjZkNjVlZDc2MjRhZGQ0MzI1Y2ZiYmMyZWVlODE1ZmNmNzZmNGMyOWRkZjA4Zjc1YiJ9fX0=",
            "cmd": 1380
        }
    },
    "Refined Amber": {
        "forge": "Perfect Amber",
        "sell": 18000,
        "museum": (1, 2, 8),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzU5NGNhNWRjNWM4NWRiM2I0YTkwZDQ4NTkzMmJlZGU1ZmJkZjQwMjNmYzRmYmZmNmZlMTRiZTQwOWMxZjk3In19fQ==",
            "cmd": 1381
        }
    },
    "Perfect Amber": {
        "sell": 100000,
        "museum": (1, 2, 9),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzdhZTIzNmNkZWMzZjJhNmY1MWVhZTE1ZTJjOGY2MjI4YjM0ZjEzN2RhMTU2OWZlYzllODAzZjljZDgxNzU5ZCJ9fX0=",
            "cmd": 1382
        }
    },

    "Dirt Shovel": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Earth Crystal", "Dirt", "Earth Crystal"],
                ["Dirt", "Golden Excavator", "Dirt"],
                ["Earth Crystal", "Dirt", "Earth Crystal"]
            ]
        },
        "rarity": Rarity.Rare,
        "mining speed": 5,
        "item": {
            "id": "wooden_shovel",
            "cmd": 1798
        }
    },

    "Dirted Clover Talisman": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Dirt", "Amber", "Dirt"],
                ["Amber", "Clover Talisman", "Amber"],
                ["Dirt", "Amber", "Dirt"]
            ]
        },
        "accessory": {
            "use": "Increases luck by +18% when mining grass or dirt",
            "slots": 2
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "ewogICJ0aW1lc3RhbXAiIDogMTY1MzY3NjIxMTE0NiwKICAicHJvZmlsZUlkIiA6ICIxZjEyNTNhYTVkYTQ0ZjU5YWU1YWI1NmFhZjRlNTYxNyIsCiAgInByb2ZpbGVOYW1lIiA6ICJtbl9raSIsCiAgInNpZ25hdHVyZVJlcXVpcmVkIiA6IHRydWUsCiAgInRleHR1cmVzIiA6IHsKICAgICJTS0lOIiA6IHsKICAgICAgInVybCIgOiAiaHR0cDovL3RleHR1cmVzLm1pbmVjcmFmdC5uZXQvdGV4dHVyZS85ZDc3ODk3MzA3ZDNkZjA3MmE2ZDkwMWNhMmZkZmRlMWIyYWI4YjMzNDdiMTlmN2Q3NmRiNTA0NjM0NWE3ODk4IgogICAgfQogIH0KfQ==",
            "cmd": 1735
        }
    },

    "Diving Helmet": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Impure Lead", "Plastic Sheet", "Impure Lead"],
                ["Gold Ingot", "Makeshift Diving Helmet", "Glass"],
                ["Oxygen Bottle", "Orichalcum Lump", "Oxygen Bottle"]
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMWRmMjg3NDRlZTE0Nzg1MWI5ZWMyZDQ5MWE2NWE0N2VkZTFhNTIxMDAwYjUzNTEwNmRjM2IxZmJmNjQ3MTQ4MSJ9fX0=",
            "cmd": 1725
        }
    },
    "Diving Suit": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Fabric", None, "Fabric"],
                ["Oxygen Bottle", "Orichalcum Shards", "Oxygen Bottle"],
                ["Impure Aluminium"] * 3
            ]
        },
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "leather_chestplate",
            "color": "28328C",
            "cmd": 1719
        }
    },
    "Diving Leggings": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Fabric", "Orichalcum Shards", "Fabric"],
                ["Oxygen Bottle", None, "Oxygen Bottle"],
                ["Impure Aluminium", None, "Impure Aluminium"]
            ]
        },
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "leather_leggings",
            "color": "28328C",
            "cmd": 1720
        }
    },
    "Diving Boots": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                [None] * 3,
                ["Orichalcum Shards", None, "Orichalcum Shards"],
                ["Impure Aluminium", None, "Impure Aluminium"]
            ]
        },
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "leather_boots",
            "color": "1E1E3C",
            "cmd": 1721
        }
    },

    "Donatium Pile": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                ["Gold Ingot"] * 3,
                ["Gold Ingot", "Gold Block", "Gold Ingot"],
                ["Gold Ingot"] * 3
            ]
        },
        "accessory": {
            "use": "Removes the cooldown on @pay for payments above 500.",
            "slots": 1
        },
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTc2YmM2ODU0N2M3NmJhNDYyNTA4NTAyOTgwNDY0N2I4MmY4MTY3MDVjOGJiNjFlMzdkMTQ4NWE3NWM3MmM1ZiJ9fX0=",
            "cmd": 1816
        }
    },

    "Dough": {
        "forge": "Bread Roll",
        "sell": 5000,
        "museum": (6, 2, 8),
        "rarity": Rarity.Rare,
        "item": {
            "id": "potato",
            "cmd": 1676
        }
    },
    "Bread Roll": {
        "forge": "Bread",
        "sell": 5000,
        "museum": (6, 2, 9),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZWYwOTQ0NTZmZDc5NGI2NTMxZmM2ZGVjNmYzOTZiNjgwYjk1MzYwMDIwNjNlMTFjZTI0ZDBhNzRiMGI3ZDg4NSJ9fX0=",
            "cmd": 1677
        }
    },
    "Bread": {
        "forge": "Baguette",
        "museum": (6, 3, 1),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTE5OTdkYTY0MDQzYjI4NDgyMjExNTY0M2E2NTRmZGM0ZThhNzIyNjY2NGI0OGE0ZTFkYmI1NTdiNWMwZmUxNCJ9fX0=",
            "cmd": 1678
        }
    },
    "Baguette": {
        "forge": "Extra Long Baguette",
        "museum": (6, 3, 2),
        "rarity": Rarity.Epic,
        "item": {
            "id": "bread",
            "cmd": 1679
        }
    },
    "Extra Long Baguette": {
        "museum": (6, 3, 3),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "bread",
            "enchanted": True,
            "cmd": 1680
        }
    },

    "Efficiency Module": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Electric Circuit", "Adamantium Scraps", "Electric Circuit"],
                ["Gold Ingot", "Golden Pickaxe", "Gold Ingot"],
                ["Electric Circuit", "Graphene", "Electric Circuit"]
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "yellow_dye",
            "cmd": 1592
        }
    },
    "Efficiency Module MK2": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Ferrosilicon", "Impure Aluminium", "Ferrosilicon"],
                ["Efficiency Module", "Advanced Circuit", "Efficiency Module"],
                ["Lead Ingot", "Palladium Ingot", "Lead Ingot"]
            ]
        },
        "module": {
            "use": "Gives +10% mining speed",
            "slots": 5
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "honeycomb",
            "cmd": 1593
        }
    },

    "Egg": {
        "museum": (4, 2, 7),
        "rarity": Rarity.Common,
        "item": {
            "id": "egg",
            "cmd": 1486
        }
    },

    "Electric Circuit": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                [None] * 3,
                [None, "Copper Wire", None],
                [None, "Iron Ingot", None]
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "filled_map",
            "color": "007800",
            "cmd": 1611
        }
    },

    "Elevator Pass": {
        "obtain": [
            "The communist shop offers this for $5,000."
        ],
        "use": [
            "Can be used next to the communist shop to travel to the nether. The item is consumed in the process."
        ],
        "rarity": Rarity.Common,
        "item": {
            "id": "paper",
            "enchanted": True,
            "cmd": 1578
        }
    },

    "Elusive Fossil": {
        "sell": 100000,
        "museum": (7, 4, 4),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODdhMGU1NmJiYjcyNDFmNjJiMDU5MjVhZGE3MjViOWIzYjIxZmU0NjhhZDE4NGI2YTAyYmU4OTU4ODllODQ3OCJ9fX0=",
            "cmd": 1754
        }
    },

    "Empty Bottle": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                [None] * 3,
                [None, "Glass", None],
                [None] * 3
            ]
        },
        "rarity": Rarity.Common,
        "item": {
            "id": "glass_bottle",
            "cmd": 1707
        }
    },

    "Ender Ore": {
        "forge": "Ender Dust",
        "sell": 7000,
        "museum": (2, 2, 5),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYTZhNzY2MzFjMjNlZTJhNzAwZjMzZGNmYTY1Yzc0ZGQzMGQwZjE1N2YzNTE1ZGIyMjU3Y2FkNjhlMmRjN2MzYSJ9fX0=",
            "cmd": 1400
        }
    },
    "Ender Dust": {
        "sell": 9500,
        "museum": (2, 2, 6),
        "rarity": Rarity.Epic,
        "item": {
            "id": "purple_dye",
            "cmd": 1403
        }
    },

    "Engine": {
        "craft": {
            "tier": CraftTier.Tech2,
            "recipe": [
                ["Iron Ingot", "Gold Ingot", "Iron Ingot"],
                ["Electric Circuit", "Magnet", "Copper Coil"],
                ["Iron Ingot", "Battery", "Iron Ingot"]
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvM2QwNDVjYTNlOGEyOWUxOTkzMTY1NjM2MmUxMjQ3NzYzM2E2ODljNDgwMWQ4ZTIxZjdkYTBmODBjYzU5ZTU2YiJ9fX0=",
            "cmd": 1648
        }
    },

    "Extreme Insight Tech Helmet": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Impure Lead", "Iron Ingot", "Impure Lead"],
                ["Advanced Circuit", "Tech Perception Gear", "Glass"],
                ["Uranium", None, "Cobalt"]
            ]
        },
        "use": [
            "Reveals Tech 2 recipes in the tech crafting table."
        ],
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjdmNzFlNDRhNmM5NGM2ZDVhOTkyZDlhZmJlYjIxZjZlYjA3OTQ4ZDRlMGIwYmRhYWI1ZTlmOThjNWQ3OGNkIn19fQ==",
            "cmd": 1666
        }
    },

    "Ferrosilicon": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Iron Ingot", "Silica", "Silica"],
                [None] * 3,
                [None] * 3
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "iron_ingot",
            "cmd": 1625
        }
    },

    "Fertilizer": {
        "craft": {
            "tier": CraftTier.Pumpkin,
            "recipe": [
                ["Iron Ingot", "Enhanced Ash", "Iron Ingot"],
                ["Fabric", "Jack O'Lantern", "Fabric"],
                ["Starite", "Iridite Sod", "Starite"]
            ]
        },
        "use": [
            "Requires [Starite] to use. Clicking on a pumpkin seed will immediately turn it into a [Pumpkin (Block)]."
        ],
        "rarity": Rarity.Rare,
        "item": {
            "id": "shears",
            "cmd": 1864
        }
    },

    "Fertilizer Upgrade": {
        "craft": {
            "tier": CraftTier.Pumpkin,
            "recipe": [
                ["Ruby Grass", "Fabric", "Iridite Grass"],
                ["Celestial Artefact", "Golden Jack O'Lantern", "Volcanic Ash Clump"],
                ["Golden Grass", "Meteorite Core", "Diamond Grass"]
            ]
        },
        "use": [
            "Can increase the [Fertilizer]'s capacity."
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "rabbit_hide",
            "cmd": 1865
        }
    },

    "Fervor of the Gemstone God": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                [None, "Water Amethyst", None],
                ["Oinx", "Arkenstone", "Perfect Aquamarine"],
                [None, "Flawless Gemstone Mesh Orb", None]
            ]
        },
        "accessory": {
            "use": "Gives +25% luck and a special @item effect.",
            "slots": 0
        },
        "rarity": Rarity.Divine,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzRkNDJmOWM0NjFjZWUxOTk3YjY3YmYzNjEwYzY0MTFiZjg1MmI5ZTVkYjYwN2JiZjYyNjUyN2NmYjQyOTEyYyJ9fX0=",
            "cmd": 1776
        }
    },

    "Flawless Gemstone Mesh Orb": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                ["Perfect Diamond", "Perfect Opal", "Perfect Amber"],
                ["Perfect Ruby", "Perfect Amethyst", "Perfect Topaz"],
                ["Perfect Onyx", "Perfect Pearl", "Perfect Hematite"]
            ]
        },
        "museum": (8, 1, 6),
        "rarity": Rarity.Exotic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzRkYTJhODg0MmY5ZGFjY2M4OTcxN2E0YmMxM2Q2Mjk3NzlkYTNjMWY3YmNkZTZjNGJjNWFlNzhkYTJmMmY1NiJ9fX0=",
            "cmd": 1777
        }
    },

    "Flippers": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                [None] * 3,
                ["Orichalcum Piece", "Diving Boots", "Orichalcum Piece"],
                ["Impure Aluminium", "Plastic Sheet", "Impure Aluminium"]
            ]
        },
        "use": [
            "Gives Dolphin's Grace when underwater."
        ],
        "depth": 10,
        "rarity": Rarity.Rare,
        "item": {
            "id": "leather_boots",
            "color": "6464C8",
            "enchanted": True,
            "cmd": 1722
        }
    },

    "Flower": {
        "museum": (7, 3, 3),
        "rarity": Rarity.Rare,
        "item": {
            "id": "pink_tulip",
            "cmd": 1742
        }
    },

    "Fossil": {
        "sell": 500,
        "museum": (5, 1, 8),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZjE1N2RiZTRmNGQ2ODFkNDhmOTIzOGFkYTM0NDBiZWUxMWJkZjI5MDIxZWYyNGE1NWFkMDEzMTI3MTdlODE0NiJ9fX0=",
            "cmd": 1566
        }
    },

    "Gemstone Mixture": {
        "obtain": [
            "The nether shop offers this for $8,000."
        ],
        "museum": (4, 2, 8),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzBmMGM2Nzc3N2IxZDU0NjJkZjVhZjZkODRhOWExMTFmNTk1MDVmYWFmNWFiZTNiM2Q1ZThhMGRiZjJlNzIwYiJ9fX0=",
            "cmd": 1483
        }
    },

    "Gemstone Pickaxe": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Gemstone Mixture", "Synthetic Diamond", "Gemstone Mixture"],
                ["Amber", "Boron Nitride Pickaxe", "Refined Ruby"],
                ["Gemstone Mixture", "Onyx", "Gemstone Mixture"]
            ]
        },
        "rarity": Rarity.Epic,
        "mining speed": 7,
        "breaking power": 6,
        "item": {
            "id": "iron_pickaxe",
            "cmd": 1482
        }
    },

    "Gilded Chunk": {
        "sell": 350,
        "museum": (1, 4, 4),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7ImlkIjoiZGNjOTBjYzkzZWRhNDQ5YTk1Y2U5MGU0NjBkZjJiYjkiLCJ0eXBlIjoiU0tJTiIsInVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzQ4MmQxYmE0YmRhYzk5MGY2ZWE5ODc3MDM1ODdmZDc5ZmU1NTU1NTM2MzI1MTk4NDY3OWQ0ZjI3OWNjMGMyYSIsInByb2ZpbGVJZCI6IjgwMThhYjAwYjJhZTQ0Y2FhYzliZjYwZWY5MGY0NWU1IiwidGV4dHVyZUlkIjoiYzQ4MmQxYmE0YmRhYzk5MGY2ZWE5ODc3MDM1ODdmZDc5ZmU1NTU1NTM2MzI1MTk4NDY3OWQ0ZjI3OWNjMGMyYSJ9fSwic2tpbiI6eyJpZCI6ImRjYzkwY2M5M2VkYTQ0OWE5NWNlOTBlNDYwZGYyYmI5IiwidHlwZSI6IlNLSU4iLCJ1cmwiOiJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlL2M0ODJkMWJhNGJkYWM5OTBmNmVhOTg3NzAzNTg3ZmQ3OWZlNTU1NTUzNjMyNTE5ODQ2NzlkNGYyNzljYzBjMmEiLCJwcm9maWxlSWQiOiI4MDE4YWIwMGIyYWU0NGNhYWM5YmY2MGVmOTBmNDVlNSIsInRleHR1cmVJZCI6ImM0ODJkMWJhNGJkYWM5OTBmNmVhOTg3NzAzNTg3ZmQ3OWZlNTU1NTUzNjMyNTE5ODQ2NzlkNGYyNzljYzBjMmEifSwiY2FwZSI6bnVsbH0=",
            "cmd": 1367
        }
    },

    "Glass": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Sand"] * 3,
                ["Silica", "Dense Sand", "Silica"],
                ["Sand"] * 3
            ]
        },
        "sell": 15000,
        "museum": (5, 3, 8),
        "rarity": Rarity.Rare,
        "item": {
            "id": "glass",
            "cmd": 1620
        }
    },

    "Glowing Candy": {
        "obtain": [
            "Mining blocks in the upper mesa mine after consuming [Grapes of Jonathan] has a chance of dropping this."
        ],
        "museum": (8, 3, 7),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzQxZTg3ZjRmMmM3MWU4NDI4MTIxOGU3OWNmMjBlN2IzZmFjMjg2ZmNhYmY3NmY3NDhlMDUwNDdmMGYwOTE5In19fQ==",
            "cmd": 1844
        }
    },
    
    "Glue": {
        "forge": "Super Glue",
        "sell": 800,
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Earth Crystal", "Plant Fibre", "Bone"],
                ["Sog Stone", None, None],
                [None, None, None]
            ]
        },
        "museum": (4, 2, 3),
        "rarity": Rarity.Common,
        "item": {
            "id": "white_dye",
            "cmd": 1437
        }
    },
    "Super Glue": {
        "museum": (4, 2, 4),
        "sell": 5000,
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "white_dye",
            "enchanted": True,
            "cmd": 1447
        }
    },

    "Gold Ore": {
        "forge": "Gold Ingot",
        "sell": 150,
        "museum": (2, 1, 6),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "firework_star",
            "color": "DECF2A",
            "cmd": 1362
        }
    },
    "Gold Ingot": {
        "forge": "Gold Block",
        "sell": 1500,
        "museum": (2, 1, 7),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "gold_ingot",
            "cmd": 1373
        }
    },
    "Gold Block": {
        "sell": 8000,
        "museum": (2, 1, 8),
        "rarity": Rarity.Epic,
        "item": {
            "id": "gold_block",
            "cmd": 1512
        }
    },

    "Gold Rod": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                [None, "Gold Ingot", None],
                [None, "Wood", None],
                [None, "Gold Ingot", None]
            ]
        },
        "sell": 4000,
        "rarity": Rarity.Rare,
        "item": {
            "id": "blaze_rod",
            "cmd": 1731
        }
    },

    "Gold Trophy": {
        "obtain": [
            "An extremely rare drop from presents."
        ],
        "museum": (3, 4, 1),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTNlNDU4MzFjMWVhODE3Zjc0NzdiY2FlYmZhM2QyZWUzYTkzNmVlOGVhMmI4YmRlMjkwMDZiN2U5YmRmNTgifX19",
            "cmd": 1510
        }
    },

    "Golden Candy": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Lush Candy", "Gold Ingot", "Rock Candy"],
                ["Glowing Candy", "Compressed Pumpkin", "Liquorice Candy"],
                ["Caramel Candy", "Spicy Candy", "Wrapped Candy"]
            ]
        },
        "museum": (8, 4, 1),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZjk3NWUwMzg3MjA3ZWM3MzM4OGRhYjFiNGQ1MDMwMzBjNGMyNmFhOGFlMThmMmNmMjJjNGZhOWVkNDY1ZmRmNCJ9fX0=",
            "cmd": 1846
        }
    },

    "Golden Excavator": {
        "obtain": [
            "The overworld shop offers this for $13,370."
        ],
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "golden_shovel",
            "cmd": 1383
        }
    },

    "Golden Grass": {
        "sell": 150,
        "museum": (1, 1, 5),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "horn_coral_fan",
            "cmd": 1341
        }
    },

    "Golden Hopper Talisman": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Gold Ingot"] * 3,
                ["Gold Block", "Hopper Talisman", "Gold Block"],
                ["Gold Ingot"] * 3
            ]
        },
        "accessory": {
            "use": "Significantly decreases [Auto Seller] tax",
            "slots": 2
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "ewogICJ0aW1lc3RhbXAiIDogMTY1MzY3NzE1NDMxMywKICAicHJvZmlsZUlkIiA6ICJhYzM2YmVkZGQxNGQ0YjVmYmQyYzc5OThlMWMwOTg3ZCIsCiAgInByb2ZpbGVOYW1lIiA6ICJtYWlzYWthIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlL2FlNzJiZDdkMGQ3YjI0NjhmOWE1ZjZkNWEwY2JiMjdhY2UxMGU2YTFlNDRjNWJiYjBiMjQ4Nzk3OTg0NDE0MGMiCiAgICB9CiAgfQp9",
            "cmd": 1738
        }
    },
    
    "Golden Pickaxe": {
        "obtain": [
            "The overworld shop offers this for $6,000."
        ],
        "rarity": Rarity.Uncommon,
        "mining speed": 1.6,
        "breaking power": 3,
        "item": {
            "id": "golden_pickaxe",
            "cmd": 1366
        }
    },

    "Grapes of Jonathan": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                [None, "Blood", None],
                ["Pumpkin", "Aureate Grapes", "Pumpkin"],
                [None, "Blood", None]
            ]
        },
        "obtain": [
            "The @waluigi shop offers this for 20 Waluigi Tokens."
        ],
        "museum": (8, 4, 2),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "sweet_berries",
            "cmd": 1838
        }
    },

    "Grass": {
        "forge": "Plant Fibre",
        "sell": 5,
        "museum": (1, 1, 3),
        "rarity": Rarity.Common,
        "obtain": [
            "The Jonathan shop (next to the beehive in the mesa) offers this for $800."
        ],
        "item": {
            "id": "grass",
            "cmd": 1340
        }
    },
    "Roots": {
        "forge": "Plant Fibre",
        "sell": 3,
        "museum": (5, 2, 1),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "dead_bush",
            "cmd": 1569
        }
    },
    "Plant Fibre": {
        "forge": "Fabric",
        "sell": 40,
        "museum": (4, 2, 1),
        "rarity": Rarity.Common,
        "item": {
            "id": "green_dye",
            "cmd": 1429
        }
    },
    "Fabric": {
        "museum": (4, 2, 2),
        "rarity": Rarity.Rare,
        "item": {
            "id": "paper",
            "cmd": 1442
        }
    },

    "Green Samurai Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Orichalcum", "Lead Ingot", "Orichalcum"],
                ["Lead Ingot", "Skin Core", "Lead Ingot"],
                ["Orichalcum", "Lead Ingot", "Orichalcum"]
            ]
        },
        "use": [
            "A skin that can be applied to a [Power Helmet MK2] or [Heavy-Duty Diving Helmet]."
        ],
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDhlNDg1ODIwODZjNjFlNWVkZjczOTQwMTQzZGJmYTFlZGJjOTdhYTMzNmM5MGQzMWQxOTJhN2FjYWY2MTdhIn19fQ==",
            "cmd": 1868
        }
    },

    "Guardian Helmet": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Orichalcum", "Omega Helmet", "Orichalcum"],
                ["Orichalcum Lump", "Diving Helmet", "Orichalcum Lump"],
                [None] * 3
            ]
        },
        "use": [
            "Reduces void damage",
            "Gives +16% mining speed",
            "Gives the Dolphin's Grace effect in water"
        ],
        "oxygen": 30,
        "depth": 10,
        "rarity": Rarity.Legendary,
        "item": {
            "id": "leather_helmet",
            "color": "FF7864",
            "enchanted": True,
            "cmd": 1808
        }
    },
    "Guardian Chestplate": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Orichalcum", None, "Orichalcum"],
                ["Orichalcum Lump", "Diving Suit", "Orichalcum Lump"],
                ["Hypercompact Rockite", "Omega Cuirass", "Hypercompact Rockite"]
            ]
        },
        "use": [
            "Reduces void damage",
            "Gives +15% mining speed"
        ],
        "oxygen": 20,
        "depth": 10,
        "rarity": Rarity.Legendary,
        "item": {
            "id": "leather_chestplate",
            "color": "009696",
            "cmd": 1809
        }
    },
    "Guardian Leggings": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Orichalcum", "Omega Leggings", "Orichalcum"],
                ["Orichalcum Lump", "Diving Leggings", "Orichalcum Lump"],
                ["Hypercompact Rockite", None, "Hypercompact Rockite"]
            ]
        },
        "use": [
            "Reduces void damage",
            "Gives +15% mining speed"
        ],
        "oxygen": 20,
        "depth": 10,
        "rarity": Rarity.Legendary,
        "item": {
            "id": "leather_leggings",
            "color": "0096B4",
            "cmd": 1810
        }
    },
    "Guardian Boots": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Orichalcum Lump", "Diving Boots", "Orichalcum Lump"],
                ["Orichalcum", "Omega Atmoboots", "Orichalcum"]
            ]
        },
        "use": [
            "Reduces void damage",
            "Gives +15% mining speed"
        ],
        "oxygen": 20,
        "depth": 10,
        "rarity": Rarity.Legendary,
        "item": {
            "id": "leather_boots",
            "color": "006464",
            "cmd": 1811
        }
    },

    "Hat of Knowledge": {
        "obtain": [
            "The nether shop offers this for $30,000."
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "leather_helmet",
            "color": "B400B4",
            "enchanted": True,
            "cmd": 1476
        }
    },
    "Hat of Wisdom": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Gemstone Mixture", "Celestial Ingot", "Gemstone Mixture"],
                ["Soul", "Hat of Knowledge", "Soul"],
                ["Gemstone Mixture", "Boron Nitride", "Gemstone Mixture"]
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "leather_helmet",
            "color": "008CB4",
            "enchanted": True,
            "cmd": 1477
        }
    },
    "Hat of Ominescence": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Void Orb", "Sage Crystal", "Void Orb"],
                ["Refined Topaz", "Hat of Wisdom", "Refined Amethyst"],
                ["Arkenstone Fragment", "Omega Shard", "Ender Ore"]
            ]
        },
        "rarity": Rarity.Legendary,
        "item": {
            "id": "leather_helmet",
            "color": "8CFA64",
            "enchanted": True,
            "cmd": 1538
        }
    },

    "Heat Chestplate": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Netherite Ingot", None, "Netherite Ingot"],
                ["Netherite Ingot", "Magma Orb", "Netherite Ingot"],
                ["Netherite Ingot", "Fabric", "Netherite Ingot"]
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "leather_chestplate",
            "color": "50000A",
            "cmd": 1459
        }
    },

    "Heavy Boots": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                [None] * 3,
                ["Lead Ingot", None, "Lead Ingot"],
                ["Weight Block", "Sturdy Boots", "Weight Block"]
            ]
        },
        "use": [
            "Allows you to walk on the sea floor and resist wind and water currents. Sneak to descend faster."
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "leather_boots",
            "color": "505050",
            "enchanted": True,
            "cmd": 1706
        }
    },

    "Heavy-Duty Diving Helmet": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Orichalcum Ingots", "Lead Plate", "Orichalcum Ingots"],
                ["Hematite", "Diving Helmet", "Hematite"],
                ["Orichalcum Ingots", "Plastic Sheet", "Orichalcum Ingots"]
            ]
        },
        "use": [
            "Reduces void damage"
        ],
        "oxygen": 40,
        "depth": 30,
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODU2OTI0NTM3MWVkZmY2M2EyNjkxM2E5NzJmMmM0NGZiZTQxZjc1ZTQyNjY4YTcyNTk5NzU5Y2Y0NTJmM2EifX19",
            "cmd": 1812
        }
    },

    "Hightech Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Copper Ingot", "Electric Circuit", "Copper Ingot"],
                ["Copper Ingot", "Skin Core", "Copper Ingot"],
                ["Copper Ingot", "Synthetic Diamond", "Copper Ingot"]
            ]
        },
        "museum": (8, 4, 6),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmI2Yzc0ODNkMjQ1YjRkY2QzMTllYzRlOTIxZWRkNWJlYmFjNmYzZjQ2YWYzNzRlZjZiMzQzZjc4NmI5Y2RhIn19fQ==",
            "cmd": 1850
        }
    },

    "Holy Book of Wah": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                [None] * 3,
                ["Fabric", "Waluigi Ball", "Amethyst"],
                [None] * 3
            ]
        },
        "use": [
            "When right-clicked, starts a Waluigi Raffle. This item is consumed upon use."
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "enchanted_book",
            "enchanted": True,
            "cmd": 1775
        }
    },

    "Honey": {
        "museum": (7, 3, 5),
        "rarity": Rarity.Epic,
        "obtain": [
            "The beehive in the mesa will convert [Honeycomb] to this for $1,000 each."
        ],
        "item": {
            "id": "honey_bottle",
            "cmd": 1746
        }
    },

    "Honeycomb": {
        "sell": 800,
        "museum": (7, 3, 4),
        "rarity": Rarity.Rare,
        "use": [
            "The beehive in the mesa will convert this to [Honey] for $1,000 each."
        ],
        "item": {
            "id": "honeycomb",
            "cmd": 1745
        }
    },

    "Hopper Talisman": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["String", None, "String"],
                [None, "Steel", None],
                [None] * 3
            ]
        },
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "ewogICJ0aW1lc3RhbXAiIDogMTY1MzY3NzE3MDk0NSwKICAicHJvZmlsZUlkIiA6ICIxNGU0NGFmZjZhODg0ZGFmOGEyNDUzYzIwZDVhNTE1YiIsCiAgInByb2ZpbGVOYW1lIiA6ICJKYW4yazE3IiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlLzY3MDMyMmQyNTg0ODFiZjU4N2QyMzdhYmFkNDY5ZWNiNTJmMzhhNDViMjZhZjAzZjJhMGM2ZTk5ODFiYmIzOWUiCiAgICB9CiAgfQp9",
            "cmd": 1737
        }
    },

    "Ice Fragments": {
        "forge": "Ice Shard",
        "sell": 100,
        "museum": (6, 2, 2),
        "rarity": Rarity.Common,
        "item": {
            "id": "prismarine_crystals",
            "cmd": 1653
        }
    },
    "Ice Shard": {
        "forge": "Ice",
        "sell": 600,
        "museum": (6, 2, 3),
        "rarity": Rarity.Common,
        "item": {
            "id": "prismarine_shard",
            "cmd": 1654
        }
    },
    "Ice": {
        "forge": "Compressed Ice",
        "sell": 3500,
        "museum": (6, 2, 4),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTZhYWI1OGZhMDFmY2U5YWY0NjllZDc0N2FlZDgxMWQ3YmExOGM0NzZmNWE3ZjkwODhlMTI5YzMxYjQ1ZjMifX19",
            "cmd": 1655
        }
    },
    "Compressed Ice": {
        "forge": "Aquamarine",
        "sell": 18000,
        "museum": (6, 2, 5),
        "rarity": Rarity.Rare,
        "item": {
            "id": "packed_ice",
            "cmd": 1656
        }
    },
    "Aquamarine": {
        "forge": "Perfect Aquamarine",
        "museum": (6, 2, 6),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvN2Y5MjYwNWVlYTQ2ZWE4NDg4ZWZjMjZiM2Y5ZmM5OTU1MTcwNWU5YzBiNWViYjJmZjg5ODQ2OGYyNzc1OTVhNiJ9fX0=",
            "cmd": 1657
        }
    },
    "Perfect Aquamarine": {
        "sell": 500000,
        "museum": (6, 2, 7),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmE4OWI1MjM2MzIzZDhmNTc2ZTcxY2I0YTEyZjI4ODE0ZGQzMjIyOTQ3OWI5NzY1ZGVhNzEwZGY2ZTM5MTA0OCJ9fX0=",
            "cmd": 1658
        }
    },

    "Icebreaker": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Ice Fragments"] * 3,
                [None, "Golden Pickaxe", None],
                [None, "Wood", None]
            ]
        },
        "rarity": Rarity.Uncommon,
        "mining speed": 5.5,
        "breaking power": 4,
        "item": {
            "id": "diamond_pickaxe",
            "enchanted": True,
            "cmd": 1760
        }
    },

    "Iridite Sod": {
        "forge": "Iridite Grass",
        "sell": 10000,
        "museum": (7, 4, 2),
        "rarity": Rarity.Epic,
        "item": {
            "id": "brain_coral_fan",
            "enchanted": True,
            "cmd": 1752
        }
    },
    "Iridite Grass": {
        "museum": (7, 4, 3),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "brain_coral",
            "enchanted": True,
            "cmd": 1753
        }
    },

    "Iron Ore": {
        "forge": "Iron Ingot",
        "sell": 90,
        "museum": (2, 1, 2),
        "rarity": Rarity.Common,
        "item": {
            "id": "firework_star",
            "color": "EB8844",
            "cmd": 1355
        }
    },
    "Iron Sand": {
        "forge": "Iron Ingot",
        "sell": 90,
        "museum": (5, 1, 6),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGI2YTI5ZWE2OGEwYzYxYjFlZGEyZDhhZWMzZTIyMjk3MjczMjNiN2QyZGE2YmMwNGNjMGNkMmRlZjNiNDcxMiJ9fX0=",
            "cmd": 1559
        }
    },
    "Iron Ingot": {
        "sell": 1000,
        "museum": (2, 1, 3),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "iron_ingot",
            "cmd": 1372
        }
    },

    "Iron Pickaxe": {
        "obtain": [
            "The overworld shop offers this for $1500."
        ],
        "rarity": Rarity.Common,
        "mining speed": 1.3,
        "breaking power": 2,
        "item": {
            "id": "iron_pickaxe",
            "cmd": 1360
        }
    },

    "Jonathan Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Cream", "Grapes of Jonathan", "Cream"],
                ["Ruby", "Skin Core", "Ruby"],
                ["Cream", "Grapes of Jonathan", "Cream"]
            ]
        },
        "museum": (9, 1, 4),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjU1MWMyZmMxNzRkMTAxOGJkYWE5YmMyMGQ5Y2ZhZTAyM2U1MjMxNTdhNjA2ZjJiYTlmM2U2OTE3MTNiMjgwNiJ9fX0=",
            "cmd": 1857
        }
    },

    "Kawaii Amogus": {
        "museum": (6, 1, 9),
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "ewogICJ0aW1lc3RhbXAiIDogMTY0MzU3MTA1MjEyMywKICAicHJvZmlsZUlkIiA6ICIxOTU3OWU4MmE0NWQ0ZGQzOWE1NTE4MmNhODQ0ZTAxYiIsCiAgInByb2ZpbGVOYW1lIiA6ICJzdXNzeWJha2EiLAogICJzaWduYXR1cmVSZXF1aXJlZCIgOiB0cnVlLAogICJ0ZXh0dXJlcyIgOiB7CiAgICAiU0tJTiIgOiB7CiAgICAgICJ1cmwiIDogImh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzZlMWMyNGRmNjVkZTAzNDc4ZTNkZWZkNTVlNzYwNjQ4NDQ0NjQwOGI5ZWEzZGY3YTAxY2Y5ZGY1NDRmOTZmNCIKICAgIH0KICB9Cn0=",
            "cmd": 1667
        }
    },

    "Kelp": {
        "forge": "Dried Kelp",
        "museum": (7, 2, 2),
        "rarity": Rarity.Rare,
        "item": {
            "id": "kelp",
            "cmd": 1726
        }
    },
    "Dried Kelp": {
        "museum": (8, 1, 8),
        "rarity": Rarity.Epic,
        "item": {
            "id": "dried_kelp",
            "cmd": 1727
        }
    },

    "Lantern": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                [None, "Iron Ingot", None],
                [None, "Magma Gem", None],
                [None, "Wood", None]
            ]
        },
        "use": [
            "Hold to illuminate surroundings",
            "Can be used to light up a pumpkin"
        ],
        "rarity": Rarity.Uncommon,
        "lore": [
            "Hold it to illuminate your surroundings.",
            "Can also light up jack o'lantern blocks."
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmVmN2I3OTU4YTkzNTIxYjBhNmU5M2ZiNjMxMzhmNDhmNGYxMWY0YWQ1ZWRiMDE5MGE4MzRlZGFkMWIxNmRhYyJ9fX0=",
            "cmd": 1858
        }
    },

    "Lead Drill": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Impure Lead"] * 3,
                [None, "Battery", None],
                [None, "Ender Dust", None]
            ]
        },
        "rarity": Rarity.Uncommon,
        "mining speed": 16,
        "breaking power": 5,
        "item": {
            "id": "iron_horse_armor",
            "cmd": 1644
        }
    },

    "Lead Helmet": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Impure Lead"] * 3,
                ["Impure Lead", None, "Impure Lead"],
                [None] * 3
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "netherite_helmet",
            "cmd": 1626
        }
    },
    "Lead Chestplate": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Impure Lead", None, "Impure Lead"],
                ["Impure Lead"] * 3,
                ["Impure Lead"] * 3
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "netherite_chestplate",
            "cmd": 1627
        }
    },
    "Lead Leggings": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Impure Lead"] * 3,
                ["Impure Lead", None, "Impure Lead"],
                ["Impure Lead", None, "Impure Lead"]
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "netherite_leggings",
            "cmd": 1628
        }
    },
    "Lead Boots": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                [None] * 3,
                ["Impure Lead", None, "Impure Lead"],
                ["Impure Lead", None, "Impure Lead"]
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "netherite_boots",
            "cmd": 1629
        }
    },

    "Lead Ore": {
        "forge": "Impure Lead",
        "sell": 500,
        "museum": (5, 3, 9),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "firework_star",
            "color": "434343",
            "cmd": 1585
        }
    },
    "Impure Lead": {
        "forge": "Lead Ingot",
        "sell": 3000,
        "museum": (5, 4, 1),
        "rarity": Rarity.Uncommon,
        "obtain": [
            "The Jonathan shop (next to the beehive in the mesa) offers this for $35,000."
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvN2ZmOTgxN2Q3NjdkMmVkZTcxODFhMDU3YWEyNmYwOGY3ZWNmNDY1MWRlYzk3ZGU1YjU0ZWVkZTFkZDJiNDJjNyJ9fX0=",
            "cmd": 1586
        }
    },
    "Lead Ingot": {
        "forge": "Lead Plate",
        "sell": 16000,
        "museum": (5, 4, 2),
        "rarity": Rarity.Rare,
        "lore": [
            "A full ingot of lead.",
            "Can reduce radiation due",
            "to its high density."
        ],
        "item": {
            "id": "netherite_ingot",
            "cmd": 1587
        }
    },
    "Lead Plate": {
        "sell": 90000,
        "museum": (5, 4, 3),
        "rarity": Rarity.Epic,
        "item": {
            "id": "blackstone_pressure_plate",
            "cmd": 1588
        }
    },

    "Lead Talisman": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["String", None, "String"],
                [None, "Lead Ingot", None],
                [None] * 3
            ]
        },
        "accessory": {
            "use": "Increases radiation resistance by 3",
            "slots": 1
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "ewogICJ0aW1lc3RhbXAiIDogMTY1MzY3NzE4NjU5MCwKICAicHJvZmlsZUlkIiA6ICJmZTYxY2RiMjUyMTA0ODYzYTljY2E2ODAwZDRiMzgzZSIsCiAgInByb2ZpbGVOYW1lIiA6ICJNeVNoYWRvd3MiLAogICJzaWduYXR1cmVSZXF1aXJlZCIgOiB0cnVlLAogICJ0ZXh0dXJlcyIgOiB7CiAgICAiU0tJTiIgOiB7CiAgICAgICJ1cmwiIDogImh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNWE1MzU2MjkwZmE5NTYyZmUwYmQ2YWVjMzZiMjJjZmE4YTZhMjBkY2ZmNzUzZGMwOTNjMDQ4MDQ2NGMwODcyNyIKICAgIH0KICB9Cn0=",
            "cmd": 1739
        }
    },

    "Lesser Fuel Chunk": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                [None, "Coal", None],
                ["Coal", "Grass", "Coal"],
                [None, "Coal", None]
            ]
        },
        "obtain": [
            "The communist shop offers this for $2,000.",
            "The Jonathan shop (next to the beehive in the mesa) offers this for $2,500."
        ],
        "use": [
            "Right-click the forge with this to decrease the time by 2 minutes."
        ],
        "rarity": Rarity.Common,
        "item": {
            "id": "coal",
            "cmd": 1438
        }
    },
    "Greater Fuel Chunk": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Coal"] * 3,
                ["Magma Stone", "Lesser Fuel Chunk", "Magma Stone"],
                ["Coal"] * 3
            ]
        },
        "use": [
            "Right-click the forge with this to decrease the time by 30 minutes."
        ],
        "rarity": Rarity.Common,
        "item": {
            "id": "charcoal",
            "cmd": 1439
        }
    },
    "Super Fuel Chunk": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Sulfur", "Magma Gem", "Sulfur"],
                ["Anthracite", "Greater Fuel Chunk", "Anthracite"],
                ["Sulfur", "Magma Gem", "Sulfur"]
            ]
        },
        "use": [
            "Right-click the forge with this to decrease the time by 2 hours."
        ],
        "rarity": Rarity.Common,
        "item": {
            "id": "flint",
            "cmd": 1440
        }
    },

    "Light Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Waluigi Ball", "Refined Amethyst", "Waluigi Ball"],
                ["Cream", "Skin Core", "Cream"],
                ["Mustache Polish"] * 3
            ]
        },
        "museum": (8, 4, 9),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZWJmM2Q5M2NmZjdmMWY0ZTVjNjE3NDA1NmNhZmNhYjMwNmExMDhiNjUzYzY3MGZmZWVkYmZmYWIyOTkyNmNhMCJ9fX0=",
            "cmd": 1853
        }
    },

    "Lift Fuel Core": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipes": [
                [
                    ["Meteorite Core", None, None],
                    [None] * 3,
                    [None] * 3
                ], [
                    ["Magma Orb", "Magnesium", None],
                    [None] * 3,
                    [None] * 3
                ]
            ]
        },
        "use": [
            "Can be inserted into the lift in the nether hub to take you to the mountain mine. This item is consumed upon use."
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "magma_cream",
            "cmd": 1867
        }
    },

    "Liquorice Candy": {
        "museum": (8, 3, 6),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDI5NWZiNTRkMTQ0YjZjZmIyZTc5NjFjNTUxNGE2M2NlNjE4OGI4Y2IzZjM5YmE3OTM4NjA3ZTc0ZjM3ZjQ2NCJ9fX0=",
            "cmd": 1842
        }
    },

    "Loser's Apple": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                ["Ruby", "Grass", "Ruby"],
                ["Ruby"] * 3,
                ["Ruby"] * 3
            ]
        },
        "use": [
            "A musical instrument that can be played."
        ],
        "audio": "vibraphone",
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTIxMTI3ZDIyNjc1YzVjNzY5YTBjMDhiNTcyMDE4ZDI5OWM4MzA0NmY4ZTFmOTQzZWQ5ZDUxYmUwM2IwNyJ9fX0=",
            "cmd": 1791
        }
    },

    "Lucky Gemstone Mixture": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Gemstone Mixture", "Aureate Grapes", "Gemstone Mixture"],
                ["Refined Amber", "Refined Amethyst", "Refined Ruby"],
                [None, "Adamantium", None]
            ]
        },
        "rarity": Rarity.Legendary,
        "lore": [
            "Can be applied to gear in an anvil up to 6 times",
            "to increase its base luck. First time gives +10%, but",
            "subsequent dusts on the same item give less."
        ],
        "use": [
            "Increases base luck of gear when combined in an anvil"
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTliZWRjYWVkZjUxYmQ2NTYxZDU2MGFiYTFjZjg0ZDVmNWZiODMyODZkOGYxY2M3NDFjYWYxOWViMjQwMjJjMSJ9fX0=",
            "cmd": 1869
        }
    },

    "Lush Candy": {
        "obtain": [
            "Mining blocks in the dirt layer after consuming [Grapes of Jonathan] has a chance of dropping this."
        ],
        "museum": (8, 3, 3),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODdmNTA0Y2RiZjViMjExMjFiODIxODUyOGRjZTU2NzUwNWQ0NTY3ZDdlNzJjZDQzYTQ2M2NkNTFjODAxM2E2In19fQ==",
            "cmd": 1839
        }
    },

    "Magical Shoe Polish": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Earth Crystal", "Magnesium", "Sog Stone"],
                ["Iron Ingot", "Flower", "Iron Ingot"],
                ["Iron Ingot"] * 3
            ]
        },
        "accessory": {
            "use": "Increases radius of Boots of Snow and Boots of Growth",
            "slots": 2
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmUxYzdhYzQzNmMwZTQ5NzJkMDkzYThmNjMzMDY0MDllM2ZhNTMyMWRiNGJmMTA2ZjRlZjFkODBjYzM2MDc3NCJ9fX0=",
            "cmd": 1743
        }
    },

    "Magical Snowball": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Compressed Snow"] * 3,
                ["Compressed Snow", "Starite", "Compressed Snow"],
                ["Compressed Snow"] * 3
            ]
        },
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMWRmZDc3MjRjNjlhMDI0ZGNmYzYwYjE2ZTAwMzM0YWI1NzM4ZjRhOTJiYWZiOGZiYzc2Y2YxNTMyMmVhMDI5MyJ9fX0=",
            "cmd": 1527
        }
    },

    "Magma Stone": {
        "forge": "Magma Gem",
        "sell": 200,
        "museum": (2, 3, 3),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "red_dye",
            "cmd": 1365
        }
    },
    "Magma Gem": {
        "forge": "Magma Orb",
        "sell": 1200,
        "museum": (2, 3, 4),
        "rarity": Rarity.Rare,
        "item": {
            "id": "red_dye",
            "enchanted": True,
            "cmd": 1407
        }
    },
    "Magma Orb": {
        "forge": "Magma Core",
        "sell": 7000,
        "museum": (2, 3, 5),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNWI4ZjIxZWRiNzExNjkwODBjMGRkNDI5MzVlZTAwMjQyYzhjYzliYjkxNjU5YWI3MDA0ODlhZjliN2M1OGUxNyJ9fX0=",
            "cmd": 1457
        }
    },
    "Magma Core": {
        "sell": 45000,
        "museum": (2, 3, 6),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvY2Q0YTdmY2U2Zjg4OGU4MDQyZDYzNGM3OTczYjNjYmM3ZTkzMjBmMTc0NDYwOGU2YzVjZGQ1ZjRlZjljYTM5MyJ9fX0=",
            "cmd": 1458
        }
    },

    "Magnet": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Iron Ingot", "Sulfur", "Cobalt Ore"],
                [None] * 3,
                [None] * 3
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYWJhOGViYzRjNmE4MTczMDk0NzQ5OWJmN2UxZDVlNzNmZWQ2YzFiYjJjMDUxZTk2ZDM1ZWIxNmQyNDYxMGU3In19fQ==",
            "cmd": 1647
        }
    },

    "Makeshift Diving Helmet": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Gold Ingot", "Impure Lead", "Gold Ingot"],
                ["Impure Lead", "Glass", "Impure Lead"],
                [None] * 3
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzE5YzE2NzFiMDQ1ZTg0MDEyMmMyNzQxMWI3YzhiYTNlZDZjNTUxOGE3NjRjY2Q0M2Q1M2FiOWE1OWU5ODY4YSJ9fX0=",
            "cmd": 1674
        }
    },

    "Mega Bomb": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Magma Gem", "Sulfur", "Magma Gem"],
                ["Sulfur", "Bomb", "Sulfur"],
                ["Magma Gem", "Sulfur", "Magma Gem"]
            ]
        },
        "rarity": Rarity.Rare,
        "breaking power": 3,
        "lore": ["More destruction."],
        "item": {
            "id": "fire_charge",
            "enchanted": True,
            "cmd": 1408
        }
    },

    "Meteorite": {
        "forge": "Meteorite Bar",
        "rads": 0.25,
        "museum": (8, 1, 3),
        "rarity": Rarity.Epic,
        "item": {
            "id": "cocoa_beans",
            "enchanted": True,
            "cmd": 1768
        }
    },
    "Meteorite Bar": {
        "rads": 1,
        "museum": (8, 1, 4),
        "rarity": Rarity.Epic,
        "item": {
            "id": "netherite_scrap",
            "enchanted": True,
            "cmd": 1769
        }
    },

    "Meteorite Core": {
        "sell": 10000,
        "rads": 1.5,
        "museum": (8, 1, 5),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "fire_charge",
            "cmd": 1770
        }
    },

    "Meteorite Helmet": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Meteorite Bar", "Meteorite", "Meteorite Bar"],
                ["Meteorite", None, "Meteorite"],
                [None] * 3
            ]
        },
        "use": [
            "Gives +3.2% mining speed",
            "When wearing the full set, emits flame particles"
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYTdlNjQ2NTU1OTRhZjQ1M2Q3YzFkZTM4ZGYzYWFlMWE5MmNhZjk0ZmE2M2YyYzRhNmUxMWExM2I2MzllZCJ9fX0=",
            "cmd": 1783
        }
    },
    "Meteorite Chestplate": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Meteorite", None, "Meteorite"],
                ["Meteorite", "Meteorite Bar", "Meteorite"],
                ["Meteorite"] * 3
            ]
        },
        "use": [
            "Gives +3.2% mining speed",
            "When wearing the full set, emits flame particles"
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "leather_chestplate",
            "color": "FF6400",
            "cmd": 1784
        }
    },
    "Meteorite Leggings": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Meteorite Bar", "Meteorite", "Meteorite Bar"],
                ["Meteorite", None, "Meteorite"],
                ["Meteorite", None, "Meteorite"]
            ]
        },
        "use": [
            "Gives +3.2% mining speed",
            "When wearing the full set, emits flame particles"
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "leather_leggings",
            "color": "FA5032",
            "cmd": 1785
        }
    },
    "Meteorite Boots": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                [None] * 3,
                ["Meteorite", None, "Meteorite"],
                ["Meteorite Bar", "Aeroboots", "Meteorite Bar"]
            ]
        },
        "use": [
            "Gives +3.2% mining speed",
            "When wearing the full set, emits flame particles"
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "leather_boots",
            "color": "503C32",
            "cmd": 1786
        }
    },

    "Meteorite Pickaxe": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Meteorite Bar", "Meteorite", "Meteorite Bar"],
                ["Meteorite", "Boron Nitride Pickaxe", "Meteorite"],
                ["Magma Gem"] * 3
            ]
        },
        "rarity": Rarity.Epic,
        "mining speed": 8,
        "breaking power": 6,
        "item": {
            "id": "golden_pickaxe",
            "cmd": 1782
        }
    },

    "Meteorite Talisman": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["String", "Meteorite", "String"],
                ["Meteorite", "Meteorite Bar", "Meteorite"],
                [None, "Meteorite", None]
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTZjODQ0N2E4YjZiMGUwYzdlNzYyOWM2ODk4ZWM5Yzc0OWE3YTBhMmI0NTJiOWMzODUyYzc4NDdiYjRkYzUifX19",
            "cmd": 1771
        }
    },
    "Meteorite Talisman +": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Meteorite Bar", "Meteorite Core", "Meteorite Bar"],
                ["Meteorite", "Meteorite Talisman", "Meteorite"],
                ["Meteorite Bar", "Refined Ruby", "Meteorite Bar"]
            ]
        },
        "accessory": {
            "use": "Gives +9% mining speed",
            "slots": 2
        },
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzM2ODdlMjVjNjMyYmNlOGFhNjFlMGQ2NGMyNGU2OTRjM2VlYTYyOWVhOTQ0ZjRjZjMwZGNmYjRmYmNlMDcxIn19fQ==",
            "cmd": 1772
        }
    },

    "Milk Bucket": {
        "obtain": [
            "Mine [Smooth Quartz Block] with an [Oil Pump] or [Turbo Oil Pump] with a [Bucket] in your hotbar."
        ],
        "museum": (6, 4, 2),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjUxYzAzYjVlNjU5Mjc1ZWQ4NWNhMmM4YWQ5ODhjNzU1Y2NmYmE0NWFmZjNmNmQ4ZDZmMjczOGIwOTY3Y2NjZCJ9fX0=",
            "cmd": 1688
        }
    },

    "Miner's Helmet": {
        "obtain": [
            "The overworld shop offers this for $500."
        ],
        "sell": 0,
        "rarity": Rarity.Common,
        "item": {
            "id": "leather_helmet",
            "color": "DCDC00",
            "cmd": 1361
        }
    },
    "Miner's Chestplate": {
        "obtain": [
            "The overworld shop offers this for $8,000."
        ],
        "rarity": Rarity.Rare,
        "item": {
            "id": "chainmail_chestplate",
            "cmd": 1479
        }
    },
    "Miner's Leggings": {
        "obtain": [
            "The nether shop offers this for $16,000."
        ],
        "rarity": Rarity.Rare,
        "item": {
            "id": "chainmail_leggings",
            "cmd": 1494
        }
    },

    "Miner's Sandwich": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Clover", "Salt", "Clover"],
                ["Bacon", "Luxury Cheese", "Bacon"],
                ["Egg", "Banana", "Egg"]
            ]
        },
        "museum": (4, 3, 2),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNGEyMTJmNzBmYjY2NTQ4ZmRmMmFiY2RiY2U4ZjMxNzA0MzRiODk5NWUyMWQxNGY5YjFmZjE0OTdjNjQ4ZCJ9fX0=",
            "cmd": 1506
        }
    },

    "Modular Helmet": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Impure Lead", "Electric Circuit", "Impure Lead"],
                ["Plastic Sheet", None, "Plastic Sheet"],
                [None] * 3
            ]
        },
        "rarity": Rarity.Legendary,
        "modular": {
            "slots": 2,
            "capacity": 6
        },
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTIxMmVlYWU4MDcyZTdlNDkwMzM0YjA5MzBkOWI2NTM0NmMwMjA4OGRmMTAzZTc5MzA4Y2FlMmM3ZTRmMzY2NSJ9fX0=",
            "cmd": 1596
        }
    },
    "Modular Chestplate": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Impure Lead", None, "Impure Lead"],
                ["Impure Lead", "Electric Circuit", "Impure Lead"],
                ["Plastic Sheet", "Lead Ingot", "Plastic Sheet"]
            ]
        },
        "rarity": Rarity.Legendary,
        "modular": {
            "slots": 2,
            "capacity": 6
        },
        "item": {
            "id": "leather_chestplate",
            "color": "FF9600",
            "cmd": 1589
        }
    },
    "Modular Leggings": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Impure Lead", "Electric Circuit", "Impure Lead"],
                ["Plastic Sheet", None, "Plastic Sheet"],
                ["Impure Lead", None, "Impure Lead"]
            ]
        },
        "rarity": Rarity.Legendary,
        "modular": {
            "slots": 2,
            "capacity": 6
        },
        "item": {
            "id": "leather_leggings",
            "color": "FF8C00",
            "cmd": 1594
        }
    },
    "Modular Boots": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                [None] * 3,
                ["Plastic Sheet", None, "Plastic Sheet"],
                ["Impure Lead", "Electric Circuit", "Impure Lead"]
            ]
        },
        "rarity": Rarity.Legendary,
        "modular": {
            "slots": 2,
            "capacity": 6
        },
        "item": {
            "id": "leather_boots",
            "color": "FF6400",
            "cmd": 1595
        }
    },

    "Mosquito Amber": {
        "sell": 20000,
        "museum": (1, 2, 4),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGRlZTViYmFlM2M4NTIyZWJlZWM5OThmNmNjMDcwZTljNDRjMzUxMzY3Yzc5ZWFmZjUxMTA3MTJmMDZhMDMwOSJ9fX0=",
            "cmd": 1431
        }
    },

    "Mustache Polish": {
        "sell": 500,
        "rarity": Rarity.Epic,
        "obtain": [
            "The @waluigi shop offers this for 5 Waluigi Tokens."
        ],
        "item": {
            "id": "black_dye",
            "cmd": 1773
        }
    },

    "Nether Miner's Chestplate": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                [None, "Water Orb", None],
                ["Heat Chestplate", "Super Glue", "Miner's Chestplate"],
                [None, "Water Orb", None]
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "netherite_chestplate",
            "cmd": 1481
        }
    },

    "Netherite Aeroboots": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Netherite Ingot", None, "Netherite Ingot"],
                [None, "Aeroboots", None],
                ["Netherite Ingot", None, "Netherite Ingot"]
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "netherite_boots",
            "cmd": 1480
        }
    },

    "Netherite Ingot": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                [None, "Netherite Scrap", None],
                ["Gold Ingot", "Amber", "Gold Ingot"],
                [None, "Netherite Scrap", None]
            ]
        },
        "museum": (2, 2, 1),
        "rarity": Rarity.Epic,
        "item": {
            "id": "netherite_ingot",
            "cmd": 1401
        }
    },

    "Netherite Pickaxe": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Diamond Pickaxe", "Netherite Ingot", None],
                [None] * 3,
                [None] * 3
            ]
        },
        "rarity": Rarity.Epic,
        "mining speed": 4,
        "breaking power": 5,
        "item": {
            "id": "netherite_pickaxe",
            "cmd": 1409
        }
    },

    "Netherite Scrap": {
        "sell": 1000,
        "museum": (2, 1, 9),
        "rarity": Rarity.Rare,
        "item": {
            "id": "netherite_scrap",
            "cmd": 1398
        }
    },

    "Nightvision Module": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Starite", "Glass", "Starite"],
                ["Magnesium Ingot", "Miner's Helmet", "Magnesium Ingot"],
                ["Electric Circuit"] * 3
            ]
        },
        "module": {
            "use": "Gives night vision",
            "slots": 1
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmMxNTFhN2RhZTkwM2FlNDdhZWY2MzdmMTBkNWU1N2ZlNzNmYTkyMzNiYzQ2N2I0ODUzYzdlMWJjZWFhOTVjZSJ9fX0=",
            "cmd": 1204
        }
    },

    "Obsidian": {
        "forge": "Large Obsidian",
        "sell": 1000,
        "museum": (2, 2, 7),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNGU3NjBiYmMxMTNjMjczZmFjNDA4OTZmYTIwODlhNTZjYzc0NmE3OWE3YTgyNzVmNjM4NTdlNjllNmY3NzAzYSJ9fX0=",
            "cmd": 1399
        }
    },
    "Large Obsidian": {
        "forge": "Onyx",
        "sell": 6000,
        "museum": (2, 2, 8),
        "rarity": Rarity.Epic,
        "item": {
            "id": "obsidian",
            "cmd": 1402
        }
    },
    "Onyx": {
        "forge": "Refined Onyx",
        "museum": (2, 2, 9),
        "rarity": Rarity.Epic,
        "lore": ["A small, gray-black gem."],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZjVkYjU2NDMwMGY5Y2Q2Njc4NTIwMDc5OWJlZjg5ODk0ZGMzYzM2Yjk3MjcyMmI3ODJjZGE3ZDljOTI4YjE5MSJ9fX0=",
            "cmd": 1404
        }
    },
    "Refined Onyx": {
        "forge": "Perfect Onyx",
        "museum": (2, 3, 1),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTg4YmNlNDk3Y2ZhNWY2MTE4MzlmNmRhMjFjOTVkMzRlM2U3MjNjMmNjNGMzYzMxOWI1NjI3NzNkMTIxNiJ9fX0=",
            "cmd": 1405
        }
    },
    "Perfect Onyx": {
        "sell": 1000000,
        "museum": (2, 3, 2),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzhjZWI4NjMxYWRkN2NiYjU2NWRjYjcwNWYxMjEyMzQ5Y2NjZDc1NTk2NWM0NmE5MjI4NTJjOWZkOTQ4YjRiYiJ9fX0=",
            "cmd": 1406
        }
    },

    "Oil Bucket": {
        "obtain": [
            "Mine [Sand (Block)] with an [Oil Pump] or [Turbo Oil Pump] with a [Bucket] in your hotbar."
        ],
        "sell": 3000,
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmNlMDRiNDFkMTllYzc5MjdmOTgyYTYzYTk0YTNkNzlmNzhlY2VjMzMzNjMwNTFmZGUwODMxYmZhYmRiZCJ9fX0=",
            "cmd": 1615
        }
    },

    "Oil Pump": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Electric Circuit"] * 3,
                ["Impure Lead", "Vacuum Tube", "Impure Lead"],
                [None, "Lead Ingot", None]
            ]
        },
        "rarity": Rarity.Rare,
        "mining speed": 1,
        "item": {
            "id": "hopper",
            "cmd": 1617
        }
    },
    "Turbo Oil Pump": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Vacuum Tube"] * 3,
                ["Impure Lead", "Oil Pump", "Impure Lead"],
                ["Impure Palladium", "Advanced Circuit", "Impure Palladium"]
            ]
        },
        "rarity": Rarity.Epic,
        "mining speed": 30,
        "item": {
            "id": "hopper",
            "enchanted": True,
            "cmd": 1618
        }
    },

    "Oinx": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                ["Blood"] * 3,
                ["Pig Steel", "Onyx", "Pig Steel"],
                ["Blood"] * 3
            ]
        },
        "museum": (8, 1, 1),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZWY5ZDc2ZGNjNTcxOTE4ZWJmYmM0NDljZGQ5YzIzMWQzZjc4MTg4NDE2ZGY5MTk3MWFlMmM5MTc5NGIwOWY0ZCJ9fX0=",
            "cmd": 1732
        }
    },

    "Old Lantern Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Wood", "Iron Ingot", "Wood"],
                ["Wood", "Skin Core", "Wood"],
                ["Wood", "Gold Ingot", "Wood"]
            ]
        },
        "museum": (9, 1, 5),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTgzMmRiN2Q3YTg4ZmY2ODc0N2JjYjU1ZDcyZDNjMWZhY2QzZDM4OWMxNDRmNDI2NGJmZTg5OTMwNDhkMDA2ZiJ9fX0=",
            "cmd": 1859
        }
    },

    "Omega Alloy": {
        "craft": {
            "tier": CraftTier.Crafting3,
            "recipe": [
                ["Topaz", "Arkenstone Fragment", "Topaz"],
                ["Void Alloy", "Omega Shard", "Adamantium"],
                ["Pig Steel", "Gold Block", "Celestial Ingot"]
            ]
        },
        "sell": 500000,
        "museum": (4, 3, 8),
        "rarity": Rarity.Exotic,
        "item": {
            "id": "gold_ingot",
            "enchanted": True,
            "cmd": 1545
        }
    },

    "Omega Cutter": {
        "craft": {
            "tier": CraftTier.Crafting3,
            "recipe": [
                [None, "Omega Alloy", None],
                ["Omega Shard", "Void Cutter+", "Omega Shard"],
                [None, "Gold Block", None]
            ]
        },
        "rarity": Rarity.Exotic,
        "mining speed": 25,
        "breaking power": 8,
        "lore": ["The end of the journey."],
        "item": {
            "id": "golden_axe",
            "cmd": 1540
        }
    },

    "Omega Helmet": {
        "craft": {
            "tier": CraftTier.Crafting3,
            "recipe": [
                ["Voidwalker Helmet", "Omega Alloy", None],
                [None] * 3,
                [None] * 3
            ]
        },
        "rarity": Rarity.Exotic,
        "item": {
            "id": "player_head",
            "value": "ewogICJ0aW1lc3RhbXAiIDogMTY0MzEzMTM0MDUwNiwKICAicHJvZmlsZUlkIiA6ICIxNmFkYTc5YjFjMDk0MjllOWEyOGQ5MjgwZDNjNjE5ZiIsCiAgInByb2ZpbGVOYW1lIiA6ICJMYXp1bGl0ZV9adG9uZSIsCiAgInNpZ25hdHVyZVJlcXVpcmVkIiA6IHRydWUsCiAgInRleHR1cmVzIiA6IHsKICAgICJTS0lOIiA6IHsKICAgICAgInVybCIgOiAiaHR0cDovL3RleHR1cmVzLm1pbmVjcmFmdC5uZXQvdGV4dHVyZS8xMzljNWUwNWE4N2JlNjE0NGM4ZGNhNzM2NzI5NDFjMjcwNjViOTM0ZGI4MjA5YjZhMTFhYzFhN2ExOTQyYTRmIiwKICAgICAgIm1ldGFkYXRhIiA6IHsKICAgICAgICAibW9kZWwiIDogInNsaW0iCiAgICAgIH0KICAgIH0KICB9Cn0=",
            "cmd": 1541
        }
    },
    "Omega Cuirass": {
        "craft": {
            "tier": CraftTier.Crafting3,
            "recipe": [
                ["Voidwalker Chestplate", "Omega Alloy", "Nether Miner's Chestplate"],
                [None] * 3,
                [None] * 3
            ]
        },
        "rarity": Rarity.Exotic,
        "item": {
            "id": "golden_chestplate",
            "cmd": 1542
        }
    },
    "Omega Leggings": {
        "craft": {
            "tier": CraftTier.Crafting3,
            "recipe": [
                ["Voidwalker Leggings", "Omega Alloy", None],
                [None] * 3,
                [None] * 3
            ]
        },
        "rarity": Rarity.Exotic,
        "item": {
            "id": "golden_leggings",
            "cmd": 1543
        }
    },
    "Omega Atmoboots": {
        "craft": {
            "tier": CraftTier.Crafting3,
            "recipe": [
                ["Voidwalker Aeroboots", "Omega Alloy", None],
                [None] * 3,
                [None] * 3
            ]
        },
        "use": [
            "Reduces void damage",
            "Gives +12.5% mining speed",
            "Gives slow falling",
            "Gives +10% movement speed"
        ],
        "rarity": Rarity.Exotic,
        "item": {
            "id": "golden_boots",
            "cmd": 1544
        }
    },

    "Omega Shard": {
        "sell": 100000,
        "museum": (4, 3, 7),
        "rarity": Rarity.Exotic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTQ1ZjQ3ZmViNGQ3NWNiMzMzOTE0YmZkYjk5OWE0ODljOWQwZTMyMGQ1NDhmMzEwNDE5YWQ3MzhkMWUyNGI5In19fQ==",
            "cmd": 1539
        }
    },

    "Ominescence Eye": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Silica", "Gemstone Mixture", "Silica"],
                ["Omega Shard", "Hat of Ominescence", "Omega Shard"],
                ["Gold Ingot", "Honey", "Gold Ingot"]
            ]
        },
        "accessory": {
            "use": "Reveals Tier 3 crafting recipes.",
            "slots": 1
        },
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjU5MzYzZDA3Y2IxODI2MDZhNmFmMTZiMjI5YWU2N2Y1NWI5ODVjYTYyYmVkODIyMmFlODA1MWM5MmY4ODA2NCJ9fX0=",
            "cmd": 1762
        }
    },

    "Ominous Egg": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Bone", "Ancient Skull", "Bone"],
                ["Ancient Tooth", "Mosquito Amber", "Ancient Tooth"],
                ["Bone", "Soul", "Bone"]
            ]
        },
        "museum": (4, 2, 5),
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYWU4NjljZGNhMzc1MTFlZGZhZjZlYmY4YTI0MzI0Yzk3ZmFhNmUxYTI1ZjFmODY4NjcxNjM4OWVkMDQwNmQ4OSJ9fX0=",
            "cmd": 1434
        }
    },

    "Orichalcum Chips": {
        "forge": "Orichalcum Scrap",
        "sell": 100,
        "museum": (6, 4, 9),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "melon_seeds",
            "cmd": 1691
        }
    },
    "Orichalcum Scrap": {
        "forge": "Orichalcum Shards",
        "sell": 350,
        "rads": 0.02,
        "museum": (7, 1, 1),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "warped_button",
            "cmd": 1692
        }
    },
    "Orichalcum Shards": {
        "forge": "Orichalcum Piece",
        "sell": 1000,
        "rads": 0.07,
        "museum": (7, 1, 2),
        "rarity": Rarity.Rare,
        "item": {
            "id": "prismarine_crystals",
            "cmd": 1693
        }
    },
    "Orichalcum Piece": {
        "forge": "Orichalcum Lump",
        "sell": 3500,
        "rads": 0.12,
        "museum": (7, 1, 3),
        "rarity": Rarity.Rare,
        "item": {
            "id": "prismarine_shard",
            "cmd": 1694
        }
    },
    "Orichalcum Ore": {
        "forge": "Orichalcum Lump",
        "sell": 5000,
        "museum": (7, 1, 4),
        "rarity": Rarity.Epic,
        "item": {
            "id": "firework_star",
            "color": "253192",
            "cmd": 1695
        }
    },
    "Orichalcum Lump": {
        "forge": "Impure Orichalcum",
        "sell": 8000,
        "rads": 0.3,
        "museum": (7, 1, 5),
        "rarity": Rarity.Epic,
        "item": {
            "id": "light_blue_dye",
            "cmd": 1696
        }
    },
    "Impure Orichalcum": {
        "forge": "Orichalcum",
        "sell": 12000,
        "rads": 0.45,
        "museum": (7, 1, 6),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzBhYzk5YTgwNzQ4OGRlNjBiNTMyMDNmZWUyZGYzOTg1NjliYmYwNGRiYzhjMDJiZmE3NDk3ODFjYWEyYmYyMCJ9fX0=",
            "cmd": 1697
        }
    },
    "Orichalcum": {
        "forge": "Orichalcum Ingots",
        "sell": 20000,
        "rads": 0.6,
        "museum": (7, 1, 7),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "diamond",
            "cmd": 1698
        }
    },
    "Orichalcum Ingots": {
        "sell": 30000,
        "museum": (7, 1, 8),
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTNlYzU5NWU2MzMwOWJiNTA1NjhjOWMyM2M5YjVlYjFkZjdjMmJiMzM5OTExYzQxOTY0MTIyYmYzYzEzMzRjYiJ9fX0=",
            "cmd": 1699
        }
    },

    "Orichalcum Drill": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Orichalcum Piece", "Orichalcum Piece", None],
                ["Electric Circuit", "Orichalcum Lump", "Orichalcum Pickaxe"],
                ["Orichalcum Piece", "Orichalcum Piece", None]
            ]
        },
        "rarity": Rarity.Legendary,
        "mining speed": 22.5,
        "breaking power": 7,
        "depth": 80,
        "item": {
            "id": "leather_horse_armor",
            "color": "00FFFF",
            "cmd": 1787
        }
    },
    "Pristine Orichalcum Drill": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Processing Unit", "Lead Plate", "Orichalcum Lump"],
                ["Battery", "Orichalcum Drill", "Impure Orichalcum"],
                ["Hematite", "Omega Alloy", "Orichalcum Lump"]
            ]
        },
        "rarity": Rarity.Mythic,
        "mining speed": 28,
        "breaking power": 8,
        "depth": 90,
        "item": {
            "id": "diamond_horse_armor",
            "cmd": 1788
        }
    },

    "Orichalcum Pick": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Orichalcum Shards", "Orichalcum Piece", "Orichalcum Shards"],
                [None, "Gold Rod", None],
                [None, "Gold Rod", None]
            ]
        },
        "rarity": Rarity.Epic,
        "mining speed": 15,
        "breaking power": 6,
        "depth": 65,
        "item": {
            "id": "diamond_hoe",
            "cmd": 1728
        }
    },

    "Orichalcum Pickaxe": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Orichalcum Pick", "Waterproof Glue", "Orichalcum Piece"],
                [None, "Sulfur", None],
                [None] * 3
            ]
        },
        "rarity": Rarity.Epic,
        "mining speed": 20,
        "breaking power": 6,
        "depth": 70,
        "item": {
            "id": "diamond_pickaxe",
            "cmd": 1729
        }
    },

    "Overclocker": {
        "obtain": [
            "If the [Strange Construct] accessory is equipped, there is a 1/3 chance for a [Sage Crystal] drop to change into this."
        ],
        "rarity": Rarity.Godly,
        "item": {
            "id": "structure_void",
            "enchanted": True,
            "cmd": 1862
        }
    },

    "Oxycoral": {
        "sell": 800,
        "obtain": [
            "The water mine shop offers this for $1,800."
        ],
        "museum": (6, 4, 4),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "tube_coral",
            "cmd": 1704
        }
    },

    "Oxygen Bottle": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Empty Bottle", "Oxycoral", None],
                [None] * 3,
                [None] * 3
            ]
        },
        "rarity": Rarity.Common,
        "item": {
            "id": "potion",
            "color": "FFFFFF",
            "cmd": 1673
        }
    },

    "Oxygen Compressor": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Orichalcum Piece", "Oxycoral", "Orichalcum Piece"],
                ["Oxycoral", "Engine", "Oxycoral"],
                ["Orichalcum Piece", "Oxycoral", "Orichalcum Piece"]
            ]
        },
        "module": {
            "use": "Uses suit charge to generate air",
            "slots": 2
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTExM2VlNjEwODQxZGVkMjE1YWNkMmI0Y2FhZWVmODdkZmQ2ZTNkNDc2OGU3YWI0ZTE5ZWI3NmIzZDgxMjFjZiJ9fX0=",
            "cmd": 1866
        }
    },

    "Oxygen Tank Module": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Orichalcum Piece", "Impure Aluminium", "Orichalcum Piece"],
                ["Impure Aluminium", "Oxycoral", "Impure Aluminium"],
                ["Orichalcum Piece", "Impure Aluminium", "Orichalcum Piece"]
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDU5ZGU1NjExN2I5NzU4MzlkNDA0YTUyNTc5ZDYzYTA0NDFiOWUzM2JkNTdhMzA0MmU3ZDRjYWZhYWQ2N2ZmOCJ9fX0=",
            "cmd": 1789
        }
    },
    "Oxygen Tank Module MK2": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Copper Ingot", "Oxygen Tank Module", "Copper Ingot"],
                ["Glass", "Orichalcum", "Glass"],
                ["Copper Ingot", "Oxygen Tank Module", "Copper Ingot"]
            ]
        },
        "module": {
            "use": "Gives +30 oxygen capacity",
            "slots": 4
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTFmNDM3YmQ5NzU0ZjM4NmUyNzY4N2RhYjdmNzYxZmQyM2YxNGJmM2E1ODM1MzY1ZDZiOTM4Yzk1MzEwYjE0NSJ9fX0=",
            "cmd": 1790
        }
    },

    "Palladium Ore": {
        "forge": "Impure Palladium",
        "sell": 2500,
        "museum": (5, 4, 5),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "firework_star",
            "color": "EB8844",
            "cmd": 1633
        }
    },
    "Impure Palladium": {
        "forge": "Palladium Ingot",
        "sell": 80000,
        "museum": (5, 4, 6),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzA3MmU0MmM1OGM2ZTljODhjZmI0ZGFhNmM2ZjRkMzdiNWE2YTg2NGMxMzU1MDhmOGY0ZmZiYzcyN2UxYTcifX19",
            "cmd": 1634
        }
    },
    "Palladium Ingot": {
        "museum": (5, 4, 7),
        "rarity": Rarity.Rare,
        "item": {
            "id": "brick",
            "cmd": 1635
        }
    },

    "Pebble": {
        "forge": "Stone Chunk",
        "sell": 2,
        "museum": (1, 1, 1),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "stone_button",
            "cmd": 1344
        }
    },
    "Stone Chunk": {
        "forge": "Cobblestone Chunk",
        "sell": 15,
        "museum": (1, 3, 1),
        "rarity": Rarity.Common,
        "item": {
            "id": "firework_star",
            "cmd": 1345
        }
    },
    "Cobblestone Chunk": {
        "forge": "Compressed Stone",
        "sell": 15,
        "museum": (4, 2, 9),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZGMxNzU0ODUxZTM2N2U4YmViYTJhNmQ4ZjdjMmZlZGU4N2FlNzkzYWM1NDZiMGYyOTlkNjczMjE1YjI5MyJ9fX0=",
            "cmd": 1346
        }
    },
    "Andesite Chunk": {
        "forge": "Compressed Stone",
        "sell": 18,
        "museum": (4, 3, 1),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYWRiN2JmMDU5YTYyZDI3YjFlMWUyZjM0Mzk0ZjNmMzhlZDhjZGE0NTQ3MWY2ZjRkNWI0N2MzOTEyZDE4MTEzNSJ9fX0=",
            "cmd": 1347
        }
    },
    "Compressed Stone": {
        "forge": "Huge Compressed Stone",
        "sell": 100,
        "museum": (1, 3, 2),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmNlY2M4NDM4ODYyZjE5MThiZmRkYzVhNTE2YzlkYmUwNzZiZDM3ZTdmYTVhYzE3OGMyZWM2NzE4MWUzZWFiYyJ9fX0=",
            "cmd": 1348
        }
    },
    "Huge Compressed Stone": {
        "forge": "Hypercompact Stone",
        "sell": 550,
        "museum": (1, 3, 3),
        "rarity": Rarity.Common,
        "item": {
            "id": "polished_andesite",
            "cmd": 1352
        }
    },
    "Hypercompact Stone": {
        "forge": "Synthetic Diamond",
        "sell": 3000,
        "museum": (1, 3, 4),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTE1M2M4Njk1YTExOGQzYmQzZGQ1MmUyNGI3MmU2MWJiYWI4ZmNjYjU3ZmVkNTQyZWFiZmYyNTkxMDdlZmU1YSJ9fX0=",
            "cmd": 1374
        }
    },
    "Synthetic Diamond": {
        "forge": "Perfect Diamond",
        "museum": (1, 3, 5),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTUwNjQ5NjI2YzQxMDEzNTJjNTk5NWM1M2I0OGJmZjYwYTkzODIxMmI3Y2U5MDI0MTVmZWI3NmVhMjczYjM1ZiJ9fX0=",
            "cmd": 1376
        }
    },
    "Perfect Diamond": {
        "sell": 100000,
        "museum": (1, 3, 6),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGU5M2ViYWNiNjBiNzE3OTMzNTVmZGUwZDRiYmE0M2E5YzVlYzA5YzNmMzg4OTdjNDhjMWY4NTc1MjNhMGEyOSJ9fX0=",
            "cmd": 1378
        }
    },

    "Personal Battery": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Impure Lead", "Sulfur", "Impure Lead"],
                ["Battery"] * 3,
                ["Impure Aluminium", "Electric Circuit", "Impure Aluminium"]
            ]
        },
        "module": {
            "use": "Allows modular gear to store and supply electric energy",
            "slots": 0
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzc2N2EwY2FjZGQ3MzE2ZDQwZTY5ZjZiYjkyM2NiNmI4YmYyZDgyNDk5MThkOGQxYjk0ZjJiZjQ2OWQ1Y2VmYyJ9fX0=",
            "cmd": 1636
        }
    },

    "Personal Solar Generator": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Solar Cell", "Glass", "Solar Cell"],
                ["Aluminium Ingot", "Ferrosilicon", "Aluminium Ingot"],
                ["Electric Circuit", "Battery", "Electric Circuit"]
            ]
        },
        "module": {
            "use": "Charges modular gear during the day on the surface",
            "slots": 0
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzRmZTEzNWMzMTFmNzA4NmVkY2M1ZTZkYmM0ZWY0YjIzZjgxOWZkZGFhNDJmODI3ZGFjNDZlMzU3NGRlMjI4NyJ9fX0=",
            "cmd": 1637
        }
    },

    "Pig Steel": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Bacon", "Blood", "Bacon"],
                ["Bacon", "Steel", "Bacon"],
                ["Bacon", "Blood", "Bacon"]
            ]
        },
        "museum": (3, 2, 6),
        "rarity": Rarity.Epic,
        "item": {
            "id": "brick",
            "cmd": 1472
        }
    },

    "Plastic Sheet": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Oil Bucket"] * 3,
                ["Oil Bucket", "Salt", "Oil Bucket"],
                ["Oil Bucket"] * 3
            ]
        },
        "sell": 15000,
        "rarity": Rarity.Rare,
        "item": {
            "id": "paper",
            "cmd": 1616
        }
    },

    "Plutonium Ore": {
        "forge": "Plutonium",
        "sell": 5000,
        "rads": 1.5,
        "museum": (6, 1, 6),
        "rarity": Rarity.Epic,
        "item": {
            "id": "firework_star",
            "color": "ABABAB",
            "cmd": 1650
        }
    },
    "Plutonium": {
        "sell": 30000,
        "rads": 7,
        "museum": (6, 1, 7),
        "rarity": Rarity.Epic,
        "item": {
            "id": "phantom_membrane",
            "cmd": 1651
        }
    },

    "Plutonium-239": {
        "craft": {
            "tier": CraftTier.Tech2,
            "recipe": [
                ["Plutonium", "Battery", "Plutonium"],
                ["Plutonium", "Water Core", "Plutonium"],
                ["Cobalt", "Lead Plate", "Palladium Ore"]
            ]
        },
        "rads": 20,
        "museum": (6, 1, 8),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzg0YjE1Y2U2YmMwZmUyYmIxNTY0ZTM1MGVkMTczZjJlNDkwY2NkNWZkNGE2N2FhM2ViMjEyYTgzNThiNzgzNiJ9fX0=",
            "cmd": 1652
        }
    },

    "Potion of Abundance I": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipe": [
                [None, "Anthracite", None],
                [None, "Iron Ore", None],
                [None, "Water Bottle", None]
            ]
        },
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "potion",
            "color": "74C4CC",
            "cmd": 1817
        }
    },
    "Potion of Abundance II": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipe": [
                [None, "Netherite Scrap", None],
                [None, "Iron Ingot", None],
                [None, "Potion of Abundance I", None]
            ]
        },
        "use": [
            "+50% to double drops from breaking blocks"
        ],
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "potion",
            "color": "31BECC",
            "cmd": 1818
        }
    },
    "Potion of Abundance III": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipe": [
                [None, "Hypercompact Stone", None],
                ["Boron Nitride", "Sulfur", "Boron Nitride"],
                [None, "Water Bottle", None]
            ]
        },
        "use": [
            "+75% to double drops from breaking blocks"
        ],
        "rarity": Rarity.Rare,
        "item": {
            "id": "potion",
            "color": "1FAECC",
            "cmd": 1819
        }
    },
    "Potion of Abundance IV": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipe": [
                [None, "Magnesium Ingot", None],
                ["Wurtzite Boron Nitride", "Adamantium Scraps", "Wurtzite Boron Nitride"],
                [None, "Honey", None]
            ]
        },
        "use": [
            "+100% to double drops from breaking blocks"
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "potion",
            "color": "00C1FF",
            "cmd": 1820
        }
    },

    "Potion of Cheating": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipe": [
                [None, "Amethyst", None],
                [None, "Mustache Polish", None],
                [None, "Water Bottle", None]
            ]
        },
        "use": [
            "Doubles Waluigi Ticket drops"
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "potion",
            "color": "9600FF",
            "cmd": 1805
        }
    },

    "Potion of Fortune": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipe": [
                [None] * 3,
                [None, "Clover", None],
                [None, "Water Bottle", None]
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "potion",
            "color": "007800",
            "cmd": 1802
        }
    },
    "Potion of Fortune II": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipe": [
                [None] * 3,
                ["Clover", "Gold Ore", "Clover"],
                [None, "Potion of Fortune", None]
            ]
        },
        "use": [
            "+100% luck"
        ],
        "rarity": Rarity.Rare,
        "item": {
            "id": "potion",
            "color": "00A000",
            "cmd": 1803
        }
    },

    "Potion of Haste": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipe": [
                [None] * 3,
                [None, "Golden Grass", None],
                [None, "Water Bottle", None]
            ]
        },
        "use": [
            "+20% mining speed"
        ],
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "potion",
            "color": "FFFF00",
            "cmd": 1799
        }
    },
    "Potion of Haste II": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipe": [
                [None, "Earth Crystal", None],
                ["Iron Ore", "Anthracite", "Iron Ore"],
                [None, "Potion of Haste", None]
            ]
        },
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "potion",
            "color": "FFC800",
            "cmd": 1806
        }
    },
    "Potion of Haste III": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipe": [
                [None, "Graphite", None],
                ["Amber", "Gold Ingot", "Amber"],
                [None, "Potion of Haste II", None]
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "potion",
            "color": "FF9600",
            "cmd": 1807
        }
    },

    "Power Helmet": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Impure Aluminium", "Advanced Circuit", "Impure Aluminium"],
                ["Lead Ingot", "Modular Helmet", "Lead Ingot"],
                ["Impure Palladium", "Lead Helmet", "Impure Palladium"]
            ]
        },
        "rarity": Rarity.Godly,
        "modular": {
            "slots": 5,
            "capacity": 12
        },
        "use": [
            "Gives +5% mining speed",
            "Gives +1 radiation resistance"
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTUzZjdlOGYxYzQ5MWRiN2RlZjNlOTM3NjAyNDFhMzI4NDVkYmEzMzMyZGQ2ZmFiMDEzYjE2YmVmMGFiMzQ1MiJ9fX0=",
            "cmd": 1597
        }
    },
    "Power Chestplate": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Impure Aluminium", "Advanced Circuit", "Impure Aluminium"],
                ["Lead Ingot", "Modular Chestplate", "Lead Ingot"],
                ["Impure Palladium", "Lead Chestplate", "Impure Palladium"]
            ]
        },
        "rarity": Rarity.Godly,
        "modular": {
            "slots": 5,
            "capacity": 12
        },
        "use": [
            "Gives +5% mining speed",
            "Gives +1 radiation resistance"
        ],
        "item": {
            "id": "leather_chestplate",
            "color": "FF6E00",
            "cmd": 1598
        }
    },
    "Power Leggings": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Impure Aluminium", "Advanced Circuit", "Impure Aluminium"],
                ["Lead Ingot", "Modular Leggings", "Lead Ingot"],
                ["Impure Palladium", "Lead Leggings", "Impure Palladium"]
            ]
        },
        "rarity": Rarity.Godly,
        "modular": {
            "slots": 5,
            "capacity": 12
        },
        "use": [
            "Gives +5% mining speed",
            "Gives +1 radiation resistance"
        ],
        "item": {
            "id": "leather_leggings",
            "color": "FF5000",
            "cmd": 1599
        }
    },
    "Power Boots": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Impure Aluminium", "Advanced Circuit", "Impure Aluminium"],
                ["Lead Ingot", "Modular Boots", "Lead Ingot"],
                ["Impure Palladium", "Lead Boots", "Impure Palladium"]
            ]
        },
        "rarity": Rarity.Godly,
        "modular": {
            "slots": 5,
            "capacity": 12
        },
        "use": [
            "Gives +5% mining speed",
            "Gives +1 radiation resistance"
        ],
        "item": {
            "id": "leather_boots",
            "color": "FF3200",
            "cmd": 1600
        }
    },

    "Power Helmet MK2": {
        "craft": {
            "tier": CraftTier.Tech2,
            "recipe": [
                ["Aluminium Ingot", "Processing Unit", "Aluminium Ingot"],
                ["Engine", "Power Helmet", "Plastic Sheet"],
                ["Cobalt", "Thick Lead Helmet", "Plutonium"]
            ]
        },
        "rarity": Rarity.Exotic,
        "modular": {
            "slots": 8,
            "capacity": 21
        },
        "use": [
            "Gives +10% mining speed",
            "Gives +3 radiation resistance"
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODVlY2IxZjQ4MGUwNmUzOTlkNTY3ZTU4NWY3ODdjZWQzMjRkYmYxODM3ZGRlYTZlNmMyODFkZGU4YzI1NiJ9fX0=",
            "cmd": 1668
        }
    },
    "Power Chestplate MK2": {
        "craft": {
            "tier": CraftTier.Tech2,
            "recipe": [
                ["Aluminium Ingot", "Processing Unit", "Aluminium Ingot"],
                ["Engine", "Power Chestplate", "Plastic Sheet"],
                ["Cobalt", "Thick Lead Chestplate", "Plutonium"]
            ]
        },
        "modular": {
            "slots": 8,
            "capacity": 21
        },
        "use": [
            "Gives +10% mining speed",
            "Gives +3 radiation resistance"
        ],
        "rarity": Rarity.Exotic,
        "item": {
            "id": "leather_chestplate",
            "color": "FF3C00",
            "cmd": 1669
        }
    },
    "Power Leggings MK2": {
        "craft": {
            "tier": CraftTier.Tech2,
            "recipe": [
                ["Aluminium Ingot", "Processing Unit", "Aluminium Ingot"],
                ["Engine", "Power Leggings", "Plastic Sheet"],
                ["Cobalt", "Thick Lead Leggings", "Plutonium"]
            ]
        },
        "modular": {
            "slots": 8,
            "capacity": 21
        },
        "use": [
            "Gives +10% mining speed",
            "Gives +3 radiation resistance"
        ],
        "rarity": Rarity.Exotic,
        "item": {
            "id": "leather_leggings",
            "color": "FF3C50",
            "cmd": 1670
        }
    },
    "Power Boots MK2": {
        "craft": {
            "tier": CraftTier.Tech2,
            "recipe": [
                ["Aluminium Ingot", "Processing Unit", "Aluminium Ingot"],
                ["Engine", "Power Boots", "Plastic Sheet"],
                ["Cobalt", "Thick Lead Boots", "Plutonium"]
            ]
        },
        "modular": {
            "slots": 8,
            "capacity": 21
        },
        "use": [
            "Gives +10% mining speed",
            "Gives +3 radiation resistance"
        ],
        "rarity": Rarity.Exotic,
        "item": {
            "id": "leather_boots",
            "color": "FF006E",
            "cmd": 1671
        }
    },

    "Pot of Gold": {
        "obtain": [
            "A random drop from presents."
        ],
        "sell": 15000,
        "museum": (3, 4, 3),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTRhZWFiMDFjMDRmMzZiYTg4N2I3YmRhOGQ5YzUzOGJjOTY4NmRiYmNlN2UzYTViYjEwZjMwOGM1MDMwMmJjNCJ9fX0=",
            "cmd": 1502
        }
    },

    "Potato": {
        "forge": "Baked Potato",
        "sell": 500,
        "museum": (4, 3, 3),
        "rarity": Rarity.Common,
        "item": {
            "id": "potato",
            "cmd": 1532
        }
    },
    "Baked Potato": {
        "forge": "Burning Potato",
        "sell": 2500,
        "museum": (4, 3, 4),
        "rarity": Rarity.Common,
        "item": {
            "id": "baked_potato",
            "cmd": 1533
        }
    },
    "Burning Potato": {
        "sell": 2,
        "museum": (4, 3, 5),
        "rarity": Rarity.Common,
        "item": {
            "id": "blaze_powder",
            "cmd": 1534
        }
    },

    "Present": {
        "museum": (3, 4, 4),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzc4NGVmZTc1Yzc4NmJhNzQ3MzFmNTVkMDE2ZjM5ODAwMzM0Y2I5OTQ1ZWQ0M2NhYWMxNTBiZTc5YTc3ZDU1YSJ9fX0=",
            "cmd": 1497
        }
    },
    "Black Present": {
        "museum": (3, 4, 5),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmUwYzdhZjU5MWJkMTMzNzk0NGFiZmFjNTJiOWJjZjg4MzUyOGRiNzJhYWNiNmRiYzRlZGQ1NmE4MDM2NjdmNCJ9fX0=",
            "cmd": 1498
        }
    },
    "Gold Present": {
        "museum": (3, 4, 6),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmNhYWQ4NmM3MDhlYjI3NzczYTY0ZjkzNDc5ZTM5ZjA0NDJhNWNlMDg2YjYzMjk2YzdiN2QxY2Y1MTE2MDk1NiJ9fX0=",
            "cmd": 1499
        }
    },

    "Processing Unit": {
        "craft": {
            "tier": CraftTier.Tech2,
            "recipe": [
                ["Advanced Circuit", "Electric Circuit", "Advanced Circuit"],
                ["Sulfuric Acid", "Cobalt", "Sulfuric Acid"],
                ["Plastic Sheet", "Steel", "Plastic Sheet"]
            ]
        },
        "rarity": Rarity.Mythic,
        "item": {
            "id": "filled_map",
            "color": "0000B4",
            "cmd": 1613
        }
    },

    "Pumpkin": {
        "forge": "Compressed Pumpkin",
        "sell": 400,
        "museum": (8, 2, 4),
        "rarity": Rarity.Rare,
        "item": {
            "id": "pumpkin",
            "cmd": 1830
        }
    },
    "Compressed Pumpkin": {
        "forge": "Exquisite Pumpkin",
        "sell": 2500,
        "museum": (8, 2, 5),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMWE4NTk4YjQ2OWE5OWNhZDA2MDBlMjk4YWEyNjBjZThjN2M2YmM0ZGJhMzgyNmRkOWJhNjI2ODQ1NDhkMzc5OCJ9fX0=",
            "cmd": 1831
        }
    },
    "Exquisite Pumpkin": {
        "forge": "Jack O'Lantern",
        "sell": 15000,
        "museum": (8, 2, 6),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDlmNmY3Yjk2MDVkZmYzMjg3NTg0NzUxODFjZjMyNTBhZjFiMGVjNjc5Zjg5YzVjNWY5MjM2YjY0NWMyNTUwIn19fQ==",
            "cmd": 1832
        }
    },
    "Jack O'Lantern": {
        "forge": "Golden Jack O'Lantern",
        "sell": 80000,
        "museum": (8, 2, 7),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTY4NGYxMTQ4MGMwZmM5NzQ4MGVkMWI3MGMyMzEzOWJiNGZjZDYxNmNjOTY3ZTZjNzc5YmExZDJlZDU1In19fQ==",
            "cmd": 1833
        }
    },
    "Golden Jack O'Lantern": {
        "forge": "Diamond Jack O'Lantern",
        "sell": 450000,
        "museum": (8, 2, 8),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTRhOTg5ZmFiNTUzZjM3OTE5MjYzOGY3MjU4OTMxM2Q5MTNmYzBiMzVlMGNjZjdiYWQwNzFkODcyNjA3ZWUzMSJ9fX0=",
            "cmd": 1834
        }
    },
    "Diamond Jack O'Lantern": {
        "forge": "Arkenpumpkin",
        "sell": 2000000,
        "museum": (8, 2, 9),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjhjZTRkMjY4OTU2YmY0NzA4NjNiMGM4NTk1ZGM1ZjA2OTRkNjA0YmNiYzg1OWU2ZTY2MThmYTMwMTJkMGUwYyJ9fX0=",
            "cmd": 1835
        }
    },
    "Arkenpumpkin": {
        "museum": (8, 3, 1),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzVkYTNhMWRjNGYyMzU5YzliMWU0M2Q5MjUzMTk2ZTZhYjVhMmQyNDg0N2EwMzg1N2NkN2I4M2Y2ODU0YWU1ZCJ9fX0=",
            "cmd": 1836
        }
    },

    "Pumpkin Seeds": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Pumpkin", None, None],
                [None] * 3,
                [None] * 3
            ]
        },
        "sell": 10,
        "museum": (8, 3, 2),
        "rarity": Rarity.Rare,
        "lore": [
            "Can be planted on grass.",
            "Will slowly grow into a pumpkin",
            "block that drops additional",
            "seeds when harvested. Pumpkins",
            "grow 2x as fast during rain."
        ],
        "item": {
            "id": "pumpkin_seeds",
            "cmd": 1829
        }
    },

    "Pumpkin Talisman": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["String", None, "String"],
                [None, "Exquisite Pumpkin", None],
                [None] * 3
            ]
        },
        "accessory": {
            "use": "Causes planted pumpkins to have a growth headstart of 3 stages",
            "slots": 2
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmQ2OWE3MGE3MzVjYTZiNGI0ODY1MmUzZTIzYTVkMTlkMTBiODcyNzZhNWEyNWVmNzNkYTNmNTY4YjIxZDJjIn19fQ==",
            "cmd": 1837
        }
    },

    "Quartz": {
        "forge": "Silica",
        "sell": 700,
        "museum": (2, 4, 3),
        "rarity": Rarity.Rare,
        "item": {
            "id": "quartz",
            "cmd": 1392
        }
    },
    "Silica": {
        "sell": 4000,
        "museum": (2, 4, 4),
        "rarity": Rarity.Rare,
        "item": {
            "id": "sugar",
            "cmd": 1393
        }
    },

    "QuikBackpack Access": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Ender Dust", "Obsidian", "Ender Dust"],
                ["Obsidian", "Large Backpack Core", "Obsidian"],
                ["Ender Dust", "Obsidian", "Ender Dust"]
            ]
        },
        "accessory": {
            "use": "Right-clicking backpacks in your inventory allows you to open them",
            "slots": 1
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTI5NGI4OTc5MTM2YjBmN2NlZTk5YjU1ZDMyNDJhM2M0M2QyYmMzOTU2MDg1ZTYxZTBhMTVkMTY4ZjNhZWE2NiJ9fX0=",
            "cmd": 1813
        }
    },

    "Radiation Shield Module": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Impure Lead", "Lead Ingot", "Impure Lead"],
                ["Electric Circuit"] * 3,
                ["Copper Wire", "Iron Ingot", "Copper Wire"]
            ]
        },
        "module": {
            "use": "Gives +3 radiation resistance",
            "slots": 2
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "iron_trapdoor",
            "cmd": 1590
        }
    },
    "Radiation Shield Module MK2": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Impure Lead", "Lead Plate", "Impure Lead"],
                ["Brick", "Radiation Shield Module", "Brick"],
                ["Impure Palladium", "Aluminium Ingot", "Impure Palladium"]
            ]
        },
        "module": {
            "use": "Gives +8 radiation resistance",
            "slots": 3
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "daylight_detector",
            "cmd": 1591
        }
    },

    "Red Herring": {
        "museum": (5, 2, 4),
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvY2VjOGZmNTc2NWQ3MmJhNmVhNzQzOTM4ZjAzM2E0NmFhMTlhZjYxMTkyNzhmZTIyN2E3YjZkNmJkZmYxOSJ9fX0=",
            "cmd": 1570
        }
    },

    "Reinforced Bedrock": {
        "museum": (7, 4, 6),
        "rarity": Rarity.Divine,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGEzYzNmOTY0OTkzNGI4ZmVlM2I1MWI1NTY1YWE2MTE2MGZkOWMxMGYyNTYyM2QxMjE5NThmYmU3NzI4NDdhIn19fQ==",
            "cmd": 1758
        }
    },
    
    "Ribcage": {
        "forge": "Bone Block",
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Bone", None, "Bone"],
                ["Bone"] * 3,
                ["Bone"] * 3
            ]
        },
        "rarity": Rarity.Common,
        "item": {
            "id": "chainmail_chestplate",
            "cmd": 1571
        }
    },
    "Bone Block": {
        "museum": (5, 2, 5),
        "rarity": Rarity.Common,
        "item": {
            "id": "bone_block",
            "cmd": 1572
        }
    },

    "RNG Talisman": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["String", "Gold Ingot", "String"],
                [None, "RNG Trophy", None],
                [None] * 3
            ]
        },
        "accessory": {
            "use": "+10% luck",
            "slots": 1
        },
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODRlMjRiZDAwZWYzYzEwYjU0NWVkN2JmZTc5YmM5ZTM5NDBiNDlkZjJhOTkwNjA3MjExZWE0MjAzMTIxOWMwYyJ9fX0=",
            "cmd": 1795
        }
    },

    "RNG Trophy": {
        "sell": 133700,
        "museum": (1, 1, 8),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTVkZmEyODRhYTE1MzI0ZTUxNzg1NjFmODAzZjU5NzYyMjhkOTUxMTU1ODNhYjAzMTI2NmFlMjRlZTFhOTlkMSJ9fX0=",
            "cmd": 1504
        }
    },

    "Rock Candy": {
        "obtain": [
            "Mining blocks in the stone/coal layer after consuming [Grapes of Jonathan] has a chance of dropping this."
        ],
        "museum": (8, 3, 4),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYTA4NDRkMjlkZWQ4ODZkN2NlYWFhMDI2NjRiZjEyZmUwNzkwZDU4Y2E3NWVmZGRjMTFjYTAxZTk0YTJhYzUwMSJ9fX0=",
            "cmd": 1840
        }
    },

    "Rockite": {
        "forge": "Rockite Chunk",
        "sell": 10,
        "museum": (7, 2, 3),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "firework_star",
            "cmd": 1710
        }
    },
    "Rockite Chunk": {
        "forge": "Processed Rockite",
        "museum": (7, 2, 4),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTNjOWYwZjczY2U1MzhmODY0ZmVhOWFjM2Q4ZGExODVjZDc0ZTRlZWY2NWRjNTVjMDdlYTgxNDUxZTM1YWU5YyJ9fX0=",
            "cmd": 1711
        }
    },
    "Processed Rockite": {
        "forge": "Compressed Rockite",
        "museum": (7, 2, 5),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvM2Q1MTJmMzI0ZDgzZTNmODU4YTVlMzk1MTBkMzdkZGE4ZWMzMWUzZmZkZjUxOTM2ZDFlMjNjYmYxMWZiNTY5ZCJ9fX0=",
            "cmd": 1712
        }
    },
    "Compressed Rockite": {
        "forge": "Hypercompact Rockite",
        "museum": (7, 2, 6),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTdhNGVhZWM1OWZjMjY5NzM3YTc2ZmExNjcxYzM3ODc1YzZhYjU1YTE0ODIxNzNiNTVmZWM1ZjgwYmM4ZWNhMiJ9fX0=",
            "cmd": 1713
        }
    },
    "Hypercompact Rockite": {
        "forge": "Hematite",
        "sell": 3500,
        "museum": (7, 2, 7),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOWUyYjA5MjRhYTJiNDI0ZTBmZjY2MTZhOTNjOGVmNDg3MDU3NzQ1YWYxYWE1Y2QyMjNjNTQxZWJkM2E2ODhhMyJ9fX0=",
            "cmd": 1714
        }
    },
    "Hematite": {
        "forge": "Refined Hematite",
        "sell": 10000,
        "museum": (7, 2, 8),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTg3OWVkMmIzOWZhMDQ2MmM3NDI5MmY1Y2EzZDE4ODQyMDEyOGI0YTYzYWM3NWRiOGM5N2EwOTRkMWFjNjNmNCJ9fX0=",
            "cmd": 1715
        }
    },
    "Refined Hematite": {
        "forge": "Perfect Hematite",
        "museum": (7, 2, 9),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmRiMjJiMGMyNjhhYTAxZDA4YWIyOWRjZTYyMTNkOGJmYmI0YTQzZmZmNDIyNDdlNzViZWU0MjNjZmE1NjhjZCJ9fX0=",
            "cmd": 1716
        }
    },
    "Perfect Hematite": {
        "sell": 250000,
        "museum": (7, 3, 1),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTExNWRjODhlMzIxNGMzODI0M2Q3ODJkNjNlZGIwYTZlMDYyOTFlYjZkYThlNjAwYzdlMmVhMzZlN2Y2MWIzMSJ9fX0=",
            "cmd": 1717
        }
    },

    "Rough Flint": {
        "forge": "Flint",
        "sell": 50,
        "museum": (6, 4, 6),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "charcoal",
            "cmd": 1700
        }
    },
    "Flint": {
        "forge": "Flint Edge",
        "sell": 500,
        "museum": (6, 4, 7),
        "rarity": Rarity.Common,
        "item": {
            "id": "flint",
            "cmd": 1701
        }
    },
    "Flint Edge": {
        "museum": (6, 4, 8),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "flint",
            "enchanted": True,
            "cmd": 1702
        }
    },

    "Royal Backpack Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Gold Ingot", "Refined Ruby", "Gold Ingot"],
                ["Refined Ruby", "Skin Core", "Refined Ruby"],
                ["Gold Ingot", "Huge Backpack Core", "Gold Ingot"]
            ]
        },
        "museum": (9, 1, 2),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDhjMWUxYzYyZGM2OTVlYjkwZmExOTJkYTZhY2E0OWFiNGY5ZGZmYjZhZGI1ZDI2MjllYmZjOWIyNzg4ZmEyIn19fQ==",
            "cmd": 1855
        }
    },

    "'Stache Orb": {
        "rarity": Rarity.Epic,
        "obtain": [
            "The @waluigi shop offers this for 35 Waluigi Tokens."
        ],
        "accessory": {
            "use": "+6% luck",
            "slots": 1
        },
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzYzNmYyNzI0YWE2YWE0ZGU3YWM0NmMxOWYzYzg0NWZiMTQ4NDdhNTE4YzhmN2UwM2Q3OTJjODJlZmZiMSJ9fX0=",
            "cmd": 1774
        }
    },

    "Sage Crystal": {
        "obtain": [
            "The @waluigi shop offers this for 30 Waluigi Tokens."
        ],
        "museum": (4, 3, 6),
        "rarity": Rarity.Mythic,
        "lore": [
            "Apply this on an item in an anvil",
            "to enhance it, without increasing",
            "its sell value. If applied onto gear,",
            "it gains +20% mining speed."
        ],
        "item": {
            "id": "end_crystal",
            "enchanted": True,
            "cmd": 1537
        }
    },

    "Salt": {
        "sell": 1500,
        "museum": (3, 1, 4),
        "rarity": Rarity.Common,
        "item": {
            "id": "sugar",
            "cmd": 1507
        }
    },

    "Sand": {
        "forge": "Sandstone",
        "sell": 6,
        "museum": (4, 4, 8),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNGY0OTNkZDgwNjUzM2Q5ZDIwZTg0OTUzOTU0MzY1ZjRkMzY5NzA5Y2ViYzlkZGVmMDIyZDFmZDQwZDg2YTY4ZiJ9fX0=",
            "cmd": 1556
        }
    },
    "Sandstone": {
        "forge": "Dense Sand",
        "sell": 25,
        "museum": (4, 4, 9),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDhmODBlOWIyZDY1OTNhMzJkN2M0NGM4YmM4NjBmZWJhMzRiMzRmOGQ1NGQwY2RiNzIxMWUyM2U4ZGRjMzNhNCJ9fX0=",
            "cmd": 1557
        }
    },
    "Dense Sand": {
        "forge": "Compressed Sand",
        "sell": 150,
        "museum": (5, 1, 1),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYTMxOTkzZTRjZmRhMTUzZWFmN2RjMTM4ZDUyYmJhNWMyODNkMDE2MzI2MDIyNjIxNjE3NzZmMGY0Yjg2YSJ9fX0=",
            "cmd": 1560
        }
    },
    "Compressed Sand": {
        "forge": "Hypercompact Sand",
        "museum": (5, 1, 2),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjI1MmZmNGM4ZjNhZDBiYmI2NWVlOTkyZTVkYjZjMjgxNDIxM2ZmN2E1M2NmZGY0M2NlNDM5Njk3MmE3OGY0NiJ9fX0=",
            "cmd": 1561
        }
    },
    "Hypercompact Sand": {
        "forge": "Sand Pearl",
        "museum": (5, 1, 3),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDM2ZTk4NjI4MzJhNmZjYzQ4NTVmYTc5YzFhYWU1ZTczYjkxOTdlYzZiYmQzOGY2MzEyZWZhYzY4MGM2MzI4NSJ9fX0=",
            "cmd": 1562
        }
    },
    "Sand Pearl": {
        "forge": "Perfect Pearl",
        "museum": (5, 1, 4),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjdlNmFkNGI3OGJkMzUxODdhNjU3MDg5OTE4MTdlMjY2OTlmOTAyYzc3MzhjODFjMzc1ODU5ZDcyNzUzOSJ9fX0=",
            "cmd": 1563
        }
    },
    "Perfect Pearl": {
        "sell": 200000,
        "museum": (5, 1, 5),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNDE0N2MyMGM0ZjM1YmQyN2QzZDQxOTEyNzkyYTc5OGU5ZjRmOWJiZmUwNGYwZDMyNTVkOWJjYWRmOGE0MWFhZSJ9fX0=",
            "cmd": 1564
        }
    },

    "Sandfish": {
        "sell": 500,
        "museum": (5, 1, 7),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTcwMDg3ZGRlMTMwODQ2YzBlOTc1ZmU2ODQzNWQ4OTQwZjA5MzM5ZmFiYzYwMjZhOTY5OWZkYjYxMmI0ZjEyMSJ9fX0=",
            "cmd": 1558
        }
    },

    "Sans Bone": {
        "obtain": [
            "Mining any block with the [sans] enchantment has a chance to drop this."
        ],
        "sell": 69,
        "museum": (5, 2, 6),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "bone",
            "enchanted": True,
            "cmd": 1573
        }
    },

    "Sans Ribcage": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Sans Bone", None, "Sans Bone"],
                ["Sans Bone", "Perfect Diamond", "Sans Bone"],
                ["Sans Bone"] * 3
            ]
        },
        "use": [
            "Swap hands (F) to teleport a short distance forwards"
        ],
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "chainmail_chestplate",
            "enchanted": True,
            "cmd": 1574
        }
    },

    "Serendipity Module": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Electric Circuit", "Starite", "Electric Circuit"],
                ["Starite", "Golden Clover Bag", "Starite"],
                ["Electric Circuit", "Starite", "Electric Circuit"]
            ]
        },
        "module": {
            "use": "+6% luck",
            "slots": 1
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjRhZjhkNTc1ZjBhNTI0ZWY2NmEyMTU3M2U4YTRhOGFjN2Q2NDBiMDBkOThlMmU5Mzc0ZTYwNDcwZTdjODZmMCJ9fX0=",
            "cmd": 1603
        }
    },

    "Shell": {
        "sell": 1000,
        "museum": (5, 1, 9),
        "rarity": Rarity.Rare,
        "item": {
            "id": "nautilus_shell",
            "cmd": 1565
        }
    },

    "Silver Trophy": {
        "obtain": [
            "A very rare drop from presents."
        ],
        "sell": 120000,
        "museum": (3, 3, 9),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDYyMzc5Y2U5YWIyYjczNzZiZmExOGIwMTY1NWIyZDU4Zjk1ODc1NzQwZjJkNDk3MmNjYjdlNDc4MTE0MSJ9fX0=",
            "cmd": 1509
        }
    },

    "Skin Core": {
        "obtain": [
            "The @waluigi shop offers this for 55 Waluigi Tokens."
        ],
        "museum": (8, 4, 3),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "firework_star",
            "color": "7B2FBE",
            "enchanted": True,
            "cmd": 1860
        }
    },

    "Slowfall Module": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Impure Aluminium", "Aluminium Ingot", "Impure Aluminium"],
                ["Electric Circuit", "Celestial Boots", "Electric Circuit"],
                ["Impure Aluminium", "Aluminium Ingot", "Impure Aluminium"]
            ]
        },
        "module": {
            "use": "Gives slow falling",
            "slots": 2
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZWZjMDVhZjBlODhjNmZiMTBiNGM4YzhiODFiN2FhNjU4ZTY0NjQ5NzI0Y2I3M2JiOWJiMGYyNWYyOGJkIn19fQ==",
            "cmd": 1210
        }
    },

    "Small Backpack": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Stone Chunk", "Plant Fibre", "Stone Chunk"],
                ["Plant Fibre", "Small Backpack Core", "Plant Fibre"],
                ["Stone Chunk", "Plant Fibre", "Stone Chunk"]
            ]
        },
        "use": [
            "Gives 5 extra inventory slots."
        ],
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmY2OGQ1MDliNWQxNjY5Yjk3MWRkMWQ0ZGYyZTQ3ZTE5YmNiMWIzM2JmMWE3ZmYxZGRhMjliZmM2ZjllYmYifX19",
            "cmd": 1421
        }
    },
    "Medium Backpack": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Compressed Stone", "Iron Ingot", "Compressed Stone"],
                ["Iron Ingot", "Medium Backpack Core", "Iron Ingot"],
                ["Compressed Stone", "Iron Ingot", "Compressed Stone"]
            ]
        },
        "use": [
            "Gives 9 extra inventory slots."
        ],
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvY2UyMjM5MWUzNWEzZTViY2VlODlkYjMxMmU4NzRmZGM5ZDllN2E2MzUxMzE0YjgyYmRhOTdmYmQyYmU4N2ViOCJ9fX0=",
            "cmd": 1422
        }
    },
    "Large Backpack": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Onyx", "Netherite Ingot", "Refined Ruby"],
                ["Graphene", "Large Backpack Core", "Hypercompact Stone"],
                ["Refined Ruby", "Netherite Ingot", "Onyx"]
            ]
        },
        "use": [
            "Gives 27 extra inventory slots."
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNmFlNGJlM2ZjNzg1ZjZjN2NjNzc3YzkzN2Y1YWRlOGZlOGQ3MWY2ZGZhNDhkYTg4ODllOThhZjA3NTI1ZmVmZiJ9fX0=",
            "cmd": 1423
        }
    },
    "Huge Backpack": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Perfect Diamond", "Celestial Artefact", "Perfect Amber"],
                ["Water Core", "Huge Backpack Core", "Magma Core"],
                ["Perfect Amethyst", "Wurtzite Boron Nitride Compound Plate", "Perfect Ruby"]
            ]
        },
        "use": [
            "Gives 54 extra inventory slots."
        ],
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTIyNmFmZWZmYWM1NzdlNTM3NGQ1YTU1MDgyY2YzYWFhNGEyYmZmNTQ1MTI5MzRhMDYzYjdlMDMzMTE4ZDkyYyJ9fX0=",
            "cmd": 1424
        }
    },

    "Small Backpack Core": {
        "obtain": [
            "The backpack shop offers this for $500."
        ],
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZWU4Y2M5YWQ3YTg4NmFjZTRiZjQ5MTA1MmQwODQyMzYwMmU1N2NkNDA5MmY1ZjM1ZWMwY2FhODVkOWQyNGJkIn19fQ==",
            "cmd": 1425
        }
    },
    "Medium Backpack Core": {
        "obtain": [
            "The backpack shop offers this for $5,000."
        ],
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTNiMjI4ZjcwYTM1ZDBhYTMyMzUwNDY3ZDllOGMwOWFhZTlhZTBhZTA4NzVmZGM4YzMxMWE4NzZiZTE5MDcxNyJ9fX0=",
            "cmd": 1426
        }
    },
    "Large Backpack Core": {
        "obtain": [
            "The backpack shop offers this for $50,000."
        ],
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvY2YwZTRhNjI5MmJjNWVlNzY0MmNhZTczNzZlZWRhNDQ2YzA0NzcxZTM5MDZmOGMwYjU4NjQxY2IzMWNmNjM3MyJ9fX0=",
            "cmd": 1427
        }
    },
    "Huge Backpack Core": {
        "obtain": [
            "The backpack shop offers this for $500,000."
        ],
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjVkOTc3NTk2ZWU3NWMyZGRhYWY0NjU2MjBiNjMyYjAwOGFjYzMxYWQzMTA1ZDY0MmViNmVjYWEzMmNkYmE5MSJ9fX0=",
            "cmd": 1428
        }
    },

    "Snow Shovel": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Snow Chunk", "Snow Block", "Snow Chunk"],
                ["Snow Block", "Golden Excavator", "Snow Block"],
                ["Snow Chunk", "Snow Block", "Snow Chunk"]
            ]
        },
        "rarity": Rarity.Rare,
        "mining speed": 6,
        "item": {
            "id": "iron_shovel",
            "cmd": 1797
        }
    },
    
    "Snowball": {
        "forge": "Snow Chunk",
        "sell": 10,
        "museum": (4, 1, 3),
        "rarity": Rarity.Common,
        "item": {
            "id": "snowball",
            "cmd": 1523
        }
    },
    "Snow Chunk": {
        "forge": "Snow Block",
        "sell": 60,
        "museum": (4, 1, 4),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNWRkNmZlMjY3YTQxOGRjYzdmMzdhOGY3Njg1NWI1MzI4YjEzMDM4OTdiMzQyYTEwN2NmMTYyZjE0ZmUzZCJ9fX0=",
            "cmd": 1524
        }
    },
    "Snow Block": {
        "forge": "Compressed Snow",
        "sell": 400,
        "museum": (4, 1, 5),
        "rarity": Rarity.Common,
        "item": {
            "id": "snow_block",
            "cmd": 1525
        }
    },
    "Compressed Snow": {
        "forge": "Hypercompact Snow",
        "sell": 2500,
        "museum": (4, 1, 6),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMmM3NjRiYjJlZjA4NTEzNDgwMzA2ZTEzYWJlOTQ0YzY2M2M4MGUzNzA4NDgwMWFkMTdlOTg5NzE2YzA1ZmNkYiJ9fX0=",
            "cmd": 1526
        }
    },
    "Hypercompact Snow": {
        "forge": "Opal",
        "sell": 15000,
        "museum": (4, 1, 7),
        "rarity": Rarity.Rare,
        "lore": ["Freezingly cold. But compact."],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDU2Mjk1MjMwMDIyNTU2YTM4MjM2MjliNDMzODViMGIyZGFjMTBjY2M4NTM1ODYyODdmMzM0ZTQ2Yjk3NzAwMiJ9fX0=",
            "cmd": 1528
        }
    },
    "Opal": {
        "forge": "Perfect Opal",
        "museum": (4, 1, 8),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNWQxNWVkNzBlNzIwMDQwYWQ3MzExZTY5MzU5ZGZkZjVlMTE0ZWFkZDJhNGMxZjk3MWE5NTAxMzQxYTQ1MjY0YiJ9fX0=",
            "cmd": 1529
        }
    },
    "Perfect Opal": {
        "sell": 500000,
        "museum": (4, 1, 9),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYWQ3OThlMjBhNDdkMjUxYTllMzNkNDAzMzI5NzNjNzE4OWFjMTU1MDc2MGJhMjVjNGI5NTZjOTE1OTM2NDU2OCJ9fX0=",
            "cmd": 1530
        }
    },

    "Snowball Shield": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Snowball", "Snowball", "Snowball"],
                ["Snowball", "Iron Ingot", "Snowball"],
                ["Snowball", "Snowball", "Snowball"]
            ]
        },
        "accessory": {
            "use": "Negates [Snowball] knockback",
            "slots": 1
        },
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjUyNTU5ZjJiY2VhZDk4M2Y0YjY1NjFjMmI1ZjJiNTg4ZjBkNjExNmQ0NDY2NmNlZmYxMjAyMDc5ZDI3Y2E3NCJ9fX0=",
            "cmd": 1748
        }
    },

    "Snowglobe": {
        "rarity": Rarity.Legendary,
        "lore": [
            "Gives all chests you find a 50% chance",
            "to contain a gift of a random tier."
        ],
        "accessory": {
            "slots": 2,
            "use": "Gives a 50% chance to find presents in chests."
        },
        "obtain": [
            "A rare drop from presents"
        ],
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvN2JiZThmZDFhYTM5ZjE1MDc2ZTg4NGRmZTZkZGI5YTNmMzc2MWRiMzFlMmIxZjk5NDBiNWRmZDM0ZDFjNGQifX19",
            "cmd": 1861
        }
    },

    "Sog Stone": {
        "forge": "Sog Gem",
        "sell": 150,
        "museum": (2, 3, 7),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "cyan_dye",
            "cmd": 1410
        }
    },
    "Sog Gem": {
        "forge": "Water Orb",
        "sell": 900,
        "museum": (2, 3, 8),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "cyan_dye",
            "enchanted": True,
            "cmd": 1411
        }
    },
    "Water Orb": {
        "forge": "Water Core",
        "sell": 5000,
        "museum": (2, 3, 9),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjFhMTExZWMxMTAyYzQwYzAyZDFkNDBmNDdlNjA5Mzg1MTIzOTNlOWRkYWZlZmQ1MDI4ZDJkM2EyMmJmNTE4ZSJ9fX0=",
            "cmd": 1417
        }
    },
    "Water Core": {
        "museum": (2, 4, 1),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzc0MDBlYTE5ZGJkODRmNzVjMzlhZDY4MjNhYzRlZjc4NmYzOWY0OGZjNmY4NDYwMjM2NmFjMjliODM3NDIyIn19fQ==",
            "cmd": 1418
        }
    },

    "Solar Cell": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Glass"] * 3,
                ["Ferrosilicon", "Electric Circuit", "Ferrosilicon"],
                ["Copper Wire", "Plastic Sheet", "Copper Wire"]
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZTdmNGMwMDM1NmQxYWRkYjg1YjQ1YmE1MzUyOTkyZDNlY2MwYzlkMTFmZWI5MDQxNDgyZjg1MzFmZDI3ZDAxNCJ9fX0=",
            "cmd": 1624
        }
    },

    "Soul Fragments": {
        "forge": "Soul Shard",
        "sell": 300,
        "museum": (2, 4, 8),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "prismarine_crystals",
            "cmd": 1413
        }
    },
    "Soul Shard": {
        "forge": "Soul",
        "sell": 2000,
        "museum": (2, 4, 9),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "prismarine_shard",
            "cmd": 1414
        }
    },
    "Soul": {
        "sell": 11000,
        "museum": (3, 1, 1),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZmJjODQyNmUzYjk1NzhmMjc0Y2JjNDM2NTI4MzkzZWRiNzdlMGY0YTUyNzVmN2U0ZTRjYmMzZmUxMGM1OGY4ZCJ9fX0=",
            "cmd": 1461
        }
    },

    "Soul Grass": {
        "sell": 450,
        "museum": (2, 4, 7),
        "rarity": Rarity.Uncommon,
        "item": {
            "id": "tube_coral_fan",
            "cmd": 1412
        }
    },

    "Spicy Candy": {
        "obtain": [
            "Mining blocks in the nether layer after consuming [Grapes of Jonathan] has a chance of dropping this."
        ],
        "museum": (8, 3, 5),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzdjYjA5ODJkNjk3NWQ1OGI2MzE0NzkzMmYzNzNjZDIxZTNjY2JjYWVhZDMyNzVjNWFhZThiMjcwMTVmODBjNiJ9fX0=",
            "cmd": 1841
        }
    },

    "Stalinium": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Communite"] * 3,
                ["Steel", "Communite", "Steel"],
                ["Communite"] * 3
            ]
        },
        "sell": 1500,
        "museum": (5, 2, 9),
        "rarity": Rarity.Godly,
        "item": {
            "id": "brick",
            "enchanted": True,
            "cmd": 1577
        }
    },
    
    "Starite": {
        "forge": "Celestial Ingot",
        "sell": 2000,
        "museum": (2, 2, 2),
        "rarity": Rarity.Epic,
        "item": {
            "id": "nether_star",
            "enchanted": True,
            "cmd": 1384
        }
    },
    "Celestial Ingot": {
        "forge": "Celestial Artefact",
        "sell": 15000,
        "museum": (2, 2, 3),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "iron_ingot",
            "enchanted": True,
            "cmd": 1385
        }
    },
    "Celestial Artefact": {
        "sell": 90000,
        "museum": (2, 2, 4),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "quartz",
            "cmd": 1446
        }
    },

    "Steel": {
        "forge": "Steel Plate",
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Iron Ingot"] * 3,
                ["Iron Ingot", "Anthracite", "Iron Ingot"],
                ["Iron Ingot"] * 3
            ]
        },
        "museum": (2, 1, 4),
        "rarity": Rarity.Rare,
        "item": {
            "id": "iron_ingot",
            "cmd": 1448
        }
    },
    "Steel Plate": {
        "sell": 60000,
        "museum": (2, 1, 5),
        "rarity": Rarity.Epic,
        "item": {
            "id": "heavy_weighted_pressure_plate",
            "cmd": 1449
        }
    },

    "Steel Pickaxe": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Coal"] * 3,
                ["Iron Ingot", "Iron Pickaxe", "Iron Ingot"],
                ["Coal"] * 3
            ]
        },
        "rarity": Rarity.Rare,
        "mining speed": 2.2,
        "breaking power": 3,
        "item": {
            "id": "iron_pickaxe",
            "cmd": 1478
        }
    },

    "Stone": {
        "sell": 20,
        "rarity": Rarity.Mundane,
        "item": {
            "id": "stone",
            "cmd": 1343
        }
    },

    "Stone Ball": {
        "museum": (7, 4, 8),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvY2IyYjVkNDhlNTc1Nzc1NjNhY2EzMTczNTUxOWNiNjIyMjE5YmMwNThiMWYzNDY0OGI2N2I4ZTcxYmMwZmEifX19",
            "cmd": 1350
        }
    },

    "Stone Pick": {
        "obtain": [
            "The overworld shop offers this for $100."
        ],
        "mining speed": 0.6,
        "breaking power": 1,
        "rarity": Rarity.Common,
        "item": {
            "id": "stone_hoe",
            "cmd": 1339
        }
    },

    "Stone Pickaxe": {
        "obtain": [
            "The overworld shop offers this for $300."
        ],
        "mining speed": 0.7,
        "breaking power": 2,
        "rarity": Rarity.Common,
        "item": {
            "id": "stone_pickaxe",
            "cmd": 1357
        }
    },

    "Stone Shovel": {
        "obtain": [
            "The overworld shop offers this for $500."
        ],
        "mining speed": 1.5,
        "breaking power": 0,
        "rarity": Rarity.Common,
        "item": {
            "id": "stone_shovel",
            "cmd": 1359
        }
    },

    "Strange Construct": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Sage Crystal", "Void Alloy", "Sage Crystal"],
                ["Refined Copper", None, "Refined Copper"],
                ["Sage Crystal", "Celestial Artefact", "Sage Crystal"]
            ]
        },
        "accessory": {
            "use": "Has a 1/3 chance to transform a [Sage Crystal] drop into an [Overclocker].",
            "slots": 4
        },
        "rarity": Rarity.Exotic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjA5NWE3ZmQ5MGRhYTFiYmU3MDY5MDg5NzQwZTA1ZDBiZmM2NjI5NmVlM2M0MGVlNzFhNGUwYTY2MTZiMmJiYyJ9fX0=",
            "cmd": 1863
        }
    },

    "String": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Plant Fibre", "Earth Crystal", "Plant Fibre"],
                [None] * 3,
                [None] * 3
            ]
        },
        "sell": 100,
        "rarity": Rarity.Common,
        "item": {
            "id": "string",
            "cmd": 1740
        }
    },

    "Stupid Stone": {
        "sell": -1,
        "lore": ["why"],
        "museum": (5, 3, 7),
        "rarity": Rarity.Divine,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOGM4NGY3NTQxNmU4NTNhNzRmNmM3MGZjN2UxMDkzZDUzOTYxODc5OTU1YjQzM2JkOGM3YzZkNWE2ZGYifX19",
            "cmd": 1619
        }
    },

    "Sturdy Boots": {
        "obtain": [
            "The communist shop offers this for $3,000."
        ],
        "rarity": Rarity.Common,
        "item": {
            "id": "leather_boots",
            "cmd": 1579
        }
    },

    "Subspace Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Void Shard"] * 3,
                ["Gold Ingot", "Skin Core", "Refined Amber"],
                ["Void Shard", "Refined Ruby", "Void Shard"]
            ]
        },
        "museum": (8, 4, 4),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZWZkNTc2ZTQyZDlkZmU1NjkzMTE1MGU2N2ZhYWZmNGViNmIzZjkwNGI1YmUwZWY2YTg3ZTBjMjM5ODE0YjEwYiJ9fX0=",
            "cmd": 1848
        }
    },

    "Sulfur": {
        "sell": 650,
        "museum": (2, 4, 2),
        "rarity": Rarity.Rare,
        "item": {
            "id": "glowstone",
            "cmd": 1390
        }
    },

    "Sulfur Drill Unit": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Sulfur", "Battery", "Sulfur"],
                ["Sulfur", "Netherite Pickaxe", "Sulfur"],
                ["Sulfur", "Impure Lead", "Sulfur"]
            ]
        },
        "rarity": Rarity.Rare,
        "mining speed": 12,
        "breaking power": 6,
        "item": {
            "id": "golden_horse_armor",
            "cmd": 1641
        }
    },

    "Sulfuric Acid": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Sulfur"] * 3,
                ["Sog Stone", "Iron Ingot", "Sog Stone"],
                ["Sulfur"] * 3
            ]
        },
        "sell": 20,
        "museum": (5, 4, 4),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzlmODRjNGVmYWQ1MTI3YzBiY2RmYzlhMjE0ZDA5MjRiZDY0MzQwOWUyNDg0MWYyMzlkZTFhYTk4MDdlYjJkMSJ9fX0=",
            "cmd": 1622
        }
    },

    "Tech Perception Gear": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Impure Lead", "Aluminium Ingot", "Impure Lead"],
                ["Uranium", "Hat of Knowledge", "Uranium"],
                ["Impure Lead", "Battery", "Impure Lead"]
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvN2YzNTJkMjgzMjgzNDFjZGRmZTUyNTVhNDEzNjc3YjVhNGFjMTk4ZTQxMmI1M2MxNjliOGYzMWQxYzYxZmJlOSJ9fX0=",
            "cmd": 1638
        }
    },

    "Telekinesis Orb": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                [None, "Gold Ore", None],
                ["Gold Ore", "Iron Ingot", "Gold Ore"],
                [None, "Gold Ore", None]
            ]
        },
        "accessory": {
            "use": "Items go into your inventory when mined",
            "slots": 0
        },
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNTgxOGU2NzI1YmI4NDUwMDBlZTU2NWFmMGE0ZTJkNjY3NTU4MzkxMTU0MWVjNWE0ZmIyYWNiZDg5MTNhMDM3YSJ9fX0=",
            "cmd": 1764
        }
    },

    "Thick Lead Helmet": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Lead Ingot", "Impure Lead", "Lead Ingot"],
                ["Impure Lead", "Lead Helmet", "Impure Lead"],
                [None] * 3
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "netherite_helmet",
            "cmd": 1661
        }
    },
    "Thick Lead Chestplate": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Impure Lead", None, "Impure Lead"],
                ["Lead Ingot", "Lead Chestplate", "Lead Ingot"],
                ["Impure Lead"] * 3
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "netherite_chestplate",
            "cmd": 1662
        }
    },
    "Thick Lead Leggings": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                ["Lead Ingot", "Impure Lead", "Lead Ingot"],
                ["Impure Lead", "Lead Leggings", "Impure Lead"],
                ["Impure Lead", None, "Impure Lead"]
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "netherite_leggings",
            "cmd": 1663
        }
    },
    "Thick Lead Boots": {
        "craft": {
            "tier": CraftTier.Tech1,
            "recipe": [
                [None] * 3,
                ["Impure Lead", None, "Impure Lead"],
                ["Lead Ingot", "Lead Boots", "Lead Ingot"]
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "netherite_boots",
            "cmd": 1664
        }
    },

    "Uranium Cookie": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Cookie", "Glue", "Uranium"],
                [None] * 3,
                [None] * 3
            ]
        },
        "rads": 0.5,
        "rarity": Rarity.Rare,
        "item": {
            "id": "cookie",
            "enchanted": True,
            "cmd": 1665
        }
    },

    "Uranium Ore": {
        "forge": "Uranium",
        "rads": 0.5,
        "museum": (6, 1, 4),
        "rarity": Rarity.Rare,
        "item": {
            "id": "firework_star",
            "color": "3B511A",
            "cmd": 1639
        }
    },
    "Uranium": {
        "sell": 10000,
        "rads": 2,
        "museum": (6, 1, 5),
        "rarity": Rarity.Rare,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjVhNDc1NDYwYjVmOWEzNjc3OTBkZjlkZjViYmJmYmMxMGMwNzlkNDU0OGUzMzgyZGIzNmYzMzY0ZWMwODg0NSJ9fX0=",
            "cmd": 1640
        }
    },

    "Vacuum Tube": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Glass", "Lead Ingot", "Glass"],
                ["Void Shard"] * 3,
                ["Glass", "Lead Ingot", "Glass"]
            ]
        },
        "sell": 40000,
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvM2Y1NmEyNmE5NDljMTMzYWI5NTAyMTFkZGRhZmViMjU1MWMwNTJlMWNmZmY2MTcyZmM2OGNkYTMyMTliMDg0In19fQ==",
            "cmd": 1621
        }
    },

    "Void Alloy": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Void Shard", "Adamantium Scraps", "Void Shard"],
                ["Magnesium Ingot", "Celestial Ingot", "Steel"],
                ["Void Shard", "Adamantium Scraps", "Void Shard"]
            ]
        },
        "sell": 10000,
        "museum": (3, 3, 7),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "netherite_ingot",
            "enchanted": True,
            "cmd": 1488
        }
    },

    "Void Cutter": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipes": [
                [
                    ["Adamantium", "Adamantium", "Celestial Artefact"],
                    ["Netherite Ingot", "Wurtzite Boron Nitride", "Gemstone Pickaxe"],
                    [None, "Wurtzite Boron Nitride", None]
                ], [
                    ["Adamantium", "Adamantium", "Celestial Artefact"],
                    ["Netherite Ingot", "Wurtzite Boron Nitride", "Meteorite Pickaxe"],
                    [None, "Wurtzite Boron Nitride", None]
                ]
            ]
        },
        "rarity": Rarity.Godly,
        "mining speed": 10,
        "breaking power": 7,
        "item": {
            "id": "netherite_axe",
            "cmd": 1490
        }
    },
    "Void Cutter+": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Void Shard", "Celestial Crowbar", "Void Shard"],
                ["Void Shard", "Void Cutter", "Void Shard"],
                ["Void Shard", "Void Alloy", "Void Shard"]
            ]
        },
        "rarity": Rarity.Godly,
        "mining speed": 14,
        "breaking power": 7,
        "item": {
            "id": "netherite_axe",
            "cmd": 1505
        }
    },
    
    "Void Shard": {
        "forge": "Void Matter",
        "sell": 550,
        "museum": (3, 3, 2),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZDQ0YzE2NWExNGViMTNkZjZiMDdjODVmMjA5Yzc5ZTIwMDhlMGI2N2FkMGIxNjA5M2IwMDBlZDAxMmNjZjI4OSJ9fX0=",
            "cmd": 1487
        }
    },
    "Void Matter": {
        "forge": "Void Orb",
        "sell": 15000,
        "museum": (3, 3, 3),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7ImlkIjoiMjVhYzQ4M2M2N2UwNGQ3YWE3ZGExMWU2MzllNDFlN2IiLCJ0eXBlIjoiU0tJTiIsInVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjgwZDQ0Y2ExNWUzMDNhMTcxNGQ4ZDY4OGJjM2QwYzQ4NDhhZjQ4YmJlMTZiMzg4OTNlNjQyOThkZGNmZTEwZSIsInByb2ZpbGVJZCI6IjE1ZmFjZGVjZTM3MzQzYTE4Y2Q4YTZhN2ZkMzllZjg4IiwidGV4dHVyZUlkIjoiMjgwZDQ0Y2ExNWUzMDNhMTcxNGQ4ZDY4OGJjM2QwYzQ4NDhhZjQ4YmJlMTZiMzg4OTNlNjQyOThkZGNmZTEwZSJ9fSwic2tpbiI6eyJpZCI6IjI1YWM0ODNjNjdlMDRkN2FhN2RhMTFlNjM5ZTQxZTdiIiwidHlwZSI6IlNLSU4iLCJ1cmwiOiJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlLzI4MGQ0NGNhMTVlMzAzYTE3MTRkOGQ2ODhiYzNkMGM0ODQ4YWY0OGJiZTE2YjM4ODkzZTY0Mjk4ZGRjZmUxMGUiLCJwcm9maWxlSWQiOiIxNWZhY2RlY2UzNzM0M2ExOGNkOGE2YTdmZDM5ZWY4OCIsInRleHR1cmVJZCI6IjI4MGQ0NGNhMTVlMzAzYTE3MTRkOGQ2ODhiYzNkMGM0ODQ4YWY0OGJiZTE2YjM4ODkzZTY0Mjk4ZGRjZmUxMGUifSwiY2FwZSI6bnVsbH0=",
            "cmd": 1518
        }
    },
    "Void Orb": {
        "forge": "Void Singularity",
        "sell": 75000,
        "museum": (3, 3, 4),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjIwMWFlMWE4YTA0ZGY1MjY1NmY1ZTQ4MTNlMWZiY2Y5Nzg3N2RiYmZiYzQyNjhkMDQzMTZkNmY5Zjc1MyJ9fX0=",
            "cmd": 1519
        }
    },
    "Void Singularity": {
        "forge": "Antimatter",
        "sell": 250000,
        "museum": (3, 3, 5),
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNWFjOTFhYjI1ODM2ZDEzNDgzODY0Y2RkYmQ0MzJkYmIyMmQ0YWMyOTNmMWM5OWZiMjg5MTljZjM5YzMifX19",
            "cmd": 1520
        }
    },
    "Antimatter": {
        "sell": 1000000,
        "museum": (3, 3, 6),
        "rarity": Rarity.Exotic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTdjMjE0NGZkY2I1NWMzZmMxYmYxZGU1MWNhYmRmNTJjMzg4M2JjYjU3ODkyMzIyNmJlYjBkODVjYjJkOTgwIn19fQ==",
            "cmd": 1521
        }
    },

    "Void Suppression Module": {
        "craft": {
            "tier": CraftTier.Tech0,
            "recipe": [
                ["Void Matter", "Electric Circuit", "Void Matter"],
                ["Electric Circuit", "Vacuum Tube", "Electric Circuit"],
                ["Void Matter", "Void Alloy", "Void Matter"]
            ]
        },
        "module": {
            "use": "Decreases void damage",
            "slots": 1
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYWRmODkwOTQ5OGMyNWY2ZTc1ZWYxOWUzNzZhN2Y4NGY2MWFmMjM0NTI1ZDYzOWJhNDYzZjk5MWY0YzgyZDAifX19",
            "cmd": 1205
        }
    },

    "Voidcruiser Skin": {
        "craft": {
            "tier": CraftTier.Skin,
            "recipe": [
                ["Void Shard", "Synthetic Diamond", "Void Shard"],
                ["Gold Ingot", "Skin Core", "Gold Ingot"],
                ["Void Shard", "Iron Ingot", "Void Shard"]
            ]
        },
        "museum": (9, 1, 6),
        "rarity": Rarity.Legendary,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzRjZjNjNWYyNGM5YmY4YjkwMzFlOGFlZDUzMzdiNmEwN2Y4MTljZGU4YzYyMjA4NTU0NTE2MmY4YTY5MzA2MCJ9fX0=",
            "cmd": 1847
        }
    },

    "Voidwalker Helmet": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Void Shard", "Void Alloy", "Void Shard"],
                ["Void Shard", "Miner's Helmet", "Void Shard"],
                [None] * 3
            ]
        },
        "rarity": Rarity.Godly,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvY2M3NDIxNjliODlkOTk3ZDQxZTNiZTkxZGUyMmFlMjJjZWI3OTI3M2MyMWZhNTQ2OGUzODQ0ZjhiOGVmOTEifX19",
            "cmd": 1489
        }
    },
    "Voidwalker Chestplate": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Void Shard", None, "Void Shard"],
                ["Void Shard", "Miner's Chestplate", "Void Shard"],
                ["Void Shard", "Void Alloy", "Void Shard"]
            ]
        },
        "rarity": Rarity.Godly,
        "item": {
            "id": "netherite_chestplate",
            "cmd": 1491
        }
    },
    "Voidwalker Leggings": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                ["Void Shard", "Void Alloy", "Void Shard"],
                ["Void Shard", "Miner's Leggings", "Void Shard"],
                ["Void Shard", None, "Void Shard"]
            ]
        },
        "rarity": Rarity.Godly,
        "item": {
            "id": "netherite_leggings",
            "cmd": 1492
        }
    },
    "Voidwalker Aeroboots": {
        "craft": {
            "tier": CraftTier.Crafting2,
            "recipe": [
                [None] * 3,
                ["Void Shard", "Netherite Aeroboots", "Void Shard"],
                ["Void Shard", "Void Alloy", "Void Shard"]
            ]
        },
        "rarity": Rarity.Godly,
        "item": {
            "id": "netherite_boots",
            "cmd": 1493
        }
    },

    "Volcanic Ash": {
        "forge": "Enhanced Ash",
        "sell": 5,
        "museum": (3, 1, 3),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "gunpowder",
            "cmd": 1456
        }
    },
    "Enhanced Ash": {
        "forge": "Volcanic Ash Clump",
        "sell": 11,
        "museum": (8, 1, 9),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "gunpowder",
            "enchanted": True,
            "cmd": 1822
        }
    },
    "Volcanic Ash Clump": {
        "forge": "Volcanic Ash Conglomerate",
        "sell": 13,
        "museum": (8, 2, 1),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "gray_dye",
            "cmd": 1823
        }
    },
    "Volcanic Ash Conglomerate": {
        "forge": "Volcanic Ash Ingot",
        "museum": (8, 2, 2),
        "rarity": Rarity.Mundane,
        "item": {
            "id": "clay_ball",
            "cmd": 1824
        }
    },
    "Volcanic Ash Ingot": {
        "sell": 20,
        "museum": (8, 2, 3),
        "rarity": Rarity.Mundane,
        "lore": [
            "Through ingotization,",
            "this ash conglomerate",
            "has formed a complex",
            "type of resource:",
            "The Ingot.",
            "This stage of the ash's",
            "life should be called",
            "nothing short of",
            "\"The Ingoting\".",
            "The world has yet to",
            "see any more",
            "spectacular event",
            "than this.",
            "A sight to behold..."
        ],
        "item": {
            "id": "netherite_ingot",
            "cmd": 1825
        }
    },

    "Waluigi Ball": {
        "obtain": [
            "Chests have a chance to contain this if you have the [Waluigi Charm]."
        ],
        "museum": (8, 1, 2),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYTgwMjU5NzA5ODg4OGM1OTJlMDlkNTlhMmFkZTU3NmQ3NWQzZTQ5NDY1ZDE1NzI0YjRhODc4OWQ4NjNmNWJkNCJ9fX0=",
            "cmd": 1766
        }
    },

    "Waluigi Ceremonial Mask": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                ["Amethyst"] * 3,
                ["Amethyst", "Waluigi Ball", "Amethyst"],
                ["Oinx", None, "Oinx"]
            ]
        },
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvOTBhMTZlNGQ5OGMyYTI0MWQ4OWY4Njk5ZGNlOWQzY2M1MmMyM2JmMTg4YWJjMTgzNmM5MzRkYTlmZDBhYzgxZSJ9fX0=",
            "cmd": 1767
        }
    },

    "Waluigi Charm": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                ["String", "Perfect Amethyst", "String"],
                ["Amethyst", "Oinx", "Amethyst"],
                ["Large Backpack Core", "Potassium", "Large Backpack Core"]
            ]
        },
        "accessory": {
            "use": "Gives +5% luck and the ability to find Waluigi Balls in chests.",
            "slots": 1
        },
        "rarity": Rarity.Mythic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvODk3MmY0YjkxM2RlZWQzNDE4ZDZmOWRlZjZjNGZlYWU4NmEzZmZhMDk2ZTgyMjczNmY0NTliMmE1ZmE1YzBlMSJ9fX0=",
            "cmd": 1765
        }
    },

    "Waluigi Taco": {
        "craft": {
            "tier": CraftTier.Walgo,
            "recipe": [
                ["Salt", "Luxury Cheese", "Grass"],
                ["Dough", "Bacon", "Dough"],
                ["Waluigi Ball", "Dough", "Waluigi Ball"]
            ]
        },
        "museum": (8, 1, 7),
        "rarity": Rarity.Rare,
        "item": {
            "id": "baked_potato",
            "cmd": 1796
        }
    },

    "Water Amethyst": {
        "sell": 10000,
        "museum": (7, 3, 2),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzRlOGZmMzBlMzkzNzA5ODYzN2MwYWYwM2ExZjJhNmIxN2YwZTgyOGFiMmE1N2EyNjdhMDFkYTQ4NGJhMGM1NyJ9fX0=",
            "cmd": 1718
        }
    },

    "Water Bottle": {
        "craft": {
            "tier": CraftTier.Brewing,
            "recipes": [
                [
                    ["Sog Stone", "Empty Bottle", None],
                    [None] * 3,
                    [None] * 3
                ], [
                    ["Ice Fragments", "Empty Bottle", None],
                    [None] * 3,
                    [None] * 3
                ]
            ]
        },
        "rarity": Rarity.Common,
        "item": {
            "id": "potion",
            "water": True,
            "cmd": 1800
        }
    },

    "Waterproof Glue": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Orichalcum Chips", "Super Glue", "Clay"],
                ["Sog Stone", "Processed Rockite", "Impure Lead"],
                [None] * 3
            ]
        },
        "rarity": Rarity.Rare,
        "item": {
            "id": "lapis_lazuli",
            "enchanted": True,
            "cmd": 1730
        }
    },

    "Weight Block": {
        "craft": {
            "tier": CraftTier.Water,
            "recipe": [
                ["Brick"] * 3,
                ["Brick", "Lead Ingot", "Brick"],
                ["Brick"] * 3
            ]
        },
        "rarity": Rarity.Epic,
        "item": {
            "id": "netherite_block",
            "cmd": 1703
        }
    },

    "Wood": {
        "craft": {
            "tier": CraftTier.Crafting0,
            "recipe": [
                ["Roots", "Roots", None],
                ["Roots", "Roots", None],
                [None] * 3
            ]
        },
        "sell": 80,
        "museum": (6, 2, 1),
        "rarity": Rarity.Common,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNGIzODhjMGM1MDcxMGJkMmFkOTY2ODZlYjEzMGJkMmYzZDg3NjYwYjgzODMyYmI0MzA0MmU5YWJhYjhlYjcwZiJ9fX0=",
            "cmd": 1672
        }
    },

    "Wood Ingot": {
        "sell": 100,
        "museum": (7, 4, 9),
        "rarity": Rarity.Mundane,
        "lore": ["Yes"],
        "item": {
            "id": "brick",
            "cmd": 1759
        }
    },

    "Wooden Pick": {
        "forge": "Wooden Pickaxe",
        "obtain": [
            "The overworld shop offers this for $15."
        ],
        "rarity": Rarity.Common,
        "mining speed": 0.4,
        "item": {
            "id": "wooden_hoe",
            "cmd": 1338
        }
    },
    "Wooden Pickaxe": {
        "forge": "Empowered Wooden Pickaxe",
        "rarity": Rarity.Legendary,
        "mining speed": 0.9,
        "item": {
            "id": "wooden_pickaxe",
            "cmd": 1436
        }
    },
    "Empowered Wooden Pickaxe": {
        "forge": "Perfect Wooden Pickaxe",
        "rarity": Rarity.Godly,
        "mining speed": 26,
        "breaking power": 2,
        "item": {
            "id": "wooden_pickaxe",
            "enchanted": True,
            "cmd": 1690
        },
        "use": [
            "Gives +10% luck"
        ]
    },
    "Perfect Wooden Pickaxe": {
        "rarity": Rarity.Divine,
        "mining speed": 28.1,
        "breaking power": 7,
        "item": {
            "id": "wooden_hoe",
            "enchanted": True,
            "cmd": 1826
        }
    },

    "Wooden Shovel": {
        "obtain": [
            "The overworld shop offers this for $50."
        ],
        "rarity": Rarity.Common,
        "mining speed": 1,
        "item": {
            "id": "wooden_shovel",
            "cmd": 1358
        }
    },

    "Wrapped Candy": {
        "obtain": [
            "Mining blocks in the water mine after consuming [Grapes of Jonathan] has a chance of dropping this."
        ],
        "museum": (8, 3, 9),
        "rarity": Rarity.Epic,
        "item": {
            "id": "player_head",
            "value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzZiMzViYTRjYTk2YzBjY2E4YzFmZTg2NDFiMWQ1NzBlOGMzZjY2Mjk4ZTBlNWQ3ZjMzYzEzMDQ2ZTU4NjM3MCJ9fX0=",
            "cmd": 1845
        }
    },

    "Wurtzite Boron Nitride Compound Plate": {
        "craft": {
            "tier": CraftTier.Crafting1,
            "recipe": [
                ["Wurtzite Boron Nitride", "Synthetic Diamond", "Wurtzite Boron Nitride"],
                ["Steel Plate", "Refined Onyx", "Steel Plate"],
                ["Wurtzite Boron Nitride", "Refined Ruby", "Wurtzite Boron Nitride"]
            ]
        },
        "sell": 400000,
        "museum": (3, 1, 7),
        "rarity": Rarity.Mythic,
        "item": {
            "id": "netherite_scrap",
            "cmd": 1455
        }
    }
}