from ..utils.utils import (
    goto_first_dep_page_payload,
    goto_last_page_payload,
    goto_next_page_payload,
    goto_prev_page_payload,
)
from ..config.settings import shared_columns
from ..config.settings import URL, HEADERS
from .detailed_jobs import (
    JobScraperDetails,
    depa_value,
    columns,
    paginator,
)
import requests
import tqdm

import pandas as pd, re, math, numpy as np
from bs4 import BeautifulSoup


def remove_extra_spaces(text):
    """Removes multiple spaces from a string."""
    return re.sub(r"\s+", " ", text).strip()


class JobScrapper:
    def __init__(
        self,
        dep="01",
        url=URL,
        headers=HEADERS,
    ):
        self.url = url
        self.headers = headers
        self.dep = dep
        # Obtenenmos la session y el valor de view_value
        self.first_session()

        # vamos a la primera pagina del departamento
        self.soup = self.go_first_page()
        # obtenemos el total de paginas existentes
        self.get_label_page()

        self.scrapper_fn = JobScraperDetails(
            view_value=self.view_state_value, session=self.session
        )
        self.data = []
        self.card_data = []

    # @staticmethod
    def scrapper_cards(self, html):
        jobs_info = html.find_all("div", class_="cuadro-vacantes")

        data_cards = []
        for job in jobs_info:
            position = job.find("div", class_="titulo-vacante").get_text(strip=True)
            card_details = job.find_all("span", class_="detalle-sp")
            info = [
                remove_extra_spaces(card_detail.get_text(strip=True))
                for card_detail in card_details
            ]
            data_cards.append(info + [position])
        # self.data_cards
        self.card_data.append(pd.DataFrame(data_cards))
        return self

    def scrapper_page(self, n=10) -> list:

        try:
            # insertar ubicacion por parametro
            detail_scrapper = self.scrapper_fn.get_details_data_in_page(n)

            self.data.append(detail_scrapper)
            return detail_scrapper
        except:
            pass

    def scrapper_seq(self, iteration_total, change_page, side=None):
        dep = self.dep
        name_depa = depa_value[dep].title()
        name_description = f"Departamento de {name_depa} - {dep} "

        if side is not None:
            name_description = f"Departamento de {name_depa} - {side}"
        if dep == "15":
            colour = "blue"
        else:
            colour = None

        for _ in tqdm.tqdm(
            range(iteration_total), desc=name_description, colour=colour
        ):
            page_content_jobs = change_page()
            self.scrapper_cards(page_content_jobs)

            jobs = page_content_jobs.find_all("div", class_="cuadro-vacantes")
            n_jobs = len(jobs)
            # print(n_jobs)
            self.scrapper_page(n_jobs)

    @staticmethod
    def get_metadata_data(html_soup):
        ubication_spans = html_soup.find_all("span", text="Ubicación:")
        locations = [
            ubication.find_next("span", class_="detalle-sp").get_text(strip=True)
            for ubication in ubication_spans
        ]
        locations = [remove_extra_spaces(loc) for loc in locations]
        return locations

    def get_data(self):
        data_details = pd.concat(self.data, ignore_index=True)
        data_details = data_details.rename(columns=columns)
        card_data = pd.concat(self.card_data, ignore_index=True)
        card_data.columns = shared_columns
        title = ["job_posting_number", "public_institution"]
        for t in title:
            card_data[t] = card_data[t].str.title().str.strip()
        try:
            data_details = pd.merge(data_details, card_data, how="left")
        except:
            try:
                data_details["ubication"] = card_data["ubication"]
            except:
                pass
        # data_details['ubication'] = data
        data_details.loc[data_details["ubication"].isna(), "ubication"] = depa_value[
            self.dep
        ]
        # depa_value[dep]
        data_details = data_details.replace({np.nan: None})
        # print(data_details)
        return data_details

    def scrapper_sequential(self):
        total_pages = self.total_pages
        self.scrapper_cards(self.soup)
        self.scrapper_page()  # primera pagian
        n_discount = 1
        # print(total_pages)

        iteration_total = total_pages - n_discount
        change_page = self.go_next_page
        self.scrapper_seq(iteration_total, change_page)
        return self.get_data()

    def scrapper_both_left(self):
        self.scrapper_page()
        change_page = self.go_next_page

        total_pages = self.total_pages
        n_discount = 2
        iteration_total = math.floor((total_pages - n_discount) / 2)

        self.scrapper_seq(iteration_total, change_page, side="izquierda a derecha")
        return self.get_data()

    def scrapper_both_right(self):
        page_content_jobs = self.go_last_page()
        self.scrapper_cards(page_content_jobs)

        jobs = page_content_jobs.find_all("div", class_="cuadro-vacantes")
        n_jobs = len(jobs)
        # ubication = self.get_ubication(page_content_jobs)
        self.scrapper_page(n_jobs)
        change_page = self.go_prev_page

        total_pages = self.total_pages
        n_discount = 2
        iteration_total = math.ceil((total_pages - n_discount) / 2)

        self.scrapper_seq(iteration_total, change_page, side="derecha a izquierda")
        return self.get_data()

    # @staticmethod
    def get_label_page(self):

        page_n = self.soup.find("label", class_="control-label btn-paginator-cnt").text
        actual_page, last_page = paginator(page_n)
        self.total_pages = last_page
        return page_n

    @staticmethod
    def get_view_state(soup):
        """Obtiene el valor del view state del HTML."""
        view_state_input = soup.find("input", {"name": "javax.faces.ViewState"})
        view_state_value = view_state_input["value"]
        return view_state_value

    def first_session(self):
        session = requests.Session()
        fp_requests = session.get(self.url, headers=self.headers)
        # Es la pagina que se muestra al cargar no es relevante por el momento
        fp_soup = BeautifulSoup(fp_requests.content, features="lxml")
        view_state_vale = self.get_view_state(fp_soup)
        self.session = session
        self.view_state_value = view_state_vale
        self.fpsoup = fp_soup
        return self

    def goto_page(self, data: dict):
        """Realiza una petición POST para navegar entre páginas. Retorna un Html"""
        result_page = self.session.post(
            url=self.url, headers=self.headers, data=data
        ).content
        return result_page

    def go_first_page(self):
        first_page_payload = goto_first_dep_page_payload(
            self.view_state_value, self.dep
        )
        first_page_reg = self.goto_page(first_page_payload)
        return BeautifulSoup(first_page_reg, features="lxml")

    def go_next_page(self):
        next_page_payload = goto_next_page_payload(self.view_state_value, self.dep)
        next_page_reg = self.goto_page(next_page_payload)
        return BeautifulSoup(next_page_reg)

    def go_last_page(self):
        last_page_payload = goto_last_page_payload(self.view_state_value, self.dep)
        last_page_reg = self.goto_page(last_page_payload)
        return BeautifulSoup(last_page_reg)

    def go_prev_page(self):
        prev_page_payload = goto_prev_page_payload(self.view_state_value, self.dep)
        prev_page_reg = self.goto_page(prev_page_payload)
        return BeautifulSoup(prev_page_reg)
