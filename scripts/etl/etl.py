import json
import time
import os

SOURCE_FILE = "/var/log/pessoas/pessoas.log"
TARGET_FILE = "/var/log/pessoas/pessoas_transformado.log"

VIOLENT_CAUSES = [
    "Acidente de Trânsito", "Homicídio", "Violência Urbana", "COVID-19"
]

def classify_tipo_morte(cause):
    if cause in VIOLENT_CAUSES:
        return "Violenta"
    elif cause:
        return "Natural"
    else:
        return "Não Informada"

def classify_faixa_etaria(age):
    if age is None:
        return "Não Informada"
    if age <= 17:
        return "0-17 anos"
    elif age <= 29:
        return "18-29 anos"
    elif age <= 59:
        return "30-59 anos"
    else:
        return "60+ anos"

def process_line(line):
    try:
        data = json.loads(line)
        new_log = {
            "timestamp": data.get("timestamp"),
            "level": data.get("level"),
            "person_id": data.get("person_id"),
            "birth_year": data.get("birth_year"),
            "death_year": data.get("death_year"),
            "age_at_death": data.get("age_at_death"),
            "cause_of_death": data.get("cause_of_death"),
            "tipo_morte": classify_tipo_morte(data.get("cause_of_death")),
            "faixa_etaria": classify_faixa_etaria(data.get("age_at_death")),
            "region": data.get("region")
        }
        return json.dumps(new_log)
    except Exception as e:
        print(f"Erro ao processar linha: {e}")
        return None

def run_etl():
    # Garantir que arquivo de saída esteja limpo
    if os.path.exists(TARGET_FILE):
        os.remove(TARGET_FILE)

    while True:
        if os.path.exists(SOURCE_FILE):
            with open(SOURCE_FILE, "r") as src, open(TARGET_FILE, "a") as tgt:
                for line in src:
                    transformed = process_line(line)
                    if transformed:
                        tgt.write(transformed + "\n")
        else:
            print("Arquivo de origem ainda não encontrado...")
        
        time.sleep(5)

if __name__ == "__main__":
    run_etl()