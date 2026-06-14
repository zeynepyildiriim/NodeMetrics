# NodeMetrics - Cloud Infrastructure Diagnostics
# Zeynep Yildirim | Student ID: 250221021031

import csv
import os

# --- Threshold Values ---
CPU_WARNING = 70.0
CPU_CRITICAL = 80.0
MEM_WARNING = 65.0
MEM_CRITICAL = 75.0

def analyze_infrastructure():
    dataset_name = "cloud_dataset.csv"

    if not os.path.exists(dataset_name):
        print(f"Error: {dataset_name} file not found!")
        return

    # Core Data Structures (Basic Hash-Map and Inverted Index)
    server_dictionary = {}  # Hash-Map: User_ID -> Resource Metrics
    status_groups = {       # Inverted Index: Status -> List of Unique IDs
        "Critical": [],
        "Warning": [],
        "Healthy": []
    }

    print(f"\nReading {dataset_name}...")

    # Step 1: Read CSV file line by line
    with open(dataset_name, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            node_id = row.get("User_ID", "Unknown").strip()
            
            try:
                cpu = float(row["CPU_Usage"])
                mem = float(row["Memory_Usage"])
            except (ValueError, KeyError):
                continue  # Skip rows with missing or corrupted data

            # Step 2: Determine Health Status based on thresholds
            if cpu >= CPU_CRITICAL or mem >= MEM_CRITICAL:
                current_status = "Critical"
            elif cpu >= CPU_WARNING or mem >= MEM_WARNING:
                current_status = "Warning"
            else:
                current_status = "Healthy"

            # Step 3: Update structures cleanly without duplicates
            if node_id in server_dictionary:
                old_status = server_dictionary[node_id]["status"]
                # If the status changed, remove from the old list
                if old_status != current_status:
                    if node_id in status_groups[old_status]:
                        status_groups[old_status].remove(node_id)

            # Insert or update data into Hash-Map
            server_dictionary[node_id] = {
                "cpu": cpu,
                "mem": mem,
                "status": current_status
            }

            # Insert into Inverted Index list if not already there
            if node_id not in status_groups[current_status]:
                status_groups[current_status].append(node_id)

    # Step 4: Print Summary Report
    print("=" * 40)
    print("      NODEMETRICS SUMMARY REPORT")
    print("=" * 40)
    print(f"Total Unique Servers (User_ID): {len(server_dictionary)}")
    print(f"Healthy Nodes : {len(status_groups['Healthy'])}")
    print(f"Warning Nodes : {len(status_groups['Warning'])}")
    print(f"Critical Nodes: {len(status_groups['Critical'])}")
    print("-" * 40)

    # Print first 5 critical nodes as an example
    if status_groups["Critical"]:
        print("\nCRITICAL ANOMALIES DETECTED:")
        for nid in status_groups["Critical"][:5]:
            info = server_dictionary[nid]
            print(f"ID: {nid} | CPU: {info['cpu']}% | RAM: {info['mem']}%")

    # Step 5: Simple Search Menu
    search_choice = input("\nDo you want to query a specific ID? (y/n): ").lower()
    if search_choice == 'y':
        while True:
            selected_id = input("Enter Node ID to search (Type 'exit' to quit): ").strip()
            if selected_id.lower() == 'exit':
                print("Exiting search menu.")
                break
            
            if selected_id in server_dictionary:
                metrics = server_dictionary[selected_id]
                print(f"--- {selected_id} Status ---")
                print(f"CPU: {metrics['cpu']}% | RAM: {metrics['mem']}% | Status: {metrics['status']}")
            else:
                print("Node ID not found in the registry.")

if __name__ == "__main__":
    analyze_infrastructure()
