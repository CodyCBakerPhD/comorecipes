from ..._base_measurement import Measurement
from ..._base_recipe import Recipe
from ..._measurement_registration import MeasurementRegistry
from ..._recipe_registration import default_recipe_registry


class CornbreadDressing(Recipe):
    name: str = "Cornbread Dressing"
    measurements: tuple[Measurement, ...] = (
        MeasurementRegistry.get_measurement(amount=2, unit="portions", name="of cornbread"),
        MeasurementRegistry.get_measurement(amount=2, unit="tbsp", name="butter"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="cup", name="chopped celery"),
        MeasurementRegistry.get_measurement(amount=1, unit="small", name="white onion"),
        MeasurementRegistry.get_measurement(amount=2, unit="cups", name="not-chicken stock"),
        MeasurementRegistry.get_measurement(amount=2, unit="tbsp", name="dried sage"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp", name="salt"),
        MeasurementRegistry.get_measurement(amount=1 / 2, unit="tsp", name="pepper"),
    )
    instructions: tuple[str, ...] = (
        "Make cornbread 1-2 days in advance, crumble and leave to dry. Melt butter and saute celery and onion until soft.",
        "Combine with cornbread. If not stuffing into turkey, then incorporate stock and spices. If stuffing, only incorporate the spices.",
        "Bake for 30 minutes at 350 F.",
    )


default_recipe_registry.add_recipe(recipe=CornbreadDressing())
