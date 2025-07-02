import asyncio
from typing import Annotated
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext

AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3ZWM1NTU3OS01MDRjLTQxODQtYTM1OC0yNzQzMmFhM2VlYzUiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjliZGFkY2U0LTkyZmItNDA2Yi1iOThiLTgzNDgwZDAzMzFkZSJ9.BrSl3wmdcFVKmnqfkt8DF_ltkjgEoyShzjOESOwx7ec" # noqa: E501
session = GenAISession(jwt_token=AGENT_JWT)


@session.bind(
    name="generate_email_prompt",
    description="This agent returns email prompt"
)
async def generate_email_prompt(
    agent_context: GenAIContext,
    test_arg: Annotated[
        str,
        "This is a test argument. Your agent can have as many parameters as you want. Feel free to rename or adjust it to your needs.",  # noqa: E501
    ],
):
    # Split into lines
    lines = test_arg.strip().split("\n")
    
    # Initialize values
    recipient = ""
    purpose = ""
    key_points = []

    # Parse each line
    for line in lines:
        if line.lower().startswith("recipient:"):
            recipient = line.split(":", 1)[1].strip()
        elif line.lower().startswith("purpose:"):
            purpose = line.split(":", 1)[1].strip()
        elif line.strip().startswith("-"):
            key_points.append(line.strip().lstrip("- ").strip())

    # Create a bullet point string for prompt
    key_points_text = "\n".join([f"- {point}" for point in key_points])

    # Build the final prompt
    prompt = f"""
You are a helpful assistant that writes professional and respectful emails.

Generate an email using the following details:
Recipient: {recipient}
Purpose: {purpose}
Key Points:
{key_points_text}

Structure the email with:
- A subject line
- A greeting using the recipient’s name or title
- A clear and concise body incorporating all key points
- A professional closing

Keep the tone natural and polite.
"""

    return prompt


async def main():
    print(f"Agent with token '{AGENT_JWT}' started")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
