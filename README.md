# Simulação de Infecção Bacteriana com Autômatos Celulares

Este projeto implementa um modelo computacional para simular a propagação de uma infecção bacteriana em uma grade que representa uma seção da circulação sanguínea. Utilizando Python com as bibliotecas NumPy e Matplotlib, a simulação demonstra como interações locais simples podem gerar padrões complexos e emergentes.

## Sumário do Projeto

A compreensão dos mecanismos de propagação de infecções bacterianas na corrente sanguínea é essencial para o avanço de estratégias terapêuticas e prevenção de doenças sistêmicas. Este projeto propõe um modelo computacional baseado em autômatos celulares para simular a dinâmica da infecção em um sistema discreto. Cada célula da grade assume um dos três estados:
- **Saudável**: Representa o sangue normal.
- **Infectada**: Indica a presença da bactéria.
- **Imune**: Células que, após infecção, adquirem resistência.

A implementação utiliza operações vetorizadas com NumPy para atualizar a simulação e o Matplotlib para visualização e animação dos estados ao longo das iterações. Ao final, é gerado um gráfico que mostra a evolução dos estados das células, servindo como uma ferramenta didática e exploratória em investigações interdisciplinares envolvendo biologia computacional e modelagem de sistemas dinâmicos.

## Pré-requisitos

- **Python 3.x** instalado no sistema.
- Conexão com a internet para instalação das dependências.

## Configuração do Ambiente Virtual e Instalação das Dependências

### 1. Clone o repositório (ou baixe os arquivos do projeto)

```bash
git clone https://github.com/FelipeSantanaC/cellular-automata-ufrpe
cd <NOME_DA_PASTA_DO_PROJETO>
