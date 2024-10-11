from dotenv import load_dotenv, find_dotenv
import os, datetime, pytz
from supabase import create_client, Client
import pandas as pd
from rich import print

load_dotenv(find_dotenv())

key = os.environ.get("SUPABASE_KEY")
url = os.environ.get("SUPABASE_URL")
mail = os.environ.get("mail_admin")
pssword = os.environ.get("password_admin")
supabase: Client = create_client(url, key)

gmt5 = pytz.timezone("Etc/GMT+5")
today = datetime.datetime.now(gmt5)

# Hace 20 días
days_ago = today - datetime.timedelta(days=20)

# Formato de las fechas
today_str = today.strftime("%d-%m-%Y")
days_ago_str = days_ago.strftime("%d-%m-%Y")


data_table = supabase.table("job_postings")


def remove_extra_spaces(text):
    import re

    """Removes multiple spaces from a string."""
    return re.sub(r"\s+", " ", text).strip()


def upload_and_drop_data(data):
    data_r = data.to_dict("records")
    response = supabase.auth.sign_in_with_password(
        {
            "email": mail,
            "password": pssword,
        }
    )

    data_table.insert(data_r).execute()

    response = supabase.auth.sign_out()


# upload_and_drop_data()

LOGS = "https://raw.githubusercontent.com/TJhon/talento_peru_jobs/refs/heads/main/data_logs/logs.csv"


def get_logs():
    # retorna los logs
    df_logs = pd.read_csv(LOGS)
    last_date_col = "last_date_format"
    df_logs[last_date_col] = pd.to_datetime(df_logs["last_date"], dayfirst=True)
    last_scrapper, last_n_jobs = df_logs.sort_values(
        last_date_col, ascending=False
    ).loc[len(df_logs) - 1, ["last_date", "n_jobs"]]
    df_logs = df_logs[["last_date", "path_data", "n_jobs"]]
    # print(df_logs.to_dict("records"))
    data = {
        "last_scrapper": str(last_scrapper),
        "n_last_jobs": int(last_n_jobs),
        "data": df_logs.to_dict("records"),
    }

    return data


def get_log_date(date):
    # print(date)
    # try:
    df_logs = pd.read_csv(LOGS)
    n_jobs, date = df_logs.query("last_date == @date")[["n_jobs", "last_date"]].values[
        0
    ]
    # print(date_data)

    return {"date": str(date), "n_jobs": int(n_jobs)}


def get_jobs_data(date, page: int = None, dep=None):

    n_by_page = 11
    data = data_table.select(
        "vacancies, salary, job_posting_url, start_publication_date, end_publication_date, ubication_region, ubication_dist",
        "job_title",
        "unique_id",
        "public_institution",
    ).eq("scraping_date", date)
    if dep is not None:
        data = data.eq("ubication_region", dep)
        # print()
    if page is not None:
        last_n = page * n_by_page
        begin_n = last_n - n_by_page
        data = data.range(begin_n, last_n)

    data = data.execute()
    return data.data


def get_job_data(date, uuid):
    data = (
        data_table.select("*").eq("scraping_date", date).eq("unique_id", uuid).execute()
    )
    # print(data)
    return data


def get_regions(date):
    data = (
        data_table.select("distinct ubication_region", distinct=True)
        .eq("scraping_date", date)
        .execute()
    )
    # print(data)
    return data
