# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM `loan_project`.`default`.`loan_project`
# MAGIC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %sql
# MAGIC describe loan_project;

# COMMAND ----------

# MAGIC %md
# MAGIC # Gender Wise Distrubtion 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT Gender , count(Customer_ID) as `Number of Customers` FROM `loan_project`.`default`.`loan_project`
# MAGIC group by Gender;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT Gender , sum(Loan) as `Total Loan` FROM `loan_project`.`default`.`loan_project`
# MAGIC group by Gender;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT Occupation , Gender , Customer_ID FROM `loan_project`.`default`.`loan_project`
# MAGIC where Income > 600000;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT count(Customer_ID) as `Number of Customers who have more than 4 kids`FROM `loan_project`.`default`.`loan_project`
# MAGIC where Family_Size > 4;

# COMMAND ----------

# MAGIC %md
# MAGIC # Top Occupation of taking Loan

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT distinct Occupation FROM `loan_project`.`default`.`loan_project` 
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT  Occupation , sum(Loan) as `Total Loan` FROM `loan_project`.`default`.`loan_project`
# MAGIC GROUP BY Occupation 
# MAGIC ORDER BY 2 DESC
# MAGIC limit 10;

# COMMAND ----------

# MAGIC %md
# MAGIC # Loan Category Distribution 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT  Loan_Category FROM `loan_project`.`default`.`loan_project`
# MAGIC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT  Loan_Category , sum(Loan) as `Total Loan` FROM `loan_project`.`default`.`loan_project`
# MAGIC GROUP BY 1 
# MAGIC ORDER BY 2 DESC
# MAGIC LIMIT 5
# MAGIC ;

# COMMAND ----------

# MAGIC %md
# MAGIC # Marital Status taking Loan

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT  Marital_Status , sum(Loan) as `Total Loan` FROM `loan_project`.`default`.`loan_project`
# MAGIC GROUP BY 1 
# MAGIC ORDER BY 2 DESC
# MAGIC ;
