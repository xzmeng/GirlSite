from flask import Flask
from flask import render_template
from tools import PageBar

app = Flask(__name__)

resource_dir = 'static/mm131.com'
PAGE_ITEM_COUNT = 20


@app.route('/')
def index():
    return index_page(1)


@app.route('/page/<int:page_num>')
def index_page(page_num):
    start = (page_num - 1) * PAGE_ITEM_COUNT
    end = page_num * PAGE_ITEM_COUNT
    girl_titles = os.listdir(resource_dir)
    girl_num = len(girl_titles)  # 获取总共的女孩数目
    total_num = (girl_num - 1) // PAGE_ITEM_COUNT + 1  # 计算总共需要的页数
    girl_titles = girl_titles[start:end]  # 获取当前页的女孩数目
    girl_paths = map(lambda x: os.path.join(resource_dir, x), girl_titles)  # 获取当前页的女孩路径

    def get_thumb(girl_path):  # 获取女孩缩略图
        pics = os.listdir(girl_path)
        if pics:
            if pics[1]:
                return os.path.join(girl_path, pics[1])
            else:
                return pics[0]
        else:
            return 'static/notfound.png'

    thumbs = map(get_thumb, girl_paths)
    items = zip(girl_titles, thumbs)  # 列表元素为(女孩标题,缩略图)
    bar = PageBar(page_num, total_num)

    return render_template('index.html', items=items, page_bar=bar)

@app.route('/girl/<title>')
def girl(title):
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
