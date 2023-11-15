from pydantic import UUID4, BaseModel, EmailStr, validator, Field


from .general import Response

from app.models.food import FoodType, Food as FoodModel, Calories as CalorieModel

from tortoise.contrib.pydantic import pydantic_model_creator
from decimal import Decimal

# create pydantic model for FoodModel using create_tortoise_model
FoodModel = pydantic_model_creator(
    FoodModel, name="FoodModel", exclude=["type", "user"]
)

CalorieModel = pydantic_model_creator(
    CalorieModel, name="CalorieModel", exclude=["type", "user"]
)

class Food(BaseModel):
    name: str
    unit: str
    calories: str
    fat: str
    carbs: str
    protein: str
    link: str
    number_of_units: int = 1


class FoodSearchResponse(Response):
    items: list[Food]


class FoodCreateRequest(Food):
    type: FoodType


class TotalCaloriesResponse(Response):
    total_calories: Decimal

class PredictCaloriesRequest(BaseModel):
    weight: float
    height: float
    age: int

class CaloriePredictionResponse(Response):
    calories: float

