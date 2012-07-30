from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', page_title="Home", org="CWRU", root_url="/")

@app.route('/champions')
def champions():
	champions = [{'name': 'Amumu'}, 
				 {'name': 'Akali'}, 
				 {'name': 'Alistar'}, 
				 {'name': 'Ahri'}, 
				 {'name': 'Anivia'}, 
				 {'name': 'Annie'}, 
				 {'name': 'Ashe'}, 
				 {'name': 'Blitzcrank'}, 
				 {'name': 'Brand'}, 
				 {'name': 'Caitlyn'}, 
				 {'name': 'Cassiopeia'}, 
				 {'name': 'Galio'}, 
				 {'name': 'Gangplank'}, 
				 {'name': 'Jayce'}]

	return render_template('champion_list.html', page_title="Champions", org="CWRU", root_url="../", champions=champions)

@app.route('/champions/<champ>')
def champ_info(champ):
	champion = {'name': champ, 'portrait': "http://placehold.it/320x240", "subtitle": "The Defender of Tomorrow"}

	return render_template('champion.html', page_title=champ, org="CWRU", root_url="../../", champion=champion, summoner_wins='', summoner_percent="")

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

	return render_template('league.html', page_title="League Statistics", org="CWRU", root_url="../", most_wins=most_wins, percentage=percentage, games=games, most_popular=most_popular, winningest=winningest)

if __name__ == '__main__':
	app.debug = True
	app.run()