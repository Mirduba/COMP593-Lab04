import requests

def post_new_paste(title, body_text, expiration='N', listed=True):
    """
    Posts a new paste to PasteBin

    :param title: Paste title
    :param body_text: Paste body text
    :param expiration: Expiration date of paste(N=never, 10M=minutes, 1H, 1D,1W,2W,1M,6M,1Y)
    :param listed: Whether paste is publicly listed (True) or not (False)
    :returns: URL of new paste, if successful. Otherwise None.

    """
    print("Posting a new paste to PasteBin", end=" ")
    pastebin_param = {
        'api_dev_key': '109i-TsREMVJRHA5-Ox4SY8Zy0g-N5jW',
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_private':  0 if listed else 1,
        'api_paste_expire_date': expiration
    }

    paste_url = 'https://pastebin.com/api/api_post.php'
    response_message = requests.post(paste_url, data=pastebin_param)

    if response_message.status_code == requests.codes.ok:
        print("Success")
        return response_message.text
    else:
        print("Failure")
        print(f"Status code: {response_message.status_code}, Error reason: {response_message.reason}")
        return None


