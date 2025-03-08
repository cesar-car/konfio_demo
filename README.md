#  How to resolve Coding Challenge - Bitcoin Price
# Objective:
Develop an automated and scalable process to obtain the 5-day moving
average of Bitcoin's price during the first quarter of 2022.
# Brief:
The finance team needs to analyze Bitcoin's behavior to determine if it's feasible to invest in this cryptocurrency. Your task is to automate this process and be prepared for real-time adjustments when necessary.
# Tasks:
1. Explore the Crypto API CoinGecko API Documentation
2. Create a DEMO account in the API to avoid any costs.
3. Retrieve a list of all cryptocurrencies with id, name, and symbol (using the CoinGecko API).
4. Retrieve the Bitcoin coin id.
5. Get Bitcoin's price in USD and by date for the first quarter of 2022 (using the CoinGecko API).
6. Save the data in the database of your choice.
7. Use the data previously stored in the database to calculate the 5-day moving average using a window/partition function in Python (you may use either pandas or PySpark).

