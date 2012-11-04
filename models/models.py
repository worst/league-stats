from elixir import *

metadata.bind = "sqlite:///database.sqlite"
metadata.bind.echo = True


class Champion(Entity):
    name = Field(Unicode(20))
    riot_name = Field(Unicode(30))
    title = Field(Unicode(30))
    thumbnail = Field(Text())
    splash_art = Field(Text())
    rel_date = Field(Date())
    wins = Field(Integer, default=0)
    losses = Field(Integer, default=0)
    stats = OneToMany("Summoner_Stats")
    member = OneToMany('TeamMember')

    def __repr__(self):
        return '<Champion %s, %s>' % (self.name, self.title)


class Summoner(Entity):
    summoner_name = Field(Unicode(30))
    riot_id = Field(Integer)
    fname = Field(Unicode(15))
    lname = Field(Unicode(30))
    year = Field(Integer)
    picture = Field(Unicode(30))
    stats = OneToMany('Summoner_Stats')
    wins = Field(Integer, default=0)
    losses = Field(Integer, default=0)
    member = OneToMany('TeamMember')

    def __repr__(self):
        return '<%s %s (%s)>' % (self.fname, self.lname, self.summoner_name)


class Side(Entity):
    color = Field(Integer)
    teams = OneToMany('Team')
    winners = OneToMany('Game')


class Team(Entity):
    side = ManyToOne('Side')
    game = ManyToOne('Game')
    members = OneToMany('TeamMember')


class TeamMember(Entity):
    summoner = ManyToOne('Summoner')
    champion = ManyToOne('Champion')
    team = ManyToOne('Team')


class Game(Entity):
    teams = OneToMany('Team')
    winner = ManyToOne('Side')
    date = Field(Date)
    length = Field(Integer)
    replay_path = Field(Text())


class Summoner_Stats(Entity):
    summoner = ManyToOne('Summoner')
    champion = ManyToOne('Champion')
    games_played = Field(Integer, default=0)
    wins = Field(Integer, default=0)
    losses = Field(Integer, default=0)
