# Telco Customer Churn Prediction (Capstone Project)

## Objective
This project aims to predict customer churn using real-world telecom data. By applying classification models like Logistic Regression and Random Forest, we identify which customers are likely to leave the service — helping companies proactively reduce churn.

---

## Dataset
- **Source**: Telco Customer Churn CSV
- **Rows**: 7,032 customers after cleaning
- **Target**: `Churn` (Yes/No → 1/0)

---

## Project Workflow
1. **Data Inspection**
2. **Data Cleaning and Preprocessing**
   - Type conversions, handling missing values
   - Encoding categorical features
3. **Exploratory Data Analysis (EDA)**
   - Heatmaps, histograms, scatter plots, box plots
4. **Feature Scaling & Train-Test Split**
5. **Modeling**
   - Logistic Regression
   - Random Forest with hyperparameter tuning
6. **Evaluation**
   - Accuracy
   - Confusion Matrix
   - Precision & Recall

---

## Results

| Model              | Accuracy | Precision | Recall | OOB Estimate |
|-------------------|----------|-----------|--------|--------------|
| Logistic Regression | 80.6%    | 65.4%     | 57.2%  | —            |
| Random Forest       | 79.2%    | 65.1%     | 46.7%  | 20.1%        |

> **Conclusion**: Logistic Regression was better at identifying actual churners (higher recall), making it the more suitable model for this task.

---

## Tools Used
- Python (Jupyter Notebook)
- pandas, seaborn, matplotlib
- scikit-learn

---

## Next Steps
- Try advanced models (XGBoost, LightGBM)
- Use SMOTE or resampling to improve recall
- Build a real-time churn dashboard

---

This project showcases end-to-end machine learning, visual storytelling, and model evaluation best practices.
