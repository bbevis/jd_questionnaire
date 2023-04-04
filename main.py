# Take in number of firms selected
# Samples random 3 questions per firm without replacement


import LUT as lut
import random
import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def all_questions():

    # get variables parsed fromm url
    # EY_select = int(request.args.get('EY_select', ''))
    # BCG_select = int(request.args.get('BCG_select', ''))
    # Leonnova_select = int(request.args.get('Leonnova_select', ''))
    # Innovia_select = int(request.args.get('Innovia_select', ''))
    # Systemlogic_select = int(request.args.get('Systemlogic_select', ''))

    # get list of questions and randomly sample without replacement
    questions = random.sample(lut.optional_questions, len(lut.optional_questions))
    indepth_questions = random.sample(lut.indepth_questions, len(lut.indepth_questions))
    keys = random.sample(lut.optional_keys, len(lut.optional_keys))
    indepth_keys = random.sample(lut.indepth_keys, len(lut.indepth_keys))
    
    questions.extend(indepth_questions)
    keys.extend(indepth_keys)

    return json.dumps(dict(zip(keys, questions)))


if __name__ == "__main__":
    app.run(debug=True)

    # print(all_questions())
