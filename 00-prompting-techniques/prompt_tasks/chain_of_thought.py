import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

query = input("Enter query related to React: ")

prompt = f'''

    You are a React Frontend Trainer of 15 years of experience.
    
    Explain about the concepts step-by-step clearly with professional tone.
    
    - Explain concept in 2 lines
    - Give an example where they apply that concept in real-world
    - Give simple example for it in React
    - Do not make it long explanation
    - Make it short as much as possible
    
    Input: {query}
    Output: 

    
'''

print(get_completion(prompt))