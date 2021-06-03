import logging
import beepy
import re
import multiprocessing


def get_discord_link(area_name):
    if area_name == "bbmp":
        return "https://discord.com/api/webhooks/840098585655246849/F7aErtmtuGHlCOsinRdeAmL6DaYGXUB4oTaQDY4eWLId6nhL7t5zL5xp3evGhzFNoBaL"
    if area_name == "navimumbai":
        return "https://discord.com/api/webhooks/840107796887502868/Z_Y3ckPePpeYy0vk3FMnMa8G5G8U0pANkmxoLH7PquxXO5_ICB6qLfe3TeCsiwoi6xRS"
    if area_name == "thane":
        return "https://discord.com/api/webhooks/840117914345930762/9FnC5dzwHEuAlBxjzqqFm-D9tO1NjfW6yBTSPJTvlsQvJzI8Su1cT-T3o0eVqP1aPjG7"
    if area_name == "jamshedpur":
        return "https://discord.com/api/webhooks/840243438041825331/RgW8K9WtrlVgY8cmcJuoOPuPBK0p2JK4ymobgqDM00p1oZn6Slte-wB_IgrHMXXnRfkr"
    if area_name == "darbhanga":
        return "https://discord.com/api/webhooks/840243822406664202/QpD4wB3vJi4wdqo2umihiNx8AuqIyeXsPYjFQ-PmRwRJ8M4oAkYV9d61W7loOwb_LcpI"
    if area_name == "dhanbad":
        return "https://discord.com/api/webhooks/840243668664320010/iMWkSlYOn13fZTSPOMMGps8Q0ACpQljpFryBWm5mpwrWto4IP36ljX7DsLNmGCmGhmbm"
    if area_name == "lucknow":
        return "https://discord.com/api/webhooks/840896737526546443/W0n5ChgEi9h7A7kZuoQadseKKEr3Cr_rvNxMAiC-dljq5SFJa8gnr-iSWcLpHiEacTWV"
    return "https://discord.com/api/webhooks/840084936840577024/bGBUa8wIcWdoAEI8f7kt7fVwIq9oDpIdOW4-Nv1KXrammGvEFkXcJ3L-_bYi6aB0N-AE"


def show_dialog(title="Title", message="EMPTY"):
    import os

    body_Str = message
    title_Str = title
    os.system(
        'osascript -e \'Tell application "System Events" to display dialog "'
        + body_Str
        + '" with title "'
        + title_Str
        + "\"'"
    )


def say_pincode(code):
    code = " ".join(str(code))
    print(f"Saying {code}")
    import os

    os.system(f"say {code}")


def check_for_vaccine_by_district(district_id, discord_link, date_range):
    from datetime import datetime, timedelta
    import requests
    import json

    pin_matcher = "(?<!\d)\d{6}(?!\d)"
    # print(district_id)
    dates = [
        (datetime.now() + timedelta(days=i)).strftime("%d-%m-%Y")
        for i in range(0, date_range)
    ]
    headers = {
        "Content-type": "application/json",
        "Accept": "text/plain",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    }
    co_win_url = (
        "https://api.cowin.gov.in/api/v2/appointment/sessions/public/calendarByDistrict"
    )
    output = ""
    for date in dates:
        url = f"{co_win_url}?district_id={district_id}&date={date}"
        try:
            r = requests.get(url, verify=True)
            if r.status_code != 200:
                print(r.status_code)
                continue
            res = r.json()
            for center in res["centers"]:
                for session in center["sessions"]:
                    try:
                        if (
                            session["min_age_limit"] < 45
                            and session["available_capacity"] > 1
                        ):
                            district_name = center["district_name"]
                            address = center["address"]
                            pincode = center["pincode"]
                            session_date = session["date"]
                            block_name = center["block_name"]
                            output += f"Vaccine status for {district_name} on {session_date} at pinCode: {pincode}\n"
                            name = center["name"]
                            vaccine = session["vaccine"]
                            slots = session["slots"]
                            fee = center["fee_type"]
                            avl = session["available_capacity"]
                            output += f"date: {session_date}, address: {name} {address} {pincode}, vaccine: {vaccine}, fee: {fee}, aval_capacity: {avl}\n\n"
                            payload = {"content": output}
                            payload = json.dumps(payload)
                            print(payload)
                            pincodes = set(re.findall(pin_matcher, output))
                            if len(pincodes) == 1:
                                pincodes = pincodes.pop()
                                say_pincode(pincodes)
                            print("*" * 22)
                            print(f"******* {pincodes} *******")
                            print("*" * 22)
                            # say_pincode(pincode)
                            beepy.beep(sound=6)
                            show_dialog(message=payload["content"])
                            try:
                                requests.post(
                                    discord_link,
                                    data=payload,
                                    headers=headers,
                                    verify=True,
                                )
                            except Exception as e:
                                print(e)
                            output = ""
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)


def run_config_by_district():
    import time

    count = 0
    # print(". ", end="")
    while True:
        s = time.time()
        # beepy.beep(sound="ping")
        count += 1
        date_range_check = 25
        area_details = get_area_details_district()
        jobs = []
        for area_detail in area_details:
            # test_discord_config(area_detail['name'])
            p = multiprocessing.Process(
                target=check_for_vaccine_by_district,
                args=(
                    area_detail["district_id"],
                    area_detail["discord_link"],
                    date_range_check,
                ),
            )
            jobs.append(p)
            p.start()
            # check_for_vaccine_by_district(area_detail['district_id'], area_detail['discord_link'], date_range_check)
            # print(". ", end="\n" if count % 60.0 == 0 else "", flush=True)
        for j in jobs:
            j.join()
        # print('\a', end="")
        print(f"{int(time.time() - s)}s ", end="")
        if count % 30 == 0:
            print()
        time.sleep(1)


def get_area_details_district():
    return [
        # {
        #     "name": "North Delhi",
        #     "district_id": "146",
        #     "discord_link": get_discord_link("navimumbai"),
        # },
        # {
        #     "name": "East Delhi",
        #     "district_id": "145",
        #     "discord_link": get_discord_link("mumbai"),
        # },
        # {
        #     "name": "central Delhi",
        #     "district_id": "141",
        #     "discord_link": get_discord_link("thane"),
        # },
        # {
        #     "name": "North East Delhi",
        #     "district_id": "147",
        #     "discord_link": get_discord_link("darbhanga"),
        # },
        # {
        #     "name": "Noida",
        #     "district_id": "650",
        #     "discord_link": get_discord_link("dhanbad"),
        # },
        # {
        #     "name": "Ghaziabad",
        #     "district_id": "651",
        #     "discord_link": get_discord_link("jamshedpur"),
        # },
        # {
        #     "name": "New Delhi",
        #     "district_id": "140",
        #     "discord_link": get_discord_link("lucknow"),
        # },

        {
            "name": "BBMP",
            "district_id": "294",
            "discord_link": get_discord_link("lucknow"),
        },

        {
            "name": "Bangalore Rural",
            "district_id": "276",
            "discord_link": get_discord_link("lucknow"),
        },

        {
            "name": "Bangalore Urban",
            "district_id": "275",
            "discord_link": get_discord_link("lucknow"),
        },
    ]


if __name__ == "__main__":
    run_config_by_district()