import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

sentence = input("Enter Any Sentence You Want To Translate Into Telugu: ")

prompt = f'''
    Translate the below english sentence into Telugu in simple line:
    sentence: {sentence}
'''

print(get_completion(prompt))

