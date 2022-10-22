from vkaudiotoken import get_kate_token, get_vk_official_token, TwoFAHelper

login = "YOUR_LOGIN"
password = "YOUR_PASSWORD"
# get Kate Mobile App token and user agent
kate = get_kate_token(login, password)
print(kate['token'])
print(kate['user_agent'])

# get official Android app token and user agent
androidApp = get_vk_official_token(login, password)
print(androidApp['token'])
print(androidApp['user_agent'])

f = open('config.py', 'w')
f.write(f"tokenKate = '{kate['token']}'\nuserAgentKate = '{kate['user_agent']}'\n")
f.write(f"tokenAndroidApp = '{androidApp['token']}'\nuserAgentAndroidApp = '{androidApp['user_agent']}'\n")
f.close()
