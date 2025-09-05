from pathlib import Path
import polars as pl

# Pasta raiz onde estão as subpastas
root_path = Path(r"C:\tcc\tcc-especializacao\results")

# Lista as subpastas em ordem alfabética (ou você pode definir a ordem manualmente)
subfolders = sorted([f for f in root_path.iterdir() if f.is_dir()])

dfs = []

for folder in subfolders:
    # Procura todso os CSVs dentro da subpasta
    csv_files = list(folder.glob("*.csv"))

    for csv_file in csv_files:
        # Lê o CSV
        df = pl.read_csv(csv_file)

        # Adiciona coluna com o nome da subpasta (modelo)
        df = df.with_columns(pl.lit(folder.name).alias("model"))


        dfs.append(df)

# Concatena todos os DataFrames na ordem das pastas
combined_df = pl.concat(dfs)

# Salva o CSV final
combined_csv_path = root_path / "combined_results.csv"
combined_df.write_csv(combined_csv_path)

print(f"CSV combinado salvo em: {combined_csv_path}")