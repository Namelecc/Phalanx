import berserk
user = "USERNAME"
token = "API TOKEN"

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

stuff = client.games.export_by_player(user)
games = list(stuff)
for game in games:
    if game['status'] == "cheat":
            player_color = "black" 
            if game['players']['white']['user']['id'] == user.casefold: 
                player_color = "white"
            if game['winner'] != player_color:
                print(f"Cheater, {game['id']}")