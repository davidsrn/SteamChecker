# encoding=utf8
import sys
import urllib, json
# import urllib.request as ur
import numpy as np
import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding('utf8')

# i = 0;

user_jsons = []
game_values = []
game_names = []
api_key = "0ED38B6C1B1501586ECD21A8A09A1A47"
total = []
mostla = 76561198320021572

# url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=" + api_key + "&steamid=" + str(mostla) + "&relationship=friend"
url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=0ED38B6C1B1501586ECD21A8A09A1A47&steamid=76561198320021572&relationship=friend"
response = urllib.urlopen(url)
keys_json = json.loads(response.read())['friendslist']['friends']
keys = []

info = []

for key in keys_json:
    keys.append(key['steamid'])

url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=0ED38B6C1B1501586ECD21A8A09A1A47&steamids=" + str(keys)
response = urllib.urlopen(url)
players = json.loads(response.read())['response']['players']

for player in players:
    info.append([player['personaname'], player['steamid'], "null"])

for key in info:
    print(key)
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+ api_key + "&steamid=" + str(key[1]) +"&include_appinfo=1&include_played_free_games=1&format=json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    key[2] = data

# print(info)
# #
#
i = 0;
for player in info:
    print("------------------------")
    print("|                      |")
    print("| Datos de " + player[0] + " |")
    print("|                      |")
    print("------------------------")
    if('games' in player[2]['response']):
        games = player[2]['response']['games']
        # del json['response']['games']['VRChat']
    else:
        games = []
    fig, ax = plt.subplots()
    # plt.figure(figsize=(20,10))
    # plt.suptitle(player[0])
    total_hours = 0
    for game in games:
        if game['name'] != "VRChat" and game['name'] != "YouTube VR":
            print("Game id")
            print(game['appid'])
            print("Game name")
            print(game['name'])
            game_names.append(str(game['name']))
            print("Tiempo de juego total: ")
            print(game['playtime_forever'])
            total_hours += game['playtime_forever']
            game_values.append(game['playtime_forever']/60)
    x = np.arange(len(game_names))
    # plt.ylabel('Horas')
    # plt.xticks(
    #     rotation=45,
    #     horizontalalignment='right',
    #     fontweight='light',
    #     fontsize='x-small'
    # )
    # plt.bar(game_names, game_values)
    # plt.margins(0, 0.1)
    # plt.tight_layout()
    # plt.savefig(player[0], dpi=300)
    total.append([player[0], total_hours/60])
    i += 1;


plt.tight_layout()
plt.figure(figsize=(20,10))
total = np.array(total)
plt.bar(total[:, 0], total[:, 1])
plt.xticks(
rotation=45,
horizontalalignment='right',
fontweight='light',
fontsize='x-small'
)
plt.savefig("Total", dpi=300)
