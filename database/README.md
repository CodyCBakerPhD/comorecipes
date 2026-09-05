# Notes

The 'ingredients' in high-level recipes are officially referred to as 'measurements' in the low-level API.

By convention, the ingredients of a recipe are listed in the order they are incorporated.



### Recipes as ingredients

An ingredient written with the same name as another recipe (such as `marinara sauce` in Spaghetti) is that recipe, and the site links the two pages both ways. A recipe never counts as its own ingredient (Rice measures out `rice`, the grain).

When the ingredient is not written exactly as the recipe's name, add a `recipe` key with the other recipe's file stem:

```yaml
- amount: '1'
  unit: portions
  ingredient: biscuits
  recipe: buttermilk_biscuits
```

The site build fails if that stem does not exist.

When an ingredient shares a recipe's name but means the plain ingredient, set the key to `null` so the two are not linked (Cornbread Dressing sautees raw `celery`; it does not call for the Celery snack):

```yaml
- amount: '2'
  unit: portions
  ingredient: celery
  recipe: null
```



### Default references

There are several ingredients which are shortened for readability, but are expanded here for reference.

|      Default       |             Full name              |
|:------------------:|:----------------------------------:|
|       sugar        |       granulated white sugar       |
|       flour        |         all-purpose flour          |
|       butter       |          unsalted butter           |
|        milk        |              2% milk               |
|   condensed milk   |      sweetened condensed milk      |
|    brown sugar     |         light brown sugar          |
|      vanilla       |          vanilla extract           |
|      cinnamon      |          ground cinnamon           |
|        sage        |         dried ground sage          |
|       ginger       |        dried ground ginger         |
|      parsley       |        dried parsley flakes        |
|    fresh ginger    |         fresh ginger root          |
|       pepper       |        ground black pepper         |
|       yeast        |          active dry yeast          |
|     olive oil      |       extra virgin olive oil       |
|       cream        |            heavy cream             |
|       squash       |           yellow squash            |
|        rice        |             white rice             |
|     mushrooms      |   baby bella (button) mushrooms    |
|     chickpeas      |          dried chickpeas           |
|  crushed tomatoes  |  canned crushed tomatoes (28 oz.)  |
|    green beans     |         fresh green beans          |
|       onion        |            white onion             |



### Default practices

Onions and garlic will always be chopped.

Fresh tomatoes should be the ripest able to be purchased (usually from Costco), ideally garden grown.

Potatoes are always scrubbed thoroughly or peeled if necessary.



### Quality

All chocolate references assume the highest quality available, such as Ghirardelli.

All cocoa powders assume Dutch processed.

Vanilla extract is assumed to be pure, not synthetic.
