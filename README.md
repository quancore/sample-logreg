This repo contains an example machine learning application using Logistic regression. The task and dataset: https://www.kaggle.com/uciml/pima-indians-diabetes-database
**Properties:**
- The model pipeline has been trained on *logreg_train.ipynb*. The notebook pickles the model on *model* folder.
- The Flask API has been exposed on *api.py*. Currently, only predict[POST] method has been implemented.
- Input format for predict method: [{"feature1": value1, "feature2": value2, ...}, {"feature1": value1, "feature2": value2, ...}]. 
**Example**: [{"pregnant": 7, "glucose": 100, "bp": 70, "skin": 40, "insulin": 100, "bmi": 40, "pedigree": 0.3, "age": 40}]
- Output format for predict method: {"prediction":[0 or 1, 0 or 1, 0 or 1,...]}
**Example**: {"prediction":[0, 1, 1, 0]}
- The Dockerfile has also been placed.

**Reproduction:**
1. Build docker image from Dockerfile
```docker
docker build -t "<app_name>" -f Dockerfile .
```
2. Run the docker container after build
```docker
docker run -p  5000:8000 "<app_name>"
```