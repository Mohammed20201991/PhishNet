# 🛡️ PhishNet: Detecting Phishing Attacks using ML/DL Models

PhishNet is a project focused on detecting phishing emails using machine learning(ML) models & Natural Languge Processing (NLP). It provides a full pipeline from training to deployment, including a Flask web interface and trained model files.

---

## 📦 Clone the Repository

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


