import uuid
import pandas as pd, re

from xarray import DataArray

from TalentPeru.extract.utils.utils import limpiar_espacios
from ..utils import today


def job_wage_float(wage: str):
    # 'S/. 1,950.00' -> 1950.00
    wage = wage.replace(",", "").replace("S/.", "").strip()
    return float(wage)


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9áéíóúÁÉÍÓÚ\s]", "", text)
    return text.strip


def custom_title(text):
    # Primero guardamos los números romanos
    roman_numbers = []

    def save_roman(match):
        roman_numbers.append(match.group())
        return f"[ROMAN{len(roman_numbers)-1}]"

    # Patrón para números romanos (I, II, III, IV, V, VI, VII, VIII, IX, X)
    roman_pattern = r"\b[IVX]{1,5}\b"

    temp_text = re.sub(roman_pattern, save_roman, text)

    temp_text = temp_text.title()

    for i, roman in enumerate(roman_numbers):
        temp_text = temp_text.replace(f"[Roman{i}]", roman)

    return temp_text


def extract_min_degree(education):
    """
    Extrae el mínimo grado académico requerido de un texto según la jerarquía educativa peruana.

    Jerarquía:
    0 - Sin educación
    1 - Primaria
    2 - Secundaria
    3 - Técnico
    4 - Bachiller
    5 - Titulado
    6 - Magister
    7 - Doctorado

    Args:
        text (str): Texto que contiene los requisitos educativos

    Returns:
        str: El mínimo grado académico requerido
    """
    # Convertir texto a minúsculas y normalizar
    text = education.lower().replace("/", " ").replace("(", " ").replace(")", " ")

    # Patrones de búsqueda para cada nivel educativo
    patterns = {
        "primaria": r"primaria",
        "secundaria": r"secundaria",
        "tecnico": r"técnico|tecnic[ao]|carrera técnica|instituto",
        # 'estudiante': r'',
        "egresado": r"egresad",
        "bachiller": r"bachiller",
        "titulado": r"titulo|titul[ao]d[ao]|título profesional|título universitario|licenciatura|licenciad[ao]",
        "colegiado": r"colegiad[ao]|colegiatura",
        "magister": r"magister|maestr[ií]a|egresado de maestria",
        "doctorado": r"doctorado|doctor",
    }

    # Asignar valores numéricos a cada nivel
    degree_values = {
        "doctorado": 8,
        "magister": 7,
        "colegiado": 6,
        "titulado": 6,
        "bachiller": 5,
        "egresado": 4,
        "tecnico": 3,
        "secundaria": 2,
        "primaria": 1,
    }

    # Buscar todas las coincidencias
    found_degrees = []
    for degree, pattern in patterns.items():
        if re.search(pattern, text):
            found_degrees.append((degree_values[degree], degree))

    # Si no se encuentra ningún grado, retornar "sin educacion"
    if not found_degrees:
        return None

    # Obtener el grado mínimo encontrado
    min_degree = min(found_degrees)[1]

    return min_degree


def extract_first_experience(text):

    text = text.upper().replace("\n", " ").replace("(", "").replace(")", "")

    pattern = r"(\d+)\s*(?:AÑO|AÑOS|MES|MESES)"
    match = re.search(pattern, text)

    if match:
        number = int(match.group(1))
        after_number = text[match.end() - 10 : match.end() + 3]
        if "AÑO" in after_number:
            return number * 12
        elif "MES" in after_number:
            return number

    return 0


to_clean_txt = [
    "required_experience",
    "educational_background",
    "specialization",
    "required_knowledge",
    "skills",
]


def clean_jobs_data(data_raw: pd.DataFrame):
    # basic clean
    data = data_raw.copy()
    ubication_col = ["ubication_region", "ubication_dist"]
    data[ubication_col] = data["ubication"].str.split("-", expand=True, n=1)
    for u in ubication_col:
        data[u] = data[u].str.strip()

    data["salary"] = data["salary"].apply(job_wage_float)
    data = data[data["job_title"].str.strip().str.len() >= 3]
    data["day_data_extract_dmy"] = today

    data["uuid"] = data.index.map(lambda _: uuid.uuid4())
    data["job_title"] = data["job_title"].apply(custom_title)
    data["experience_months"] = data["required_experience"].apply(
        extract_first_experience
    )
    data["min_education"] = data["educational_background"].apply(extract_min_degree)
    data[to_clean_txt] = data[to_clean_txt].map(limpiar_espacios)
    data[to_clean_txt] = data[to_clean_txt].map(custom_title)
    return data
