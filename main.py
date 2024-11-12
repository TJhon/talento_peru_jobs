# from concurrent.futures import ThreadPoolExecutor, as_completed
from TalentPeru.extract import extract_jobs_in_parallel
from TalentPeru.transform import clean_jobs_data
from TalentPeru.load import save_data_gh, save_logs_gh

data = extract_jobs_in_parallel(lima="03")

clean_data = clean_jobs_data(data)


save_data_gh(data, clean_data)
save_logs_gh(data)
