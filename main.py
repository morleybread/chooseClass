import requests
import ast
from bs4 import BeautifulSoup
from playsound import playsound
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# def setcookie():  #由于获取cookie难度较大 所以采用burpsuite抓包cookie的方法
#     with open("headertextdic/Dicclasstableheader.text", "r") as file:
#         a = file.read()
#         adi = ast.literal_eval(a)  # 把文件在添加{}才可成功
#     cookie = getcookie()
#     hh = adi
#     hh["cookie"] = cookie
#     with open("headertextdic/Dicclasstableheader.text", "w") as fio:
#         fio.write(str(hh))
#     return hh

def logcount():
    with open("log/log.text","a+") as fop:
        times=time.localtime()
        local=time.strftime("%Y-%m-%d %H:%M:%S",times)
        fop.write(local+"cookie有效"+"\n")


def playgetcookiemusic():
    playsound("music/成龙、刘媛媛 - 国家.mp3")


def playmusic():
    playsound("music/hi.ogg")


def mainp():
    with open("headertextdic/Dicclasstableheader.text", "r") as file:
        a = file.read()
        adi = ast.literal_eval(a)  # 把文件在添加{}才可成功

    urls = "https://webvpn.ypi.edu.cn/http/webvpn3137322e31362e31382e3937/web_xsxk/ty_xsxk_xh_sql_new.aspx?xsxh=2005390320&dm=0003-008&mc=%e4%bd%93%e8%82%b2%e9%80%89%e9%a1%b9&xkfs="

    opio = 0
    aop = adi
    while True:
        request = requests.get(url=urls, headers=aop, verify=False)
        # print(request.text)
        htmls = request.text
        soup = BeautifulSoup(htmls, features="html.parser")
        if str(soup.title.string) == "登录页面":
            print("cookies失效！")

        else:
            opio += 1
            print("第" + str(opio) + "次请求成功！")
            print("此界面为" + str(soup.title.string))
            logcount()
            lists = soup.select(".dg1-item")
            count = 0
            for x in lists:
                count += 1
                textpa = x.get_text()
                if "台球" in textpa and list(str(textpa))[-2] != "0" and list(str(textpa))[-3] != "0":
                    print("快抢台球" + "在第" + str(count) + "个")
                    playmusic()
                elif "桥牌" in textpa and list(str(textpa))[-2] != "0" and list(str(textpa))[-3] != "0":
                    print('快抢桥牌' + "在第" + str(count) + "个")
                    playmusic()
            time.sleep(7200)

mainp()