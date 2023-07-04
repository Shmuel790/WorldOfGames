from flask import Flask
from utils import *

def score_server():
    try:
        file = open(scores_file_name, 'r')
        score = file.read()
        server = f'''<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1>The score is <div id="score">{score}</div></h1>
</body>
</html>'''

    except:
        server = '''<html>
<head>
<title>Scores Game</title>
</head>
<body>
<body>
<h1><div id="score" style="color:red">'ERROR'</div></h1>
</body>
</html>'''

