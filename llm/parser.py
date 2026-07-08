import json

from tools.registry import TOOLS


def parse_response(llm_response: str):
    """
    Parse and validate the LLM response.

    Expected format:

    {
        "tool": "...",
        "arguments": {
            ...
        }
    }
    """

    try:

        # Remove markdown if the model returns ```json ... ```
        cleaned = (
            llm_response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        decision = json.loads(cleaned)

    except json.JSONDecodeError:

        return {
            "success": False,
            "error": "Invalid JSON returned by the LLM."
        }
    # validating tool

    tool_name = decision.get("tool")

    if tool_name not in TOOLS:

        return {
            "success": False,
            "error": f"Unknown tool: {tool_name}"
        }

    tool = TOOLS[tool_name]


    # Validate arguments


    arguments = decision.get("arguments", {})

    missing = []

    for parameter in tool.parameters:

        if parameter not in arguments:
            missing.append(parameter)

    return {

        "success": True,

        "tool": tool,

        "arguments": arguments,

        "missing_arguments": missing
    }

    