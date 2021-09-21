import cherrypy

FIN = 'base.html'


def leggi_html():
    with open(FIN, 'r') as fin:
        html = fin.read()
        return html


class InserisciVerbale(object):
    @cherrypy.expose
    def index(self):
        return leggi_html()

    @cherrypy.expose
    def generate(self, chi, data=None, ora=None, pdl=None,
                 delimitazione_c=None, delimitazione_m=None, delimitazione_nc=None, delimitazione_descrizione=None, delimitazione_azione=None,
                 pdl_c=None, pdl_m=None, pdl_nc=None, pdl_descrizione=None, pdl_azione=None,
                 dpi_c=None, dpi_m=None, dpi_nc=None, dpi_descrizione=None, dpi_azione=None,
                 ordine_c=None, ordine_m=None, ordine_nc=None, ordine_descrizione=None, ordine_azione=None,
                 sollevamenti_c=None, sollevamenti_m=None, sollevamenti_nc=None, sollevamenti_descrizione=None, sollevamenti_azione=None,
                 attrezzature_c=None, attrezzature_m=None, attrezzature_nc=None, attrezzature_descrizione=None, attrezzature_azione=None,
                 guida_c=None, guida_m=None, guida_nc=None, guida_descrizione=None, guida_azione=None,
                 ponteggi_c=None, ponteggi_m=None, ponteggi_nc=None, ponteggi_descrizione=None, ponteggi_azione=None,
                 pimus_c=None, pimus_m=None, pimus_nc=None, pimus_descrizione=None, pimus_azione=None,
                 quota_c=None, quota_m=None, quota_nc=None, quota_descrizione=None, quota_azione=None,
                 confinati_c=None, confinati_m=None, confinati_nc=None, confinati_descrizione=None, confinati_azione=None,
                 altro_c=None, altro_m=None, altro_nc=None, altro_descrizione=None, altro_azione=None,
                 gravita=None
                 ):
        print(data, ora)
        return 'verbale eseguito da %s' % chi


if __name__ == '__main__':
    cherrypy.quickstart(InserisciVerbale())
