from flask import Flask,render_template,request,url_for
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return render_template("index.html")
d={}
@app.route("/add",methods=['GET','POST'])
def add():
    var1=request.form.get("name")
    var2=request.form.get("phone")
    d[var1]=var2
    print(d)
    return render_template("add.html",d=d,var1=var1,var2=var2)
@app.route("/display",methods=['GET','POST'])
def display():
    return render_template("display.html",d=d)
@app.route("/search",methods=['GET','POST'])
def search():
    var3=request.form.get("search")

    return render_template("search.html",d=d,var3=var3)


if __name__=="__main__":
    app.run(debug=True)
