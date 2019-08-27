#!/usr/bin/env python


import cachetools.func
import flask
import lxml.html
import requests

MANAGER_URL = "https://www.baseball-reference.com/managers/bochybr01.shtml"


@cachetools.func.ttl_cache(ttl=(15 * 60))
def get_document(url=MANAGER_URL):
    return requests.get(url).text


def extract_table(doc, table_id):
    return doc.find('.//table[@id="{}"]'.format(table_id))


def extract_table_footer(table):
    return table.find("./tfoot")


def extract_field(row, field):
    return row.find('.//td[@data-stat="{}"]'.format(field)).text


def extract_row(rows, index):
    return rows.find(".//tr[{}]".format(index))


def get_wins(doc):
    table = extract_table(doc, "manager_stats")
    footer = extract_table_footer(table)
    row = extract_row(footer, "last()")
    value = extract_field(row, "W")

    return value


def get_revised(doc):
    return doc.find("./head/meta[@name='revised']").attrib["content"]


class HowManyManagerWins(flask.Flask):

    def __init__(self, manager_url, name):
        self.manager_url = manager_url
        super().__init__(name)
        self.route("/")(self.index)

    def index(self):
        doc = lxml.html.fromstring(get_document(self.manager_url))
        wins = get_wins(doc)
        revised = get_revised(doc)
        content = flask.render_template("index.html", wins=wins, revised=revised)
        return flask.make_response(content)


def create_app():
    return HowManyManagerWins(MANAGER_URL, "HowManyWinsDoesBruceBochyHave")


if __name__ == "__main__":
    create_app().run()
