from fastapi import FastAPI, Request,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pickle
import numpy as np
from typing import Annotated

app = FastAPI()
# first endpoint for furnture prediction
with open('../models/furniture_model.pkl', 'rb') as file:
    model_furniture = pickle.load(file)

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/furniture", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("furniture_form.html", {"request": request})


# Define the endpoint
@app.post("/furniture/predict/")
async def predict_furniture(request: Request, category: Annotated[int, Form()],sellable_online: Annotated[int, Form()],other_colors: Annotated[int, Form()],depth: Annotated[int, Form()],height: Annotated[int, Form()],width: Annotated[int, Form()]):
    # Convert the input features to a format that can be used for prediction
   
   
    input_features = [[category, sellable_online, other_colors,
                       depth, height, width]]

    # Make the prediction using the loaded model
    prediction = model_furniture.predict(input_features)
    print(prediction)
    # Render the result using a Jinja2 template
    

    return templates.TemplateResponse("furniture_output.html", {"request": request,"predicted_price":prediction[0]})


# Second endpoint for housse prediction 
with open('../models/housse_model.pkl', 'rb') as file:
    model_housse = pickle.load(file)

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/housse_price", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("house.html", {"request": request})


# Define the endpoint
@app.post("/housse_price/predict/")
async def predict_furniture(request: Request, Area: Annotated[int, Form()],Bedrooms: Annotated[int, Form()],Bathrooms: Annotated[int, Form()],Stories: Annotated[int, Form()],mainroad: Annotated[int, Form()],guestroom: Annotated[int, Form()],basement: Annotated[int, Form()],hotwaterheating: Annotated[int, Form()],airconditioning: Annotated[int, Form()],parking: Annotated[int, Form()],prefarea: Annotated[int, Form()],furnishingstatus: Annotated[int, Form()]):
    # Convert the input features to a format that can be used for prediction
   
   
    input_features = [[Area,Bedrooms,Bathrooms,Stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus]]

    # Make the prediction using the loaded model
    prediction = model_housse.predict(input_features)
    print(prediction)
    # Render the result using a Jinja2 template
    

    return templates.TemplateResponse("result.html", {"request": request,"predicted_price":prediction[0]})


    
if __name__ == "__main__":
    import uvicorn


    uvicorn.run("app:app", port=8000, reload=True)