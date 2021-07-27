import requests

download_url = "https://testpay.yffsc.com:9098/prod-api/common/download?fileName=%E8%AE%A2%E5%8D%95%E6%98%8E%E7%BB%86_20210620-20210621.xlsx&delete=true"

res = requests.get(download_url)

with open("test.xml","wb") as f:
    f.write(res.content)

print(res)