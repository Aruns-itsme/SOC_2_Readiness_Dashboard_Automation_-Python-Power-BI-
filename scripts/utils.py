
import pandas as pd

def load_controls(file_path):
    """Load the controls data from Excel file."""
    try:
        df = pd.read_excel(file_path)
        print(f"Loaded controls data from {file_path}")
        return df
    except Exception as e:
        print(f"Error loading controls file: {e}")
        return None

def load_evidence(file_path):
    """Load the evidence data from CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded evidence data from {file_path}")
        return df
    except Exception as e:
        print(f"Error loading evidence file: {e}")
        return None

def calculate_compliance(df_controls):
    """Calculate compliance score by category."""
    df_controls['Compliance Score'] = df_controls['Status'].apply(
        lambda x: 1 if str(x).strip().lower() == 'complete' else 0
    )
    summary = df_controls.groupby('Category').agg({
        'Compliance Score': ['sum', 'count']
    }).reset_index()
    summary.columns = ['Category', 'Completed', 'Total']
    summary['Compliance Percentage'] = (summary['Completed'] / summary['Total']) * 100
    return summary

def get_verified_controls(df_evidence):
    """Return a list of control IDs with verified evidence."""
    verified = df_evidence[df_evidence['Status'].str.lower() == 'verified']['Control ID'].unique()
    return verified

def update_evidence_status(df_controls, verified_controls):
    """Update the Evidence Provided field based on verified evidence."""
    df_updated = df_controls.copy()
    df_updated['Evidence Provided'] = df_updated.apply(
        lambda row: 'Yes' if row['Control ID'] in verified_controls else row['Evidence Provided'],
        axis=1
    )
    return df_updated
