# from concurrent.futures import ThreadPoolExecutor, as_completed
from TalentPeru.extract import extract_jobs_in_parallel
from TalentPeru.transform import clean_jobs_data

data = extract_jobs_in_parallel(lima="15")


print(clean_jobs_data(data))
print(data.columns)

# from TalentPeru.extract import JobScrapper
# from TalentPeru.Scrapper_jobs.api.api_jobs import clean_jobs_data
# from time import time
# import pandas as pd


# # deps = [str(n).zfill(2) for n in range(1, 26) if n != 15]
# deps = [str(n).zfill(2) for n in range(1, 2) if n != 15]
# lima = "02"
# # lima = "15"


# from TalentPeru.Scrapper_jobs.config.settings import (
#     MAPPING_COLUMNS,
#     PATH_LOG,
#     data_path,
#     today,
# )

# columns = MAPPING_COLUMNS

# if __name__ == "__main__":
#     start = time()

#     def ejecutar(dep):
#         data_dep = JobScrapper(dep=dep).scrapper_sequential()
#         return data_dep

#     def both_sides(right=True):  # lima
#         if right:
#             data_dep = JobScrapper(dep=lima).scrapper_both_right()
#         else:
#             data_dep = JobScrapper(dep=lima).scrapper_both_left()
#         return data_dep

#     data_dep_list = []

#     # Ejecutar both_sides en paralelo junto con ejecutar(dep)
#     with ThreadPoolExecutor(
#         max_workers=10
#     ) as executor:  # max_workers aumentado para incluir both_sides
#         # Crear futuros para deps
#         future_to_dep = {
#             executor.submit(both_sides, right_side): f"both_sides_{right_side}"
#             for right_side in [True, False]
#         }

#         # Añadir both_sides a los futuros
#         future_to_dep.update({executor.submit(ejecutar, dep): dep for dep in deps})

#         # Recolectar resultados de ambos tipos de tareas
#         for future in as_completed(future_to_dep):
#             data_dep_list.append(future.result())

#     print("\n" * 10)
#     data = pd.concat(data_dep_list, ignore_index=True).drop_duplicates()
#     data["scraping_date"] = today
#     # data = data.rename(columns=columns)
# data = clean_jobs_data(data)
#     data.to_csv(data_path, index=False)
#     # data["day_scrapper"] = today_sp

#     #########
#     last_log = pd.read_csv(PATH_LOG)
#     end = time() - start
#     data_log = {
#         "dep": ["all"],
#         "last_date": today,
#         "path_data": [data_path],
#         "n_jobs_text": [len(data) - 10],
#         "n_jobs": [len(data) - 10],
#         "time": [end],
#     }
#     day_data = pd.concat([last_log, pd.DataFrame(data_log)], ignore_index=True)

#     end = time() - start
#     day_data.to_csv(PATH_LOG, index=False)

#     print(f"Tiempo de ejecución: {end } segundos")
