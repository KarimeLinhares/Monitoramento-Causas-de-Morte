# Observabilidade Social - ETL de Logs de Mortalidade

Este projeto simula, transforma e analisa logs relacionados à expectativa de vida e causas de morte no Brasil, usando uma stack de observabilidade: _Promtail + Loki + Grafana_.

Inclui um processo _ETL (Extract, Transform, Load)_ em Python para enriquecer os logs antes de enviá-los ao Loki, permitindo dashboards mais organizados, rápidos e claros.

Equipe:
Arimatéia Júnior - Matrícula: 2417061
Karime Linhares - Matrícula: 2416877
Bruno Negreiros - Matrícula: 2419432
Pedro Henrique - Matrícula: 2325859

---

## Arquitetura do Projeto

```plaintext
log-generator (gera pessoas.log)
    ⮕ etl-transformer (gera pessoas_transformado.log)
        ⮕ promtail (envia pessoas_transformado.log)
            ⮕ loki (armazenamento)
                ⮕ grafana (visualização)
```

⸻

Serviços Utilizados
• Log Generator: Gera logs brutos de pessoas simuladas.
• ETL Transformer:
• Classifica tipo_morte (Violenta/Natural).
• Classifica faixa_etaria (0-17, 18-29, 30-59, 60+).
• Prepara os logs para visualização analítica.
• Promtail: Lê os logs transformados e envia ao Loki.
• Loki: Armazena os eventos de log.
• Grafana: Visualiza os dados de forma amigável.

⸻

Organização dos Dados no Log Transformado

Cada evento gerado no arquivo pessoas_transformado.log inclui:

Campo
Descrição
timestamp
Data e hora do evento
level
Severidade (INFO, WARN, ERROR, CRITICAL)
person_id
Identificador da pessoa
birth_year
Ano de nascimento
death_year
Ano de morte
age_at_death
Idade ao morrer
cause_of_death
Causa da morte
tipo_morte
Classificação: Natural ou Violenta
faixa_etaria
Faixa etária: 0-17, 18-29, 30-59, 60+
region
Região do Brasil
