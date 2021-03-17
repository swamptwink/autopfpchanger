import time
import random
import requests


images=0
auto_steamid64   = int(input("SteamID64:    "))     #Change int(input(***)) to input(***) if you get errors
auto_loginsecure = input("Steam Secure: ")

imageAmount=int(input("How many images do you have?:    "))
z=random.randint(1,imageAmount)

auto_request_session             = requests.Session()
auto_request_session_response    = auto_request_session.get('http://steamcommunity.com/')
auto_steam_sessionid             = auto_request_session.cookies.get_dict()["sessionid"]

while True:
        try:
                y=z
                z=random.randint(1, imageAmount)
                if y == z:
                        z=random.randint(1, imageAmount)
                x=str(y)

                auto_imgpath     = (x +".jpg")
                auto_imgbytes    = open(auto_imgpath, "rb")

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
                        print("Total Changes:  "+ str(images))

                else:
                        print("You are most likely being rate limited by Steam. Wait a few minutes and it will go away.")


                sTime = random.uniform(60, 70)

                bTime = time.gmtime(sTime)
                aTime = time.strftime("%H:%M:%S",bTime)
                print("Time until next change:  "+ aTime)
                time.sleep(sTime)

            
                print("\n\n\n") #shhhhh

        except:
                print("error")
