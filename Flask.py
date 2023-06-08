from flask import Flask, render_template, request
import codecs
app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def HomePage():
    file = codecs.open("Search Desk Home.html", "r", "utf-8")
    return file

@app.route('/Search', methods=['POST','GET'])
def Search():
    if request.method == "POST":
        text = request.form.get("text")
        #flash("Successful" + text)
        links = ['Hellooooo', 'WEare','11','ads']
        print(links)
        return render_template('header.html', links= links)

if __name__ == '__main__':
	app.run(debug=True)
