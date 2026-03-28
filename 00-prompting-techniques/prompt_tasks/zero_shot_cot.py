import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

area = input("Enter area name: ")
days = int(input("Enter no. of days for the trip: "))

prompt = f'''

    You are a Trip planner. You will have the information of number of days and area name.

    Let's think step-by-step
    - Plan locations to visit in those days
    - Suggest Famous food in that area
    - Do not hallucinate if you do not know about that area 
    - Return a message that "I do not have idea on this place that you want to visit".
    - What is the precautions they have to take.
    - Each point has to be simple in one bullet point and human understandable.

    Input:
    Area: {area}
    days: {days} 

    Output:
'''
print(get_completion(prompt))