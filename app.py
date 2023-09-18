from flask import Flask,render_template,request

app = Flask(__name__)
#home page
@app.route("/")
def home():
    return render_template('home.html')

#about page
@app.route("/about")
def about():
    return render_template('about.html')
#contact page
@app.route("/contact")
def contact():
    return render_template('contact.html')

#login page
@app.route("/login")
def login():
    return render_template('login.html')

#services page
@app.route("/services")
def services():
    return render_template('services.html')


@app.route("/form",methods=['GET','POST'])
def form():
    
    if request.method=='GET':
       return render_template('home.html')
    else:
       input1=float(request.form['input1'])
       input2=float(request.form['input2'])
    
       addition=(input1+input2)
       subtraction=(input1-input2)
       multiplication=(input1*input2)
       division=(input1/input2)
       
       return render_template('home.html',result1=addition,result2=subtraction,result3=multiplication,result4=division)


if __name__ == "__main__":
    app.run(debug=True)