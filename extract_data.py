# from concurrent.futures import ThreadPoolExecutor, as_completed
from TalentPeru.extract import extract_jobs_in_parallel
data = extract_jobs_in_parallel(lima="15")
