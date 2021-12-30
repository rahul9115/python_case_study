from flask import Flask,render_template,request,redirect

app=Flask(__name__,template_folder="html_files")
@app.route("/",methods=["POST","GET"])
def display():
    return render_template("index.html")
if __name__ == "__main__" :
    app.debug=True
    app.run(host="127.0.0.1",port=5000)