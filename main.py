import requests
import config


def get_response():
    session = requests.session()
    session.headers.update({'User-Agent': config.userAgentKateApp})
    response = session.get("https://api.vk.com/method/audio.search",
                           params=[('access_token', config.tokenKateApp),
                                   ('q', 'pharaoh'),
                                   ('v', '5.95'),
                                   ('count', '50')]
                           )
    print(response.text)


if __name__ == '__main__':
    get_response()
