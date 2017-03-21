import requests, os
from lxml import html


def main():
    url = "http://my.51job.com/my/history/My_AppHistory.php?pageno={}&total=&rand=840900682".format(1)
    print(url)
    cookies_content = ("guid=14900818708430220023; 51job=cuid%3D32340218%26%7C%26cusername%3Dsguzch%25"
    "40163.com%26%7C%26cpassword%3D%26%7C%26cname%3D%25D6%25A3%25B3%25A3%25BB%25AA%26%7C%26cemail%3D"
    "sguzch%2540163.com%26%7C%26cemailstatus%3D3%26%7C%26cnickname%3Dsguzch%26%7C%26ccry%3D.0IIHvuTZ6"
    "r6I%26%7C%26cconfirmkey%3Dsg7pJGOaUQhus%26%7C%26cresumeids%3D.0KFcKZQ4tO76%257C.0ftGf7lIbr.I%25"
    "7C.0tZoltd6muwQ%257C%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnameke"
    "y%3DsgvfYAehpiU5o%26%7C%26to%3DWmFaMwJjCzlUNQBuUDRRagB%252FVyUGZ1p6Ui4FNAxuVhYNNABtBGUHL1dlDj0LM"
    "1coADIGMlNnUjZSYgZlDDEAOFpqWjk%253D%26%7C%26%3D; ps=us%3DDDVUO1QoADdSNwpjVi1WZFdgBjNSegdkVmhUegky"
    " DzsBMAVuBGZWaFMzCm4FaFxnADRUbQY5UXgHR1ZWWzNVYgxg%26%7C%26needv%3D0; nolife=fromdomain%3Dwww; sli"
    "fe=resumeguide%3D1%26%7C%26")
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Cookie":cookies_content,
    }
    print(cookies_content)
    path = os.path.join("cached", "1.html")
    page = requests.get(url, headers=headers).text
    root_page = html.fromstring(page)
    page_number = root_page.xpath("//strong[@class='orareg']")
    print(len(page_number))
    # r = requests.get(url, headers=headers)
    # with open(path, "wb") as f:
    #     f.write(r.content)


if __name__ == "__main__":
    main()