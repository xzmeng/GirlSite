import os
resource_dir = 'static/mm131.com'

def index():
    girl_titles = os.listdir(resource_dir)
    girl_paths = map(lambda x: os.path.join(resource_dir, x), girl_titles)
    thumbs = map(lambda x: os.path.join(x, os.listdir(x)[0]), girl_paths)
    items = zip(girl_titles, thumbs)  # 列表元素为(女孩标题,缩略图)
    for item in items:
        print(item)



index()