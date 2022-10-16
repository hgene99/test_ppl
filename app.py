from flask import Flask, render_template, request, jsonify
from module.crawling import crawl_cartoon

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crawling_form')
def crawling_form():
    return render_template('crawl_cartoon_form.html')

@app.route('/crawling', methods=['POST'])
def crawling():
    data = request.form
    crawl_cartoon(data['url'], data['name'])
    return jsonify({'code':'200'})

if __name__ == '__main__':
    app.run(debug=True)