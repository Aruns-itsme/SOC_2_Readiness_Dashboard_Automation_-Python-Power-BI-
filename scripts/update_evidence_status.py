
import pandas as pd
import os

# File paths
controls_file = os.path.join('data', 'controls_template_enhanced.xlsx')
evidence_file = os.path.join('data', 'evidence_status_enhanced.csv')
output_file = os.path.join('data', 'controls_template_enhanced_updated.xlsx')

def load_data():
    try:
        df_controls = pd.read_excel(controls_file)
        df_evidence = pd.read_csv(evidence_file)
        return df_controls, df_evidence
    except Exception as e:
        print(f"Error loading files: {e}")
        return None, None

def update_controls_with_evidence(df_controls, df_evidence):
    # Get verified control IDs
    verified_controls = df_evidence[df_evidence['Status'].str.lower() == 'verified']['Control ID'].unique()

    # Update evidence-provided field
    df_controls_updated = df_controls.copy()
    df_controls_updated['Evidence Provided'] = df_controls_updated.apply(
        lambda row: 'Yes' if row['Control ID'] in verified_controls else row['Evidence Provided'],
        axis=1
    )

    # Optionally, update last reviewed date if evidence is verified
    df_controls_updated['Last Reviewed'] = df_controls_updated.apply(
        lambda row: pd.Timestamp.today().strftime('%Y-%m-%d') if row['Control ID'] in verified_controls else row['Last Reviewed'],
        axis=1
    )

    return df_controls_updated

def save_updated_controls(df, output_path):
    try:
        df.to_excel(output_path, index=False)
        print(f"Updated control sheet saved to {output_path}")
    except Exception as e:
        print(f"Error saving updated controls: {e}")

def main():
    print("Loading enhanced control and evidence data...")
    df_controls, df_evidence = load_data()
    if df_controls is not None and df_evidence is not None:
        print("Updating control sheet based on verified evidence...")
        df_updated = update_controls_with_evidence(df_controls, df_evidence)
        save_updated_controls(df_updated, output_file)
        print("Update complete.")
    else:
        print("Could not update control sheet due to data loading issues.")

if __name__ == "__main__":
    main()
