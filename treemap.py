import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

df = pd.read_csv(r'blkjckhands.csv')
df = df.iloc[:, 1:]


def treemap():
    count_df = df.groupby(['PlayerNo', 'winloss', 'plybustbeat']).size().reset_index(name='count')

    fig = px.treemap(count_df, path=['PlayerNo', 'winloss', 'plybustbeat'], values='count', color='PlayerNo',
                 hover_data={'count': True})

    fig.update_layout(title='Figuur 7: Treemap het resultaat van de gespeelde handen per speler')
    return fig.show()

print(treemap())
