# Real Estate and Furniture Price Prediction with FastAPI
## Overview
This project demonstrates the deployment of machine learning models for predicting prices in the real estate and furniture markets using FastAPI. The models are trained in a Jupyter notebook, and the trained models are saved in a .pkl file. The FastAPI application is then created to consume these models and provide predictions through a user-friendly web interface.

## Project Structure
Notebooks: The notebooks directory contains Jupyter notebooks used for data exploration, preprocessing, and model training. The notebooks are named housing-price-with-eda-and-linear-approach.ipynb and housing-price-with-eda-and-linear-approach.ipynb.

Models: The models directory holds the serialized .pkl files containing the trained machine learning models. The models are named housse_model.pkl for real estate prediction and furniture_model.pkl for furniture price prediction.

Static: The static directory contains static files such as CSS or JavaScript, used to enhance the appearance and functionality of the web interface.

Templates: The templates directory includes HTML templates for rendering web pages. It contains furniture_form.html and house.html for input forms, and furniture_output.html and result.html for displaying prediction results.

app.py: This is the main FastAPI application script. It includes two sets of endpoints for predicting real estate and furniture prices, respectively.

## Usage
#### Install Dependencies:


pip install -r requirements.txt

#### Run the FastAPI Application:

RUN 
python app.py


## Access the Web Interface:
Open a web browser and go to http://localhost:8000. You will find two sections for real estate and furniture price prediction
![Screenshot (102)](https://github.com/CHAFIQMohamed/house_price_fastapi/assets/76255423/6f14ccc6-cbb6-4d10-b818-7746441093c1)

![Screenshot (101)](https://github.com/CHAFIQMohamed/house_price_fastapi/assets/76255423/c01e8a35-1f83-4b87-b847-23214b1f5b2b)
.


Submit Predictions:
Fill in the required input fields in the provided forms and click the "Predict" button to get the model predictions.

## Training the Models
The machine learning models for real estate and furniture price prediction are trained in Jupyter notebooks. You can find the training notebooks in the notebooks directory. 

## Note
Ensure that you have Python installed on your system, and it is recommended to set up a virtual environment to manage project dependencies.

This project is intended for educational purposes and demonstrates a simple deployment of machine learning models using FastAPI. Further enhancements and optimizations can be made for production use.





