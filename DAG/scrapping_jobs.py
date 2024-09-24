from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Parámetros por defecto del DAG
default_args = {
    "start_date": datetime(2024, 9, 24),
    "retries": 1,
}

# Crear una lista de pares de registros que se pasarán como argumentos al script
n_reg_pairs = [(i, i + 1) for i in range(1, 26, 2)]  # [(1, 2), (3, 4), ..., (25,)]

# Definir el DAG
with DAG(
    "scraping_talent_peru",
    default_args=default_args,
    schedule_interval="@daily",
    max_active_tasks=2,  # Limitar la cantidad de tareas en paralelo a 2
    catchup=False,
) as dag:

    # Crear una lista para almacenar las tareas BashOperator
    tasks = []

    # Crear una tarea para cada par de n_regs
    for idx, (n1, n2) in enumerate(n_reg_pairs, start=1):
        task = BashOperator(
            task_id=f"run_scraping_task_{idx}",
            bash_command=f"python /path/to/your/script.py --n_regs {n1} {n2}",
        )
        tasks.append(task)

    # Encadenar las tareas para ejecutarlas en paralelo de 2 en 2
    for i in range(len(tasks) - 1):
        tasks[i] >> tasks[i + 1]
