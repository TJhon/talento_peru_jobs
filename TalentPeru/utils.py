import pytz
import datetime

gmt5 = pytz.timezone("Etc/GMT+5")
today = datetime.datetime.now(gmt5).strftime("%d-%m-%Y")


PATH_LOG = "./data/logs/logs.csv"
data_path = f"./data/clean/{today}.csv"
raw_path = f"./data/raw/{today}.csv"
