from pathlib import Path
import polars as pl
import matplotlib.pyplot as plt

# Caminho para o CSV combinado
combined_csv_path = Path(r"C:\tcc\tcc-especializacao\results\combined_results.csv")

# Lê o CSV
df = pl.read_csv(combined_csv_path)

# Seleciona a última época de cada modelo - CORRIGIDO
last_epoch_df = df.group_by("model").agg([
    pl.max("epoch").alias("max_epoch")
])
last_metrics = df.join(last_epoch_df, on=["model", "epoch" == "max_epoch"])

print("Métricas finais por modelo:")
print(last_metrics.select(["model", "accuracy", "f1_macro", "precision_macro", "recall_macro"]))

# Plot accuracy por época
plt.figure(figsize=(10,6))
for model in df["model"].unique():
    model_df = df.filter(pl.col("model") == model)
    plt.plot(model_df["epoch"], model_df["accuracy"], label=model)

plt.title("Accuracy por época")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.show()

# Plot losses por época
plt.figure(figsize=(10,6))
for model in df["model"].unique():
    model_df = df.filter(pl.col("model") == model)
    plt.plot(model_df["epoch"], model_df["train_loss"], label=f"{model} train")
    plt.plot(model_df["epoch"], model_df["val_loss"], '--', label=f"{model} val")

plt.title("Train/Validation Loss por época")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()