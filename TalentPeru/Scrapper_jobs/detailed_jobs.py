import re
import uuid
from bs4 import BeautifulSoup


def remove_extra_spaces(text):
    """Removes multiple spaces from a string."""
    return re.sub(r"\s+", " ", text).strip()


class JobScraper:
    def __init__(self, view_value, session, n=10):
        self.view_value = view_value
        self.session = session
        self.n = n

    def get_n_job_description(self, job_n):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "es,en;q=0.9,en-US;q=0.8",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
            "pragma": "no-cache",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Opera";v="113", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
        }
        payload = {
            "frmLstOfertsLabo": "frmLstOfertsLabo",
            "frmLstOfertsLabo:modalidadAcceso": "03",
            "frmLstOfertsLabo:txtPerfil": "",
            "frmLstOfertsLabo:cboDep_focus": "",
            "frmLstOfertsLabo:cboDep_input": "15",
            "frmLstOfertsLabo:txtPuesto": "",
            "frmLstOfertsLabo:autocompletar_input": "",
            "frmLstOfertsLabo:autocompletar_hinput": "",
            "frmLstOfertsLabo:txtNroConv": "",
            f"frmLstOfertsLabo:idPnlRepeatPuestos:{job_n}:j_idt71": "",
            "javax.faces.ViewState": self.view_value,
        }
        url_post = "https://app.servir.gob.pe/DifusionOfertasExterno/faces/consultas/ofertas_laborales.xhtml"
        url_get = "https://app.servir.gob.pe/DifusionOfertasExterno/faces/consultas/detalle_ofertas_laborales.xhtml"

        # Realiza las solicitudes POST y GET
        self.session.post(url_post, headers=headers, data=payload, timeout=1)
        detail_i = self.session.get(url_get, headers=headers, timeout=1)

        return detail_i

    def get_details_data(self, html_soup_n):
        details = html_soup_n.find_all("div", class_="seccion-detalle")
        title_details = details[0]  # position, institution
        job_details = details[1]  # details
        job_details_dtl = job_details.find_all(
            "span", class_="sub-titulo"
        )  # Span details

        position = title_details.find("span", class_="sp-aviso0").get_text(strip=True)
        institution = title_details.find("span", class_="sp-aviso").get_text(strip=True)

        # Requisitos específicos
        job_req = job_details.find("p", class_="sub-titulo").find_all_next(
            "span", class_="sub-titulo-2"
        )

        requerimientos_job = {}
        for jr in job_req:
            key_req = self.remove_extra_spaces(jr.text.strip()).title()
            detail_req = jr.find_next("span").get_text(strip=True)
            if len(detail_req) > 0:
                requerimientos_job[key_req] = detail_req

        job_more_details = {}
        for jb in job_details_dtl:
            name = self.remove_extra_spaces(jb.text).title()
            value_html = jb.find_next("span")
            if name.lower() == "detalle:":
                # Obtener URL de la convocatoria
                name = "url_convocatoria"
                value = value_html.find("a", href=True)["href"]
                if value == "#":
                    value = value_html.get_text(strip=True).lower()
            else:
                value = self.remove_extra_spaces(
                    value_html.get_text(strip=True)
                ).title()
            job_more_details[name] = value

        job_more_details.update(requerimientos_job)
        job_more_details["position"] = position
        job_more_details["institution"] = institution.title()
        job_more_details["uuid"] = str(uuid.uuid5(uuid.NAMESPACE_DNS, position))

        return job_more_details

    def get_details_data_in_page(self):
        data_in_page = []
        for i in range(self.n):
            soup_i = BeautifulSoup(self.get_n_job_description(i).content, "html.parser")
            result_i = self.get_details_data(soup_i)
            data_in_page.append(result_i)
        return data_in_page

    def remove_extra_spaces(self, text):
        """Función auxiliar para limpiar espacios extra."""
        return " ".join(text.split())
