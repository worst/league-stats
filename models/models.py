from elixir import *

metadata.bind = "sqlite:///database.sqlite"
metadata.bind.echo = True


class Champion(Entity):
    name = Field(Unicode(20))
    title = Field(Unicode(30))
    thumbnail = Field(Text())
    splash_art = Field(Text())
    rel_date = Field(Date())

    def __repr__(self):
        return '<Champion %s, %s>' % (self.name, self.title)


class Summoner(Entity):
    summoner_name = Field(Unicode(30))
    summoner_id = Field(Integer)
    fname = Field(Unicode(15))
    lname = Field(Unicode(30))
    year = Field(Integer)
    teams = ManyToMany('Team')
    picture = Field(Unicode(30))

    def __repr__(self):
        return '<%s %s (%s)>' % (self.fname, self.lname, self.summoner_name)


class Side(Entity):
    color = Field(Integer)
    teams = OneToMany('Team')
    winners = OneToMany('Game')


class Team(Entity):
    side = ManyToOne('Side')
    summoners = ManyToMany('Summoner')
    champions = ManyToMany('Champion')
    game = ManyToOne('Game')


class Game(Entity):
    teams = OneToMany('Team')
    winner = ManyToOne('Side')
    date = Field(Date)
    length = Field(Integer)
    replay_path = Field(Text())
