from fuzzywuzzy import fuzz

class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, recipe_id, name, category, ingredients, preparation_time, weight):
        recipe = {
            'name': name,
            'category': category,
            'ingredients': ingredients,
            'preparation_time': preparation_time,
            'serving_weight': weight
        }
        self.recipes[recipe_id] = recipe

    def get_recipe(self, recipe_id):
        return self.recipes.get(recipe_id)

    def delete_recipe(self, recipe_id):
        if recipe_id in self.recipes:
            del self.recipes[recipe_id]

    def print_all_recipes(self):
        for recipe_id, recipe in self.recipes.items():
            print(f"Recipe ID: {recipe_id}")
            print(f"Name: {recipe['name']}")
            print(f"Ingredients: {recipe['ingredients']}")
            print(f"Preparation Time: {recipe['preparation_time']} min")
            print(f"Serving weight: {recipe['serving_weight']} gram")
            print("-------------------")

    def print_recipe(self, recipe_id):
        recipe = self.get_recipe(recipe_id)
        if recipe:
            print(f"Recipe ID: {recipe_id}")
            print(f"Name: {recipe['name']}")
            print(f"Ingredients: {recipe['ingredients']}")
            print(f"Preparation Time: {recipe['preparation_time']} min")
            print(f"Serving weight: {recipe['serving_weight']} gram")
        else:
            print(f"Recipe with ID '{recipe_id}' not found.")
        print("-------------------")

    def get_id(self, title):
        best_ratio = 0
        best_recipe_id = None

        for recipe_id, recipe in self.recipes.items():
            ratio = fuzz.partial_ratio(title.lower(), recipe['name'].lower())
            if ratio > best_ratio:
                best_ratio = ratio
                best_recipe_id = recipe_id

        return best_recipe_id

  
    def sort_by_name(self):
        sorted_recipes = sorted(self.recipes.items(), key=lambda x: x[1]['name'])
        for recipe_id, recipe in sorted_recipes:
            print(f"Recipe ID: {recipe_id}")
            print(f"Name: {recipe['name']}")
            print(f"Ingredients: {recipe['ingredients']}")
            print(f"Preparation Time: {recipe['preparation_time']} min")
            print(f"Serving weight: {recipe['serving_weight']} gram")
            print("-------------------")
          
    def sort_by_category(self, category):
      sorted_recipes = []

      for recipe_id, recipe in self.recipes.items():
          if recipe['category'] == category:
              sorted_recipes.append((recipe_id, recipe))

      
      print(f"Recipes in the '{category}' category:")
      for recipe_id, recipe in sorted_recipes:
          print(f"Recipe ID: {recipe_id}, Recipe: {recipe['name']}")
      print("-------------------")


# Create an instance of RecipeBook
recipe_book = RecipeBook()

# Add recipes
recipe_book.add_recipe("recipe1", "Pilaf with beef", "Second course", ["Rice", "Beef", "Carrot", "Sunflower oil", "Spices"], 35, 325)
recipe_book.add_recipe("recipe2", "Pilaf with chicken", "Second course", ["Rice", "Chicken", "Onion", "Sunflower oil", "Spices"], 30, 325)
recipe_book.add_recipe("recipe3", "Borscht", "First course", ["Beef", "Sour cream", "Red wine vinegar", "Carrot",], 60, 500)
recipe_book.add_recipe("recipe4", "Mushroom soup", "First course", ["Mushrooms", "Sour cream", "Potato", "Carrot", "Onion"], 25, 500)
recipe_book.add_recipe("recipe5", "Meringue", "Dessert", ["Eggs", "Sugar", "Lemon juice"], 15, 150)






# Without sort
print("1) Print all without sotring:")
print("\n")
recipe_book.print_all_recipes()
print("\n\n")

# ID
print("2) Print recipe by ID:")
print("\n")
recipe_book.print_recipe("recipe1")
recipe_book.print_recipe("recipe3")
recipe_book.print_recipe("recipe5")
recipe_book.print_recipe("recipe6") # Non-existent recipe

print("\n\n")

# Name
print("3) Print recipe by name (keywords):") # Keyword search
print("\n")
print(f"Keyword: plov beef")
recipe_book.print_recipe(recipe_book.get_id("plov beef"))
print(f"Keyword: brsch")
recipe_book.print_recipe(recipe_book.get_id("brsch"))
print(f"Keyword: plov chicken")
recipe_book.print_recipe(recipe_book.get_id("plov chicken"))
print("\n\n")

# Sorted
print("4) Print sorted recipe book (by name):") # Keyword search
print("\n")
recipe_book.sort_by_name()
print("\n\n")

# Category
print("5) Print recipes by category:")
print("\n")
recipe_book.sort_by_category("First course")
recipe_book.sort_by_category("Dessert")
print("\n\n")

# Delete some recipe
print("6) Print recipe book without some deleted recipe:")
print("\n")
recipe_book.delete_recipe(recipe_book.get_id("mushroom"))
recipe_book.print_all_recipes()
print("\n\n")

