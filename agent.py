from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Connect to Gemini
client = genai.Client(api_key=api_key)


def create_plan(goal):
    prompt = f"""
You are an AI planning agent.

The user has given you this goal:

{goal}

Break this goal into 3 clear, practical steps.
Return only the numbered steps.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text


def execute_plan(goal, plan):
    prompt = f"""
You are an AI execution agent.

User goal:
{goal}

The planner created this plan:
{plan}

Now execute the plan conceptually and produce a useful,
structured result for the user.

Do not simply repeat the plan.
Actually provide the result of carrying out the steps.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text


def review_result(goal, result):
    prompt = f"""
You are an AI review agent.

User goal:
{goal}

The executor produced this result:

{result}

Review the result.

Identify:
1. What was done well
2. What is missing
3. What should be improved

Give concise and useful feedback.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text

def improve_result(goal, result, feedback):
    prompt = f"""
You are an AI improvement agent.

User goal:
{goal}

Original result:
{result}

Review feedback:
{feedback}

Improve the original result using the reviewer's feedback.

Return only the improved final result.
Make it practical, clear, and well structured.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text

