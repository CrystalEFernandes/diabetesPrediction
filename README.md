# PYTHON Project: Diabetes Prediction System

## I. INTRODUCTION

**PROJECT TOPIC:** Diabetes Prediction System

**GROUP MEMBERS:**  
- 9539 Crystal Fernandes 
- 9607 Lisa Gonsalves 
- 9620 Aditya Mahanwar

**INTRODUCTION:**  
We aim to design a diabetes prediction system in Python using the SVM algorithm. The system takes input for various parameters and predicts if the person is diabetic. We'll train the SVM model using a dataset from Kaggle.

**PURPOSE:**  
With diabetes becoming increasingly common, this system offers a faster method to predict diabetes without special tests. Hospitals can use this to assess if a patient needs further diagnostic tests.

**NOVELTY:**  
- Utilizes the Support Vector Machine (SVM) algorithm for accurate predictions.
- Incorporates advanced data preprocessing techniques.
- User-friendly web-based interface.
- Thoroughly tested with real-world data.

**SrNo** | **URL**  
--------|--------
1 | [Type 2 Diabetes Risk Assessment](https://www.idf.org/type-2-diabetes-risk-assessment/)
2 | [Do I Have Diabetes Quiz](https://patient.info/news-and-features/quiz-do-i-have-diabetes)

### II. DESIGN

**FUNCTIONAL REQUIREMENTS:**
- Data Preprocessing Module
- Support Vector Machine (SVM) Model Building Module
- Training Module
- Model Testing Module
- Model Deployment Module

**HARDWARE REQUIRED:**  
No hardware required.

**SOFTWARE AND DATABASE REQUIRED:**  
Google Colab for collaborative work, PyCharm's IDE for the front end.

## ALGORITHM
1. Import necessary libraries.
2. Load the PIMA diabetes dataset into a pandas dataframe.
3. Check dataset info, head, tail, shape, and null values.
4. Replace 0 values with mean or median.
5. Standardize the data.
6. Split the dataset into training and testing data.
7. Train a Support Vector Machine (SVM) model.
8. Predict outcomes of the testing data.
9. Calculate accuracy score.

## III. CONCEPT
SVM works by finding the optimal hyperplane that best separates different classes in a dataset. In the simplest case, where the classes are linearly separable, this hyperplane is a straight line in two dimensions, a plane in three dimensions, and a hyperplane in higher dimensions.

The hyperplane that SVM finds not only separates the classes but also maximizes the margin, which is the distance between the hyperplane and the nearest data point from each class. Maximizing the margin helps improve the generalization ability of the classifier, making it more robust to noise and outliers.

The data points closest to the hyperplane are called support vectors. These support vectors are critical in defining the hyperplane and are used to determine its position and orientation.

Once the hyperplane is determined during the training phase, SVM can classify new data points by simply determining which side of the hyperplane they fall on.

## CONCLUSION
Our system provides a faster method to predict diabetes without special tests, assisting hospitals in early diagnosis.

## DEMO

https://github.com/CrystalEFernandes/diabetesPrediction/assets/68494281/25992e5a-0f7a-499a-a69c-1a5c835bc0b4

### REPORT
[Python Diabetes Prediction Report.pdf](https://github.com/user-attachments/files/15526161/Python.Diabetes.Prediction.Report.pdf)

