from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

resource_dir = 'static/mm131.com'


@app.route('/')
def index():
    girl_titles = os.listdir(resource_dir)
    girl_paths = map(lambda x: os.path.join(resource_dir, x), girl_titles)

    def get_thumb(girl_path):
        pics = os.listdir(girl_path)
        if pics:
            return os.path.join(girl_path, pics[0])
        else:
            return 'static/notfound.png'

    thumbs = map(get_thumb, girl_paths)
    items = zip(girl_titles, thumbs)  # 列表元素为(女孩标题,缩略图)
    return render_template('index.html', items=items)


@app.route('/girl/<title>')
def girl_page(title):
    girl_path = os.path.join(resource_dir, title)
    pic_list = os.listdir(girl_path)
    pic_path_list = map(lambda x: os.path.join(girl_path, x), pic_list)
    return render_template('girl_page.html', girl_path=girl_path,
                           title=title, pic_path_list=pic_path_list)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
