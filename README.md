# 🧩 Sistema de Controle e Qualidade de Peças – Automação Industrial

## ⚙️ Explicação do Funcionamento

O sistema foi desenvolvido em **Python** com o objetivo de simular o processo de **inspeção e controle de qualidade de peças** em uma linha de produção industrial. Ele automatiza a análise de cada peça produzida, verificando se atende aos critérios de qualidade e armazenando os resultados em listas organizadas.

As principais funcionalidades são:

- **Cadastro de novas peças:** permite inserir o ID, peso, cor e comprimento de cada peça.
- **Verificação automática da qualidade:** o sistema avalia se a peça está **aprovada** ou **reprovada** com base em critérios definidos.
- **Controle de caixas:** peças aprovadas são armazenadas em caixas com capacidade limitada (10 peças). Quando a caixa atinge esse limite, ela é “fechada” e uma nova caixa é iniciada.
- **Listagem e relatórios:** o programa permite listar todas as peças (aprovadas e reprovadas), remover peças cadastradas, consultar caixas fechadas e gerar um relatório final consolidado.

### Critérios de aprovação
Para que uma peça seja **aprovada**, ela deve atender simultaneamente a três condições:
1. Peso entre **95 g e 105 g**
2. Cor igual a **azul** ou **verde**
3. Comprimento entre **10 cm e 20 cm**

Se qualquer critério não for atendido, a peça é **reprovada**, e o sistema registra os motivos correspondentes.

---

## Como Rodar o Programa

### Pré-requisitos
- Ter o **Python** instalado no computador.
- Um editor de código (exemplo: VS Code, PyCharm) ou o terminal do sistema operacional.

### Passo a passo

1. **Baixe ou clone o projeto** para o seu computador.  
2. Abra o arquivo principal `Projeto2_autopecas.py`.  
3. Execute o código:
   ```bash
   python Projeto2_autopecas.py
   ```
4. O menu interativo será exibido no terminal.  
   Escolha uma das opções digitando o número correspondente:

   ```
   1 - Cadastrar nova peça
   2 - Listar peças aprovadas/reprovadas
   3 - Remover peça cadastrada
   4 - Listar caixas fechadas
   5 - Gerar relatório final
   0 - Sair
   ```

5. Siga as instruções na tela para inserir os dados e navegar pelas opções.

---

## Exemplos de Entradas e Saídas

### Exemplo 1 – Peça aprovada
**Entrada:**
```
ID da peça: P001
Peso da peça (g): 100
Cor da peça: azul
Comprimento da peça (cm): 15
```

**Saída:**
```
✅ Peça P001 APROVADA e armazenada.
Adicionada à caixa atual (1/10).
```

---

### Exemplo 2 – Peça reprovada
**Entrada:**
```
ID da peça: P002
Peso da peça (g): 110
Cor da peça: vermelha
Comprimento da peça (cm): 8
```

**Saída:**
```
❌ Peça P002 REPROVADA.
Motivos: Peso fora do limite, Cor inválida, Comprimento fora do limite.
```

---

### Exemplo 3 – Fechamento de caixa
Quando 10 peças são aprovadas:
```
Caixa CHEIA e FECHADA! Nova caixa iniciada.
```

---

### Exemplo 4 – Relatório Final
```
=== Relatório Final ===
Total de peças aprovadas: 17
Total de peças reprovadas: 3
Quantidade de caixas utilizadas: 2

Motivos das reprovações:
  - Peça P002: Peso fora do limite, Cor inválida, Comprimento fora do limite
  - Peça P005: Cor inválida
  - Peça P012: Comprimento fora do limite
```
