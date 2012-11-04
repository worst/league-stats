from flask import *
from models import *
import parse
from upload import *
from sqlalchemy import asc, desc

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
    champion = Champion.get_by(name=champ)
    summoner_wins = Summoner_Stats.query.filter_by(champion=champion).order_by(desc(Summoner_Stats.wins)).first()
    summoner_percent = Summoner_Stats.query.filter_by(champion=champion).order_by(desc(Summoner_Stats.wins/Summoner_Stats.games_played)).first()
    recent_matches = Game.query.order_by(desc(Game.date)).filter(Game.teams.any(Team.members.any(TeamMember.champion == champion))).limit(10).all()

    return render_template('champion.html',
                           page_title=champ,
                           org="CWRU",
                           root_url="../../",
                           champion=champion,
                           summoner_wins=summoner_wins,
                           summoner_percent=summoner_percent,
                           matches=recent_matches)


@app.route('/league')
def league():
    summoner_wins = Summoner.query.order_by(desc(Summoner.wins)).first()
    summoner_percent = Summoner.query.order_by(desc(Summoner.wins / (Summoner.wins + Summoner.losses))).first()
    summoner_games = Summoner.query.order_by(desc(Summoner.wins + Summoner.losses)).first()
    champ_wins = Champion.query.order_by(desc(Champion.wins)).first()
    champ_percent = Champion.query.order_by(desc(Champion.wins / (Champion.wins + Champion.losses))).first()
    champ_popular = Champion.query.order_by(desc(Champion.wins + Champion.losses)).first()
    recent_matches = Game.query.order_by(desc(Game.date)).limit(10).all()

    return render_template('league.html',
                           page_title="League Statistics",
                           org="CWRU", root_url="../",
                           summoner_wins=summoner_wins,
                           summoner_percent=summoner_percent,
                           summoner_games=summoner_games,
                           champ_wins=champ_wins,
                           champ_percent=champ_percent,
                           champ_popular=champ_popular,
                           matches=recent_matches)


@app.route('/summoners', methods=['GET', 'POST'])
def summoners():
    if request.method == 'POST':
        #Get results here
        search_string = request.form['search-term']
        if search_string == '':
            results = Summoner.query.all()
        else:
            results = Summoner.query.filter_by(summoner_name=search_string)
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


@app.route('/summoners/<riot_id>')
def summoner_info(riot_id):
    summoner = Summoner.get_by(summoner_name=riot_id)
    champ_popular = Summoner_Stats.query.filter_by(summoner=summoner).order_by(desc(Summoner_Stats.games_played)).first()
    champ_wins = Summoner_Stats.query.filter_by(summoner=summoner).order_by(desc(Summoner_Stats.wins)).first()
    champ_percent = Summoner_Stats.query.filter_by(summoner=summoner).order_by(desc(Summoner_Stats.wins/Summoner_Stats.games_played)).first()
    recent_matches = Game.query.order_by(desc(Game.date)).filter(Game.teams.any(Team.members.any(TeamMember.summoner == summoner))).limit(10).all()

    return render_template('summoner.html',
                           page_title=summoner.summoner_name,
                           org="CWRU",
                           root_url='../../',
                           summoner=summoner,
                           champ_wins=champ_wins,
                           champ_percent=champ_percent,
                           champ_popular=champ_popular,
                           matches=recent_matches)


@app.route('/upload', methods=['GET', 'POST'])
def start_upload():
    if request.method == 'GET':
        return render_template('upload.html',
                               page_title="Upload",
                               org="CWRU",
                               root_url="../")
    elif request.method == 'POST':
        file = request.files['replay-upload']
        uploader = Uploader(app)

        if uploader.upload_file(file):
            parser = parse.UploadParser(uploader.get_upload_path())
            parser.process_replay_data()
            return render_template('upload.html',
                                   page_title="Upload",
                                   org="CWRU",
                                   root_url="../",
                                   success=True)
        else:
            return "Upload Failed. Please try it again."


if __name__ == '__main__':
    setup_all()
    create_all()
    app.debug = True
    app.run(host='0.0.0.0')
