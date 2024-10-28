import pydantic

class Recipe(pydantic.BaseModel):
    name: str
    description: str
    ingredients: List[str]
    steps: List[str]
    tags: List[str]
    image: str
    source: str

    class Config:
        orm_mode = True

    def __init__(self, **data):
        super().__init__(**data)
        self.id = None

    def __repr__(self):
        return f"<Recipe {self.name}>"