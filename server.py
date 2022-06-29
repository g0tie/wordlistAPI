from flask import Flask, request, jsonify
import linecache
import itertools

app = Flask(__name__)

# Get one word from the list
@app.route("/rocku/<index>", methods=['GET'])
def getWord(index):
    with open('rockyou.txt', 'r', encoding = "ISO-8859-1") as file:
        lines = file.readlines()
    word = lines[ int(index) ]

    return jsonify(word.replace('\n', ''))

# Get a custom list from a range of lines
@app.route("/rocku/range", methods=['GET'])
def getWordsByRange():
    args = request.args
    start = int( args.get("start") )
    end = int( args.get("end") )
    words = []

    with open('rockyou.txt', 'r', encoding = "ISO-8859-1") as file:
        for index, text in enumerate(file):
            if start <= index <= end:
                words.append(text)


    return ''.join(words)

# Get a custom list ending at a given line
@app.route("/rocku/<index>/lines", methods=['GET'])
def getWords(index):
    words = []

    with open('rockyou.txt', 'r', encoding = "ISO-8859-1") as file:
        for i, text in enumerate(file):
            if i == int( index ):
                break

            words.append(text)

    return ''.join(words)
