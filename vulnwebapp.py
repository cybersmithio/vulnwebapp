from flask import Flask, request, redirect, send_file, render_template
import requests
import sys
import io
import subprocess
import os

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('home_page.html')


@app.route('/images/')
def show_images():
    imageurl=request.args.get('imageurl')
    print(f"Attempting to get {imageurl}", file=sys.stderr)
    r = requests.get(imageurl)
    print(f"Response code {r.status_code}", file=sys.stderr)
    #print(f"Response {r.content}", file=sys.stderr)
    mem = io.BytesIO()
    mem.write(r.content)
    mem.seek(0)

    return send_file(mem, mimetype=r.headers['content-type'])

@app.route('/ping/')
def ping_ip():
    ipaddress = request.args.get('ipaddress')
    results = os.popen(f"ping -c 4 {ipaddress}").read()
    return(results)


