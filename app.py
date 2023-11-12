from flask import Flask, render_template
import os

app = Flask(__name__)

# 현재 스크립트의 디렉토리에서 'templates' 디렉토리까지의 경로를 가져옴
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app.template_folder = template_dir

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
