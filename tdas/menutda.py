import inquirer
import json


ERROR_05 = "Didn't such the data file"


class Menu:
    def __init__(self):
        self.close = False
        self.selectName = None
        self.selectUrl = None
        self.selectQuality = None

    def Open(self):
        data = openJson()
        if not data:
            return False
        options = [
            inquirer.List("option", message="Select a Bangumi", choices=data),
        ]
        answer = inquirer.prompt(options)
        if answer:
            self.selectName = answer["option"]
            self.selectUrl = data.get(answer["option"])
            return True

        return False

    def Quality(self):
        if not self.selectName:
            return False
        list_quality = ["360", "480", "720", "1080", "1440"]
        options = [
            inquirer.List(
                "option", message="Select a Quality video", choices=list_quality
            ),
        ]
        answer = inquirer.prompt(options)

        if answer:
            self.selectQuality = answer["option"]
            return True

        return False

    def playingMenu(self):
        if not self.selectName:
            return False

        options = [
            inquirer.List("option", message="The video is running", choices=["Stop"]),
        ]
        answer = inquirer.prompt(options)
        if not answer:
            return False

        return True


def openJson():
    readfile = None
    try:
        with open("data/bangumi.json", "r") as file:
            readfile = json.load(file)
    except Exception as e:
        print(e)
    if not readfile:
        return

    dic = {bangumi["name"]: bangumi["url"] for bangumi in readfile}
    return dic


def GetListName(readfile):
    if not readfile:
        print(ERROR_05)
        return

    list_name = [d["name"] for d in readfile]

    return list_name
