-- SQL Query to extract raw customer data for Python cleaning pipeline
SELECT 
    customer_id,
    gender,
    contract_type,
    tenure_months,
    churn_value,
    churn_reason,
    cltv_value
FROM 
    enterprise_telecom_db.customer_records
WHERE 
    account_status = 'Active' 
    OR churn_value = 1;
