**PROPOSED ACTION:** Add banana bread recipe to Dasharo documentation

**Solution:**

Create a new file `docs/recipes/banana_bread.md` with the following content:

```markdown
# Banana Bread Recipe

## Ingredients

* 3 large ripe bananas, mashed
* 1 1/2 cups all-purpose flour
* 1 tsp baking powder
* 1/2 tsp baking soda
* 1/2 tsp salt
* 1/4 cup unsalted butter, melted
* 1 cup granulated sugar
* 2 large eggs
* 1 tsp vanilla extract
* Optional: chopped walnuts or pecans

## Instructions

1. Preheat oven to 350°F (180°C). Grease a 9x5-inch loaf pan.
2. In a large mixing bowl, combine flour, baking powder, baking soda, and salt.
3. In a separate bowl, mix together mashed bananas, sugar, melted butter, eggs, and vanilla extract.
4. Add the dry ingredients to the wet ingredients and stir until just combined.
5. Fold in optional chopped nuts, if using.
6. Pour the batter into the prepared loaf pan and smooth the top.
7. Bake for 55-60 minutes or until a toothpick inserted into the center comes out clean.
8. Let the bread cool in the pan for 10 minutes before transferring it to a wire rack to cool completely.

## Notes

* This recipe makes one 9x5-inch loaf.
* You can store the bread at room temperature for up to 3 days or wrap it tightly and freeze for up to 2 months.
```

**PROPOSED ACTION:** Update `docs/README.md` to include a link to the banana bread recipe

```markdown
# Dasharo Documentation

...

## Recipes

* [Banana Bread Recipe](recipes/banana_bread.md)

...
```

**PROPOSED ACTION:** Add a link to the banana bread recipe to the Dasharo documentation navigation menu

```html
<!-- docs/_layouts/navbar.html -->

...

<nav>
  ...
  <li><a href="recipes/banana_bread.md">Recipes</a></li>
  ...
</nav>

...
```

This solution adds a new recipe to the Dasharo documentation and updates the navigation menu to include a link to the recipe.