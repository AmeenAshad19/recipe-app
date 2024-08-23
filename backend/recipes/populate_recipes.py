from recipes.models import Recipe
from django.core.files import File
import os

# Define the media root directory where the images are stored
media_root = os.path.join('media', 'recipe_images')

# Sample recipes
dessert_recipes = [
    {
        "title": "Chocolate Cake",
        "description": "A rich and moist chocolate cake with a decadent chocolate frosting.",
        "ingredients": [
            "1 3/4 cups all-purpose flour",
            "1 1/2 cups granulated sugar",
            "3/4 cup unsweetened cocoa powder",
            "1 1/2 tsp baking powder",
            "1 1/2 tsp baking soda",
            "1/2 tsp salt",
            "2 large eggs",
            "1 cup milk",
            "1/2 cup vegetable oil",
            "2 tsp vanilla extract",
            "1 cup boiling water"
        ],
        "instructions": [
            "Preheat the oven to 350°F (175°C). Grease and flour two 9-inch round cake pans.",
            "In a large bowl, mix flour, sugar, cocoa, baking powder, baking soda, and salt.",
            "Add eggs, milk, oil, and vanilla. Beat on medium speed for 2 minutes.",
            "Stir in boiling water. Pour batter into prepared pans.",
            "Bake for 30 to 35 minutes or until a toothpick inserted comes out clean.",
            "Cool for 10 minutes, then remove from pans and frost as desired."
        ],
        "search_tags": ["chocolate", "cake", "dessert", "rich", "moist"],
        "is_vegetarian": True,
        "image_name": "chocolate_cake.png"
    },
    {
        "title": "Lemon Meringue Pie",
        "description": "A tangy lemon filling topped with fluffy meringue on a flaky pie crust.",
        "ingredients": [
            "1 pre-baked pie crust",
            "1 1/2 cups granulated sugar",
            "1/4 cup cornstarch",
            "1/4 tsp salt",
            "1 1/2 cups water",
            "3 large egg yolks",
            "1/2 cup lemon juice",
            "2 tbsp unsalted butter",
            "3 large egg whites",
            "1/4 tsp cream of tartar",
            "6 tbsp granulated sugar"
        ],
        "instructions": [
            "In a saucepan, mix sugar, cornstarch, and salt. Gradually add water and cook over medium heat until thickened.",
            "In a bowl, whisk egg yolks, then add a small amount of hot mixture to temper. Pour back into saucepan and cook for 2 minutes.",
            "Remove from heat and stir in lemon juice and butter. Pour filling into pie crust.",
            "Beat egg whites and cream of tartar until soft peaks form. Gradually add sugar and beat until stiff peaks form.",
            "Spread meringue over pie filling and bake at 350°F (175°C) for 10-12 minutes until golden brown."
        ],
        "search_tags": ["lemon", "meringue", "pie", "tart", "dessert"],
        "is_vegetarian": True,
        "image_name": "lemon_meringue_pie.png"
    },
    {
        "title": "Tiramisu",
        "description": "An Italian dessert made with layers of coffee-soaked ladyfingers and a rich mascarpone cream.",
        "ingredients": [
            "6 large egg yolks",
            "3/4 cup granulated sugar",
            "1 cup mascarpone cheese",
            "1 cup heavy cream",
            "1 cup strong brewed coffee, cooled",
            "1/4 cup coffee liqueur (optional)",
            "24 ladyfingers",
            "Cocoa powder for dusting"
        ],
        "instructions": [
            "Whisk egg yolks and sugar over a double boiler until thick and pale. Remove from heat and stir in mascarpone.",
            "Beat heavy cream until stiff peaks form, then fold into mascarpone mixture.",
            "Combine coffee and liqueur. Dip ladyfingers quickly into coffee and arrange in a dish.",
            "Spread half the mascarpone mixture over ladyfingers. Repeat layers and refrigerate for at least 4 hours.",
            "Dust with cocoa powder before serving."
        ],
        "search_tags": ["tiramisu", "coffee", "dessert", "Italian", "cream"],
        "is_vegetarian": True,
        "image_name": "tiramisu.png"
    },
    {
        "title": "Cheesecake",
        "description": "A creamy and rich cheesecake with a buttery graham cracker crust.",
        "ingredients": [
            "1 1/2 cups graham cracker crumbs",
            "1/4 cup granulated sugar",
            "1/2 cup unsalted butter, melted",
            "4 (8 oz) packages cream cheese, softened",
            "1 cup granulated sugar",
            "1 tsp vanilla extract",
            "4 large eggs",
            "1 cup sour cream",
            "1/4 cup all-purpose flour"
        ],
        "instructions": [
            "Preheat oven to 325°F (160°C). Mix graham cracker crumbs, sugar, and melted butter. Press into the bottom of a springform pan.",
            "Beat cream cheese until smooth. Gradually add sugar and vanilla. Add eggs one at a time, beating well after each addition.",
            "Add sour cream and flour, mix until smooth. Pour over crust.",
            "Bake for 1 hour. Turn off oven and let cake cool in oven with door ajar for 1 hour.",
            "Chill in the refrigerator for at least 4 hours before serving."
        ],
        "search_tags": ["cheesecake", "dessert", "rich", "creamy", "sweet"],
        "is_vegetarian": True,
        "image_name": "cheesecake.png"
    },
    {
        "title": "Brownies",
        "description": "Fudgy brownies with a crackly top and gooey center.",
        "ingredients": [
            "1/2 cup unsalted butter",
            "1 cup granulated sugar",
            "2 large eggs",
            "1 tsp vanilla extract",
            "1/3 cup unsweetened cocoa powder",
            "1/2 cup all-purpose flour",
            "1/4 tsp salt",
            "1/4 tsp baking powder"
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C). Grease and line an 8x8 inch baking pan.",
            "Melt butter and mix with sugar, eggs, and vanilla. Stir in cocoa powder, flour, salt, and baking powder.",
            "Spread batter into prepared pan. Bake for 20-25 minutes.",
            "Cool before cutting into squares."
        ],
        "search_tags": ["brownies", "chocolate", "fudgy", "dessert", "sweet"],
        "is_vegetarian": True,
        "image_name": "brownies.png"
    },
    {
        "title": "Apple Pie",
        "description": "A classic apple pie with a flaky crust and spiced apple filling.",
        "ingredients": [
            "2 1/2 cups all-purpose flour",
            "1 cup unsalted butter, chilled and cubed",
            "1/4 cup granulated sugar",
            "1/4 cup ice water",
            "5 cups peeled and sliced apples",
            "3/4 cup granulated sugar",
            "1/4 cup brown sugar",
            "1/4 cup all-purpose flour",
            "1 tsp cinnamon",
            "1/4 tsp nutmeg",
            "1/4 tsp salt"
        ],
        "instructions": [
            "Preheat oven to 425°F (220°C). In a bowl, mix flour and sugar. Cut in butter until mixture resembles coarse crumbs. Add ice water and mix until dough comes together.",
            "Roll out dough and fit into a pie pan. Mix apples, sugars, flour, cinnamon, nutmeg, and salt. Fill pie crust with apple mixture.",
            "Roll out remaining dough and place over filling. Trim and seal edges. Cut slits in top crust to allow steam to escape.",
            "Bake for 45-50 minutes until crust is golden brown and filling is bubbly."
        ],
        "search_tags": ["apple", "pie", "dessert", "classic", "flaky"],
        "is_vegetarian": True,
        "image_name": "apple_pie.png"
    },
    {
        "title": "Panna Cotta",
        "description": "A creamy Italian dessert made with vanilla and topped with fruit compote.",
        "ingredients": [
            "2 cups heavy cream",
            "1/2 cup granulated sugar",
            "1 vanilla bean, split and scraped",
            "2 tsp gelatin powder",
            "3 tbsp water",
            "Fresh berries for topping"
        ],
        "instructions": [
            "In a saucepan, heat cream, sugar, and vanilla bean until sugar is dissolved. Do not boil.",
            "In a small bowl, dissolve gelatin in water and let sit for 5 minutes. Add to cream mixture and stir until gelatin is dissolved.",
            "Pour mixture into molds and refrigerate for at least 4 hours or until set.",
            "Serve with fresh berries on top."
        ],
        "search_tags": ["panna cotta", "Italian", "cream", "vanilla", "dessert"],
        "is_vegetarian": True,
        "image_name": "panna_cotta.png"
    },
    {
        "title": "Mango Sorbet",
        "description": "A refreshing and fruity sorbet made with ripe mangoes.",
        "ingredients": [
            "4 cups diced ripe mangoes",
            "1 cup granulated sugar",
            "1 cup water",
            "2 tbsp lime juice"
        ],
        "instructions": [
            "In a blender, combine mangoes, sugar, water, and lime juice. Blend until smooth.",
            "Pour mixture into an ice cream maker and churn according to manufacturer's instructions.",
            "Transfer to a container and freeze until firm."
        ],
        "search_tags": ["mango", "sorbet", "fruit", "dessert", "refreshing"],
        "is_vegetarian": True,
        "image_name": "mango_sorbet.png"
    },
    {
        "title": "Creme Brulee",
        "description": "A creamy vanilla custard with a caramelized sugar topping.",
        "ingredients": [
            "2 cups heavy cream",
            "1 vanilla bean, split and scraped",
            "5 large egg yolks",
            "1/2 cup granulated sugar",
            "Additional sugar for caramelizing"
        ],
        "instructions": [
            "Preheat oven to 325°F (160°C). Heat cream and vanilla bean in a saucepan until just boiling. Remove from heat and let steep.",
            "Whisk egg yolks and sugar until pale. Gradually add hot cream to egg yolks, whisking constantly.",
            "Strain mixture into ramekins. Place ramekins in a baking dish and fill with hot water halfway up the sides.",
            "Bake for 40-45 minutes until custards are set but still slightly wobbly in the center.",
            "Chill custards for at least 2 hours. Before serving, sprinkle sugar on top and caramelize with a torch."
        ],
        "search_tags": ["creme brulee", "vanilla", "custard", "caramel", "dessert"],
        "is_vegetarian": True,
        "image_name": "creme_brulee.png"
    },
    {
        "title": "Raspberry Cheesecake Bars",
        "description": "Cheesecake bars with a raspberry swirl on a graham cracker crust.",
        "ingredients": [
            "1 1/2 cups graham cracker crumbs",
            "1/4 cup granulated sugar",
            "1/2 cup unsalted butter, melted",
            "2 (8 oz) packages cream cheese, softened",
            "1 cup granulated sugar",
            "1 tsp vanilla extract",
            "2 large eggs",
            "1 cup sour cream",
            "1/4 cup all-purpose flour",
            "1/2 cup raspberry puree"
        ],
        "instructions": [
            "Preheat oven to 325°F (160°C). Mix graham cracker crumbs, sugar, and melted butter. Press into the bottom of a baking pan.",
            "Beat cream cheese until smooth. Gradually add sugar and vanilla. Add eggs one at a time, beating well after each addition.",
            "Add sour cream and flour, mix until smooth. Pour over crust.",
            "Drop raspberry puree over cheesecake batter and swirl with a knife.",
            "Bake for 45-50 minutes until set. Cool and refrigerate for at least 4 hours before cutting into bars."
        ],
        "search_tags": ["cheesecake", "raspberry", "bars", "dessert", "sweet"],
        "is_vegetarian": True,
        "image_name": "raspberry_cheesecake_bars.png"
    },
    {
        "title": "Sticky Toffee Pudding",
        "description": "A moist sponge cake covered in a rich toffee sauce.",
        "ingredients": [
            "1 cup chopped dates",
            "1 cup boiling water",
            "1 tsp baking soda",
            "1/2 cup unsalted butter",
            "1/2 cup granulated sugar",
            "2 large eggs",
            "1 cup all-purpose flour",
            "1 tsp baking powder",
            "1/2 tsp salt",
            "1 cup heavy cream",
            "1/2 cup brown sugar"
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C). Grease and flour a baking dish.",
            "Combine dates, baking soda, and boiling water. Let sit for 10 minutes.",
            "In a bowl, cream butter and sugar until light and fluffy. Beat in eggs one at a time.",
            "Mix in flour, baking powder, and salt. Stir in date mixture.",
            "Pour batter into prepared dish and bake for 30-35 minutes.",
            "For the sauce, heat cream and brown sugar until sugar is dissolved. Pour over warm pudding."
        ],
        "search_tags": ["sticky toffee pudding", "toffee", "cake", "dessert", "sweet"],
        "is_vegetarian": True,
        "image_name": "sticky_toffee_pudding.png"
    },
    {
        "title": "Banana Bread",
        "description": "A moist and flavorful banana bread with walnuts.",
        "ingredients": [
            "1/2 cup unsalted butter, softened",
            "1 cup granulated sugar",
            "2 large eggs",
            "1 cup mashed ripe bananas",
            "1 tsp vanilla extract",
            "1 1/2 cups all-purpose flour",
            "1 tsp baking powder",
            "1/2 tsp baking soda",
            "1/4 tsp salt",
            "1/2 cup chopped walnuts (optional)"
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C). Grease and flour a loaf pan.",
            "Cream butter and sugar until light and fluffy. Beat in eggs one at a time.",
            "Mix in bananas and vanilla. Combine flour, baking powder, baking soda, and salt. Gradually add to banana mixture.",
            "Fold in walnuts. Pour batter into prepared pan.",
            "Bake for 60-70 minutes until a toothpick comes out clean. Cool before slicing."
        ],
        "search_tags": ["banana", "bread", "dessert", "moist", "sweet"],
        "is_vegetarian": True,
        "image_name": "banana_bread.png"
    }
]

# Create and save recipes
for recipe in dessert_recipes:
    # Prepare the image file path
    image_path = os.path.join(media_root, recipe['image_name'])

    # Create the Recipe instance
    new_recipe = Recipe(
        title=recipe['title'],
        description=recipe['description'],
        ingredients=recipe['ingredients'],
        instructions=recipe['instructions'],
        search_tags=recipe['search_tags'],
        is_vegetarian=recipe['is_vegetarian']
    )

    # Save the image if it exists
    if os.path.exists(image_path):
        with open(image_path, 'rb') as img_file:
            django_file = File(img_file, name=recipe['image_name'])
            new_recipe.image.save(recipe['image_name'], django_file, save=True)

    # Save the Recipe instance
    new_recipe.save()
    print(f"Added recipe: {recipe['title']}")

print("Dessert recipes added successfully.")
