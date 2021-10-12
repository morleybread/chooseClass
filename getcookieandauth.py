import requests
import ast
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def getcookie():
    with open("headertextdic/Dicgetcookie.text") as fil:
        aa = fil.read()
        headers = ast.literal_eval(aa)

    urls = "https://webvpn.ypi.edu.cn/enlink/sso/login"
    respnose = requests.get(url=urls, headers=headers, verify=False)

    dic = dict(respnose.headers)
    lis = (dic["Set-Cookie"])  # 取出cookie
    yu = lis[:-16]  # 精简cookie

    # 认证加权
    with open("headertextdic/Dicauth.text", "r") as fp:
        du = fp.read()
        dc = ast.literal_eval(du)
        dc["Cookie"] = "".join(yu)  # 字化cookie设置cookie在header中

        datas = "username=2005390320&password=zzM%2B0wwanDw1mK8OrgmuBg%3D%3D"
        urlp = "https://webvpn.ypi.edu.cn/enlink/sso/login/submit"
        head = dc
        res = requests.post(url=urlp, data=datas, headers=head, verify=False)
        print(res.status_code)
        if res.status_code == 200:
            print("成功！")
            return dc["Cookie"]

print(getcookie())