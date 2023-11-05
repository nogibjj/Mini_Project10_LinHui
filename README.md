[![CI](https://github.com/nogibjj/Mini_Project10_LinHui/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Mini_Project10_LinHui/actions/workflows/cicd.yml)
# PySpark Data Processing

This repository contains a PySpark script for processing data from the VIX.csv dataset.

## Dataset

The `VIX.csv` file contains 5-year daily historical data for the Volatility Index (VIX). It includes columns for dates, opening prices, closing prices, highs, lows, and possibly other financial indicators.

## Script

The `main.py` file is a PySpark script that performs data loading, transformation, and analysis on the VIX dataset.

### Transformations
he script includes the following data transformations:
- Calculation of the daily range (the difference between the day's high and low prices)
- Export the new dataframe with daily range column to folder `transformed_VIX_DailyRange.csv`

### Analysis
The script performs analysis using Spark SQL, including:
- Calculation of average daily range

## Usage

To run the script, you need to have PySpark installed and properly configured. Then you can execute the script in a Spark environment.

```bash
spark-submit main.py
```
 or in the terminal of the root directory
 ```bash
 python main.py
 ```
