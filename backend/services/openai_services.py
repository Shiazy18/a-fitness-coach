from openai import AzureOpenAI
from config import settings

client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_KEY,
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_version=settings.AZURE_OPENAI_VERSION
)

def generate_fitness_plan(user):
    prompt = f"""
    You are an expert fitness and nutrition coach.
    Create a detailed 7-day plan based on this profile:

    Age: {user['age']}
    Weight: {user['weight']}
    Height: {user['height']}
    Goal: {user['goal']}
    Activity Level: {user['activity_level']}
    Diet Preference: {user['diet_preference']}

    Include:
    - Daily workouts (sets + reps)
    - Meal plan with calories/macros
    - Tips & motivation
    """

    response = client.chat.completions.create(
        model=settings.AZURE_OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1200
    )

    return response.choices[0].message["content"]
