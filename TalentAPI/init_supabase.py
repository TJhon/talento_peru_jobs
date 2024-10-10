from dotenv import load_dotenv, find_dotenv
import os, datetime, pytz
from supabase import create_client, Client

load_dotenv(find_dotenv())

key = os.environ.get("SUPABASE_KEY")
url = os.environ.get("SUPABASE_URL")
mail = os.environ.get("mail_admin")
pssword = os.environ.get("password_admin")
supabase: Client = create_client(url, key)
import pandas as pd

gmt5 = pytz.timezone("Etc/GMT+5")
today = datetime.datetime.now(gmt5)

# Hace 20 días
days_ago = today - datetime.timedelta(days=20)

# Formato de las fechas
today_str = today.strftime("%d-%m-%Y")
days_ago_str = days_ago.strftime("%d-%m-%Y")


data_table = supabase.table("jobs")


def upload_and_drop_data(data: pd.DataFrame):
    data_r = data.to_dict()
    response = supabase.auth.sign_in_with_password(
        {
            "email": mail,
            "password": pssword,
        }
    )
    data_table.insert(data_r).execute()

    data_table.delete().eq("day_scrapper", days_ago_str)


# response = supabase.table("test").delete().in_("id", [100, 1021]).execute()
# print(response)
# print("12")
