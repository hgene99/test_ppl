import os

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

@app.route('/detection_form')
def detection_form():
    return render_template('detection_form.html')

# @app.route('/detection', methods=['POST'])
# def detection():
#     data = request.files.getlist('file[]')
#     # 이미지 객체검출하는 소스
#     for el in data:
#         print(el)
#         el.save()
#     # data.save('./image/' + data.filename)
#     return jsonify({'code': '200'})

@app.route('/detection', methods=['POST'])
def detection():
    data = request.files.getlist('file[]')
    ppl_data = request.files['ppl_file']
    item_url = request.form['item_url']
    # 이미지 객체검출하는 소스
    for el in data:
        print(el)
        # el.save()
    # data.save('./image/' + data.filename)
    ppl_data.save(os.getcwd() + '/static/상품/' + ppl_data.filename)
    dir_name = '프리드로우/제457화 킹 안드레 (2)'
    detected_image_list = []
    for el in data:
        detected_image_list.append(el.filename)
    return jsonify({'code': '200', 'dir_name': dir_name, 'detected_image_list': detected_image_list, 'ppl_data': ppl_data.filename, 'item_url': item_url})

@app.route('/cartoon_view', methods=['GET'])
def cartoon_view():
    dir_name = request.values.get('dir_name')
    path = os.getcwd() + '/' + 'static/' + dir_name
    file_list = os.listdir(path)
    return render_template('cartoon_view.html', dir_name = dir_name, file_list = file_list)

@app.route('/ppl_view', methods=['GET'])
def ppl_view():
    ppl_data = request.values.get('ppl_data')
    item_url = request.values.get('item_url')
    print(item_url)
    return render_template('ppl_view.html', ppl_data = ppl_data, item_url = item_url)

if __name__ == '__main__':
    app.run(debug=True)