import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

inp = input("Enter query: ")

prompt = f'''
    Classify the following ticket into:
    - Technical Issue
    - Billing Issue
    - Account Issue
    - General Query
    
    Example 1:
    Input: The app crashes when I try to login.
    Output: Technical Issue

    Example 2:
    Input: I was charged twice for my subscription.
    Output: Billing Issue

    Example 3:
    Input: I forgot my password and cannot access my account.
    Output: Account Issue

    Example 4:
    Input: How do I change my profile picture?
    Output: General Query

    Example 5:
    Input: Payment failed but money was deducted.
    Output: Billing Issue

    Now classify the following:

    Input: {inp}
    Output:
'''

res = get_completion(prompt)
print(res) 