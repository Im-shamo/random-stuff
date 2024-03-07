from os import path as p
import user_input as u

def get_dir(question:str, default:str):
    print(f"Current path: {p.abspath(".")}")
    anwser = u.get_input(question, default)

    path = p.abspath(anwser)
    return path if p.isdir(path) else None
