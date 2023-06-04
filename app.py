from flask import Flask,render_template,request
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os
app = Flask(__name__)

category_to_id = {0: 'Debt collection',
 1: 'Consumer Loan',
 2: 'Mortgage',
 3: 'Credit card',
 4: 'Credit reporting',
 5: 'Student loan',
 6: 'Bank account or service',
 7: 'Payday loan',
 8: 'Money transfers',
 9: 'Other financial service',
 10: 'Prepaid card'}

mask_result = {'Debt collection': 'Debt collection',
 'Consumer Loan': 'Consumer Loan',
 'Credit card': 'Mortgage',
 'Credit reporting': 'Credit card',
 'Bank account or service': 'Debt collection',
 'Money transfers': 'Student loan',
'Mortgage': 'Bank account or service',
 'Other financial service': 'Payday loan',
 'Payday loan': 'Money transfers',
 'Prepaid card': 'Other financial service',
 'Student loan': 'Money transfers'}

model = pickle.load(open("customer_classification_model_lr-1.pkl","rb"))
tfidf_vect = pickle.load(open("tfidf.pkl","rb"))
def complaint_classifier(str1):
    
	#tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern='\w{1,}', max_features=5000)
	texts = [str1]
	text_features = tfidf_vect.transform(texts)
	predictions = model.predict(text_features)

	return "   -Predicted as: {}".format(mask_result[category_to_id[predictions[0]]])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        string1 = request.form.get("string1")
        result = complaint_classifier(string1)
        # result = mask_result[result]
        check = True
        return render_template("result.html", check=check, text=result)

if __name__ == "__main__":
    app.run(debug=True)
