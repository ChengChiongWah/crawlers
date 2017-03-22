import requests, os
from lxml import html


def cache_url(url, pagenumber):
    """把页面下载下来
    """
    filename = str(pagenumber) + ".html"
    path = os.path.join("cache" + filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    else:
        r = requests.get(url)
        with open(path, "wb") as f:
            f.write(r.content)



def main():
    url = "http://my.51job.com/my/history/My_AppHistory.php?pageno={}&total=&rand=840900682"
    url_root = url.format(1)
    cookies_content = ("guid=14901546665369820047; ps=us%3DCzJVOgR4ATYCZwxlVS5SYAUyCj8BKQdkXGJccgox"
                       "UWUMPQVuBWYDMABlAWtSPwM4AToDN1BuVn8HWQEZWzVSZAt2%26%7C%26needv%3D0; 51job=cui"
                       "d%3D32340218%26%7C%26cusername%3Dsguzch%2540163.com%26%7C%26cpassword%3D%26%7C"
                       "%26cname%3D%25D6%25A3%25B3%25A3%25BB%25AA%26%7C%26cemail%3Dsguzch%2540163.com%26"
                       "%7C%26cemailstatus%3D3%26%7C%26cnickname%3Dsguzch%26%7C%26ccry%3D.0IIHvuTZ6r6I%2"
                       "6%7C%26cconfirmkey%3Dsg7pJGOaUQhus%26%7C%26cresumeids%3D.0KFcKZQ4tO76%257C.0ftGf7"
                       "lIbr.I%257C.0tZoltd6muwQ%257C%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%2"
                       "6sex%3D0%26%7C%26cnamekey%3DsgvfYAehpiU5o%26%7C%26to%3DXGdUPQRlBDZUNV0zUTVUb1AvB"
                       "nRaOwcnUi5XZgBiDk4NNAJvUDEDK1NhXG9RaQZ5BTcBNVtvUzcFNVE6WGIEMlxsVDc%253D%26%7C%26")
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Cookie":cookies_content,
    }
    path = os.path.join("cached", "1.html")
    page = requests.get(url_root, headers=headers).text
    root_page = html.fromstring(page)
    xpath_page_number = root_page.xpath("//strong[@class='orareg']")
    page_number = xpath_page_number[0].text.rsplit("/", 1)[1]
    page_number = int(page_number)
    number = 1
    print(url.format(number), page_number)
    while number <= page_number:
        cache_url(url.format(number), number)
        number =+ 1


if __name__ == "__main__":
    main()