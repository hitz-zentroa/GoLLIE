import json
import pandas as pd
import argparse
import openpyxl

# Function to load json files and merge their information into a table
def generate_table_from_json(json_files):
    rows = []
    models = []
    
    # Traverse all provided json files
    for json_file in json_files:
        model_name = json_file  # Use the full path as the model name
        models.append(model_name)
        with open(json_file) as f:
            data = json.load(f)
            for task_name, task_data in data.items():
                f1_score = None
                if 'f1-score' in task_data.get('entities', {}):
                    f1_score = task_data['entities']['f1-score']
                elif 'f1-score' in task_data.get('events', {}):
                    f1_score = task_data['events']['f1-score']
                elif 'f1-score' in task_data.get('arguments', {}):
                    f1_score = task_data['arguments']['f1-score']
                
                if f1_score is not None:
                    rows.append([task_name, model_name, f1_score])
    
    # Create a dataframe from the collected rows
    df = pd.DataFrame(rows, columns=['Dataset', 'Model', 'F1-Score'])
    df = df.drop_duplicates(subset=['Dataset', 'Model'])  # Drop duplicate entries
    pivot_df = df.pivot(index='Dataset', columns='Model', values='F1-Score')
    
    return pivot_df

# Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a comparison table from JSON files.")
    parser.add_argument('json_files', nargs='+', help="Paths to the JSON files to be evaluated")
    parser.add_argument('--save_csv', type=str, help="Path to save the CSV file", default=None)
    args = parser.parse_args()
    
    result_df = generate_table_from_json(args.json_files)
    print(result_df)
    
    # Optionally save to CSV
    if args.save_csv:
        result_df.to_csv(args.save_csv)
        
# Save to Excel for visualization
result_df.to_excel("model_comparison.xlsx", index=True)