import requests
import warnings
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup as bsoup
from .utils import limpiar_espacios, total_numbers
from .global_env import URL, HEADERS, PAYLOAD

warnings.filterwarnings("ignore")

cookies = {
    "JSESSIONID": "AfLN1NxlepP0QpGSuesFamCh.node31",
    "_ga": "GA1.3.1210958502.1727727309",
    "_gid": "GA1.3.1263883292.1727727309",
}


def get_payload(soup):
    view_state_input = soup.find("input", {"name": "javax.faces.ViewState"})
    view_state_value = view_state_input["value"]
    PAYLOAD["javax.faces.ViewState"] = view_state_value
    return PAYLOAD


def first_session(url=URL, head=HEADERS):

    session = requests.Session()

    proxy = {"ip": "67.43.236.19", "port": "17293"}

    p = {
        "http": f"http://{proxy['ip']}:{proxy['port']}",
        "https": f"http://{proxy['ip']}:{proxy['port']}",
    }

    fp_request = session.get(url, headers=head, cookies=cookies, proxies=p, timeout=10)

    fp_page_soup = bsoup(fp_request.content, features="lxml")
    payload = get_payload(fp_page_soup)
    return session, fp_page_soup, payload


def next_page(data: dict, session: requests.Session):
    result_next_page = session.post(url=URL, headers=HEADERS, data=data).content
    return result_next_page


def souper(content_html):
    soup_html = bsoup(content_html, features="lxml")
    return soup_html


def get_label_page(soup_html):

    page_n = soup_html.find("label", class_="control-label btn-paginator-cnt").text
    return page_n


def find_jobs(page: bsoup):
    jobs_info = page.find_all("div", class_="cuadro-vacantes")
    return jobs_info


def get_info_jobs(job_n):
    """
    Obtienen la informacion de los trabajos
    """
    position = job_n.find("div", class_="titulo-vacante").get_text()

    spans_cuadro = job_n.find_all("span", class_="detalle-sp")
    # print(psan)
    info = [limpiar_espacios(span.get_text(strip=True)) for span in spans_cuadro]
    return [position] + info


def get_data_next_page(session, payload, last_number_page=100):

    for num_page in tqdm(range(last_number_page - 1)):
        # while n <= last_number_page:
        content_html = next_page(session=session, data=payload)

        html_page = souper(content_html)
        data = convert_in_df(html_page)
        # print(data)


def convert_in_df(html_page):
    jobs = find_jobs(html_page)  # all jobs
    info_jobs = []

    for job in jobs:
        info_jobs.append(get_info_jobs(job))

    data = pd.DataFrame(
        info_jobs,
        columns=[
            "position",
            "institution",
            "ubication",
            "num_conv",
            "n_vac",
            "wage",
            "begin_date",
            "end_date",
        ],
    )

    return data


algo = requests.get("https://cat-fact.herokuapp.com")
print(algo.status_code)
print("google done")

session, first_page_soup, payload = first_session()


text_page_numbers = get_label_page(first_page_soup)
_, total = total_numbers(text_page_numbers)
data1 = convert_in_df(first_page_soup)
print(total / 60)
print(data1)
get_data_next_page(session, payload, total)
