import pandas as pd

def load_and_convert(file_path, output_csv):
    """
    Load a .txt file and save it as a CSV file.
    
    Parameters:
        file_path (str): Path to the .txt file.
        output_csv (str): Path to save the CSV file.
    """
    try:
        # Load the dataset
        data = pd.read_csv(file_path, delimiter="|")
        print(f"Data loaded successfully! Shape: {data.shape}")
        
        # Save as CSV
        data.to_csv(output_csv, index=False)
        print(f"Data saved as CSV at: {output_csv}")
    except Exception as e:
        print(f"Error loading or saving data: {e}")

# Example usage
if __name__ == "__main__":
    load_and_convert("/home/bbm/Downloads/MachineLearningRating_v3.txt", "/home/bbm/Documents/projects/MachineLearningRating_v3.csv")