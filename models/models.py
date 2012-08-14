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
