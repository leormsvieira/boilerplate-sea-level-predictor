import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Lê os dados do arquivo
    df = pd.read_csv('epa-sea-level.csv')

    # Cria o gráfico de dispersão
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Cria a primeira linha de melhor ajuste (usando todos os dados de 1880 a 2013)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Estende a linha até 2050
    years_extended = range(1880, 2051)
    line1 = [slope1 * year + intercept1 for year in years_extended]
    plt.plot(years_extended, line1, 'r', label='Linha de melhor ajuste (1880-2013)')

    # Cria a segunda linha de melhor ajuste (usando dados de 2000 em diante)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Estende a linha de 2000 até 2050
    years_recent = range(2000, 2051)
    line2 = [slope2 * year + intercept2 for year in years_recent]
    plt.plot(years_recent, line2, 'g', label='Linha de melhor ajuste (2000-2013)')

    # Adiciona rótulos e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Salva o gráfico e retorna os dados para teste (NÃO MODIFICAR)
    plt.savefig('sea_level_plot.png')
    return plt.gca()