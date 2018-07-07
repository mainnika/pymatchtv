from urllib import request
from time import localtime, strftime
from matchtv.match import Match
import json
import matchtv


class Api:

    @staticmethod
    def get_matches():
        today = strftime("%Y%m%d", localtime())
        api_cmd = "{}/stats/Api/listGamesByDate.json?date={}".format(matchtv.BASE, today)
        raw = request.urlopen(api_cmd)
        data = json.loads(raw.read())

        current = data[today]
        rubrics = current["rubrics"]

        for rubric_id in rubrics:
            rubric = rubrics[rubric_id]
            championships = rubric["championships"]
            matches = []

            for championship_id in championships:
                championship = championships[championship_id]
                games = championship["games"]

                for game in games:
                    home = game["home"]["name"]
                    guest = game["guest"]["name"]
                    url = game["url"]

                    matches.append(Match(home, guest, url))

        return matches
