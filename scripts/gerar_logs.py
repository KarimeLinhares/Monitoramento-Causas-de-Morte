import random
import time
import json
import os
from datetime import datetime

causas_morte = [
    "Doença Cardiovascular", "Câncer", "Acidente de Trânsito",
    "Violência Urbana", "Infarto", "Diabetes", "Homicídio", "COVID-19"
]

regioes = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]

LOG_DIR = "/var/log/pessoas"
LOG_FILE = f"{LOG_DIR}/pessoas.log"

def gerar_log():
    nascimento = random.randint(1920, 2010)
    idade_atual = 2025 - nascimento

    morreu = random.random() < 0.7 or idade_atual > 85

    if morreu:
        if idade_atual >= 30:
            idade_morte = random.randint(30, min(idade_atual, 95))
        else:
            idade_morte = random.randint(1, idade_atual)  # Morreu jovem
        ano_morte = nascimento + idade_morte
        causa = random.choice(causas_morte)

        if causa in ["Acidente de Trânsito", "Violência Urbana", "Homicídio", "COVID-19"]:
            level = "ERROR" if idade_morte < 50 else "CRITICAL"
        else:
            level = "INFO" if idade_morte >= 65 else "WARN"
    else:
        idade_morte = None
        ano_morte = None
        causa = None
        level = "INFO"

    log = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": level,
        "person_id": f"br-{random.randint(1000,9999)}",
        "birth_year": nascimento,
        "death_year": ano_morte,
        "age_at_death": idade_morte,
        "cause_of_death": causa,
        "region": random.choice(regioes)
    }
    return log

if __name__ == "__main__":
    # Garante que a pasta existe
    os.makedirs(LOG_DIR, exist_ok=True)

    while True:
        log = gerar_log()
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log) + "\n")
        print(log)
        time.sleep(2)