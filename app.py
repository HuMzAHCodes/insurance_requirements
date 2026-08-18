from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict_output, model, MODEL_VERSION
from schema.user_input import UserInput


app = FastAPI()


# human readable
@app.get("/")
def home():
    return {"message": "home of our api"}


# machine readable
@app.get("/health")
def check_health():
    return {
        "message": "OK!",
        "version": MODEL_VERSION
    }


@app.post('/predict')
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'response': prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))