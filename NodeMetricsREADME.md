# NodeMetrics: Real-Time Cloud Infrastructure Diagnostics Framework

A zero-dependency, lightweight system monitoring and anomaly detection framework built in pure Python. NodeMetrics is mathematically optimized to track, analyze, and report cloud resource utilization logs with O(1) constant time complexity, making it ideal for low-cost, resource-constrained edge computing devices like the **Banana Pi**.

---

## 🚀 Key Features

* **O(1) Constant Time Ingestion & Lookup:** Utilizes an optimized Hash-Map structure (Python dictionaries) to ensure lookup speeds remain completely unaffected by the growth of the dataset.
* **Zero-Dependency Architecture:** Built strictly using Python's standard library (`csv`, `os`). No Pandas, NumPy, or heavy database engines required—drastically reducing the memory footprint.
* **Inverted Indexing for Instant Reporting:** Maintains a parallel reverse index categorized by health states (`Healthy`, `Warning`, `Critical`) to compile anomaly reports instantly without re-scanning the entire dataset.
* **Deterministic Threshold Evaluation:** Implements standard cloud infrastructure health boundaries (%80 CPU / %75 RAM for Critical alerts) to isolate operational risks in real-time.

---

## 📊 Dataset & Performance Brief

The framework was benchmarked using a real-world cloud resource consumption dataset consisting of **14,400 logs** and **10 unique user workloads**. 

* **Execution Time:** < 0.5 seconds for full ingestion, diagnosis, and index compilation.
* **Diagnostic Breakdown:**
  * **Healthy Nodes:** 4 unique users
  * **Warning Nodes:** 1 unique user
  * **Critical Nodes (Anomalies):** 5 unique users

---

## 🛠️ File Structure

* `nodemetrics_code.py` — The core Python application script containing the ingestion pipeline, simple search menu, and inverted index logic.
* `cloud_dataset.csv` — The raw infrastructure resource log dataset (place this in the root directory).
* `README.md` — Project overview, documentation, and setup instructions.

---

## 💻 Setup & Execution Instructions

Follow these simple steps to run the framework locally or deploy it on an ARM-based edge device:

### 1. Prerequisites
Ensure you have Python 3.x installed on your system. You can verify your version by running:
```bash
python --version
