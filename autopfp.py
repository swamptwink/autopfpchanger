import time
import random
import requests

images=0
imageHistory = []
imageNumber = int(input("How many images do you have:  "))
loginSecure = input("Steam Login Secure:  ")
id64 = int(input("Steam ID64:  "))
z=random.randint(1, imageNumber)

while True:
    y=z
    z=random.randint(1, imageNumber)
    if y == z:
        z=random.randint(1, imageNumber)
    x=str(y)
    
    auto_steamid64   = id64
    auto_loginsecure = loginSecure
    auto_imgpath     = (x +".jpg")
    auto_imgbytes    = open(auto_imgpath, "rb")

    auto_request_session             = requests.Session()
    auto_request_session_response    = auto_request_session.get('http://steamcommunity.com/')
    auto_steam_sessionid             = auto_request_session.cookies.get_dict()["sessionid"]

    print("Setting new profile picture")

    auto_request = requests.post(
        url     = "https://steamcommunity.com/actions/FileUploader",
        data    = {
            "MAX_FILE_SIZE":    "1048576",
            "type":             "player_avatar_image",
            "sId":              auto_steamid64,
            "sessionid":        auto_steam_sessionid,
            "doSub":            "1"
        },
        cookies = {
            "steamLoginSecure": auto_loginsecure,
            "sessionid":        auto_steam_sessionid
        },
        files   = {
            "avatar":           auto_imgbytes
        }
    )

    if auto_request.status_code == 200:
        print("Set "+ auto_imgpath +" as profile picture")
        images+=1
        imageHistory.append(auto_imgpath)
        print("Total Changes:  "+ str(images))
        print("\n Image History:  \n", imageHistory ,"\n\n")

    else:
        print("You are most likely being rate limited by Steam. Wait a few minutes and it will go away.")


    sTime = random.uniform(300, 900)

    bTime = time.gmtime(sTime)
    aTime = time.strftime("%H:%M:%S",bTime)
    print("Time until next change:  "+ aTime)
    time.sleep(sTime)

    
    print("\n\n\n") #shhhhh
