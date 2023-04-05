from flask import Flask
from flask import jsonify
app =Flask(__name__)

@app.route('/')
def hello():
    print ("I am inside hello")
    return'Helllo World!'
@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val={"new-name": name}
    return jsonify(val)
if __name__=='__main__':
    app.run(host=127.0.0.1,port=8000,debug=True)
