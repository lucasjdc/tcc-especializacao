import kagglehub
import os
import pandas as pd

# Mapeia os rótulos numéricos para nomes das classes
label_map = {
    0: 'Mild_Dementia',
    1: 'Moderate_Dementia',
    2: 'Non_Demented',
    3: 'Very_mild_Dementia'
}

# Mapeia os nomes das pastas para rótulos numéricos
class_map = {
    'Mild Dementia': 0,
    'Moderate Dementia': 1,
    'Non Demented': 2,
    'Very mild Dementia': 3
}

# 1. Baixar os datasets (como já fez com kagglehub)
path_alzheimer = kagglehub.dataset_download("borhanitrash/alzheimer-mri-disease-classification-dataset")
path_oasis = kagglehub.dataset_download("kushagrasharma133/oasis-alzheimer-dataset")

# 2. Função para criar dataframe a partir de imagens em pastas
def criar_dataframe_de_imagens(base_path, class_map, source_name):
    dados = []
    for label_nome, label_id in class_map.items():
        pasta = os.path.join(base_path, label_nome)
        if not os.path.exists(pasta):
            continue
        for nome_arquivo in os.listdir(pasta):
            if nome_arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                with open(os.path.join(pasta, nome_arquivo), "rb") as f:
                    dados.append({
                        'image_bytes': f.read(),   # salva os bytes direto
                        'label': label_id,
                        'class_name': label_nome,
                        'source': source_name
                    })
    return pd.DataFrame(dados)

# 3. Carregar Alzheimer (parquet -> já vem em bytes)
df_parquet = None
for root, dirs, files in os.walk(path_alzheimer):
    for file in files:
        if file.endswith('.parquet') and 'train' in file:
            df_tmp = pd.read_parquet(os.path.join(root, file))
            df_tmp['image_bytes'] = df_tmp['image'].apply(lambda x: x['bytes'])
            df_tmp['class_name'] = df_tmp['label'].map(label_map)
            df_tmp['source'] = 'AlzheimerMRI'
            df_parquet = df_tmp[['image_bytes', 'label', 'class_name', 'source']]

# 4. Carregar OASIS (em pastas)
df_train_oasis = criar_dataframe_de_imagens(os.path.join(path_oasis, 'train'), class_map, 'OASIS_train')
df_test_oasis = criar_dataframe_de_imagens(os.path.join(path_oasis, 'test'), class_map, 'OASIS_test')

# 5. Unir todos
df_unificado = pd.concat([df_parquet, df_train_oasis, df_test_oasis], ignore_index=True)

# 6. Definir caminho de saída na pasta processed
output_dir = r"C:\tcc\tcc-especializacao\data\processed"
os.makedirs(output_dir, exist_ok=True)  # cria a pasta caso não exista
output_path = os.path.join(output_dir, "dataset_alzheimer_unificado.parquet")

# 7. Salvar em Parquet único para reutilizar no TCC
df_unificado.to_parquet(output_path)

print(f"Dataset final salvo em: {output_path}")
print(df_unificado['source'].value_counts())
