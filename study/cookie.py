from hyperlink import URL

a="http://119.45.152.126:8081/prod-api/system/zht/menu/app/list?scXh=0000000000000000002&jyhXh=00000000000000095087"

datas = {i[0]:i[1] for i in URL.from_text(a).query}
print(datas)

#
# datas["scXh"]="000000"
#
#
# a = "="
# b = "&"
# e = []
# for m,v in datas.items():
#     c = a.join([m,v])
#     e.append(c)
# d = b.join(e)
# print(d)






