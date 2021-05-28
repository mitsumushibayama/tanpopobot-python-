import random

text_list = [
    "popopo",
    "tanpopo",
    "potapota",
    "potage",
    "tanpo",
    "ponta",
    "ponpoco",
    "pocopoco",
    "たんぽぽ",
    "ゆ　た　ん　ぽ",
    "菊",
    "tangent",
    "tanpopopo",
    "担保",
    "だんぼぼ",
    "ponpopo"
]

def chooseword():
    word = random.choice(text_list)
    return word