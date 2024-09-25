URL_BASE = "https://raw.githubusercontent.com/TJhon/talento_peru_jobs/refs/heads/main/data/{location}/{date}.csv"

import pandas as pd, tqdm

LOGS = "https://raw.githubusercontent.com/TJhon/talento_peru_jobs/refs/heads/main/data_logs/logs.csv"

url = URL_BASE.format(location=12, date=2)

df = pd.read_csv(LOGS)
last_date_col = "last_date_format"
df[last_date_col] = pd.to_datetime(df["last_date"], dayfirst=True)


def days_scrapper(df):
    day_scrapper = df.sort_values(last_date_col, ascending=False)[
        last_date_col
    ].unique()
    return day_scrapper


def last_scrapper(df: pd.DataFrame = df, regions: list = None) -> pd.DataFrame:
    if regions is not None:
        df = df.query("dep in @regions")
    last_dates = df.loc[df.groupby("dep")[last_date_col].idxmax()]
    regions = last_dates["dep"]

    urls_to_data = []

    for i, row in last_dates.iterrows():
        urls_to_data.append(convert_to_url_csv(row["dep"], row["last_date"]))
    data_array = []
    for url, dep in zip(urls_to_data, last_dates["dep"]):
        df = read_data(url, dep)
        data_array.append(df)
    # print(data_array)
    data = pd.concat(data_array, ignore_index=True)
    # data = get_data(urls_to_data).drop_duplicates()
    return data


def convert_to_url_csv(location, date):
    url_csv = URL_BASE.format(location=location, date=date)
    return url_csv


def read_data(url, dep):
    github_data = pd.read_csv(url)
    github_data["dep"] = dep
    return github_data


# last_scrapper()
# def get_data(urls) -> pd.DataFrame:
#     data_array = []
#     for url in tqdm.tqdm(urls):

#         data_array.append(github_data)

#     data = pd.concat(data_array, ignore_index=True)
#     return data
