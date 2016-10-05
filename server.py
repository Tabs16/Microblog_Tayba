from flask import Flask,render_template,request
from random import shuffle
app = Flask(__name__)
submit = True
check = True
@app.route('/')
def index():
    return render_template("base.html")

@app.route('/answer',methods=['GET','POST'])
def test():
    list=['python','c','c++']
    x =[[i] for i in list]
    shuffle(x)
    answer=x[0]
    print(answer)
    if request.method == 'POST':
        val = request.form['lang']
        print(val)
        val1 = [val]

        if val1 == answer:
            return render_template('answer.html',k=1)
        else:
            return render_template('answer.html',k=0)
    
    
if __name__=="__main__":
    app.run(debug=True)
