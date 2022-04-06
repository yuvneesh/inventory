from flask import Flask, render_template


app = Flask(__name__)

#Adding secret key
f = open("secretKey.secret","r")
f2 = f.read()
app.config['SECRET_KEY'] = f2

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/home2')
def home2():
    return render_template("home2.html")  
    
if __name__ == "__main__":
    app.run()