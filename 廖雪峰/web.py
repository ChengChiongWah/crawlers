import requests
from lxml import html



# 这个类很奇怪
# 其实是用来让电影能够自行打印出所有属性的值的一个东西
# 忽略掉
class Model(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{} = ({})'.format(k, v) for k, v in self.__dict__.items())
        return '\n<{}:\n  {}\n>'.format(class_name, '\n  '.join(properties))


# 这是一个电影类
class Movie(Model):
    def __init__(self):
        # 电影类有 4 个属性
        self.name = ''
        self.score = 0
        self.quote = ''
        self.cover_url = ''
        self.ranking = 0
        self.reviews = 0


def movie_from_div(div):
    movie = Movie()
    # 这个和之前的 xpath 是一样的语法
    # 不同的是 .// 表示在当前节点内查找
    # 因为返回的是一个 list (哪怕只有一个元素)
    # 所以要 [0] 取到第一个节点
    # 再通过 .text 获取到文本信息
    # <span class="title"
    movie.name = div.xpath('.//span[@class="title"]')[0].text
    movie.score = div.xpath('.//span[@class="rating_num"]')[0].text
    movie.reviews = div.xpath('.//div[@class ="star"]/span')[-1].text[:-3]
    print(movie.name, movie.reviews)
    try:
        movie.quote = div.xpath('.//span[@class="inq"]')[0].text
    except IndexError as e:
        movie.quote = '消失的爱人不需要引用'
        print('消失的爱人作孽了')
    movie.ranking = div.xpath('.//div[@class="pic"]/em')[0].text
    img_url = div.xpath('.//div[@class="pic"]/a/img/@src')[0]
    print(img_url)
    movie.cover_url = img_url
    return movie


def cached_url(url):
    import os
    filename = url.split('=')[-1] + '.html'
    path = os.path.join('cached', filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f.read()
    else:
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
    return r.content


def movies_from_url(url):
    # 把页面下载下来
    page = cached_url(url)
    # r = requests.get(url)
    # 下载的页面其实是一个文本文件, HTML 格式, 用函数解析一下, 方便之后进行查找
    # html 是文件顶部引入的东西
    root = html.fromstring(page)
    #                         <div class="item">
    # 用 xpath 函数找到所有的元素, 请看上一行的原始函数和下面的 xpath 参数的写法
    # // 代表从根开始找
    movie_divs = root.xpath('//div[@class="item"]')
    # movies = [movie_from_div(div) for div in movie_divs]
    # 上面一行相当于下面四行
    movies = []
    for div in movie_divs:
        # 调用函数从 div 中解析出一个电影的数据
        movie = movie_from_div(div)
        movies.append(movie)
    return movies


def download_img(url, name):
    r = requests.get(url)
    # 通过 URL 获取到图片的数据并且写入文件
    # 'wb' 表明是 写入(write) 和 二进制(binary)
    path = 'covers/' + name
    with open(path, 'wb') as f:
        f.write(r.content)


def save_covers(movies):
    for m in movies:
        download_img(m.cover_url, m.name + '.jpg')


def main():
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}'.format(i)
        movies = movies_from_url(url)
        print(movies)
        # save_covers(movies)


if __name__ == '__main__':
    main()
