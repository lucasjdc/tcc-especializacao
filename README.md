## 📦 Estrutura de Módulo Reutilizável em Python

Este projeto utiliza uma estrutura modularizada para organizar o código de forma reutilizável e escalável, seguindo boas práticas de engenharia de software para ciência de dados.

### 📁 Diretório: `src/`

Contém os scripts com funções reutilizáveis separadas por responsabilidades:

src/
│
├── preprocessamento.py # Funções de redimensionamento, normalização, carregamento de imagens, etc.
├── modelo.py # Funções para construção de arquiteturas como CNNs, Transformers, etc.
├── avaliacao.py # Funções de avaliação: acurácia, precisão, revocação, F1-score, matriz de confusão.
└── utilitarios.py # Funções auxiliares como salvar modelos, gerar gráficos, visualizar ativação de camadas.

### 🧪 Exemplo de uso

A ideia é importar os módulos em notebooks ou scripts principais, assim:

```python
from src.preprocessamento import carregar_dados
from src.modelo import criar_cnn
from src.avaliacao import calcular_metricas

🛠️ Vantagens

    Código mais limpo e organizado.

    Facilidade de manutenção e testes.

    Possibilidade de reaproveitamento em outros projetos.

    Caminho facilitado para transformar o projeto em uma API ou serviço.
