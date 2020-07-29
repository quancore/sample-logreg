import sys
import os
import shutil
import time
import traceback
import pickle

from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# this api is very fast prototyping, so to make it simple, I just put all
# parameters to here
# inputs
training_data = 'data/diabetes.csv'
target = 'label'

model_directory = 'model'
model_name = 'logreg.pkl'
# model_columns_file_name = f'{model_directory}/model_columns.pkl'

# These will be populated at training time
features = None
model = None


@app.route('/predict', methods=['POST'])
def predict():
    """ Create http://host:port/predict POST end point. Input format: {"feature name": value} """
    if model:
        try:
            # capture the json from POST
            json_ = request.json
            query = pd.DataFrame(json_)
            print(query)
            query = query.reindex(columns=features, fill_value=0)

            prediction = list(model.predict(query))

            return jsonify({'prediction': [int(x) for x in prediction]})

        except Exception as e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print('No model has been found')
        return 'No model has been found'


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 8000

    try:
        model_path = os.path.join(model_directory, model_name)
        model = pickle.load(open(model_path, 'rb'))
        print('Model has been loaded')
        features = [col for col in model.columns if col != target]
        print(f'Model features has been loaded: {features}')

    except Exception as e:
        raise ValueError(f'Model has not been loaded with this error: {str(e)}')

    app.run(host='0.0.0.0', port=port, debug=False)
