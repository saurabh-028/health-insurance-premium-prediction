from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def predict():

    if request.method == 'POST':
        age = int(request.form['age'])
        
        charges = float(request.form['charges'])
        
        bmi = float(request.form['bmi'])
    
        children = int(request.form['children'])
        
        region = int(request.form['region'])
        
        sex = request.form['sex']
        if(sex == "Male"):
            sex = 1
        else:
            sex = 0
        
        smoker = request.form['smoker']
        if(smoker == "Yes"):
            smoker = 1
        else:
            smoker = 0              
            
        prediction= int(model.predict([[age, sex, bmi, children, smoker, region, charges]]))
        print(prediction)
        
        if prediction == 1:
            return render_template('index.html', prediction_text = "Congratulations..! You can claim an Insurance")
        else:
            return render_template('index.html', prediction_text = "Sorry, You can not claim an Insurance")
        
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

