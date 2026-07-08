from tools.registry import TOOLS


def build_system_prompt():
    """
    Dynamically build the system prompt from all
    registered tools.
    """

    prompt = """
You are an AI Email Agent.

Your job is to choose the correct tool based on the user's request.

You MUST respond ONLY with valid JSON.

Return this format:

{
    "tool": "<tool_name>",
    "arguments": {
        ...
    }
}

Available Tools:

"""

    for tool in TOOLS.values():

        prompt += f"""
Tool Name:
{tool.name}

Description:
{tool.description}

Parameters:
"""

        if tool.parameters:

            for parameter in tool.parameters:

                prompt += f"- {parameter}\n"

        else:

            prompt += "None\n"

        prompt += "\n--------------------------\n"

    return prompt