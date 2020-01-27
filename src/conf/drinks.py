# drinks_more_recipes.py
drink_list = [
    {
        "name": "Alice",
        "recipe": [
            ("ingr", "sahne", 20),
            ("ingr", "ananass", 80),
            ("ingr", "orangens", 80),
            ("ingr", "gren", 20),
        ]
    }, {
        "name": "Alice Deluxe",
        "recipe": [
            ("ingr", "sahne", 20),
            ("ingr", "ananass", 80),
            ("ingr", "orangens", 60),
            ("ingr", "gren", 20),
            ("ingr", "wodka", 20),
        ]
    }, {
        "name": "Amaretto Sour",
        "recipe": [
            ("ingr", "amaretto", 30),
            ("ingr", "zitronens", 30),
            ("ingr", "orangens", 30),
        ]
    }, {
        "name": "Bacardi Sunrise",
        "recipe": [
            ("ingr", "bacardi", 40),
            ("ingr", "zitronens", 10),
            ("ingr", "orangens", 100),
            ("ingr", "gren", 10),
        ]
    }, {
        "name": "Bacardi Cola",
        "recipe": [
            ("ingr", "bacardi", 40),
            ("ingr", "cola", 200),
        ]
    }, {
        "name": "Balalaika",
        "recipe": [
            ("ingr", "wodka", 40),
            ("ingr", "zitronens", 10),
            ("ingr", "orangenl", 20),
        ]
    }, {
        "name": "Ballerina",
        "recipe": [
            ("ingr", "ananass", 40),
            ("ingr", "zitronens", 15),
            ("ingr", "orangens", 40),
        ]
    }, {
        "name": "Baltic",
        "recipe": [
            ("ingr", "wodka", 40),
            ("ingr", "curacao", 10),
            ("ingr", "maracujas", 20),
            ("ingr", "orangens", 100),
        ]
    }, {
        "name": "Barbados Cocktail",
        "recipe": [
            ("ingr", "bacardi", 30),
            ("ingr", "orangenl", 5),
            ("ingr", "ananass", 15),
        ]
    }, {
        "name": "Barbados Dream",
        "recipe": [
            ("ingr", "kokos", 15),
            ("ingr", "zitronens", 10),
            ("ingr", "ananass", 40),
            ("ingr", "maracujas", 40),
        ]
    }, {
        "name": "Berry Me In The Sand",
        "recipe": [
            ("ingr", "wodka", 20),
            ("ingr", "orangenl", 15),
            ("ingr", "orangens", 100),
        ]
    }, {
        "name": "Best of Green",
        "recipe": [
            ("ingr", "tequila", 25),
            ("ingr", "curacao", 18),
            ("ingr", "kokos", 18),
            ("ingr", "zitronens", 7),
            ("ingr", "maracujas", 80),
        ]
    }, {
        "name": "Black Thunder",
        "recipe": [
            ("ingr", "wodka", 40),
            ("ingr", "curacao", 20),
            ("ingr", "cola", 160),
        ]
    }, {
        "name": "Blue Hawaii",
        "recipe": [
            ("ingr", "bacardi", 15),
            ("ingr", "curacao", 15),
            ("ingr", "sahne", 20),
        ]
    }, {
        "name": "Blue Hawaii 3",
        "recipe": [
            ("ingr", "bacardi", 10),
            ("ingr", "orangenl", 10),
            ("ingr", "curacao", 10),
            ("ingr", "sahne", 20),
        ]
    }, {
        "name": "Blue Hawaiian",
        "recipe": [
            ("ingr", "malibu", 20),
            ("ingr", "curacao", 20),
            ("ingr", "ananass", 60),
        ]
    }, {
        "name": "Blue Lagoon",
        "recipe": [
            ("ingr", "wodka", 30),
            ("ingr", "curacao", 20),
            ("ingr", "ananass", 70),
        ]
    }, {
        "name": "Blue Wolga",
        "recipe": [
            ("ingr", "wodka", 50),
            ("ingr", "curacao", 10),
            ("ingr", "tonic", 70),
        ]
    }, {
        "name": "Bora Bora",
        "recipe": [
            ("ingr", "ananass", 10),
            ("ingr", "maracujas", 60),
            ("ingr", "zitronens", 10),
            ("ingr", "gren", 10),
        ]
    }, {
        "name": "Brasilian Sunrise",
        "recipe": [
            ("ingr", "cachaca", 40),
            ("ingr", "gren", 20),
            ("ingr", "zitronens", 10),
            ("ingr", "orangens", 100),
        ]
    }, {
        "name": "Cococabana",
        "recipe": [
            ("ingr", "malibu", 30),
            ("ingr", "bacardi", 30),
            ("ingr", "ananass", 80),
        ]
    }, {
        "name": "Don Juan",
        "recipe": [
            ("ingr", "43", 20),
            ("ingr", "orangens", 60),
        ]
    }, {
        "name": "Drachenblut",
        "recipe": [
            ("ingr", "kirschs", 40),
            ("ingr", "ananass", 40),
            ("ingr", "gren", 10),
            ("ingr", "zitronens", 10),
        ]
    }, {
        "name": "Exotic",
        "recipe": [
            ("ingr", "orangens", 90),
            ("ingr", "ananass", 60),
            ("ingr", "mangos", 30),
            ("ingr", "curacao", 15),
            ("ingr", "kokos", 15),
        ]
    }, {
        "name": "Exotic Blue",
        "recipe": [
            ("ingr", "ananass", 60),
            ("ingr", "sahne", 15),
            ("ingr", "curacao", 30),
        ]
    }, {
        "name": "Festini",
        "recipe": [
            ("ingr", "wodka", 20),
            ("ingr", "sahne", 15),
            ("ingr", "maracujas", 60),
        ]
    }, {
        "name": "Formula One",
        "recipe": [
            ("ingr", "malibu", 20),
            ("ingr", "bacardi", 40),
            ("ingr", "ananass", 80),
            ("ingr", "gren", 15),
        ]
    }, {
        "name": "Gloom Chaser",
        "recipe": [
            ("ingr", "orangenl", 20),
            ("ingr", "gren", 10),
            ("ingr", "zitronens", 5),
        ]
    }, {
        "name": "Golden Sunrise",
        "recipe": [
            ("ingr", "bacardi", 60),
            ("ingr", "gren", 20),
            ("ingr", "zitronens", 5),
            ("ingr", "orangens", 10),
            ("ingr", "ananass", 10),
        ]
    }, {
        "name": "Grand Marnier",
        "recipe": [
            ("ingr", "curacao", 100),
            ("ingr", "orangenl", 15),
        ]
    }, {
        "name": "Grand Marnier Tonic",
        "recipe": [
            ("ingr", "orangenl", 15),
            ("ingr", "tonic", 100),
        ]
    }, {
        "name": "Gruene Witwe",
        "recipe": [
            ("ingr", "curacao", 40),
            ("ingr", "orangens", 100),
        ]
    }, {
        "name": "Indianapolis",
        "recipe": [
            ("ingr", "curacao", 20),
            ("ingr", "wodka", 20),
            ("ingr", "sahne", 20),
        ]
    }, {
        "name": "Kangaroo Jumper",
        "recipe": [
            ("ingr", "wodka", 20),
            ("ingr", "kokos", 30),
            ("ingr", "curacao", 10),
            ("ingr", "ananass", 30),
        ]
    }, {
        "name": "Kaept'n Chaos",
        "recipe": [
            ("ingr", "bacardi", 20),
            ("ingr", "wodka", 15),
            ("ingr", "gin", 10),
            ("ingr", "orangens", 30),
            ("ingr", "maracujas", 20),
            ("ingr", "zitronens", 3),
        ]
    }, {
        "name": "Lemon Drop Martini",
        "recipe": [
            ("ingr", "wodka", 30),
            ("ingr", "orangenl", 15),
            ("ingr", "zitronens", 10),
        ]
    }, {
        "name": "Little Devil",
        "recipe": [
            ("ingr", "bacardi", 30),
            ("ingr", "gin", 20),
            ("ingr", "orangenl", 15),
            ("ingr", "zitronens", 15),
        ]
    }, {
        "name": "Los Angeles",
        "recipe": [
            ("ingr", "wodka", 25),
            ("ingr", "zitronens", 10),
            ("ingr", "orangens", 60),
            ("ingr", "ananass", 20),
            ("ingr", "maracujas", 20),
            ("ingr", "gren", 20),
        ]
    }, {
        "name": "Lucky Driver",
        "recipe": [
            ("ingr", "zitronens", 10),
            ("ingr", "orangens", 40),
            ("ingr", "maracujas", 20),
            ("ingr", "gren", 10),
        ]
    }, {
        "name": "Magnolia Blossom",
        "recipe": [
            ("ingr", "gin", 30),
            ("ingr", "zitronens", 10),
            ("ingr", "sahne", 15),
        ]
    }, {
        "name": "Malibu Cola",
        "recipe": [
            ("ingr", "malibu", 20),
            ("ingr", "cola", 60),
        ]
    }, {
        "name": "Malibu Cranberry",
        "recipe": [
            ("ingr", "malibu", 20),
            ("ingr", "cranb", 60),
        ]
    }, {
        "name": "Malibu Ananass",
        "recipe": [
            ("ingr", "malibu", 20),
            ("ingr", "ananass", 60),
        ]
    }, {
        "name": "Malibu Maracuja",
        "recipe": [
            ("ingr", "malibu", 20),
            ("ingr", "maracujas", 60),
        ]
    }, {
        "name": "Malibu Orange",
        "recipe": [
            ("ingr", "malibu", 20),
            ("ingr", "orangens", 60),
        ]
    }, {
        "name": "Maracolada",
        "recipe": [
            ("ingr", "kokos", 20),
            ("ingr", "sahne", 20),
            ("ingr", "maracujas", 65),
        ]
    }, {
        "name": "Miami Cocktail",
        "recipe": [
            ("ingr", "bacardi", 40),
            ("ingr", "zitronens", 10),
            ("ingr", "orangenl", 20),
        ]
    }, {
        "name": "Cola 43",
        "recipe": [
            ("ingr", "43", 20),
            ("ingr", "cola", 60),
        ]
    }, {
        "name": "Pina Colada",
        "recipe": [
            ("ingr", "bacardi", 25),
            ("ingr", "sahne", 15),
            ("ingr", "kokos", 10),
            ("ingr", "ananass", 50),
        ]
    }, {
        "name": "Pink Pussycat",
        "recipe": [
            ("ingr", "wodka", 40),
            ("ingr", "gren", 10),
            ("ingr", "ananass", 100),
        ]
    }, {
        "name": "Pinky Colada",
        "recipe": [
            ("ingr", "bacardi", 30),
            ("ingr", "gren", 10),
            ("ingr", "kokos", 10),
            ("ingr", "sahne", 15),
            ("ingr", "ananass", 50),
        ]
    }, {
        "name": "Pussycat",
        "recipe": [
            ("ingr", "orangens", 50),
            ("ingr", "sahne", 20),
            ("ingr", "ananass", 50),
            ("ingr", "curacao", 20),
        ]
    }, {
        "name": "Red Lion",
        "recipe": [
            ("ingr", "orangenl", 20),
            ("ingr", "gin", 30),
            ("ingr", "orangens", 40),
            ("ingr", "zitronens", 10),
            ("ingr", "gren", 10),
        ]
    }, {
        "name": "Screw Driver",
        "recipe": [
            ("ingr", "wodka", 50),
            ("ingr", "orangens", 150),
        ]
    }, {
        "name": "Sex on the Beach",
        "recipe": [
            ("ingr", "wodka", 20),
            ("ingr", "pfirsichl", 40),
            ("ingr", "cranberrys", 80),
            ("ingr", "pfirsichs", 50),
        ]
    }, {
        "name": "Soft Poison",
        "recipe": [
            ("ingr", "curacao", 20),
            ("ingr", "orangens", 160),
        ]
    }, {
        "name": "Spain",
        "recipe": [
            ("ingr", "43", 30),
            ("ingr", "wodka", 20),
            ("ingr", "sahne", 20),
            ("ingr", "gren", 20),
            ("ingr", "maracujas", 70),
        ]
    }, {
        "name": "Sunset",
        "recipe": [
            ("ingr", "cola", 70),
            ("ingr", "orangens", 100),
            ("ingr", "gren", 30),
        ]
    }, {
        "name": "Tequila Sunrise",
        "recipe": [
            ("ingr", "tequila", 20),
            ("ingr", "gren", 10),
            ("ingr", "zitronens", 10),
            ("ingr", "orangens", 50),
        ]
    }, {
        "name": "Virgin Cherry Colada",
        "recipe": [
            ("ingr", "kokos", 10),
            ("ingr", "sahne", 10),
            ("ingr", "kirschs", 100),
        ]
    }, {
        "name": "Virgin Sunrise",
        "recipe": [
            ("ingr", "orangens", 90),
            ("ingr", "maracujas", 80),
            ("ingr", "gren", 30),
        ]
    }, {
        "name": "Virgin Pina Colada",
        "recipe": [
            ("ingr", "kokos", 15),
            ("ingr", "sahne", 10),
            ("ingr", "ananass", 70),
        ]
    }, {
        "name": "Tropic Star",
        "recipe": [
            ("ingr", "orangens", 80),
            ("ingr", "ananass", 80),
            ("ingr", "maracujas", 80),
        ]
    }, {
        "name": "White Lady",
        "recipe": [
            ("ingr", "orangenl", 20),
            ("ingr", "gin", 20),
            ("ingr", "zitronens", 20),
        ]
    }, {
        "name": "Wodka Tonic",
        "recipe": [
            ("ingr", "wodka", 20),
            ("ingr", "tonic", 100),
        ]
    }, {
        "name": "Extra Schuss Bacardi",
        "recipe": [("ingr", "bacardi", 20)]
    }, {
        "name": "Extra Schuss Cranberry Sirup",
        "recipe": [("ingr", "cranb", 20)]
    }, {
        "name": "Extra Schuss Cola",
        "recipe": [("ingr", "cola", 50)]
    }, {
        "name": "Extra Schuss Wodka",
        "recipe": [("ingr", "wodka", 20)]
    }, {
        "name": "Extra Schuss O-Saft",
        "recipe": [("ingr", "orangens", 50)]
    }
]

# -> Read out of DB
ingredients = {
    # code				text		is_alcoholic?
    # ohne Alkohol
    "ananass": ("Ananassaft", False),
    "cola": ("Cola", False),
    "cranb": ("Cranberry Sirup", False),
    "cranbs": ("Cranberry Saft", False),
    "gga": ("Ginger Ale", False),
    "gren": ("Grenadine", False),
    "kirschs": ("Kirschsaft", False),
    "kokos": ("Kokossirup", False),
    "mate": ("Mate", False),
    "mangos": ("Mangosaft", False),
    "maracujas": ("Maracujasaft", False),
    "orangens": ("Orangensaft", False),
    "pfirsichs": ("Pfirsichsaft", False),
    "sahne": ("Sahne", False),
    "tonic": ("Tonic Water", False),
    "zitronens": ("Zitronensaft", False),
    # mit Alkohol
    "43": ("43", True),
    "amaretto": ("Amaretto", True),
    "gin": ("Gin", True),
    "bacardi": ("Bacardi", True),
    "curacao": ("Blue Curacao", True),
    "cachaca": ("Cachaca Pitu", True),
    "malibu": ("Malibu", True),
    "orangenl": ("Orangenlikör", True),
    "rum": ("Rum", True),
    "tequila": ("Tequila", True),
    "wodka": ("Wodka", True),
    "whisky": ("Whisky", True),
}

actions = {
    # code      text     is_automatic?
    "ingr": ("Add Ingredient", True),
    "ping": ("Ring Bell", True),
    "shake": ("Shake", False),
    "stir": ("Stir", False),
    "ice": ("Add Ice", False),
    "umb": ("Add Umbrella", False),
}

# To DB -> replace
#available_ingredients = ["gren", "rum", "vodka", "gin", "tequila", "gibe", "lime", "tonic", "mate", "gga", "pine", "oj"]
available_ingredients = ["gren", "bacardi", "wodka", "orangens", "zitronens", "maracujas", "tonic", "orangenl", "sahne", "curacao", "ananass", "kokos"]


def doable(drink, available):
    return False not in [ing in available for ing in [step[1] for step in drink["recipe"] if step[0] == "ingr"]]


def alcoholic(drink):
    return True in [ingredients[step[1]][1] for step in drink["recipe"] if step[0] == "ingr"]

available_drinks = [drink for drink in drink_list if doable(drink, available_ingredients)]
