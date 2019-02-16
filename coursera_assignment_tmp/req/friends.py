import requests


# https://api.vk.com/method/users.get?v=5.71&access_token=17fd519317fd519317fd5193931795e7d2117fd17fd51934b9bef66fef03d01a94a9104&user_ids=konstmal
# {"response":[{"id":1320358,"first_name":"Konstantin","last_name":"Malinin"}]}

# https://api.vk.com/method/friends.get?v=5.71&access_token=17fd519317fd519317fd5193931795e7d2117fd17fd51934b9bef66fef03d01a94a9104&user_id=1320358&fields=bdate

# https://codebeautify.org/jsonviewer

def calc_age(uid):
    CURRENT_YEAR = 2019
    ACCESS_TOKEN = '17fd519317fd519317fd5193931795e7d2117fd17fd51934b9bef66fef03d01a94a9104'
    url = f"https://api.vk.com/method/users.get?v=5.71&access_token={ACCESS_TOKEN}&user_ids={uid}"

    http_proxy = "http://195.208.172.70:8080"
    https_proxy = "https://195.208.172.70:8080"

    proxy_dict = {
        "http": http_proxy,
        "https": https_proxy,
    }

    vk_answer = requests.get(url, proxies=proxy_dict).json()
    user_id = vk_answer["response"][0]["id"]

    url_friends = f"https://api.vk.com/method/friends.get?v=5.71 \
                    &access_token={ACCESS_TOKEN}&user_id={user_id}&fields=bdate"
    vk_answer = requests.get(url_friends, proxies=proxy_dict).json()
    vk_data = vk_answer['response']['items']

    friends_map = dict()

    for record in vk_data:
        if 'bdate' in record.keys():
            record_date = record['bdate'].split('.')
            if len(record_date) == 3:
                bdate_year = int(record_date[2])
                friend_age = CURRENT_YEAR - bdate_year

                if friend_age not in friends_map:
                    friends_map[friend_age] = 0

                friends_map[friend_age] += 1
    friends_list = sorted(friends_map.items(), key=lambda el: (-el[1], el[0]))

    return friends_list


if __name__ == '__main__':
    result = calc_age('reigning')
    print(result)
