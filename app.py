from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

resource_dir = 'static/mm131.com'


@app.route('/')
def index():
    girl_list = os.listdir(resource_dir)
    return render_template('index.html', girl_list=girl_list)


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
