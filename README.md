# Student Math Score Predictor - MLOps Project

This project is an end-to-end **MLOps pipeline** built to predict a student's **math score** using various academic and personal features.

---

## Problem Statement

Predict the **math score** of a student based on:
- **Numerical features**: `reading_score`, `writing_score`
- **Categorical features**: `gender`, `race_ethnicity`, `parental_level_of_education`, `lunch`, `test_preparation_course`

---

## Project Structure

```bash
.
├── notebook/                 # Jupyter notebooks for EDA and model training
│   ├── EDA.ipynb
│   └── Model_Training!.ipynb
├── src/
│   ├── components/           # Core modules for data handling and modeling
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/             # Pipeline scripts for training and prediction
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   ├── utils.py              # Utility functions
│   ├── logger.py             # Logging setup
│   └── exception.py          # Custom exception handler
├── templates/                # HTML templates for web interface
│   ├── index.html
│   └── home.html
├── app.py                    # Flask API to serve the model
├── requirements.txt
├── setup.py
└── README.md
```

## How to run !
1. Clone my repo, using git clone in terminal.
2. Install dependencies : pip install -r requirements.txt
3. Run the Flask app : python app.py
4. In Browser : http://localhost:5000

## Enjoy !

