import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'],
                   index_col='date')
df.index=pd.to_datetime(df.index)
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]
def draw_line_plt():
    # Copia o Dataframe Limpo
    df_line = df.copy()
    fig,ax =plt.subplots(figsize=(15,5))
    ax.plot(df_line.index,df_line['value'],
            color='firebrick', linewidth=1)
    # 4. Definir Título e Rótulos dos Eixos (Exatamente como o projeto pede)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # 5. Salvar a figura e retornar
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    # Extrair ano e mês do índice Datetime
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Agrupar por ano e mês, calculando a média da coluna 'value'
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    # 4. Reordenar as colunas para os meses ficarem na ordem cronológica
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_bar_grouped = df_bar_grouped.reindex(columns=months)

    # 5. Desenhar o gráfico de barras agrupadas
    fig = df_bar_grouped.plot(kind='bar', figsize=(15, 7)).get_figure()

    # 6. Configurar rótulos e legenda exatamente como exigido
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')

    # 7. Salvar e retornar
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # 2. Ordem correta das abreviações dos meses
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # 3. Criar a figura com 2 painéis lado a lado
    fig, axes = plt.subplots(1, 2, figsize=(20, 7))

    # 4. Primeiro Box Plot: Por Ano
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # 5. Segundo Box Plot: Por Mês
    sns.boxplot(x='month', y='value', data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # 6. Salvar e retornar
    fig.savefig('box_plot.png')
    return fig

draw_line_plt()
draw_bar_plot()
draw_box_plot()