import pandas as pd

file_path = "all_laptops.xlsx"
sheet_name = "Sheet1"
df = pd.read_excel(file_path, sheet_name)

csv_file_path = "modified_laptops.csv"
csv_df = pd.read_csv(csv_file_path)


if 'price' in df.columns and 'price' in csv_df.columns:
   
    cleaned_prices = df['price'].astype(str).str.replace('₹', '', regex=False).str.replace(',', '', regex=False)

    
    cleaned_prices = pd.to_numeric(cleaned_prices, errors='coerce')

   
    if len(cleaned_prices) == len(csv_df):
        
        csv_df['price'] = cleaned_prices

        
        csv_df.to_csv("updated_laptops.csv", index=False)

        print("Prices updated successfully.")
    else:
        print("Warning: The lengths of DataFrames do not match.")
else:
    print("Error: 'price' column is missing in one of the DataFrames.")