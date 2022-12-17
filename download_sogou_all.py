import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request

# 格式：分类名，对应的链接，页数
cates = [
    # ["城市信息", 167, 8],
    # ["自然科学", 1, 28],
    # ["社会科学", 76, 34],
    ["工程应用", 96, 75],
    # ["农林渔畜", 127, 9],
    # ["医学医药", 132, 32],
    # ["电子游戏", 436, 100],
    # ["艺术设计", 154, 17],
    # ["生活百科", 389, 77],
    # ["运动休闲", 367, 16],
    # ["人文科学", 31, 81],
    # ["娱乐休闲", 403, 101]
]

sets = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']  # windows文件命名不能有这些字符

for cate in cates:
    count = 0
    os.mkdir("./" + cate[0])
    for i in range(1, cate[2] + 1):
        html = urlopen("https://pinyin.sogou.com/dict/cate/index/" + str(cate[1]) + "/default/" + str(i))
        bsObj = BeautifulSoup(html.read(), "html.parser")
        nameList = bsObj.findAll("div", {"class": "detail_title"})
        urlList = bsObj.findAll("div", {"class": "dict_dl_btn"})
        for name, url in zip(nameList, urlList):
            count += 1
            name = name.a.get_text()
            for char in name:
                if char in sets:
                    name = name.replace(char, "")  # 去除windows文件命名中非法的字符
            urllib.request.urlretrieve(url.a.attrs['href'], "./" + cate[0] + "/" + str(count) + name + ".scel")
            # 文件名加count是因为词库名可能会重复
            print(cate[0], count, name)
