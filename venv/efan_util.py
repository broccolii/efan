import urllib.request
from bs4 import BeautifulSoup

opener = urllib.request.build_opener()
# TODO: 1. 模拟登录获取 cookie
cookie = ''
opener.addheaders = [('Cookie', cookie)]

# TODO: 2. 获取 服务id
f = opener.open("https://efan.bid/clientarea.php?action=productdetails&id=28732").read().decode("utf-8")
# for line in f.splitlines():
#     print(line)

# TODO: 3. 解析服务详情
bsobj = BeautifulSoup(f)
# print(bsobj)
div_list = bsobj.findAll('div' , {'class' : "main"})
# print(div_list[0])

# print(div_list[0].contents[3].contents[7].text)

li_string = div_list[0].contents[3].contents[7].text
# print(result_string)
result = li_string.replace("已用 / 剩余", "")
print(result)
