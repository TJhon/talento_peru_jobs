from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# from TalentPeru.Scrapper_jobs.utils import job_wage_float
from TalentPeru.Scrapper_jobs.api_jobs import (
    get_jobs_data,
    get_last_jobs_data,
    get_logs,
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
@app.get("/jobs/last")
async def get_jobs():
    return get_last_jobs_data()


@app.get("/jobs/logs")
async def get_logs_api():
    return get_logs()


# print(get_logs())


@app.get("/jobs/history/{date}")
async def get_job_history(date: str):
    return get_jobs_data(date)


@app.get("/")
def check():
    return {"hello": "world"}
