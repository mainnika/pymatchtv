from bs4 import BeautifulSoup
from urllib import request
from matchtv.stream import Stream
import re
import demjson
import matchtv


class Match:
    def __init__(self, home, guest, url):
        self.home = home
        self.guest = guest
        self.url = url

    def __str__(self):
        return "home:{},guest:{}".format(self.home, self.guest)

    def get_streams(self):
        raw = request.urlopen(matchtv.BASE + self.url)
        soup = BeautifulSoup(raw.read(), "html.parser")
        streams = []

        frame = soup.find(id="spb_player_iframe")
        player_url = frame["src"]

        if not str.startswith(player_url, matchtv.BASE):
            return None

        raw = request.urlopen(player_url)
        soup = BeautifulSoup(raw.read(), "html.parser")

        for script in soup.find_all("script"):
            objs = re.findall(r"({[^}]*})", str(script))

            if objs is None:
                continue

            for obj in objs:
                try:
                    obj = demjson.decode(obj)

                    stream = Stream(obj["src"], obj["label"], obj["type"])
                    streams.append(stream)

                except (demjson.JSONDecodeError, KeyError):
                    continue

        return streams
