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
    Create a detailed 7-day plan based on this profile in STRICT JSON FORMAT.:

    User Profile:
    Age: {user['age']}
    Weight: {user['weight']}
    Height: {user['height']}
    Goal: {user['goal']}
    Activity Level: {user['activity_level']}
    Diet Preference: {user['diet_preference']}

    JSON FORMAT (DO NOT ADD EXTRA TEXT):

    {{
      "workout": {{
        "type": "",
        "exercises": [
          {{ "name": "", "sets": 0, "reps": 0 }}
        ],
        "calories_burned": 0
      }},
      "diet": {{
        "meals": [
          {{ "meal": "", "items": [""], "calories": 0 }}
        ],
        "total_calories": 0
      }}
    }}
    """

    response = client.chat.completions.create(
        model=settings.AZURE_OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        top_p=0.9
    )

    choice = response.choices[0]
    msg = getattr(choice, "message", None) or (choice.get("message") if isinstance(choice, dict) else None)
    if hasattr(msg, "content"):
        return msg.content
    if isinstance(msg, dict):
        return msg.get("content")
    # Fallback: try common properties
    return getattr(choice, "text", None) or str(choice)
    #return response.choices[0].message["content"]
