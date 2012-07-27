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

if __name__ == '__main__':
	app.debug = True
	app.run()