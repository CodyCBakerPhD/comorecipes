from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class HoneyGarlicSalmon(Recipe):
    name: str = "Honey Garlic Salmon"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=4.0, unit="salmon", name="fillets, 250 g each"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp", name="salt"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp", name="black pepper"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="tsp", name="paprika"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tbsp", name="butter"),
        MeasurementRegistry.get_measurement(amount=4.0, unit="cloves", name="garlic, finely chopped"),
        MeasurementRegistry.get_measurement(amount=4.0, unit="tbsp", name="honey"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp", name="water"),
        MeasurementRegistry.get_measurement(amount=2.0, unit="tsp", name="soy sauce"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp", name="fresh lemon juice"),
        MeasurementRegistry.get_measurement(amount=4.0, unit="lemon", name="wedges to garnish"),
    )
    instructions: tuple[str, ...] = (
        "Move oven shelf to middle. Preheat to broil/grill settings on medium heat. Season salmon with salt, pepper, paprika. Set aside.",
        "Heat butter in a skillet over medium-high heat until melted. Add garlic and saute for a minute. Pour in honey, water, and soy sauce. Allow flavors to heat through.",
        "Add lemon juice, stir well to combine. Add the salmon to the sauce in the pan, cook each fillet for 3-4 minutes or until golden. Baste the tops with the pan juices.",
        "Season with salt and pepper to taste. Add lemon wedges around salmon if desired. Baste salmon one more time, transfer pan to the oven to broil/grill for 5-6 minutes.",
        "To serve, drizzle with sauce and a squeeze of lemon juice.",
    )


default_recipe_registry.add_recipe(recipe=HoneyGarlicSalmon())
