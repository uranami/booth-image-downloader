import sys
from bs4 import BeautifulSoup
import requests

File = "link.txt"
if len(sys.argv) == 2:
     File = sys.argv[1]

BoothLinkFile = open(File, "r")
links = BoothLinkFile.readlines()
print("Total Link: ", len(links), "\n")

for link in links:
    link = str.replace(link, "\n", "")
    header = {"User-Agent":

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    WebPage = requests.get(url=link, headers = header)
    if WebPage.status_code != 200 :
             print("[ERROR] URL %s Return Code"%link, WebPage.status_code)
             continue

    WebPage.encoding = 'utf-8'
    TargetPage = WebPage.text
    bs = BeautifulSoup(TargetPage, "html.parser")
    image = bs.find("img", class_="market-item-detail-item-image")
    image_src = image.get("src")

    print(image_src)

    image_resp = requests.get(image_src)
    image_name = "image/" + link.split("/")[-1] + ".jpg"
    with open(image_name, mode="wb") as f:
        f.write(image_resp.content)