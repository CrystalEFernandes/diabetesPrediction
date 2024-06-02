from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    df = pd.read_csv(r'C:\Users\HP\Downloads\diabetesprediction\mysite\diabetes.csv')
    X = df.drop('Outcome', axis=1)
    Y = df['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, stratify=Y, random_state=2)

    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pred = classifier.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result1 = ""
    if pred == [1]:
        result1 = "Diabetic"
    else:
        result1 = "Not Diabetic"

    return render(request, "predict.html", {"result2": result1})
