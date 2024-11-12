URL = "https://app.servir.gob.pe/DifusionOfertasExterno/faces/consultas/ofertas_laborales.xhtml"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Host": "app.servir.gob.pe",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Dest": "document",
}
PAYLOAD = {
    "javax.faces.partial.ajax": "true",
    "javax.faces.source": "frmLstOfertsLabo:j_idt56",
    "javax.faces.partial.execute": "@all",
    "javax.faces.partial.render": "frmLstOfertsLabo:mensaje frmLstOfertsLabo",
    "frmLstOfertsLabo:j_idt56": "frmLstOfertsLabo:j_idt56",
    "frmLstOfertsLabo": "frmLstOfertsLabo",
    "frmLstOfertsLabo:modalidadAcceso": "03",
    "frmLstOfertsLabo:txtPerfil": "",
    "frmLstOfertsLabo:cboDep_focus": "",
    "frmLstOfertsLabo:cboDep_input": 0,
    "frmLstOfertsLabo:txtPuesto": "",
    "frmLstOfertsLabo:autocompletar_input": "",
    "frmLstOfertsLabo:autocompletar_hinput": "",
    "frmLstOfertsLabo:txtNroConv": "",
}


share_payload = {
    "javax.faces.partial.ajax": "true",
    "javax.faces.partial.execute": "@all",
    "javax.faces.partial.render": "frmLstOfertsLabo:mensaje frmLstOfertsLabo",
    "frmLstOfertsLabo": "frmLstOfertsLabo",
    "frmLstOfertsLabo:modalidadAcceso": "03",
    "frmLstOfertsLabo:txtPerfil": "",
    "frmLstOfertsLabo:cboDep_focus": "",
    "frmLstOfertsLabo:txtPuesto": "",
    "frmLstOfertsLabo:autocompletar_input": "",
    "frmLstOfertsLabo:autocompletar_hinput": "",
    "frmLstOfertsLabo:txtNroConv": "",
}


first_page = {
    "javax.faces.source": "frmLstOfertsLabo:j_idt42",
    "frmLstOfertsLabo:j_idt42": "frmLstOfertsLabo:j_idt42",
}
next_page = {
    "javax.faces.source": "frmLstOfertsLabo:j_idt56",
    "frmLstOfertsLabo:j_idt56": "frmLstOfertsLabo:j_idt56",
}

last_page = {
    "javax.faces.source": "frmLstOfertsLabo:j_idt57",
    "frmLstOfertsLabo:j_idt57": "frmLstOfertsLabo:j_idt57",
}
prev_page = {
    "javax.faces.source": "frmLstOfertsLabo:j_idt54",
    "frmLstOfertsLabo:j_idt54": "frmLstOfertsLabo:j_idt54",
}


MAPPING_COLUMNS = {
    "url_convocatoria": "job_posting_url",
    "Cantidad De Vacantes:": "vacancies",
    "Número De Convocatoria:": "job_posting_number",
    "Remuneración:": "salary",
    "Fecha Inicio De Publicación:": "start_publication_date",
    "Fecha Fin De Publicación:": "end_publication_date",
    "Experiencia:": "required_experience",
    "Formación Académica - Perfil:": "educational_background",
    "Especialización:": "specialization",
    "Conocimiento:": "required_knowledge",
    "Competencias:": "skills",
    "position": "job_title",
    "institution": "public_institution",
    "uuid": "unique_id",
    "day_scrapper": "scraping_date",
}

shared_columns = [
    "public_institution",
    "ubication",
    "job_posting_number",
    "vacancies",
    "salary",
    "start_publication_date",
    "end_publication_date",
    "job_title",
]
