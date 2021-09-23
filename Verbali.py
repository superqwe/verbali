import cherrypy
import sqlite3
import os

FIN = 'base.html'
DB_STRING = "db.sqlite"


def leggi_html():
    with open(FIN, 'r') as fin:
        html = fin.read()
        return html


class InserisciVerbale(object):
    @cherrypy.expose
    def index(self):
        return leggi_html()

    @cherrypy.expose
    def salva(self, chi, data=None, ora=None, npdl=None,
              delimitazione=None, delimitazione_descrizione=None, delimitazione_azione=None,
              pdl=None, pdl_descrizione=None, pdl_azione=None,
              dpi=None, dpi_descrizione=None, dpi_azione=None,
              ordine=None, ordine_descrizione=None, ordine_azione=None,
              sollevamenti=None, sollevamenti_descrizione=None, sollevamenti_azione=None,
              attrezzature=None, attrezzature_descrizione=None, attrezzature_azione=None,
              guida=None, guida_descrizione=None, guida_azione=None,
              ponteggi=None, ponteggi_descrizione=None, ponteggi_azione=None,
              pimus=None, pimus_descrizione=None, pimus_azione=None,
              quota=None, quota_descrizione=None, quota_azione=None,
              confinati=None, confinati_descrizione=None, confinati_azione=None,
              altro=None, altro_descrizione=None, altro_azione=None,
              gravita=None
              ):
        return 'verbale eseguito da %s - n.pdl %s<br>--->%s<--' % (chi, data,ora)


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(InserisciVerbale(), '/', conf)
