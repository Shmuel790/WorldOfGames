from utils import *

def add_score(difficulty):
    points_of_winning = (int(difficulty) * 3) +5
    try:
        with open(scores_file_name, 'r') as file:
            scores = file.read()
            add_points = int(scores) + points_of_winning
        with open(scores_file_name, 'w') as file:
            file.write(str(add_points))
    except:
        with open(scores_file_name, 'w') as file:
            file.write(str(points_of_winning))
