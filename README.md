# Sprint-3-python
Sistema em Python para simulação, registro e análise gráfica de sons em ambientes monitorados. Desenvolvido com Pandas, Matplotlib e POO.
Descritivo do Projeto
O "Visualizando o Som" é um sistema inteligente em Python que mapeia a origem (0º a 360º) e a intensidade de ruídos em ambientes monitorados, integrando-se a câmeras e HUDs táteis para direcionar o foco visual e otimizar a segurança.

Funcionalidades
* **Menu Interativo:** Navegação otimizada por estrutura moderna.
* **Cadastro de Sons:** Entrada de dados com validação e salvamento em arquivo `.csv`.
* **Simulador de Áudio:** Captura ângulos de ruídos, converte para direções cardiais e registra alertas.
* **Painel de Descobertas:** Relatórios e gráficos estatísticos semanais de intensidade e origem.
* **Configuração de Hardware:** Simulação de ajuste de retorno tátil (vibração).

Principais Evoluções (Sprint Atual)

* **Remoção:** Exclusão de listas em memória volátil e menus longos com `if/elif/else`.
* **Modificação:** Adoção de `match/case` para navegação, tratamento robusto de erros (`try/except` para `ValueError` e `FileNotFoundError`) e foco aplicado em cenários industriais/segurança.
* **Adição:** Implementação de Programação Orientada a Objetos (classe `Usuario`), persistência física de dados com `pandas` (`.csv`) e gráficos dinâmicos de barras com `matplotlib`.
