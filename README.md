Customer Segmentation using RFM Analysis and K-Means Clustering










Project Overview

Customer segmentation is the process of dividing customers into groups based on similar purchasing behavior. Businesses use this method to better understand their customers and design targeted marketing strategies.

This project implements Customer Segmentation using the RFM (Recency, Frequency, Monetary) model combined with K-Means clustering. The results are presented through an interactive dashboard built with Plotly Dash, while FastAPI serves as the backend API.

The system analyzes customer transaction data and groups customers into different segments such as:

High-value customers

Regular customers

New customers

At-risk customers

This helps businesses improve marketing campaigns and increase customer retention.

Key Features

Customer segmentation using RFM analysis

Unsupervised learning using K-Means clustering

Optimal cluster selection using Elbow Method

Interactive 3D visualization dashboard

Backend service using FastAPI

Data preprocessing and feature engineering

Interactive charts using Plotly Dash

Technologies Used
Programming Language

Python

Machine Learning

Scikit-learn

K-Means Clustering

RFM Model

Libraries

pandas

numpy

plotly

dash

Frameworks

FastAPI

Plotly Dash

Visualization

Scatter Plot

Bar Chart

Cluster Distribution Graph

Project Architecture
Dataset
   ↓
Data Cleaning
   ↓
RFM Feature Engineering
   ↓
Data Scaling
   ↓
K-Means Clustering
   ↓
FastAPI Backend
   ↓
Plotly Dash Dashboard
   ↓
Interactive Customer Insights
RFM Model Explanation

RFM is a marketing technique used to evaluate customer behavior.

Metric	Description
Recency	Time since last purchase
Frequency	Number of purchases
Monetary	Total money spent

Customers with:

Low Recency

High Frequency

High Monetary value

are considered the most valuable customers.

Machine Learning Model

The project uses K-Means clustering, an unsupervised machine learning algorithm.

Steps

Data preprocessing

RFM feature calculation

Feature scaling

Optimal cluster detection using Elbow Method

K-Means clustering

Cluster visualization

Dashboard Visualization

The dashboard provides interactive insights into customer segments.

Visualizations include:

3D Scatter Plot of clusters

Bar chart showing customer distribution

Cluster summary statistics

Interactive exploration of segments

Project Screenshots

(Add your dashboard screenshots here)

Example:

screenshots/dashboard.png
screenshots/clusters.png

Example section:

Dashboard

Cluster Visualization

Dataset

The dataset contains customer transaction data used to calculate RFM values.

Example dataset columns:

Column	Description
CustomerID	Unique customer ID
InvoiceDate	Date of purchase
Quantity	Product quantity
UnitPrice	Price per item
TotalAmount	Total purchase value

From this data the system calculates:

Recency

Frequency

Monetary value

Installation

Clone the repository

git clone https://github.com/pasupathi5/Customer-Segmentation.git

Navigate to the project folder

cd Customer-Segmentation

Install required packages

pip install -r requirements.txt
Running the Project

Start FastAPI server

uvicorn main:app --reload

Run Plotly Dash dashboard

python dashboard.py

Open the dashboard in browser

http://127.0.0.1:8050
Example Customer Segments
Cluster	Customer Type
Cluster 0	High-value customers
Cluster 1	Loyal customers
Cluster 2	New customers
Cluster 3	At-risk customers
Real-world Applications

This system can be used in:

E-commerce platforms

Retail analytics

Marketing campaign optimization

Customer loyalty analysis

Sales forecasting

Companies like Amazon, Flipkart, and Netflix use similar segmentation techniques to personalize recommendations.

Future Improvements

Possible enhancements include:

Real-time customer segmentation

Deep learning clustering methods

Customer churn prediction

Recommendation systems

Cloud deployment (AWS / Azure)

Docker containerization

Resume Project Description

You can use this in your resume:

Customer Segmentation using RFM and K-Means Clustering

Developed a machine learning system to segment customers based on purchasing behavior using the RFM model and K-Means clustering. Built an interactive dashboard using Plotly Dash and deployed backend APIs using FastAPI to visualize customer segments and generate business insights.

Author

Pasupathi Thangadurai

Final Year – BSc Computer Science

GitHub
https://github.com/pasupathi5

License

This project is licensed under the MIT License.
