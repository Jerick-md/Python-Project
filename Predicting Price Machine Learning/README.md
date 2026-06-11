# Philippine House Price Prediction

## Overview
This project builds a Machine Learning model to predict residential property prices in the Philippines using real estate data. The workflow includes data cleaning, exploratory data analysis (EDA), outlier removal, feature engineering, model training, and evaluation.

## Dataset
The dataset contains Philippine real estate information, including:

- Price
- Bedrooms
- Bathrooms
- Floor Area
- Land Area

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Project Workflow

### 1. Data Preparation
- Load and inspect the dataset.
- Select relevant features.
- Handle missing values using mean imputation.

### 2. Exploratory Data Analysis
- Visualize price distribution using KDE plots.
- Analyze skewness of property prices.
- Create boxplots for numerical features.

### 3. Outlier Removal
- Apply the Interquartile Range (IQR) method.
- Remove extreme price outliers.

### 4. Feature Engineering
- Apply logarithmic transformation to house prices to reduce skewness.

### 5. Model Training
- Split data into training and testing sets.
- Train a Linear Regression model.

### 6. Model Evaluation
- Generate predictions on test data.
- Compare actual vs predicted values.
- Evaluate model performance using R² Score.

## Features Used

- Bedrooms
- Bathrooms
- Floor Area
- Land Area

## Example Prediction

```python
new_house = {
    "Bedrooms": 2,
    "Bathrooms": 1,
    "Floor Area": 16,
    "Land Area": 20
}
```

The model predicts the estimated property price based on these inputs.

## Results
The model uses Linear Regression to estimate property prices after preprocessing and log transformation of the target variable.

## Future Improvements

- Add more property features
- Test advanced regression models
- Perform hyperparameter tuning
- Deploy as a web application

## Author

Jerick Comedia
