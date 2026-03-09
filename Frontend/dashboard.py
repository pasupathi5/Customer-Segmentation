import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd
import requests

# Fetch data from FastAPI
data = requests.get("http://127.0.0.1:8000/customers").json()
summary = requests.get("http://127.0.0.1:8000/summary").json()

df = pd.DataFrame(data)

# Cluster distribution
cluster_counts = df["Cluster_Label"].value_counts().reset_index()
cluster_counts.columns = ["Cluster", "Customers"]

# 3D Scatter Plot
scatter_3d = px.scatter_3d(
    df,
    x="Recency",
    y="Frequency",
    z="Monetary",
    color="Cluster_Label",
    title="3D Customer Segmentation (RFM)"
)

# Bar Chart
bar_chart = px.bar(
    cluster_counts,
    x="Cluster",
    y="Customers",
    color="Cluster",
    title="Customer Distribution by Cluster"
)

# Pie Chart
pie_chart = px.pie(
    cluster_counts,
    names="Cluster",
    values="Customers",
    title="Cluster Share"
)

# Initialize app
app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Customer Segmentation Dashboard",
        style={"textAlign":"center"}
    ),

    html.H4(
        f"Total Customers: {summary['total_customers']} | "
        f"Total Segments: {summary['total_clusters']}",
        style={"textAlign":"center"}
    ),

    # Charts Row 1
    html.Div([
        dcc.Graph(figure=scatter_3d)
    ]),

    # Charts Row 2
    html.Div([
        dcc.Graph(figure=bar_chart),
        dcc.Graph(figure=pie_chart)
    ], style={"display":"flex"}),

    html.H3("Customer Dataset"),

    dash_table.DataTable(
        data=df.head(50).to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        page_size=10,
        style_table={"overflowX":"auto"}
    )

])

if __name__ == "__main__":
    app.run(debug=True)