import requests, os
from lxml import html


def cached_url(url, name):
    # 把页面下载下来
    url = 'http://www.liaoxuefeng.com' + url
    page = requests.get(url).text
    root_page = html.fromstring(page)
    content = root_page.xpath('//div[@class="x-wiki-content"]/descendant::*')
    with open('lxf.txt', 'a', encoding='utf-8') as f:
        print('\n\n\n' + name + '\n' + '============' , file=f)
    for c in content:
        with open('lxf.txt', 'a', encoding='utf-8') as f:
            print(c.text, file=f)

def main():
    url = 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
#     url = 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431675624710bb20e9734ef343bbb4bd64bcd37d4b52000'
    page = requests.get(url).text
#   print(root_page)
#   print(requests.get(url).text)
    file_formate = '/\:*?"<>|"'
    root_page = html.fromstring(page)
    ul = root_page.xpath('//ul[@class="uk-nav uk-nav-side" and @style="margin-right:-15px;"]')
    lists_url = ul[0].xpath('.//li[@*]/a/@href')
    lists_name = ul[0].xpath('.//a[@*]')
    content = root_page.xpath('//div[@class="x-wiki-content"]/descendant::*')
    for u, n in zip(lists_url, lists_name):
        print(u, n.text)
        cached_url(u, n.text)
 #    print(type(content), len(content))
 #    print(content[2].text, content[3].text, content[4].text, content[5].text, content[6].text)
 #    i = 0
 #    for c in content:
 #        print(c.text, i)
 #        i = i + 1


if __name__ == '__main__':
    main()
