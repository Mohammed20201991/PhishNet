# from sklearn.externals import joblib

# def predict_with_model(model_filename, data):
#     model = joblib.load(model_filename)
#     predictions = model.predict(data)
#     return predictions
from sklearn.externals import joblib
import os
import pandas as pd

def predict_with_model(model_filename, data):
    # Construct the full path to the model file
    model_path = os.path.join('pickle_files', model_filename)
    
    # Load the model
    model = joblib.load(model_path)
    
    # Convert input data to DataFrame
    df = pd.DataFrame([data])
    
    # Ensure only the 5 required features are used
    required_features = ['body_noFunctionWords', 'url_noIntLinks', 'body_richness', 'url_noLinks', 'url_linkText']
    df = df[required_features]
    
    # Convert DataFrame to a 2D array
    X = df.values  # This is a 2D array
    
    # Make predictions
    predictions = model.predict(X)
    return predictions