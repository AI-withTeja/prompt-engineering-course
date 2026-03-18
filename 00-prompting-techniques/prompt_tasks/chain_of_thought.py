import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = f'''

    Solve the following aptitude questions on topic "Problems on Trains".
    Use the given example as a reference and follow the same format for answering:
    - Select the correct option
    - Provide a step-by-step Explanation
    
    Example:
    
    Question 1: A train running at the speed of 60 km/hr crosses a pole in 9 seconds. What is the length of the train?
        Option A: 120 metres
        Option B: 180 metres
        Option C: 324 metres
        Option D: 150 metres
    Answer: Option D
    
    Explanation:
        Speed =	60 x (5/18) m/sec =	50/3 m/sec.

        Length of the train = (Speed x Time).

        Therefore, Length of the train =	(50/3)	x 9 m = 150 metres.
    
    Now solve:

    Question 2: A train 125 m long passes a man, running at 5 km/hr in the same direction in which the train is going, in 10 seconds. The speed of the train is:
        Option A: 45 km/hr
        Option B: 54 km/hr
        Option C: 50 km/hr
        Option D: 55 km/hr
    Answer: 
    
    Explanation: 
    
'''

print(get_completion(prompt))