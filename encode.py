a="https://webvpn.ypi.edu.cn/http/webvpn"
s="172.16.18.97"
for x in list(s):
   a+=hex(ord(x)).replace("0x","")

print(a)