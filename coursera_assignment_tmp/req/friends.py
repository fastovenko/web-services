import requests


# https://api.vk.com/method/users.get?v=5.71&access_token=17fd519317fd519317fd5193931795e7d2117fd17fd51934b9bef66fef03d01a94a9104&user_ids=konstmal
# {"response":[{"id":1320358,"first_name":"Konstantin","last_name":"Malinin"}]}

# https://api.vk.com/method/friends.get?v=5.71&access_token=17fd519317fd519317fd5193931795e7d2117fd17fd51934b9bef66fef03d01a94a9104&user_id=1320358&fields=bdate

# https://codebeautify.org/jsonviewer

def calc_age(uid):
    ACCESS_TOKEN = '17fd519317fd519317fd5193931795e7d2117fd17fd51934b9bef66fef03d01a94a9104'
    url = f"https://api.vk.com/method/users.get?v=5.71&access_token={ACCESS_TOKEN}&user_ids={uid}"

    http_proxy = "http://195.208.172.70:8080"
    https_proxy = "https://195.208.172.70:8080"

    proxy_dict = {
        "http": http_proxy,
        "https": https_proxy,
    }

    # Passing Parameters
    # params = {'user': 'uid', 'token': 'ACCESS_TOKEN'}

    vk_answer = requests.get(url, proxies=proxy_dict).json()
    user_id = vk_answer["response"][0]["id"]

    url_friends = f"https://api.vk.com/method/friends.get?v=5.71 \
                    &access_token={ACCESS_TOKEN}&user_id={user_id}&fields=bdate"
    vk_answer = requests.get(url_friends, proxies=proxy_dict).json()
    vk_data = vk_answer['response']['items']

    return vk_data


if __name__ == '__main__':
    result = calc_age('reigning')
    print(result)

    i = 1
    for record in result:
        if 'bdate' in record.keys():
            print(f"{i} {record['id']} ----- {record['bdate']}")
            i += 1

