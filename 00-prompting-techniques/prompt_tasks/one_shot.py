import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

sentence = input("Enter Statement: ")

prompt = f'''

Convert the sentence into Polite and Professional tone in simple line:
    Example:
        Input: Send me the report now.
        Output: Could you please send me the report?
    Now Solve this:
        Input: {sentence} 
        Output: 
'''
print(get_completion(prompt))