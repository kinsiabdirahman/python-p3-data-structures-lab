spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = []  # Initialize an empty list to store the names

    for food in spicy_foods:
        food_names.append(food["name"])

    return food_names

    
    # return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    heat_foods = []
    moderate_heat = 5

    # for food in spicy_foods:
    #     if (food["heat_level"]) > moderate_heat:
    #         heat_foods.append(food["name","heat_level"])
    # return heat_foods

    for food in spicy_foods:
        if (food["heat_level"]) > moderate_heat:
            heat_foods.append({"name": food["name"], "heat_level": food["heat_level"]})

    return heat_foods

# def get_spiciest_foods(spicy_foods):
#     return [{"name": food["name"], "heat_level": food["heat_level"]} for food in spicy_foods if food["heat_level"] > 5]



def print_spicy_foods(spicy_foods):
    spicy_print = []

    for food in spicy_foods:
        heat_level_emoji = "🌶" * food["heat_level"]
        spicy_print.append(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")

    for food_info in spicy_print:
        print(food_info)

# def print_spicy_foods(spicy_foods):
#     [print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}") for food in spicy_foods]


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return {"name": food["name"], "cuisine": food["cuisine"], "heat_level": food["heat_level"]}

    # Return an empty dictionary if no match is found
    return {}


# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     cat_cuisine = []

#     for food in spicy_foods:
#         if food["cuisine"] == cuisine:
#             cat_cuisine.append({"name": food["name"], "cuisine": food["cuisine"], "heat_level": food["heat_level"]})

#     return cat_cuisine

    # return [{"name": food["name"], "cuisine" : food["cuisine"], "heat_level": food["heat_level"]} for food in spicy_foods if food["cuisine"] == cuisine]


def print_spiciest_foods(spicy_foods):
    spicy_print = []
    moderate_heat = 5

    for food in spicy_foods:
        if (food["heat_level"]) > moderate_heat:
            heat_level_emoji = "🌶" * food["heat_level"]
            spicy_print.append(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")

    for food_info in spicy_print:
        print(food_info)  
    

def get_average_heat_level(spicy_foods):
    total_heat = 0
    num_foods = len(spicy_foods)

    for food in spicy_foods:
        total_heat += food["heat_level"]

    if num_foods == 0:
        return 0  
    else:
        return total_heat / num_foods


    # res = sum(spicy_foods["heat_level"]) / len(spicy_foods) 
    # return res
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods