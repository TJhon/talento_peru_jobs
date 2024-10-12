const nombres = [
  "Carlos",
  "María",
  "Luis",
  "Ana",
  "Juan",
  "Carmen",
  "José",
  "Rosa",
  "Pedro",
  "Lucía",
  "Miguel",
  "Jorge",
  "Sandra",
  "David",
  "Gloria",
  "Sergio",
  "Paola",
  "Alfredo",
  "Veronica",
  "Raul",
];

const apellidos = [
  "Flores",
  "Rodríguez",
  "Garcia",
  "Pérez",
  "González",
  "Martínez",
  "Chavez",
  "Mendoza",
  "Torres",
  "Ramos",
  "Vargas",
  "Reyes",
  "Castro",
  "Fernández",
  "Morales",
  "Vega",
  "Campos",
  "Lopez",
  "Ríos",
  "Salazar",
];

function generarCorreos() {
  const dominios = ["@gmail.com", "@hotmail.com"];
  let correos = [];

  // for (let i = 0; i < cantidad; i++) {
  // Elegir un nombre y un apellido aleatoriamente
  const nombre = nombres[Math.floor(Math.random() * nombres.length)];
  const apellido = apellidos[Math.floor(Math.random() * apellidos.length)];

  // Combinar nombre, apellido y un dominio
  const correo = `${nombre.toLowerCase()}.${apellido.toLowerCase()}${Math.floor(
    Math.random() * 100
  )}${dominios[Math.floor(Math.random() * dominios.length)]}`;

  return correo;
}

function fetch_ine() {
  const mail_random = generarCorreos();
  console.log(mail_random);

  fetch("https://facilita.gob.pe/v1/forms/12716/answers.json?locale=es", {
    headers: {
      accept: "application/json, text/plain, */*",
      "accept-language": "es,en;q=0.9,en-US;q=0.8",
      "cache-control": "no-cache",
      "content-type":
        "multipart/form-data; boundary=----WebKitFormBoundaryTk4GGesWuwFCI2UD",
      pragma: "no-cache",
      priority: "u=1, i",
      "sec-ch-ua": '"Not)A;Brand";v="99", "Opera";v="113", "Chromium";v="127"',
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": '"Windows"',
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-csrf-token":
        "42rwpqf5D/tvZ7OdeZbtPcAsjJ/fpIP/WFTb/aVpyxd6YteJW6fKhReiDMvFdzQRVigtFLhxEWdQItInr/Pgpg==",
    },
    referrer: "https://facilita.gob.pe/t/12716",
    referrerPolicy: "strict-origin-when-cross-origin",
    body: `------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="form_version"\r\n\r\n30\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[0][question_id]"\r\n\r\n148502\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[0][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[0][answer][selected]"\r\n\r\nSitio web\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[1][question_id]"\r\n\r\n148488\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[1][answer][selected][0]"\r\n\r\nEstudios y/o tareas académicas\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[1][answer][selected][1]"\r\n\r\nToma de decisiones \r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[2][question_id]"\r\n\r\n148489\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[2][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[2][answer][selected]"\r\n\r\nUna vez al mes\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[3][question_id]"\r\n\r\n148490\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[3][answer][selected][0]"\r\n\r\nSolicitudes de acceso a la información pública y/o correo electrónico\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[3][answer][selected][1]"\r\n\r\nPágina web \r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][question_id]"\r\n\r\n148524\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][answer][selected]"\r\n\r\nSi\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][0][question_id]"\r\n\r\n148557\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][0][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][0][answer][selected]"\r\n\r\nMuy difícil\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][1][question_id]"\r\n\r\n148525\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][1][answer][selected][0]"\r\n\r\nBases de datos      \r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][2][question_id]"\r\n\r\n148923\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][2][answer][selected][0]"\r\n\r\nInforme de Precios e IPC\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][2][answer][selected][1]"\r\n\r\nPBI Trimestral\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][2][answer][selected][2]"\r\n\r\nEmpleo a Nivel Nacional y Ciudades \r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][3][question_id]"\r\n\r\n148526\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][3][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][3][answer][selected]"\r\n\r\nNo\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][4][question_id]"\r\n\r\n148527\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][4][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][4][answer][selected]"\r\n\r\nNo\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][5][question_id]"\r\n\r\n148528\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][5][answer][selected][0]"\r\n\r\nEstadística de empleo\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][5][answer][selected][1]"\r\n\r\nEducación y Cultura\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][5][answer][selected][2]"\r\n\r\nCifras de pobreza\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][5][answer][selected][3]"\r\n\r\nExportaciones e Importaciones\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][6][question_id]"\r\n\r\n148922\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[4][sub_answers_attributes][4ddbf13d-114b-449b-b71d-76f9c31ef612][6][answer][selected][0]"\r\n\r\nMotores de búsqueda como Google\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[5][question_id]"\r\n\r\n148557\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[5][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[5][answer][selected]"\r\n\r\nMuy difícil\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[6][question_id]"\r\n\r\n148525\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[6][answer][selected][0]"\r\n\r\nBases de datos      \r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[7][question_id]"\r\n\r\n148923\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[7][answer][selected][0]"\r\n\r\nInforme de Precios e IPC\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[7][answer][selected][1]"\r\n\r\nPBI Trimestral\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[7][answer][selected][2]"\r\n\r\nEmpleo a Nivel Nacional y Ciudades \r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[8][question_id]"\r\n\r\n148526\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[8][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[8][answer][selected]"\r\n\r\nNo\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[9][question_id]"\r\n\r\n148527\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[9][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[9][answer][selected]"\r\n\r\nNo\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[10][question_id]"\r\n\r\n148528\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[10][answer][selected][0]"\r\n\r\nEstadística de empleo\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[10][answer][selected][1]"\r\n\r\nEducación y Cultura\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[10][answer][selected][2]"\r\n\r\nCifras de pobreza\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[10][answer][selected][3]"\r\n\r\nExportaciones e Importaciones\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[11][question_id]"\r\n\r\n148922\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[11][answer][selected][0]"\r\n\r\nMotores de búsqueda como Google\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[12][question_id]"\r\n\r\n148491\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[12][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[12][answer][selected]"\r\n\r\nNo\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[13][question_id]"\r\n\r\n148507\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[13][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[13][answer][selected]"\r\n\r\nNo \r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[14][question_id]"\r\n\r\n148511\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[14][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[14][answer][selected]"\r\n\r\nNo\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[15][question_id]"\r\n\r\n162657\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[15][answer][selected][0]"\r\n\r\nSitio web\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[16][question_id]"\r\n\r\n148523\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[16][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[16][answer][selected]"\r\n\r\nA veces\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[17][question_id]"\r\n\r\n148514\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[17][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[17][answer][selected]"\r\n\r\nPoco confiable\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[18][question_id]"\r\n\r\n148497\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[18][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[18][answer][selected]"\r\n\r\nDoctorado\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[19][question_id]"\r\n\r\n148517\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[19][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[19][answer][selected]"\r\n\r\nEconomista\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[20][question_id]"\r\n\r\n148498\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[20][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[20][answer][selected]"\r\n\r\nExtranjero\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[21][question_id]"\r\n\r\n148519\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[21][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[21][answer][selected]"\r\n\r\nPerú\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[21][sub_answers_attributes][520af7bc-ab13-4c72-a364-64278bdbaad9][0][question_id]"\r\n\r\n148520\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[21][sub_answers_attributes][520af7bc-ab13-4c72-a364-64278bdbaad9][0][answer]"\r\n\r\n40404\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[22][question_id]"\r\n\r\n148520\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[22][answer]"\r\n\r\n40404\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[23][question_id]"\r\n\r\n148499\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[23][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[23][answer][selected]"\r\n\r\nDe 30 a 44 años\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[24][question_id]"\r\n\r\n148500\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[24][answer][other_text]"\r\n\r\n\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[24][answer][selected]"\r\n\r\nHombre\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[25][question_id]"\r\n\r\n148501\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="answers[25][answer]"\r\n\r\n${mail_random}.com\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="accepts_privacy_policy"\r\n\r\ntrue\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="sisoli"\r\n\r\nsisoli\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD\r\nContent-Disposition: form-data; name="filling_start_time"\r\n\r\n2024-10-11T20:17:36.882+00:00\r\n------WebKitFormBoundaryTk4GGesWuwFCI2UD--\r\n`,
    method: "POST",
    mode: "cors",
    credentials: "include",
  })
    .then((response) => response.json())
    .then((data) => console.log(data));
}

let c = 2;
for (let i = 0; i < c; i++) {
  await new Promise((r) => setTimeout(r, 1000));
  await fetch_ine();
}
