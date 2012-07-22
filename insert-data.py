from models import *
from datetime import *

setup_all()
create_all()

champions = [["""Ahri""","""The Nine-Tailed Fox""",date(2011, 10, 14),"""AhriSquare.png""","""ahri.jpg"""],
["""Akali""","""The Fist of the Shadow""",date(2010, 5, 11),"""AkaliSquare.png""","""akali.jpg"""],
["""Alistar""","""The Minotaur""",date(2009, 2, 21),"""AlistarSquare.png""","""alistar.jpg"""],
["""Amumu""","""The Sad Mummy""",date(2009, 6, 26),"""AmumuSquare.png""","""amumu.jpg"""],
["""Anivia""","""The Cryophoenix""",date(2009, 6, 10),"""AniviaSquare.png""","""anivia.jpg"""],
["""Annie""","""The Dark Child""",date(2009, 2, 21),"""AnnieSquare.png""","""annie.jpg"""],
["""Ashe""","""The Frost Archer""",date(2009, 2, 21),"""AsheSquare.png""","""ashe.jpg"""],
["""Blitzcrank""","""The Great Steam Golem""",date(2009, 8, 02),"""BlitzcrankSquare.png""","""blitzcrank.jpg"""],
["""Brand""","""The Burning Vengeance""",date(2011, 8, 12),"""BrandSquare.png""","""brand.jpg"""],
["""Caitlyn""","""The Sheriff of Piltover""",date(2011, 11, 04),"""CaitlynSquare.png""","""caitlyn.jpg"""],
["""Cassiopeia""","""The Serpent's Embrace""",date(2010, 12, 14),"""CassiopeiaSquare.png""","""cassiepeia.jpg"""],
["""Cho'Gath""","""The Terror of the Void""",date(2009, 6, 26),"""ChoGathSquare.png""","""chogath.jpg"""],
["""Corki""","""The Daring Bombardier""",date(2009, 9, 19),"""CorkiSquare.png""","""corki.jpg"""],
["""Darius""","""The Hand of Noxus""",date(2012, 05, 23),"""DariusSquare.png""","""darius.jpg"""],
["""Dr. Mundo""","""The Madman of Zaun""",date(2009, 9, 02),"""DrMundoSquare.png""","""drmundo.jpg"""],
["""Draven""","""The Glorious Executioner""",date(2012, 6, 06),"""DravenSquare.png""","""draven.jpg"""],
["""Evelynn""","""The Widowmaker""",date(2009, 5, 01),"""EvelynnSquare.png""","""evelynn.jpg"""],
["""Ezreal""","""The Prodigal Explorer""",date(2010, 3, 16),"""EzrealSquare.png""","""ezreal.jpg"""],
["""Fiddlesticks""","""The Harbinger of Doom""",date(2009, 2, 21),"""FiddlesticksSquare.png""","""fiddlesticks.jpg"""],
["""Fiora""","""The Grand Duelist""",date(2012, 2, 29),"""FioraSquare.png""","""fiora.jpg"""],
["""Fizz""","""The Tidal Trickster""",date(2011, 11, 15),"""FizzSquare.png""","""fizz.jpg"""],
["""Galio""","""The Sentinel's Sorrow""",date(2010, 8, 10),"""GalioSquare.png""","""galio.jpg"""],
["""Gangplank""","""The Saltwater Scourge""",date(2009, 8, 19),"""GangplankSquare.png""","""gangplank.jpg"""],
["""Garen""","""The Might of Demacia""",date(2010, 4, 27),"""GarenSquare.png""","""garen.jpg"""],
["""Gragas""","""The Rabble Rouser""",date(2010, 2, 02),"""GragasSquare.png""","""gragas.jpg"""],
["""Graves""","""The Outlaw""",date(2011, 10, 19),"""GravesSquare.png""","""graves.jpg"""],
["""Hecarim""","""The Shadow of War""",date(2012, 4, 18),"""HecarimSquare.png""","""hecarim.jpg"""],
["""Heimerdinger""","""The Revered Inventor""",date(2009, 10, 10),"""HeimerdingerSquare.png""","""heimerdinger.jpg"""]]



for champion in champions:
	champ_data = Champion(name = champion[0],
						  title = champion[1],
						  rel_date = champion[2],
						  thumbnail = champion[3],
						  splash_art = champion[4])

session.commit()
