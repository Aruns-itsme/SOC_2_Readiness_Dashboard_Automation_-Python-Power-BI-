import pandas as pd
import os

controls_file = os.path.join('..', 'data', 'controls_template.xlsx')
output_file = os.path.join('..', 'data', 'readiness_summary.csv')

def load_controls(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def calculate_compliance(df):
    df['Compliance Score'] = df['Implementation Status'].apply(lambda x: 1 if str(x).strip().lower() == 'implemented' else 0)
    summary = df.groupby(['Category', 'Risk Level']).agg({
        'Compliance Score': ['sum', 'count']
    }).reset_index()
    summary.columns = ['Category', 'Risk Level', 'Implemented', 'Total']
    summary['Compliance Percentage'] = (summary['Implemented'] / summary['Total']) * 100
    return summary

def save_summary(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Readiness summary saved to {output_path}")
    except Exception as e:
        print(f"Error saving summary: {e}")

def main():
    print("Loading enhanced control data...")
    df_controls = load_controls(controls_file)
    if df_controls is not None:
        print("Calculating enhanced compliance report...")
        summary_df = calculate_compliance(df_controls)
        print("Saving summary...")
        save_summary(summary_df, output_file)
        print("Done.")
    else:
        print("Failed to process readiness report.")

if __name__ == "__main__":
    main()
