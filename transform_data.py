from TalentPeru.transform import clean_jobs_data
from TalentPeru.load import save_data_gh, save_logs_gh
from TalentPeru.extract import get_today_data

data = get_today_data()

clean_data = clean_jobs_data(data)


save_data_gh(data, clean_data)
save_logs_gh(data)
