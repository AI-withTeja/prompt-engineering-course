import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

inp = input("Enter your junk food intake: ")

prompt = f'''
    Classify the users health into 3 categories based on their junk intake:
    Categories:
    - Low Risk
    - Medium Risk
    - High Risk
    
    Example:
        Example 1:
        Input: I eat fast food once a week and mostly eat home-cooked meals.
        Output: Low Risk

        Example 2:
        Input: I eat burgers and snacks 2-3 times a week and drink soft drinks occasionally.
        Output: Moderate Risk

        Example 3:
        Input: I eat junk food every day and drink sugary beverages multiple times daily.
        Output: High Risk
    Now Answer This Input:
        input: {inp}
        output:
    
'''

print(get_completion(prompt))