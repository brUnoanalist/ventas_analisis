import random
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime, timedelta

# Generar datos simulados de ventas
def simulate_sales_data(days=7):
    stores = ['Store A', 'Store B', 'Store C', 'Store D']
    data = []
    start_date = datetime.now() - timedelta(days=days)

    for day in range(days):
        date = (start_date + timedelta(days=day)).strftime('%Y-%m-%d')
        for store in stores:
            sales = round(random.uniform(100, 2000), 2)
            data.append({
                'store': store,
                'date': date,
                'sales': sales
            })
    return data

# Guardar datos en un archivo JSON
def save_sales_data(data, filename='sales_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Cargar y analizar los datos de promedio de ventas por tienda
def analyze_sales_data(filename='sales_data.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    summary = df.groupby('store').mean(numeric_only=True).reset_index()
    print(summary)
    return df, summary
# Cargar y analizar los datos  de ventas totales por tienda en 7 dias
def analyze_total_sales_data(filename='sales_data.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    total_sells = df.groupby('store').sum(numeric_only=True).reset_index()
    print(total_sells)
    return df, total_sells

# Gráfico: Promedio de ventas por tienda
def plot_average_sales(summary):
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.barplot(x='store', y='sales', data=summary, palette="viridis")
    plt.title('Promedio de Ventas por Tienda')
    plt.ylabel('Ventas Promedio ($)')
    plt.xlabel('Tienda')
    plt.show()

# Gráfico: Tendencia de ventas diarias
def plot_sales_trend(df):
    plt.figure(figsize=(12, 6))
    for store in df['store'].unique():
        store_data = df[df['store'] == store]
        plt.plot(store_data['date'], store_data['sales'], label=store, marker='o')
    
    plt.legend(title="Tiendas")
    plt.title('Tendencia de Ventas Diarias')
    plt.xlabel('Fecha')
    plt.ylabel('Ventas ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Ejecutar el flujo completo
print("Generando datos de ventas simuladas...")
sales_data = simulate_sales_data()
save_sales_data(sales_data)

print("Analizando datos de ventas...")
df, summary = analyze_sales_data()

print("Analizando  ventas totales en 7 dias...")
df, total_sells = analyze_total_sales_data()

print("Generando gráficos...")
plot_average_sales(summary)
plot_sales_trend(df)
