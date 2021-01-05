import pprint
import whois
from flask import Flask, request, render_template

app = Flask(__name__)

TEMPLATE = 'whois.html'


@app.route('/', methods=('POST', 'GET'))
def whois_form():
    info = ''
    if request.method == 'POST':
        domain = request.form['domain']
        query = whois.query(domain)
        info = pprint.pformat(query.__dict__, indent=4) if query is not None else 'Not found'
    return render_template(TEMPLATE, info=info)


if __name__ == '__main__':
    app.run()
