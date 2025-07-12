 ### módulo reutilizável em Python

src/
│
├── preprocessamento.py      # Funções de redimensionamento, normalização, etc.
├── modelo.py                # Funções para construir modelos (CNN, ViT, etc.)
├── avaliacao.py             # Funções de métricas: acurácia, F1, matriz de confusão
└── utilitarios.py           # Funções auxiliares (ex: salvar figura, plotar camadas)


from src.preprocessamento import carregar_dados
from src.modelo import criar_cnn
from src.avaliacao import calcular_metricas
