import re
import random
import sys

def roll_dice(dice_string):
    """
    Rolls dice based on a string like "2d12+6-(1d4+1)+8".

    Args:
        dice_string: The string representing the dice roll expression.

    Returns:
        The integer result of the dice roll expression.  Returns None if the input is invalid.
    """

    def replace_dice(match):
        """Replaces a dice roll expression (e.g., "2d12") with its result."""
        try:
            num_dice, num_sides = map(int, match.group(1).split('d'))
            if num_dice <= 0 or num_sides <= 0:
                return match.group(0)  # Return original if invalid format
            rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
            return str(sum(rolls))
        except ValueError:
            return match.group(0)  # Return original if parsing fails

    # Replace all dice rolls with their results
    modified_expression = re.sub(r'(\d+d\d+)', replace_dice, dice_string)

    try:
        # Evaluate the modified expression
        result = eval(modified_expression)
        return int(result)  # Ensure integer result
    except (SyntaxError, TypeError):
        print("Invalid expression. Please check your syntax.")
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: diceroller.py \"<dice expression>\"")
        print("Example: diceroller.py \"2d12+6-(1d4+1)+8\"")
    else:
        expression = sys.argv[1]
        result = roll_dice(expression)
        if result is not None:
            print(result)