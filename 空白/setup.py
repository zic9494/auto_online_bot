import json
with open("data.json",mode="r") as file:
    data=json.load(file)

def data_writing():
    name=input("輸入google帳號(上課或上班用):")
    data["username"]=name
    passwd=input("輸入google密碼(上課或上班用)")
    data["password"]=passwd
    url1=input("google_classroom 國文科網址:")
    url2=input("google_meet 國文科網址:")
    data["chinese"]=[url1,url2]

    url1=input("google_classroom 英文科網址:")
    url2=input("google_meet 英文科網址:")
    data["English"]=[url1,url2]

    url1=input("google_classroom 數學科網址:")
    url2=input("google_meet 數學科網址:")
    data["Math"]=[url1,url2]
    
    url1=input("google_classroom 物理科網址:")
    url2=input("google_meet 物理科網址:")
    data["physic"]=[url1,url2]
    
    url1=input("google_classroom 化學科網址:")
    url2=input("google_meet 化學科網址:")
    data["chemical"]=[url1,url2]
    
    url1=input("google_classroom 自然科網址:")
    url2=input("google_meet 自然科網址:")
    data["science"]=[url1,url2]
    
    url1=input("google_classroom 社會科網址:")
    url2=input("google_meet 社會科網址:")
    data["society"]=[url1,url2]
    
    url1=input("google_classroom 公民科網址:")
    url2=input("google_meet 公民科網址:")
    data["speople"]=[url1,url2]
    
    url1=input("google_classroom 歷史科網址:")
    url2=input("google_meet 歷史科網址:")
    data["history"]=[url1,url2]
    
    url1=input("google_classroom 地理科網址:")
    url2=input("google_meet 地理科網址:")
    data["geography"]=[url1,url2]
    for i in range(10):
        url1=input(f"google_classroom 其他科{i}網址:")
        url2=input(f"google_meet 其他科{i}網址:")
        if url1==url2=="no":
            break
        data[f"other_{i}"]=[url1,url2]
    with open("data.json",mode="w") as file:
        json.dump(data,file)

def fix(subject):
    url1=input("google_classroom 更新網址:")
    url2=input("google_meet 更新網址:")
    data[F"{subject}"]=[url1,url2]

def help():
    print("learn","開始上課(科目請用英文表示)")
    print("classlist","所有課程(英文表示)")
    print("updata","修改科目網址(科目請用英文表示)")
    print("exit","關閉此網頁")
    print("done","關閉程式")

def classlist():
    English=["chinese","English","Math","physic","chemical","science","society","people","history","other0~other9"]
    Chinese=["國文","英文","數學","物理","化學","自然","社會","公民","歷史","其他(0~9)共十個"]
    for i in range(10):
        print(Chinese[i],":",English[i])