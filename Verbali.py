import cherrypy
import sqlite3
import os
import pandas as pd

FIN = 'base.html'
DB_STRING = "db.sqlite"


def leggi_html():
    with open(FIN, 'r') as fin:
        html = fin.read()
        return html


class DB(object):
    def __init__(self):
        with sqlite3.connect(DB_STRING) as con:
            con.execute("""
            CREATE TABLE verbali 
            (
                id INTEGER PRIMARY KEY,
                chi TEXT, 
                data TEXT, 
                ora TEXT, 
                npdl TEXT,
                delimitazione TEXT, 
                delimitazione_descrizione TEXT, 
                delimitazione_azione TEXT,
                pdl TEXT, 
                pdl_descrizione TEXT, 
                pdl_azione TEXT,
                dpi TEXT, 
                dpi_descrizione TEXT, 
                dpi_azione TEXT,
                ordine TEXT,
                ordine_descrizione TEXT, 
                ordine_azione TEXT,
                sollevamenti TEXT, 
                sollevamenti_descrizione TEXT, 
                sollevamenti_azione TEXT,
                attrezzature  TEXT, 
                attrezzature_descrizione TEXT, 
                attrezzature_azione TEXT,
                guida TEXT,
                guida_descrizione TEXT, 
                guida_azione TEXT,
                ponteggi TEXT,
                ponteggi_descrizione TEXT, 
                ponteggi_azione TEXT,
                pimus TEXT, 
                pimus_descrizione TEXT, 
                pimus_azione TEXT,
                quota TEXT, 
                quota_descrizione TEXT, 
                quota_azione TEXT,
                confinati TEXT, 
                confinati_descrizione TEXT, 
                confinati_azione TEXT,
                altro TEXT, 
                altro_descrizione TEXT, 
                altro_azione TEXT,
                gravita TEXT
            )""")

        def inserisci(self):
            sql = '''
            INSERT INTO verbali(chi, npdl)
            VALUES (?, ?)
            '''

            with sqlite3.connect(DB_STRING) as con:
                con.execute(sql,
                            ['a', '21C12345'])


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
        sql = '''
        INSERT INTO verbali(
            chi, data, ora, npdl,
            delimitazione, delimitazione_descrizione, delimitazione_azione,
            pdl, pdl_descrizione, pdl_azione,
            dpi, dpi_descrizione, dpi_azione,
            ordine, ordine_descrizione, ordine_azione,
            sollevamenti, sollevamenti_descrizione, sollevamenti_azione,
            attrezzature, attrezzature_descrizione, attrezzature_azione,
            guida, guida_descrizione, guida_azione,
            ponteggi, ponteggi_descrizione, ponteggi_azione,
            pimus, pimus_descrizione, pimus_azione,
            quota, quota_descrizione, quota_azione,
            confinati, confinati_descrizione, confinati_azione,
            altro, altro_descrizione, altro_azione,
            gravita
            )
        VALUES (
            ?, ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?
            )
                    '''

        with sqlite3.connect(DB_STRING) as con:
            con.execute(sql,
                        [chi, data, ora, npdl,
                         delimitazione, delimitazione_descrizione, delimitazione_azione,
                         pdl, pdl_descrizione, pdl_azione,
                         dpi, dpi_descrizione, dpi_azione,
                         ordine, ordine_descrizione, ordine_azione,
                         sollevamenti, sollevamenti_descrizione, sollevamenti_azione,
                         attrezzature, attrezzature_descrizione, attrezzature_azione,
                         guida, guida_descrizione, guida_azione,
                         ponteggi, ponteggi_descrizione, ponteggi_azione,
                         pimus, pimus_descrizione, pimus_azione,
                         quota, quota_descrizione, quota_azione,
                         confinati, confinati_descrizione, confinati_azione,
                         altro, altro_descrizione, altro_azione,
                         gravita])
        return 'verbale eseguito da %s - n.pdl %s<br>--->%s<--\n%s' % (chi, data, ora, delimitazione_azione)


if __name__ == '__main__':
    # db = DB()

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
