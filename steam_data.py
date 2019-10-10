import urllib, json
import urllib.request as ur
import numpy as np
import matplotlib.pyplot as plt

keys = {
    'ZonaVRQRO01' : 76561198980269971,
    'ZonaVRQRO02' : 76561198979834687,
    'ZonaVRQRO03' : 76561198980073163,
    'ZonaVRQRO04' : 76561198980031850,
    'ZonaVRQRO05' : 76561198982534237
}

i = 0;

user_jsons = []
game_values = []
game_names = []
api_key = "69D6E24D23A131DE7F1E38DFC9B7A165"
total = []
# user_jsons = [np.load("ex.json")]

for key in keys.values():
    print(key)
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+ api_key + "&steamid=" + str(key) +"&include_appinfo=1&include_played_free_games=1&format=json"
    response = ur.urlopen(url)
    data = json.loads(response.read())
    user_jsons.append(data)


for json in user_jsons:
    print("------------------------")
    print("|                      |")
    print("| Datos de ZonaVRQRO0" + str(i+1) + " |")
    print("|                      |")
    print("------------------------")
    if('games' in json['response']):
        games = json['response']['games']
        # del json['response']['games']['VRChat']
    else:
        games = []
    fig, ax = plt.subplots()
    plt.figure(figsize=(20,10))
    plt.suptitle("ZonaVRQRO0" + str(i+1))
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
    plt.ylabel('Horas')
    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='x-small'
    )
    plt.bar(game_names, game_values)
    plt.margins(0, 0.1)
    plt.tight_layout()
    plt.savefig("ZonaVRQRO0"+str(i+1), dpi=300)
    total.append(total_hours/60)
    i += 1;

plt.tight_layout()
plt.figure(figsize=(20,10))
plt.bar(keys.keys(), total)
plt.savefig("Total", dpi=300)
