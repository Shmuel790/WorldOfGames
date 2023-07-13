from flask import Flask
from utils import *


def score_server():
    with open(scores_file_name, 'r') as f:
        score = f.readline()
    server = f'''
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">{score}</div></h1>
        </body>
    </html>

    # <html>
    #     <head>
    #         <title>Scores Game</title>
    #     </head>
    #     <body>
    #         <h1><div id="score" style="color:red">'ERROR'</div></h1>
    #     </body>
    # </html>'''

    return server
