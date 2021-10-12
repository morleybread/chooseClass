def translate(a):
    if   a.isdigit() :
        print("请输入字符串")

    else:
        cccc = list(a).index("/")
        dddd = list(a)[(cccc + 1):]
        eeee = "".join(dddd)
        print(eeee)

        with open(a, "r") as f:
            c = f.read()
            print(c)
            a = c.replace(": ", "\":\"")
            d = a.replace("\n", "\",\n")

        with open("daka3", "w") as fp:
            fp.write(d)
            print(d)

        with open("daka3", "r") as fi:
            str = fi.readlines()

            with open("headertextdic/Dic" + eeee, "w") as gu:
                gu.write('{')
                for x in str:
                    gu.write("\"" + x)
                gu.write('"}')

translate("headertext/classtableheader.text")
