from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

hosts=list()
hosts.append(("foo", "bar", "baz"))

@app.route('/')
def index():
    return render_template("index.html", hosts=hosts)

@app.route('/api/knownHosts')
def porecelain():
    return str(hosts)

@app.route('/api/inform/<hostname>/<address>')
def inform(hostname, address):
    newhost=(hostname, address, request.remote_addr)
    if newhost not in hosts:
        hosts.append(newhost)
        return "Host registered!"
    else:
        return "Host already exists!"

if __name__=="__main__":
    app.run(debug=True)
