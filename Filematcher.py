import pandas as pd
import os

base_filenames_file = 'base_filenames.csv'
file_paths_file = 'file_paths.csv'
output_file = 'matched_file_paths.csv'

base_filenames_df = pd.read_csv(base_filenames_file)

file_paths_df = pd.read_csv(file_paths_file, header=None, names=['FilePath'])

print("Columns in file_paths_df:", file_paths_df.columns.tolist())

def extract_base_filename_from_path(file_path):
    filename = os.path.basename(file_path)
    base_filename, ext = os.path.splitext(filename)
    return base_filename

file_paths_df['BaseFilename'] = file_paths_df['FilePath'].apply(extract_base_filename_from_path)

base_filenames_df['BaseFilename'] = base_filenames_df['BaseFilename'].str.lower()
file_paths_df['BaseFilename'] = file_paths_df['BaseFilename'].str.lower()

merged_df = pd.merge(base_filenames_df, file_paths_df[['BaseFilename', 'FilePath']], on='BaseFilename', how='left')

merged_df['FilePath'].fillna('Not Found', inplace=True)

merged_df.to_csv(output_file, index=False)

print(f"Matching complete. Output saved to '{output_file}'.")