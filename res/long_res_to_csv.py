import json
import pandas as pd
import argparse

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
                # Extract general task-level scores
                for metric_type in ['entities', 'events', 'arguments']:
                    if metric_type in task_data and 'f1-score' in task_data[metric_type]:
                        f1_score = task_data[metric_type]['f1-score']
                        rows.append([f"{task_name} - {metric_type}", model_name, f1_score])
                
                # Extract class-level scores if available
                if 'class_scores' in task_data.get('events', {}):
                    class_scores = task_data['events']['class_scores']
                    for class_name, class_data in class_scores.items():
                        if 'f1-score' in class_data:
                            class_f1_score = class_data['f1-score']
                            rows.append([f"{task_name} - class: {class_name}", model_name, class_f1_score])
    
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
result_df.to_excel("long_model_comparison.xlsx", index=True)