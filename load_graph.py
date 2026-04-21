import pandas as pd
from neo4j import GraphDatabase

URI = "bolt://35.184.37.230:7687"
USER = "neo4j"
PASSWORD = "Neo4jHW4pass!"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def clear_graph(tx):
    tx.run("MATCH (n) DETACH DELETE n")

def load_row(tx, row):
    tx.run("""
        MERGE (d:Driver {driver_id: $driver_id})
        MERGE (c:Company {name: $company})
        MERGE (a:Area {area_id: $dropoff_area})
        MERGE (d)-[:WORKS_FOR]->(c)
        CREATE (d)-[:TRIP {
            trip_id: $trip_id,
            fare: $fare,
            trip_seconds: $trip_seconds
        }]->(a)
    """,
    driver_id=str(row["driver_id"]),
    company=str(row["company"]),
    dropoff_area=int(row["dropoff_area"]),
    trip_id=str(row["trip_id"]),
    fare=float(row["fare"]),
    trip_seconds=int(row["trip_seconds"]))

def main():
    df = pd.read_csv("taxi_trips_clean.csv")

    with driver.session() as session:
        session.execute_write(clear_graph)

        for _, row in df.iterrows():
            session.execute_write(load_row, row)

    driver.close()
    print("Graph loaded successfully.")

if __name__ == "__main__":
    main()
