from flask import Flask, request, render_template, jsonify, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    print("Upload endpoint invoked")
    input_file = request.files['file']
    # input_file.save(os.path.join(app.root_path, 'serverInput.ics'))
    return redirect("/")

if (__name__ == '__main__'):
    # sys.stdout = sys.stderr = open('server-log.txt', 'wt')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80)