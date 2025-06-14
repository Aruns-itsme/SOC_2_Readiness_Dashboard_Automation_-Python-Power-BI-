# SOC 2 Readiness Dashboard Automation

This project automates the generation and visualization of SOC 2 compliance readiness data using **Python** and **Power BI**. It enables organizations to continuously monitor their audit preparation status by integrating enhanced control tracking and evidence validation into a streamlined, dashboard-ready output.

---

## Project Overview

SOC 2 compliance is a critical benchmark for service providers handling customer data. Preparing for this audit involves maintaining updated controls, tracking evidence, and ensuring proper documentation across risk categories. This project tackles these tasks by:

- Automating control and evidence ingestion
- Calculating weighted compliance metrics
- Visualizing the results in an interactive Power BI dashboard

The dashboard allows auditors, security managers, and leadership to easily identify compliance gaps and implementation trends across various SOC 2 domains.

---

## Architecture Diagram

Below is a visual overview of the system architecture and data flow:

![Architecture Diagram](docs/architecture_diagram.png)

---

## Power BI Dashboard

Here's a preview of the final Power BI dashboard that displays real-time SOC 2 readiness insights:

![Power BI Dashboard](dashboards/PowerBi_Dashboard.png)

---

## Project Directory Structure

```
SOC2-Readiness-Dashboard/
├── data/
│   ├── controls_template.xlsx
│   ├── evidence_status.csv
│   └── readiness_summary.csv
├── scripts/
│   ├── generate_readiness_report.py
│   ├── update_evidence_status.py
│   └── utils.py
├── dashboards/
│   └── SOC2_Readiness.pbix
│   └── PowerBi_Dashboard.png
├── docs/
│   └── architecture_diagram.png
├── requirements.txt
├── README.md
└── LICENSE
```

---


## Project Directory Structure & File Descriptions

This section explains every folder and file used in the `SOC2-Readiness-Dashboard` project.

---

### `data/` — Input and Output Data Files

| File Name | Description |
|-----------|-------------|
| `controls_template.xlsx` | The **master input file** listing all SOC 2 controls, their categories, implementation status, owners, risk level, and review timelines. This is the central dataset for compliance tracking. |
| `evidence_status.csv` | Tracks **evidence submissions** for each control. Includes file type, size, verification status, and reviewer comments. Used to validate and update control readiness. |
| `readiness_summary.csv` | **Auto-generated output** from the Python script. This file summarizes compliance metrics by category and risk level. It feeds directly into the Power BI dashboard. |

---

### `scripts/` — Automation Logic in Python

| File Name | Description |
|-----------|-------------|
| `generate_readiness_report.py` | Core script that reads control data, calculates compliance scores, and outputs `readiness_summary.csv`. It groups results by category and risk level using weighted calculations. |
| `update_evidence_status.py` | Cross-checks `evidence_status.csv` and updates `controls_template.xlsx` with verified evidence and revised review dates. Keeps control tracking in sync with actual evidence submissions. |
| `utils.py` | Helper functions shared across scripts, such as loading data, calculating percentages, and performing common transformations. Helps keep the code modular and clean. |

---

### `dashboards/` — Visualization Layer

| File Name | Description |
|-----------|-------------|
| `SOC2_Readiness.pbix` | Power BI dashboard file that visually presents compliance data from `readiness_summary.csv`. It includes bar charts, matrices, KPIs, and slicers for filtering by category and risk level. |
| `PowerBi_Dashboard.png` | A static screenshot of the Power BI dashboard. Useful for GitHub README previews or documentation. |

---

### `docs/` — Project Documentation Assets

| File Name | Description |
|-----------|-------------|
| `architecture_diagram.png` | Visual diagram showing the architecture and data flow: from Excel and CSV → Python processing → Power BI dashboard. It helps stakeholders understand the end-to-end system. |

---


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SOC2-Readiness-Dashboard.git
cd SOC2-Readiness-Dashboard
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Input Files

Ensure the following files are present inside the `data/` folder:

- `controls_template.xlsx` – Master list of all controls
- `evidence_status.csv` – List of evidence files with verification status

### 5. Run the Python Script

This script generates a readiness summary based on the input data.

```bash
python scripts/generate_readiness_report.py
```

To update control status based on evidence verification:

```bash
python scripts/update_evidence_status.py
```

This will generate or update the file:  
```
data/readiness_summary.csv
```

---

## Load the Power BI Dashboard

1. Open Power BI Desktop
2. Load `dashboards/SOC2_Readiness.pbix`
3. Refresh the data source to pull the latest values from `readiness_summary.csv`
4. Save or export the updated dashboard

---

## Key Features

- Control-level tracking of SOC 2 implementation
- Dynamic calculation of compliance % (weighted average)
- Risk-level segmentation (High, Medium, Low)
- Real-time update via CSV/Excel inputs
- Fully customizable Power BI visuals

---

## Future Enhancements

- Integration with Jira/Confluence for auto-updating evidence
- Email listener to parse and log submitted documents
- CI/CD automation to update dashboard on a schedule


---

## 🙋‍♂️ Support

For issues or enhancements, feel free to create a pull request or submit an issue on GitHub.
