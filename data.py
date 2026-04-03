import json
import os

base=os.path.dirname(__file__)
file_path=os.path.join(base,"dataset.json")
def load_contacts():
    try:
        with open(file_path,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(Contact):
        with open(file_path,"w") as file:
            json.dump(Contact,file,indent=1)