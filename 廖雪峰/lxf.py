import requests, os
from lxml import html


def cached_url(url, name):
    # 把页面下载下来
    filename = name + '.html'
    path = os.path.join('cached', filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f.read()
    else:
        url = 'http://www.liaoxuefeng.com' + url
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write((r.content))


def main():
    url = 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
    page = requests.get(url).text
#   print(root_page)
#   print(requests.get(url).text)
    file_formate = '/\:*?"<>|"'
    root_page = html.fromstring(page)
    ul = root_page.xpath('//ul[@class="uk-nav uk-nav-side" and @style="margin-right:-15px;"]')
    lists_url = ul[0].xpath('.//li[@*]/a/@href')
    lists_name = ul[0].xpath('.//a[@*]')
    for u, n in zip(lists_url, lists_name):
        for f in file_formate:  # 对特殊字符进行转化成'_",如：a/b.text 转成a_b.text
            n.text = n.text.replace(f, '_')
        print(u, n.text)
        cached_url(u, n.text)


if __name__ == '__main__':
    main()
