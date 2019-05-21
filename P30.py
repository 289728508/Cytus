import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):       # 获取网页HTML文本
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):      # 将特定内容存入列表
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):  # 保证tr不是标签string而是子标签
            tds = tr('td')  # 找到子标签<td>,tds为bs4.element.ResultSet类型
            ulist.append([tds[0].string, tds[1].string, tds[3].string])  # 分别将所需内容存入二维列表


def printUnivList(ulist, num):      # 打印选定内容
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print("{0:^10}{1:{3}^10}\t{2:^10}".format("排名", "大学名称", "分数", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    print("Suc" + str(num))


def main():
    uinfo = []      # 用于储存爬取的数据
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 列出前20所学校的相关信息


if __name__ == '__main__':
    main()





