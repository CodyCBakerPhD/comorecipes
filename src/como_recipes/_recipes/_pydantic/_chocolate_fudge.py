from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class ChocolateFudge(Recipe):
    name: str = "Chocolate Fudge"
    measurements: tuple[Measurement] = (
        MeasurementRegistry.get_measurement(amount=1.0, unit="lb.", name="powdered sugar"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="dutch cocoa powder"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="butter"),
        MeasurementRegistry.get_measurement(amount=0.25, unit="cup", name="chocolate milk"),
        MeasurementRegistry.get_measurement(amount=1.0, unit="tbsp.", name="vanilla"),
        MeasurementRegistry.get_measurement(amount=0.5, unit="cup", name="chopped walnuts or pecans, optional"),
    )
    instructions: tuple[str] = (
        "One of several variations on chocolate fudge.",
        "Line a 6 x 8 pan with parchment paper misted very lightly with cooking spray.",
        "Sift powdered sugar and cocoa powder. Cube butter into 1 inch chunks.",
        "Pour an inch or two of water into a saucepan, then bring to a simmer.",
        "Place powdered sugar, cocoa powder, butter, and milk into a large bowl, then place the bowl on top of the saucepan with simmering water.",
        "Cook, whisking regularly, until the butter has melted, and the mixture is smooth.",
        "Remove from heat, stir in the vanilla and optional chopped nuts, then pour quickly into prepared pan.",
        "Chill until solidified.",
    )


default_recipe_registry.add_recipe(recipe=ChocolateFudge())
