from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html',name='Abdul Sami',father= "Abdul Rehman",Cnic="45564367654",phone="123456789")

@app.route("/link")
def link():
    items=[
        {"year":2016,"degree":"matriculation","institute":"OGSS","Percentage":"78"},
        {"year":2018,"degree":"Intermediate","institute":"ABGC1","Percentage":"70"},
        {"year":2020,"degree":"Bsc(P)","institute":"University of karachi","Percentage":"77"},
        {"year":2022,"degree":"MCS(F)","institute":"University of karachi","Percentage":"79"},

        ]
    return render_template('link.html',item=items)

app.run(debug=True)