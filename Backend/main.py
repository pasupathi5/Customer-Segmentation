from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load clustered dataset
df = pd.read_csv("../clustered_data.csv")

@app.get("/")
def home():
    return {"message": "Customer Segmentation API Running"}

# Full dataset
@app.get("/customers")
def get_customers():
    return df.to_dict(orient="records")

# Summary
@app.get("/summary")
def summary():

    total_customers = len(df)
    total_clusters = df["Cluster_Label"].nunique()

    cluster_counts = df["Cluster_Label"].value_counts().to_dict()

    return {
        "total_customers": total_customers,
        "total_clusters": total_clusters,
        "cluster_distribution": cluster_counts
    }