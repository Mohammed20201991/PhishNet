# 🛡️ PhishNet: Detecting Phishing Attacks using ML/DL Models

PhishNet is a project focused on detecting phishing emails using machine learning(ML) models & Natural Languge Processing (NLP). It provides a full pipeline from training to deployment, including a Flask web interface and trained model files.

---

## 📦 Clone the Repository
Recognizing Phishing in Emails by Using Natural Language Processing & Machine Learning Techniques 
```bash
git clone https://github.com/Mohammed20201991/PhishNet.git
cd PhishNet
```

## 🐍 Python Version
This project uses `Python 2.7.18` due to dependency compatibility for certain models.

## Environment Setup & Usage
📨 Option 1: mail Environment (for model testing via script)
```
# Create and activate virtual environment
py -2 -m virtualenv mail
mail\Scripts\activate

# Install dependencies
pip install -r mail_requirements.txt

# List installed packages (optional)
pip list

# Run the phishing detection script
cd Code
python Phishector.py

# Make sure to use full path to the model pickle files
# Example:
# PhishNet/pickle_files/

# Save environment dependencies
pip freeze > mail_requirements.txt

# Deactivate when done
deactivate
```

## 🌐 Option 2: keras Environment (for web interface)
```
# Create and activate keras virtual environment (if not already created)
py -2 -m virtualenv keras
keras\Scripts\activate

# Install required packages
pip install -r keras_requirements.txt

# Disable Colorama (for cleaner logs)
set FLASK_ENV=production

# Run the Flask app
cd Code
py app.py
```
🔁 Example CURL request for API testing

```
curl -X POST -H "Content-Type: application/json" ^
-d "[{\"body_noFunctionWords\": 5, \"url_noIntLinks\": 2, \"body_richness\": 0.1, \"url_noLinks\": 3, \"url_linkText\": 1}]" ^
http://127.0.0.1:5000/predict
```

## Model Training 
To retrain the phishing detection model from scratch:
```
# Create and activate a virtual environment for training
py -2 -m virtualenv training
training\Scripts\activate

# Run the training script
python train/train_and_save_model.py
```

## Dataset Used
The dataset used in this project is publicly available on Kaggle:

📎 Phishing Email Dataset (SpamAssassin)

## Results:
<table>
    <caption>Evaluation Metrics for All Classifiers</caption>
    <thead>
        <tr>
            <th>Model</th>
            <th>Accuracy</th>
            <th>Precision</th>
            <th>Recall</th>
            <th>F1-score</th>
            <th>ROC-AUC</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Light GBM</td>
            <td>0.960</td>
            <td>0.96</td>
            <td>0.96</td>
            <td>0.96</td>
            <td>0.9934</td>
        </tr>
        <tr>
            <td>Gradient Boosting</td>
            <td>0.960</td>
            <td>0.96</td>
            <td>0.96</td>
            <td>0.96</td>
            <td>0.9924</td>
        </tr>
        <tr>
            <td>SVM</td>
            <td>0.932</td>
            <td>0.91</td>
            <td>0.92</td>
            <td>0.91</td>
            <td>0.9400</td>
        </tr>
        <tr>
            <td>Random Forest</td>
            <td>0.956</td>
            <td>0.94</td>
            <td>0.95</td>
            <td>0.94</td>
            <td>0.9894</td>
        </tr>
        <tr>
            <td>Extra Trees</td>
            <td>0.940</td>
            <td>0.95</td>
            <td>0.94</td>
            <td>0.95</td>
            <td>0.9923</td>
        </tr>
        <tr>
            <td>Bagging Classifier</td>
            <td>0.880</td>
            <td>0.89</td>
            <td>0.89</td>
            <td>0.88</td>
            <td>0.9550</td>
        </tr>
        <tr>
            <td>Naive Bayes</td>
            <td>0.970</td>
            <td>0.96</td>
            <td>0.96</td>
            <td>0.96</td>
            <td>0.9927</td>
        </tr>
        <tr>
            <td>Ensemble</td>
            <td>0.980</td>
            <td>0.98</td>
            <td>0.98</td>
            <td>0.98</td>
            <td>0.9956</td>
        </tr>
    </tbody>
</table>

## Contacts
```
@misc{phishnet2025,
  author       = {Mohammed A. S. Al-Hitawi,Ahmed Hadi Ali AL-Jumaili,Nadaim, Mohammed AlSahibly, Ali Q Saeed,Taher M. Ghazal,Yaseen Hadi Ali},
  title        = {PhishNet: Recognizing Phishing in Emails by Using Natural Language Processing & Machine Learning Techniques},
  year         = {2025},
  publisher    = {GitHub},
  email        = {al_hitawe@uofallujah.edu.iq},
  Affilation   = {Computer Centre University of Fallujah},
  howpublished = {\url{https://github.com/Mohammed20201991/PhishNet}}
}
```
