# HW4 - Graph Databases and Spark

This project involves building a graph database using Neo4j, creating API endpoints with Flask, and processing data using PySpark.

## Files
- `app.py` – Flask server that exposes all Neo4j and Spark endpoints
- `load_graph.py` – Script to load the cleaned taxi data into Neo4j
- `preprocess.py` – PySpark script used for preprocessing and generating aggregated data
- `fdb_answers.txt` – Answers to FoundationDB conceptual questions
- `Design.pdf` – Short analysis comparing graph and relational approaches
- `Team.txt` – NetID
- `HW4.txt` – External IP and port for the API

## How to run
1. Run `python clean.py` to generate the cleaned dataset  
2. Run `python load_graph.py` to load data into Neo4j  
3. Run `python preprocess.py` to generate processed Spark output  
4. Run `python app.py` to start the API server  

## Screenshot (Part 2.1)
Below is a screenshot showing the contents of the `processed_data/` folder and a sample part file output:

![Processed Data Screenshot](498hw4.png)
