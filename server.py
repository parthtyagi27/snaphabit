from flask import Flask, request, render_template, jsonify, redirect, url_for

app = Flask(__name__)


if (__name__ == '__main__'):
    # sys.stdout = sys.stderr = open('server-log.txt', 'wt')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80)