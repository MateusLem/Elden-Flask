from flask import Flask, render_template, request, redirect, session, flash, url_for
import requests

app = Flask(__name__)


@app.route('/api-consumer', methods=['GET'])
def consume_api():
    api_url = 'https://eldenring.fanapis.com/api/npcs'
    response = requests.get(api_url)
    if response.status_code == 200:

        data = response.json()
        return data
    else:

        return 'Error: Unable to retrieve data from the API.'


@app.route('/ammos')
def ammos():
    api_url = 'https://eldenring.fanapis.com/api/ammos'
    response = requests.get(api_url)
    return render_template('./pages/Ammos.html', title="Ammos", response=response)


@app.route('/armors')
def armors():
    api_url = 'https://eldenring.fanapis.com/api/armors'
    response = requests.get(api_url)
    return render_template('./pages/Armors.html', title="Armors", response=response)


@app.route('/ashes-of-war')
def ashes():
    api_url = 'https://eldenring.fanapis.com/api/ashes'
    response = requests.get(api_url)
    return render_template('./pages/AshesOfWar.html', title="Ashes of War", response=response)


@app.route('/bosses')
def bosses():
    api_url = 'https://eldenring.fanapis.com/api/bosses'
    response = requests.get(api_url)
    return render_template('./pages/Bosses.html', title="Bosses", response=response)


@app.route('/classes')
def classes():
    api_url = 'https://eldenring.fanapis.com/api/classes'
    response = requests.get(api_url)
    return render_template('./pages/Classes.html', title="Classes", response=response)


@app.route('/creatures')
def creatures():
    api_url = 'https://eldenring.fanapis.com/api/creatures'
    response = requests.get(api_url)
    return render_template('./pages/Creatures.html', title="Creatures", response=response)


@app.route('/incantations')
def incantations():
    api_url = 'https://eldenring.fanapis.com/api/incantations'
    response = requests.get(api_url)
    return render_template('./pages/Incantations.html', title="Incantations", response=response)


@app.route('/items')
def items():
    api_url = 'https://eldenring.fanapis.com/api/items'
    response = requests.get(api_url)
    return render_template('./pages/Items.html', title="Items", response=response)


@app.route('/locations')
def locations():
    api_url = 'https://eldenring.fanapis.com/api/locations'
    response = requests.get(api_url)
    return render_template('./pages/Locations.html', title="Locations", response=response)


@app.route('/npcs')
def npcs():
    api_url = 'https://eldenring.fanapis.com/api/npcs'
    response = requests.get(api_url)
    return render_template('./pages/Npcs.html', title="NPCs", response=response)


@app.route('/shields')
def shields():
    api_url = 'https://eldenring.fanapis.com/api/shields'
    response = requests.get(api_url)
    return render_template('./pages/Shields.html', title="Shields", response=response)


@app.route('/sorceries')
def sorceries():
    api_url = 'https://eldenring.fanapis.com/api/sorceries'
    response = requests.get(api_url)
    return render_template('./pages/Sorceries.html', title="Sorceries", response=response)


@app.route('/spirits')
def spirits():
    api_url = 'https://eldenring.fanapis.com/api/spirits'
    response = requests.get(api_url)
    return render_template('./pages/Spirits.html', title="Spirits", response=response)


@app.route('/talismans')
def talismans():
    api_url = 'https://eldenring.fanapis.com/api/talismans'
    response = requests.get(api_url)
    return render_template('./pages/Talismans.html', title="Talismans", response=response)


@app.route('/weapons')
def weapons():
    api_url = 'https://eldenring.fanapis.com/api/weapons'
    response = requests.get(api_url)
    return render_template('./pages/Weapons.html', title="Weapons", response=response)


if __name__ == '__main__':
    app.run(debug=True)
