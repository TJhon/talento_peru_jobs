import pandas as pd
from ..utils import data_path, raw_path, today, PATH_LOG


def save_data_gh(data_raw: pd.DataFrame, data_clean: pd.DataFrame):
    data_clean.to_csv(data_path, index=False)
    data_raw.to_csv(raw_path, index=False)


def save_logs_gh(data):
    last_log = pd.read_csv(PATH_LOG)
    data_log = {"raw": raw_path, "clean": data_path, "n_jobs": [len(data) - 10]}

    log_ = pd.concat([last_log, pd.DataFrame(data_log)], ignore_index=True)
    log_.to_csv(PATH_LOG)
