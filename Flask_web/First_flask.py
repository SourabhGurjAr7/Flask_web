from flask import Flask,render_template,request

app=Flask(__name__)

#by Default home page
@app.route('/')
def index():
    return render_template("index.html")
database={"Sourabh":"1234","Rahul":"rahul55","Kritika":"590450"}

@app.route("/form.login",methods=['Post','Get'])
def login():
    name1=request.form['Username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('index.html',info="Invalid User Name")
    else:
        if database[name1]!=pwd:
            return render_template('index.html',info="Invalid Password")
        else:
            return  render_template('home.html',name=name1)

if __name__=="__main__":
    app.run(debug=True)