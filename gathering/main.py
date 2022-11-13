import pyautogui as gui
import time
import pyperclip
import requests
import random
import os
import glob
import json


def click_on(file):
    dir = "gathering/gui_img"
    path = f"{dir}/{file}"
    point = gui.locateCenterOnScreen(path,  confidence=0.9)
    if point:
        print(f"Found {file}, clicking on ({point.x},{point.y})")
        gui.click(point)
    else:
        print(f"{path} could not be found.")

    time.sleep(1)


def start_game():
    click_on("geoguessr_bookmarks.png")
    click_on("play_a_community_world.png")
    click_on("start_game.png")


def get_url():
    click_on("url_bar.png")
    gui.hotkey('ctrl', 'c')  # copy
    time.sleep(.01)
    url = pyperclip.paste()
    print(f"Got url: {url}")
    return url


def get_game_token():
    url = get_url()
    token = url.split("/")[-1]
    return token


def make_guess(game_token, latitude, longitude):
    print(f"Making guess: {latitude},{longitude}")
    base_api_url = "https://www.geoguessr.com/api/v3/games/"
    data = {
        "token": game_token,
        "lat": latitude,
        "lng": longitude,
        "timedOut": False
    }
    device_token = "45E0F3C6D2"
    ncfa = "AuvOGxiNPt8EmAb2u7VMwPp2o946vRxZADZeaYeppBE%3DBHpwdhE39j2cxR6kRQDoHwuvBvotMkGwQzEAMFro3md0lS1IhJO0v88obZGsVpIX"
    stripe_mid = "700b0981-4f64-468f-a7e4-8cb0e7894e33e2bc2b"
    headers = {
        "Content-Type": "application/json",
        "cookie": f"devicetoken={device_token}; __stripe_mid={stripe_mid}; G_ENABLED_IDPS=google; _ncfa={ncfa}"
    }

    res = requests.post(
        url=f"{base_api_url}{game_token}",
        json=data,
        headers=headers
    )
    return res


def make_random_guess(token):

    MIN_LAT = -84.99784921796194
    MAX_LAT = 81.6812215033565

    MIN_LNG = -177.3921240186748
    MAX_LNG = 178.4581818407309

    return make_guess(token, random.uniform(MIN_LAT, MAX_LAT),
                      random.uniform(MIN_LNG, MAX_LNG))


def refresh():
    gui.hotkey("F5")
    time.sleep(1.5)


def full_screen_on():
    gui.hotkey("F11")
    time.sleep(5)


def full_screen_off():
    gui.hotkey("F11")


def remove_files(dir):
    PATH = f"{dir}/*"
    files = glob.glob(PATH)
    for f in files:
        os.remove(f)


def get_last_picture_id(dir):
    PATH = f"{dir}/*"
    file_list = glob.glob(PATH)
    if not file_list:
        return 0
    last_file = max(file_list)
    number = last_file.split("/")[-1].split(".")[0]
    return int(number)


def play_game():
    ROUNDS = 5

    start_game()

    token = get_game_token()
    print("Game token: ", token)

    refresh()
    full_screen_on()

    last_picture_id = get_last_picture_id("data")  # 4

    for i in range(1, ROUNDS+1):

        picture_id = last_picture_id+i
        print(f"Taking {picture_id}. image")

        file_number = str(picture_id).zfill(5)

        gui.screenshot(f"data/{file_number}.png", region=(0, 0, 1920, 1080))

        res = make_random_guess(token)

        with open(f"data/{file_number}.json", 'w', encoding='utf-8') as f:
            json.dump(res.json(), f, ensure_ascii=False, indent=4)

        refresh()

    # view summary
    click_on("view_summary.png")
    full_screen_off()


if __name__ == "__main__":
    # remove_files("data")
    gui.PAUSE = 0.1

    N_GAMES = 2
    for i in range(N_GAMES):
        print(f"Starting {i+1} of {N_GAMES} games")
        play_game()

    print("Playng games finished")
