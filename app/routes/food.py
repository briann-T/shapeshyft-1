from fastapi import APIRouter, HTTPException, Security
from app.schemas.food import (
    Food,
    FoodSearchResponse,
    FoodCreateRequest,
    FoodModel as FoodModelSchema,
    TotalCaloriesResponse,
)
from typing import Annotated
from app.services.auth.utils import get_current_user
from app.models.food import FoodType, Food as FoodModel
from app.utils.response import responses
from app.utils.exception import ShapeShyftException
from app.services.auth import hash_password
from fatsecret import Fatsecret
from app.models.user import UserAccount
from decimal import Decimal

fs = Fatsecret("0047da412ebd469c9dd1895c7d3159d8", "2f91d6bcbaa94e72bea327eb4d6b0546")
# create a search endpoint

router = APIRouter(
    tags=["Food & Calories"],
)


# create foood
@router.post("/", response_model=FoodModelSchema, responses=responses)
async def create_food_for_user(
    data: FoodCreateRequest, current_user: UserAccount = Security(get_current_user)
):
    """
    This endpoint creates a food item for the user
    """
    food = await FoodModel.create(**data.dict(), user=current_user)
    return food


@router.get("/search", response_model=FoodSearchResponse, responses=responses)
async def search_food_database(
    query: str, current_user: UserAccount = Security(get_current_user)
):
    """
    This endpoint searches for food items based on the query string
    """
    foods = fs.foods_search(query)
    foods_array = []
    for food in foods:
        food_description = food["food_description"]
        food_description_array = food_description.split("-")
        unit = food_description_array[0].strip()
        food_nutrients = food_description_array[1].split("|")
        calories = food_nutrients[0].strip().split(":")[1].strip()[:-4]
        fat = food_nutrients[1].strip().split(":")[1].strip()[:-1]
        carbs = food_nutrients[2].strip().split(":")[1].strip()[:-1]
        protein = food_nutrients[3].strip().split(":")[1].strip()[:-1]

        link = food["food_url"]
        name = food["food_name"]
        food = Food(
            name=name,
            unit=unit,
            calories=calories,
            fat=fat,
            carbs=carbs,
            protein=protein,
            link=link,
        )
        foods_array.append(food)

    foods = FoodSearchResponse(items=foods_array)
    return foods


# get sum of all calories for user
@router.get("/totalCalories", response_model=TotalCaloriesResponse, responses=responses)
async def get_sum_of_calories_for_user(
    current_user: UserAccount = Security(get_current_user),
):
    """
    This endpoint gets the sum of all calories for the user
    """
    foods = await FoodModel.all().filter(user=current_user)
    calories = Decimal(0.0)
    for food in foods:
        try:
            calories += Decimal(food.calories) * Decimal(food.number_of_units)
        except Exception as e:
            print(e)
    return TotalCaloriesResponse(total_calories=calories)


# get all by type
@router.get("/{type}", response_model=list[FoodModelSchema], responses=responses)
async def get_food_by_type_for_user(
    type: FoodType, current_user: UserAccount = Security(get_current_user)
):
    """
    This endpoint gets all food items by type for the user
    """
    foods = await FoodModel.all().filter(user=current_user, type=type)
    return foods
