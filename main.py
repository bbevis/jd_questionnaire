# Take in number of firms selected
# Samples random 3 questions per firm without replacement


import questions as qs
import random
import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def rand_questions():

    # get variables parsed fromm url
    n_firms = int(request.args.get('n_firms', ''))
    n_questions = n_firms * 3

    # get list of questions and randomly sample without replacement
    questions = qs.questions
    rand_questions = random.sample(questions, n_questions)

    # get key values of rando questions per firm
    values = get_values(n_firms, rand_questions)
    keys = ['firm' + str(i+1) for i in range(n_firms)]

    return json.dumps(dict(zip(keys, values))) # convert to json dictionary

def get_values(n_firms, rand_questions):

    # add first 3 elements into vales
    # remove those same elementsfrom rand_questions

    values = []

    for i in range(n_firms):
        values.append(rand_questions[:3])
        rand_questions = rand_questions[3:]
    return values

if __name__ == "__main__":
    app.run(debug=True)

    # print(rand_questions(2))
