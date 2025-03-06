import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

# Estados definidos
HEALTHY = 0   # Sangue (saudável)
INFECTED = 1  # Bactéria (infectada)
IMMUNE = 2    # Célula imune (após infecção)

# Parâmetros da simulação
size = 50            # Tamanho da grade (50x50)
prob_spread = 0.5    # Probabilidade de infecção ao ter vizinho infectado
steps = 50           # Número de iterações da simulação

# Inicializa a grade: todas células saudáveis, com uma célula infectada no centro
grid = np.full((size, size), HEALTHY, dtype=int)
grid[size//2, size//2] = INFECTED

# Listas para armazenar contagens por iteração
healthy_counts = []
infected_counts = []
immune_counts = []

# Colormap customizado: vermelho (saudável), roxo (infectada) e cinza claro (imune)
custom_cmap = ListedColormap(["red", "purple", "lightgray"])

def update_grid(grid):
    """
    Atualiza a grade utilizando operações vetorizadas:
    - Verifica os 4 vizinhos usando np.roll para detectar células infectadas.
    - Células saudáveis com vizinhos infectados têm chance de se infectar.
    - Células infectadas passam para o estado imune.
    """
    infected_neighbors = (
        (np.roll(grid, 1, axis=0) == INFECTED).astype(int) +
        (np.roll(grid, -1, axis=0) == INFECTED).astype(int) +
        (np.roll(grid, 1, axis=1) == INFECTED).astype(int) +
        (np.roll(grid, -1, axis=1) == INFECTED).astype(int)
    )
    
    new_grid = grid.copy()
    
    # Transição de células saudáveis para infectadas com base na probabilidade
    infect_mask = (grid == HEALTHY) & (infected_neighbors > 0)
    random_vals = np.random.rand(size, size)
    new_grid[infect_mask & (random_vals < prob_spread)] = INFECTED
    
    # Células infectadas tornam-se imunes na próxima iteração
    new_grid[grid == INFECTED] = IMMUNE
    
    return new_grid

# Configuração da visualização e animação
fig, ax = plt.subplots(figsize=(6, 6))

def update(frame):
    global grid
    ax.clear()
    ax.imshow(grid, cmap=custom_cmap, vmin=0, vmax=2)
    ax.set_title(f"Iteração {frame}")
    
    # Calcula a quantidade de células em cada estado
    healthy_count = np.count_nonzero(grid == HEALTHY)
    infected_count = np.count_nonzero(grid == INFECTED)
    immune_count = np.count_nonzero(grid == IMMUNE)
    
    # Armazena os dados para o gráfico posterior
    healthy_counts.append(healthy_count)
    infected_counts.append(infected_count)
    immune_counts.append(immune_count)
    
    # Adiciona legenda na animação
    healthy_patch = mpatches.Patch(color="red", label="Sangue (saudável)")
    infected_patch = mpatches.Patch(color="purple", label="Bactéria (infectada)")
    immune_patch = mpatches.Patch(color="lightgray", label="Imune")
    ax.legend(handles=[healthy_patch, infected_patch, immune_patch], loc='upper right')
    
    # Atualiza a grade para a próxima iteração
    grid = update_grid(grid)

ani = animation.FuncAnimation(fig, update, frames=steps, interval=300, repeat=False)
plt.show()

# Após a simulação, cria um gráfico com os dados coletados
plt.figure(figsize=(8, 6))
plt.plot(range(len(healthy_counts)), healthy_counts, label="Sangue (saudável)", color="red", marker='o')
plt.plot(range(len(infected_counts)), infected_counts, label="Bactéria (infectada)", color="purple", marker='o')
plt.plot(range(len(immune_counts)), immune_counts, label="Imune", color="lightgray", marker='o')
plt.xlabel("Iteração")
plt.ylabel("Número de Células")
plt.title("Evolução dos Estados na Simulação")
plt.legend()
plt.grid(True)
plt.show()