from flask import Flask, request, render_template, redirect, url_for
from models import predict_with_model
import pandas as pd
import os
from email_processing import extract_msg, extract_body, extract_subj, extract_send_address, extract_replyTo_address, extract_modal_url, extract_all_links
from feature_extraction import extract_body_attributes, extract_subj_attributes, extract_send_attributes, extract_url_attributes, extract_script_attributes

app = Flask(__name__)

# Temporary folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return "No file uploaded. Please upload a file.", 400
        
        file = request.files['file']
        
        # If no file is selected
        if file.filename == '':
            return "No file selected. Please select a file.", 400
        
        # Get selected model
        selected_model = request.form.get('model', 'bagged_decision_tree.pkl')
        
        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Check if the file exists
        if not os.path.exists(file_path):
            return "File not found. Please upload a valid file.", 400
        
        try:
            # Process the email file
            with open(file_path, 'r') as f:
                email_content = f.read()
            
            # Extract necessary fields from the email
            msg = extract_msg(app.config['UPLOAD_FOLDER'], file.filename)
            necessary_fields = {
                'body': extract_body(msg),
                'subj': extract_subj(msg),
                'send': extract_send_address(msg),
                'replyTo': extract_replyTo_address(msg),
                'modalURL': extract_modal_url(msg),
                'links': extract_all_links(str(msg))
            }
            
            # Extract features
            body_attributes = extract_body_attributes(necessary_fields['body'])
            subj_attributes = extract_subj_attributes(necessary_fields['subj'])
            send_attributes = extract_send_attributes(necessary_fields['send'], necessary_fields['replyTo'], necessary_fields['modalURL'])
            url_attributes  = extract_url_attributes(necessary_fields['links'], necessary_fields['body'], necessary_fields['send'], necessary_fields['replyTo'], necessary_fields['modalURL'])
            script_attributes= extract_script_attributes(necessary_fields['body'], necessary_fields['modalURL'])
            
            # Combine all features
            features = body_attributes
            features.update(subj_attributes)
            features.update(send_attributes)
            features.update(url_attributes)
            features.update(script_attributes)
            
            # Select only the 5 features used during training
            selected_features = {
                'body_noFunctionWords': features['body_noFunctionWords'],
                'url_noIntLinks': features['url_noIntLinks'],
                'body_richness': features['body_richness'],
                'url_noLinks': features['url_noLinks'],
                'url_linkText': features['url_linkText']
            }
            
            # Make prediction with selected model
            prediction = predict_with_model(selected_model, selected_features)
            result     = "Phishing" if prediction[0] == 1 else "Not Phishing"
            
            # Render the result on the web page
            return render_template('result.html', result=result, email_content=email_content, model_used=selected_model)
        
        except Exception as e:
            return "An error occurred: {}".format(str(e)), 500
    
    # Render the upload form
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)