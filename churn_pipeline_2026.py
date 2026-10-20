import pandas as pd 
# ==========================================
# PHASE 1: LOCAL DATA INGESTION
# ==========================================
# Fixed the name to match your exact file spelling with underscores!
df = pd.read_excel("/Users/minakshikumari/Advanced_Churn_Analytics/Telco_customer_churn.xlsx", engine="openpyxl")

print("=== 🟢 PHASE 1 COMPLETE: DATA INGESTION SUCCESSFUL ===")


# ==========================================
# PHASE 2: DATA CLEANING & TYPE CONVERSION
# ==========================================
# 1. Force the Total Charges text column into clean numbers
df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')

# 2. Drop the empty rows so our dataset remains clean
df = df.dropna(subset=['Total Charges'])

print("=== 🛠️ PHASE 2 COMPLETE: TYPE NORMALIZATION SUCCESSFUL ===")


# ==========================================
# PHASE 3: EXPORTING CLEAN DATA FOR POWER BI
# ==========================================
# Save the final cleaned table into a fresh CSV file for Power BI
df.to_csv("clean_telecom_churn.csv", index=False)

print("🎉 PHASE 3 COMPLETE: 'clean_telecom_churn.csv' IS SAVED AND READY!")