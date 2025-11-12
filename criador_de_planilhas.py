"""
Trabalho: Análise estatística de fatores que influenciam o mercado de trabalho
+ Interface gráfica com abas (Tkinter)
"""

import os
import csv
import math
from statistics import mean, median
from typing import Dict, List, Optional


# ------------------- ARQUIVOS E DADOS -------------------
CSV_FILES = {
    'population': 'population.csv',
    'gdp_per_capita': 'gdp_per_capita.csv',
    'retirement_age': 'retirement_age.csv',
    'labour_force_pct': 'labour_force_pct.csv',
    'agriculture_pct': 'agriculture_pct.csv',
    'gini': 'gini.csv'
}

SAMPLE_DATA = {
    'population': {'Brazil': 212559417, 'China': 1439323776, 'India': 1380004385, 'United States': 331002651, 'Germany': 83783942, 'Japan': 126476461, 'France': 65273511, 'Canada': 37742154, 'Australia': 25499884, 'Mexico': 128932753},
    'gdp_per_capita': {'Brazil': 8900, 'China': 10400, 'India': 2100, 'United States': 65000, 'Germany': 48000, 'Japan': 40000, 'France': 41000, 'Canada': 43000, 'Australia': 54000, 'Mexico': 9700},
    'retirement_age': {'Brazil': 62, 'China': 60, 'India': 60, 'United States': 66, 'Germany': 65, 'Japan': 65, 'France': 62, 'Canada': 65, 'Australia': 66, 'Mexico': 65},
    'labour_force_pct': {'Brazil': 56.0, 'China': 68.0, 'India': 50.0, 'United States': 61.0, 'Germany': 55.0, 'Japan': 59.0, 'France': 52.0, 'Canada': 64.0, 'Australia': 63.0, 'Mexico': 59.0},
    'agriculture_pct': {'Brazil': 9.5, 'China': 25.0, 'India': 42.0, 'United States': 1.3, 'Germany': 1.2, 'Japan': 2.0, 'France': 2.5, 'Canada': 1.5, 'Australia': 2.8, 'Mexico': 12.0},
    'gini': {'Brazil': 53.9, 'China': 38.5, 'India': 35.7, 'United States': 41.4, 'Germany': 31.9, 'Japan': 32.9, 'France': 32.4, 'Canada': 33.3, 'Australia': 34.4, 'Mexico': 45.4}
}


def ensure_csvs_exist():
    for key, fname in CSV_FILES.items():
        if not os.path.exists(fname):
            with open(fname, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['country', 'value'])
                for country, val in SAMPLE_DATA[key].items():
                    writer.writerow([country, val])


def load_csv(file):
    data = []
    if os.path.exists(file):
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append((row['country'], float(row['value'])))
    return data


# ------------------- FUNÇÕES ESTATÍSTICAS -------------------
def media(vals):
    return mean([v for _, v in vals]) if vals else 0

def variancia(vals):
    if len(vals) < 2: return 0
    m = media(vals)
    return sum((v - m) ** 2 for _, v in vals) / (len(vals) - 1)

def mediana(vals):
    return median([v for _, v in vals]) if vals else 0

