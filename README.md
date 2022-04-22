## Predicting weather a person can claim health insurance or not using machine learning.

This is a web app where you can check your eligiblity to claim health insurance. This is a machine learning model deployed into web app so that anyone can use it.<br>
(hosted at miscrosft Azure) : https://healthinsurance.azurewebsites.net/

# Screenshots of Project

# Home page 
![Screenshot (153)](https://user-images.githubusercontent.com/80406834/160917335-eedea09a-c629-461c-967f-d7c6af792d63.png)

# Inserting Values
![Screenshot (154)](https://user-images.githubusercontent.com/80406834/160918046-baeb4e93-d0d4-4d49-bc8d-e66f812128de.png)

After Insertig the values, press predict button. 
# Here is the prediction.
![Screenshot (155)_LI](https://user-images.githubusercontent.com/80406834/160918629-b90bb8fb-fa73-4b18-b546-a3645859112e.jpg)

# Here is another scenario when a person cannot claim an insurance.
![Screenshot (156)](https://user-images.githubusercontent.com/80406834/160920354-c1601d21-c074-4c59-bcc8-878d53b2af84.png)

# Aim
Health insurance has become an indispensable part of our lives in recent years, and people are paying for it so that they are covered in the event of an accident or other unpredicted factors.
You are provided with medical costs dataset that has features such as Age, Cost, BMI.

Objective:
Determine the factors that contribute the most in the calculation of insurance costs.
Predict the eligiblity to health Insurance.

## About

This webapp was developed using Flask Web Framework and was deployed on microsoft azure server. The models used to predict whether a person can claim health insurance were trained on large Datasets. All the links for datasets and the python notebooks used for model creation are mentioned below in this readme.

## Dataset Links

All the datasets were used from kaggle can be found in below link also images of samples.

https://www.kaggle.com/datasets/mirichoi0218/insurance

# Video of Project

https://user-images.githubusercontent.com/80406834/161100094-6bdf1907-13ae-4066-b7ed-1bd9ad1d4b01.mp4

## Steps to run this application in your system

1. Clone or download the repo.
2. Open command prompt in the downloaded folder.
3. Create a virtual environment

```
mkvirtualenv environment_name
```

4. Install all the dependencies:

```
pip install -r requirements.txt
```

5. Run the application

```
python app.py
```

