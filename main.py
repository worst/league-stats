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
	champion = {'name': champ, 'portrait': "http://placehold.it/320x240", "subtitle": "The Damage Dealer"}

	return render_template('champion.html', page_title=champ, org="CWRU", root_url="../../", champion=champion, summoner_wins='', summoner_percent="")

if __name__ == '__main__':
	app.debug = True
	app.run()