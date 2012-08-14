from flask import *
from models import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           page_title="Home",
                           org="CWRU",
                           root_url="/")


@app.route('/champions')
def champions():
    champions = Champion.query.all()

    return render_template('champion_list.html',
                           page_title="Champions",
                           org="CWRU",
                           root_url="../",
                           champions=champions)


@app.route('/champions/<champ>')
def champ_info(champ):
    champion = Champion.query.filter_by(name=champ).one()

    return render_template('champion.html',
                           page_title=champ,
                           org="CWRU",
                           root_url="../../",
                           champion=champion,
                           summoner_wins='',
                           summoner_percent="")


@app.route('/league')
def league():
    most_wins = {'summoner': 'Kihashi',
                 'wins': 500}
    percentage = {'summoner': 'PuddinPop',
                  'wins': 60}
    games = {'summoner': "ONLY MID THX",
             'number': 10000}
    most_popular = {'champion': 'Amumu',
                    'thumbnail': 'AmumuSquare.png',
                    'games': 100}
    winningest = {'champion': 'Singed',
                  'thumbnail': 'SingedSquare.png',
                  'percent': 80}

    return render_template('league.html',
                           page_title="League Statistics",
                           org="CWRU", root_url="../",
                           most_wins=most_wins,
                           percentage=percentage,
                           games=games,
                           most_popular=most_popular,
                           winningest=winningest)


@app.route('/summoners', methods=['GET', 'POST'])
def summoners():
    if request.method == 'POST':
        #Get results here
        search_string = request.form['search-term']
        results = []
        return render_template('summoner-search-results.html',
                               page_title='Summoners',
                               org='CWRU',
                               root_url='../',
                               results=results,
                               search=search_string)
    else:
        return render_template('summoner-search.html',
                               page_title='Summoners',
                               org='CWRU',
                               root_url='../')


@app.route('/summoners/<summoner_id>')
def summoner_info(summoner_id):
    summoner = {'name': 'Kihashi', 'fname': 'John', 'lname': 'Cleaver', 'rank': 1, 'lolking_id': 47160, 'win_percentage': 70, 'wins': 10, 'losses': 7}
    champ_popular = {'champion': 'Amumu',
                    'thumbnail': 'AmumuSquare.png',
                    'games': 90}
    champ_wins = {'champion': 'Amumu',
                    'thumbnail': 'AmumuSquare.png',
                    'games': 100}
    champ_percent = {'champion': 'Singed',
                    'thumbnail': 'SingedSquare.png',
                    'percent': 80}

    return render_template('summoner.html',
                           page_title=summoner['name'],
                           org="CWRU",
                           root_url='../../',
                           summoner=summoner,
                           champ_wins=champ_wins,
                           champ_percent=champ_percent,
                           champ_popular=champ_popular)

if __name__ == '__main__':
    setup_all()
    create_all()
    app.debug = True
    app.run(host='0.0.0.0')
