import os
import pickle
from pydantic import BaseModel

from fastapi import FastAPI


path = os.path.join(os.path.dirname(__file__), "pipeline_v1.bin")

app = FastAPI()


class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float


@app.post("/predict")
def predict(client: Client):
    client = client.dict()
    with open(path, 'rb') as f_in:
        dv, model = pickle.load(f_in)
        X = dv.transform([client])
        y_pred = model.predict_proba(X)[0, 1]
        return {"result": y_pred}


path2 = os.path.join(os.path.dirname(__file__), "pipeline_v2.bin")

@app.post("/predict2")
def predict2(client: Client):
    client = client.dict()
    with open(path2, 'rb') as f_in:
        dv, model = pickle.load(f_in)
        X = dv.transform([client])
        y_pred = model.predict_proba(X)[0, 1]
        return {"result": y_pred}