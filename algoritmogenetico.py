# coding: utf-8

# In[5]:


import random

modelo = [1,1,1,1,1,1,1,1,1,1] #Objetivo a ser alcançado
largo = 10 #Comprimento do material genético
num = 10 #O número de indivíduos que estarão na população
pressure = 3 #Quantos indivíduos são selecionados para reprodução. Necessariamente superior a 2
mutation_chance = 0.2 #A probabilidade de um indivíduo mutar

print("\n\nModelo: %s\n"%(modelo))


# In[4]:


# Cria um indivíduo
def individuo(min, max):
   return[random.randint(min, max) for i in range(largo)] 


# In[ ]:


# Cria uma população de indivíduos
def criarPopulacao():
    return [individuo(1,9) for i in range(num)]


# In[ ]:


#Calcula o Fitness, ou seja, avalia um individuo de acordo com o modelo.
def calcularFitness(individuo):
    fitness = 0
    for i in range(len(individuo)):
        if individuo[i] == modelo[i]:
            fitness += 1
  
    return fitness


# In[ ]:


"""
     Pontua todos os elementos da população (população) e mantenha o melhor
     salvando-os dentro de 'selecionados'.
     Em seguida, misture o material genético dos escolhidos para criar novos indivíduos e
     preencha a população (também mantendo uma cópia dos indivíduos selecionados sem
     modificar).
  
     Finalmente, mata os indivíduos.  
"""
def selecao_e_reproducao(populacao):
    pontuados = [ (calcularFitness(i), i) for i in populacao] #Calcula a aptidão de cada indivíduo e armazena-o em pares ordenados da forma (5, [1,2,1,1,4,1,8,9,4,1])
    pontuados = [i[1] for i in sorted(pontuados)] #Ordena pares ordenados e é deixado sozinho com a matriz de valores
    populacao = pontuados
  
  
  
    selecionados =  pontuados[(len(pontuados)-pressure):] #Esta linha seleciona os indivíduos 'n' end, onde n é dado por 'pressão'
  
  
  
    # O material genético é misturado para criar novos indivíduos
    for i in range(len(populacao)-pressure):
        ponto = random.randint(1,largo-1) #Selecione um ponto para fazer a troca
        pai = random.sample(selecionados, 2) #Dois pais são escolhidos
          
        populacao[i][:ponto] = pai[0][:ponto] # O material genético dos pais é misturado em cada novo indivíduo
        populacao[i][ponto:] = pai[1][ponto:]
  
    return populacao # A matriz 'população' agora tem uma nova população de indivíduos, que são devolvidos


# In[ ]:


"""
         Os indivíduos são mutados aleatoriamente. Sem a mutação de novos genes, eu nunca poderia
         alcancar a solução.
"""
def mutacao(populacao):
    for i in range(len(populacao)-pressure):
        if random.random() <= mutation_chance: #Cada individuo da população(menos os pais) tem uma probabilidade de mutar
            ponto = random.randint(0,largo-1) #Escolhe-se um ponto aleatório
            novo_valor = random.randint(1,9) #Gera um novo valor para essa ponto
  
            #É importante verificar se o novo valor não é igual ao valor original do ponto
            while novo_valor == populacao[i][ponto]:
                novo_valor = random.randint(1,9)
  
            #Se aplica la mutacion
            populacao[i][ponto] = novo_valor
  
    return populacao


# In[7]:


populacao = criarPopulacao()#Inicializar uma população..
print("Populacao Inicial:\n%s"%(populacao)) #Mostra populacao inicial
  
  
#Evolui a populacao
for i in range(100):
    populacao = selecao_e_reproducao(populacao)
    populacao = mutacao(populacao)
  
  
print("\nPopulacao apos 100 geracoes:\n%s"%(populacao)) #Mostra População Evoluída
print("\n\n")
