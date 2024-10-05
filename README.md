# Localidade-temporal
# Códigos da Replicação Científica

Este diretório contém os códigos e os dados para replicar a análise de atividades de contribuição de programadores no repositório `react`.

## Objetivo
Replicar a análise de localidade temporal de contribuições em projetos de software, similar à análise de voluntários em projetos de ciência cidadã, como descrito no artigo-base **Volunteers' Engagement in Human Computation for Astronomy Projects**.

## Estrutura

- `getCommits.py`: Coleta os commits do repositório `react` via API do GitHub.
- `getDays.py`: Calcula o número de dias distintos em que cada programador fez pelo menos um commit.
- `graphActivity.py`: Gera o gráfico de distribuição de dias de contribuição.

## Dados
- **data.json**: Dados brutos coletados via API do GitHub em 04/10/2024.
- **activity.data**: Dados processados com o número de dias de contribuição por programador.
