from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    return render_template('home.html',pred='25%')




if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=config.DEBUG_MODE)