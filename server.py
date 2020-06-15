from flask import Flask, request, render_template, jsonify, redirect, url_for, send_file
import os
import server_helper

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    print("Upload endpoint invoked")
    input_file = request.files['file']
    print(request.values['shiftDate'])
    output = server_helper.shiftFile(input_file, request.values['shiftDate'])
    # input_file.save(os.path.join(app.root_path, 'serverInput.ics'))
    # return redirect("/")
    output_file = open(os.path.abspath("output_" + input_file.filename), "wb+")
    output_file.write(output)
    output_file.close()
    return send_file("output_" + input_file.filename, as_attachment=True)

if (__name__ == '__main__'):
    # sys.stdout = sys.stderr = open('server-log.txt', 'wt')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80)