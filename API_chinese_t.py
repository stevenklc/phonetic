
import requests
from bs4 import BeautifulSoup

one_ses = requests.session()

def phonetic(name_phonetic):

    url = "https://crptransfer.moe.gov.tw/index.jsp"
    params = {
        "SN":name_phonetic,
        "sound":"1"
    }
    chinese_list = []
    # 根據長度取值
    len_sn = len(params["SN"])

    re = one_ses.get(url,params=params)
    print(re)
    soup = BeautifulSoup(re.text, "html.parser")


    # get
    for i in soup.find_all("table",class_ = "result"):

        if len(params["SN"]) > 1:
            for i2 in i.find_all("span",class_ = "long",limit = len_sn):

                phon = i2.text.replace("。", ",")
                phon.split(",")
                for i3 in phon.split(","):
                    chinese_list.append(i3)

        else:
            for i2 in i.find_all("span",limit = 1):
                phon = i2.text.replace("。", ",")
                phon.split(",")
                for i3 in phon.split(","):
                    chinese_list.append(i3)
    
    del chinese_list[len_sn:]
    return chinese_list

if __name__ == "__main__":

    re = phonetic("高高高高高正")
    print(re)      
