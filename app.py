from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# from TalentPeru.Scrapper_jobs.utils import job_wage_float
from TalentPeru.Scrapper_jobs.api_jobs import (
    get_jobs_data,
    get_last_jobs_data,
    # get_logs,
)
from TalentAPI.init_supabase import (
    get_logs,
    get_log_date,
    get_jobs_data,
    get_job_data,
    get_regions,
)

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://192.168.1.3",
    "http://192.168.1.3:5173",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from rich import print


# @app.get("/interns")
# @app.get("/direct_jobs")
LOGS = "https://raw.githubusercontent.com/TJhon/talento_peru_jobs/refs/heads/main/data_logs/logs.csv"


@app.get("/jobs/date={date}")
async def get_jobs(*, date: str, page: int = 1, dep: str = None):
    # print(date)
    total_jobs = pd.read_csv(LOGS).query("last_date == @date").iloc[0]["n_jobs"]
    # print(total_jobs)

    data = get_jobs_data(date, page, dep)
    data = {"total_jobs": int(total_jobs), "page": page, "data": data}
    return data


@app.get("/jobs/logs")
async def get_logs_api(date=None):
    if date is not None:
        return get_log_date(date)
    return get_logs()


@app.get("/jobs/job/date={date}/uuid={uuid}")
def get_job_by_uuid(date: str, uuid: str):
    # print(date)
    return get_job_data(date, uuid)


# @app.get('/jobs/logs/')
# def get_logs_date()


@app.get("/jobs/history/{date}")
async def get_job_history(date: str):
    return get_jobs_data(date)


@app.get("/")
def check():
    date = "10-10-2024"
    return get_regions(date)
    # return {"hello": "world"}
