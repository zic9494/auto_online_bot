import connective
import json
import setup
with open("data.json",mode="r") as file:
    data=json.load(file)
if data["username"]=="":
    setup.data_writing()
while 1:
    start_work=input("輸入你要做的事情(指令教學則輸入[help]):")
    if start_work=="help":
        setup.help()

    if start_work=="classlist":
        setup.classlist()

    if start_work=="updata":
        subject=input("輸入科目(英文表示):")
        setup.fix(subject)

    if start_work=="exit":
        connective.exit()

    if start_work=="done":
        break

    if start_work=="done":
        subject=input("輸入科目(英文表示):")
        connective.google_classroom(data["username"],data["password"],data[subject][0],data[subject][1])