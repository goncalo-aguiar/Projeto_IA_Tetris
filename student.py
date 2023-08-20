import asyncio
import getpass
import json
import os

import websockets
from game import Game

class Agent:
    def __init__(self,n_mec):
        self.username = n_mec
        (self.l) = []
        self.iteracao = 0
        self.piece_atual= None
        self.game = None
        self.next_piece0 = None
        self.lista_acao_mais_altura = None
        self.primeira_iter = 0
        self.lista = []
        self.contador_auxiliar = 0
        self.constante_altura = 0.8
        self.constante_buracos = -3
        self.bumpiness = 0.5
        self.tetris = -1.7
        
        
    
    def tipo_de_peca(self,piece):
        if piece == None:
            return ''
        
        ar0 = piece[:1]
        ar1 = piece[1:2]
        ar2 = piece[2:3]
        ar3 = piece[3:4]
        ar0 = ar0[0]
        ar1 = ar1[0]
        ar2 = ar2[0]
        ar3 = ar3[0]
        
        if ar0 == [0,1] and ar1 == [1,1] and ar2 == [2,1] and ar3 == [3,1] :
            return 'I'
        elif ar0 == [2,1] and ar1 == [2,2] and ar2 == [3,2] and ar3 == [3,3] :
            return 'S'
        elif ar0 == [2,1] and ar1 == [3,1] and ar2 == [2,2] and ar3 == [2,3] :
            return 'J'
        elif ar0 == [1,2] and ar1 == [2,2] and ar2 == [1,3] and ar3 == [2,3] :
            return 'Square'
        elif ar0 == [2,1] and ar1 == [2,2] and ar2 == [2,3] and ar3 == [3,3] :
            return 'L'
        elif ar0 == [2,1] and ar1 == [2,2] and ar2 == [3,2] and ar3 == [2,3] :
            return 'T'
        elif ar0 == [2,1] and ar1 == [1,2] and ar2 == [2,2] and ar3 == [1,3] :
            return 'Z'
        else:
            return 'outrooooooooooooooooooooo'

    def altura_peça_mais_alta(self,game):
        max = 31
        i=0
        while i < len(game):
            aux = game[i]
            aux1 = aux[1]
            if max > aux1:
                max = aux1
            i= i+1
        return max
        
    
    def nextAction(self,state):
        
        if self.primeira_iter == 0:
            
            self.primeira_iter = self.primeira_iter +1
            return ''
        else:

            
            self.piece_atual = state['piece']
            self.game = state['game']
            next_pieces = state['next_pieces']
            self.next_piece0 = next_pieces[0]
            next_piece1 = next_pieces[1]
            next_piece2 = next_pieces[2]
            # print("------------GAME--------")
            # print(self.game)
            # print("----------------------")
            # print('\n')
            # print("------------ATUAL--------")
            # print(self.piece_atual)
            # print("----------------------")
            # print('\n')
            # print("------------P1--------")
            # print(self.next_piece0)
            # print("----------------------")
            # print('\n')
            # print("------------P2--------")
            # print(next_piece1)
            # print("----------------------")
            # print('\n')
            # print("------------P3--------")
            # print(next_piece2)
            # print("----------------------")


            
            ##############################
            
            if self.piece_atual == None or len(self.l)==0:         #sempre q a peça muda chama o search para a seguinte
                self.l = [] 
                self.piece_atual = self.next_piece0
                self.iteracao = 0
                self.lista_acao_mais_altura = []
                self.search()
                
                
            #############################
            
        return self.jogar()
            

    ############################################FUnção que preeche a self.l com a jogada#########################
    def search(self):
        lista = ['','','','','','','','','','','','','','','','','','','','','','','','','','','']
        lista2 = ['s','s','s','s','s','s','s','s']
        # print(self.tipo_de_peca(self.piece_atual))
        # print('......................................................................')
        if self.tipo_de_peca(self.piece_atual) == 'I':
            
            i=0
            lista_I = self.possiveis_I()
            while i < len(lista_I):
                self.play_I(lista_I[i])
                i =i+1
            jogada = self.escolha_melhor_jogada()
            
            (self.l) = jogada + lista2
            
            
        elif self.tipo_de_peca(self.piece_atual) == 'J':
            i=0
            lista_J = self.possiveis_J()
            while i < len(lista_J):
                self.contador_auxiliar =0
                self.play_J(lista_J[i],i)
                i =i+1
            jogada = self.escolha_melhor_jogada()
            
            (self.l) = jogada + lista2

        elif self.tipo_de_peca(self.piece_atual) == 'Square':
            # percorrer a lista de possiveis_Square e chamar a func play_Square para cada jogada possivel
            # depois meter a melhor jogada no self.l (que vem da self.lista_jogadas_mais_pontos )
            i=0
            lista_square = self.possiveis_Square()
            while i < len(lista_square):
                self.play_Square(lista_square[i])
                i =i+1
            jogada = self.escolha_melhor_jogada()
           
            (self.l) = jogada + lista2
            
            
            
        elif self.tipo_de_peca(self.piece_atual) == 'S':
            
            i=0
            lista_S = self.possiveis_S()
            while i < len(lista_S):
                self.play_S(lista_S[i])
                i =i+1
            jogada = self.escolha_melhor_jogada()
           
            (self.l) = jogada + lista2
            
            
        elif self.tipo_de_peca(self.piece_atual) == 'L':
            i=0
            lista_L = self.possiveis_L()
            while i < len(lista_L):
                self.contador_auxiliar =0
                self.play_L(lista_L[i],i)
                i =i+1
            jogada = self.escolha_melhor_jogada()
           
            (self.l) = jogada +lista2

        elif self.tipo_de_peca(self.piece_atual) == 'Z':
            i=0
            lista_Z = self.possiveis_Z()
            while i < len(lista_Z):
                self.play_Z(lista_Z[i])
                i =i+1
            jogada = self.escolha_melhor_jogada()
            
            (self.l) = jogada + lista2
            
            
              
        elif self.tipo_de_peca(self.piece_atual) == 'T':
            i=0
            lista_T = self.possiveis_T()
            while i < len(lista_T):
                self.contador_auxiliar =0
                self.play_T(lista_T[i],i)
                i =i+1
            jogada = self.escolha_melhor_jogada()
           
            (self.l) = jogada + lista2
            

        #########################################################################################
            
            
        
        
    ##########Primeira peça(falta saber o que vamos fazer) e jogar as restantes com base nas iteraçoes
    def jogar(self): 
        lista = ['','','','','','','','','','','','','','','','','','','','','','','','','','','']
            
        while(self.iteracao< len(self.l)):
            x = self.l[self.iteracao]
            self.iteracao = self.iteracao+1
            return x
        

            
        
    ########################################################################
    def ler_superficie_game(self):
        max = [30,30,30,30,30,30,30,30,30]
        i=0
        j=0
        while i < len(self.game):
            aux = self.game[i]
            x = aux[0]
            y = aux[1]
            if y < max[x]:
                for j in range(1,9):
                    if(x==j) and y < max[j]:
                        max[j] = y
            i= i+1
        
        grid = max
        max = [30,30,30,30,30,30,30,30,30]
        return grid
    def ler_superficie_game1(self,GameExample):
        max = [30,30,30,30,30,30,30,30,30]
        i=0
        j=0
        while i < len(GameExample):
            aux = GameExample[i]
            x = aux[0]
            y = aux[1]
            if y < max[x]:
                for j in range(1,9):
                    if(x==j) and y < max[j]:
                        max[j] = y
            i= i+1
        
        grid = max
        max = [30,30,30,30,30,30,30,30,30]
        return grid

    ###############################I-shapes#########################################
    
    def possiveis_I(self):
        lista = [['d','d','d'],['a'],[''],['d','d'],['d'],['w','d','d','d','d'],
                  ['w','d','d','d'],['w','a','a','a'],['w','a','a'],['w','d','d'],['w','d'],['w'],['w','a']]
        return lista
    
    def play_I(self,açao):
        estado_inicial = [[2, 2], [3, 2], [4, 2], [5, 2]]
        estado_final_w = [[4, 3], [4, 2], [4, 1], [4, 0]]
        i=0
        estado_final = estado_inicial
        aconteceu_w = False
        
        while i < len(açao):
            if açao[i] == 'd':
                j =0
                while j < len(estado_inicial):
                    estado_final[j]= [estado_final[j][0] + 1,estado_final[j][1]]
                    j = j+1
            elif açao[i] == 'a':
                j =0
                while j < len(estado_inicial):
                    estado_final[j]= [estado_final[j][0] -1,estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'w':
                j =0
                estado_final[0] = estado_final_w[0]
                estado_final[1] = estado_final_w[1]
                estado_final[2] = estado_final_w[2]
                estado_final[3] = estado_final_w[3]
                aconteceu_w = True
            i=i+1
        

        if aconteceu_w == False:

            superficie = self.ler_superficie_game()
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0]
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0]
            temp = [superficie[x0]] + [superficie[x1]] + [superficie[x2]] + [superficie[x3]]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1
            
            i = 0
            while i<len(estado_final):
                estado_final[i]= [estado_final[i][0],min - 1]
                i=i+1
            proxima_ronda_game = (self.game) + (estado_final)
            
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final) 

        else:
            superficie = self.ler_superficie_game()
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0]
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0]
            y_superficie0 = superficie[x0]

            i = 0
            while i<len(estado_final):
                estado_final[i]= [estado_final[i][0],y_superficie0 - 1 - i ]
                i=i+1
            proxima_ronda_game = (self.game) + (estado_final)
            
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final) 

        
        # adiciona jogada e pontos respetivos à lista de jogadas possiveis mais pontos
        
        

    #################################################################################
    ################################SQUARES###################################
    def possiveis_Square(self):   
        lista = [['a','a'],['a'],[''],['d'],['d','d'],['d','d','d'],['d','d','d','d']]
        return lista
    
    def play_Square(self,açao):
        estado_inicial = [[3, 3], [4, 3], [3, 4], [4, 4]]
        i=0
        estado_final = estado_inicial
        while i < len(açao):
            if açao[i] == 'd':
                j =0
                while j < len(estado_inicial):
                    estado_final[j]= [estado_final[j][0] +1,estado_final[j][1]]
                    j = j+1
            elif açao[i] == 'a':
                j =0
                while j < len(estado_inicial):
                    estado_final[j]= [estado_final[j][0] -1,estado_final[j][1]]
                    j = j+1
            i=i+1
        
        superficie = self.ler_superficie_game()                       
        
        x0 = estado_final[0][0] 
        x1 = estado_final[1][0]
        x2 = estado_final[2][0] 
        x3 = estado_final[3][0]

        if superficie[x0] < superficie[x1]:
            j=0
            while j < 2:
                estado_final[j]= [estado_final[j][0],superficie[x0] -2]
                j = j+1

            while j < 4:
                estado_final[j]= [estado_final[j][0],superficie[x0] - 1]
                j = j+1

        if superficie[x0] >= superficie[x1]:
            j=0
            while j < 2:
                estado_final[j]= [estado_final[j][0],superficie[x1] -2]
                j = j+1
            while j < 4:
                estado_final[j]= [estado_final[j][0],superficie[x1] - 1]
                j = j+1
       
        proxima_ronda_game = (self.game) + (estado_final)
        self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final) 
        
        
        
        ##########################################################
    ################################################################################################################################

    
    def possiveis_S(self):
        lista = [['a','a','a'],['a','a'],['a'],[''],['d'],['d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],['w','d','d','d'],['d','d','d']]
        return lista
    
    def play_S(self,açao):
        estado_inicial = [[4, 2], [4, 3], [5, 3], [5, 4]]  
        estado_final_w = [[5,2],[4,3],[4,2],[3,1]]

        i=0
        estado_final = estado_inicial
        aconteceu_w = False
        
        while i < len(açao):
            if açao[i] == 'd':
                j =0
                while j < len(estado_final):
                
                    estado_final[j]= [estado_final[j][0] + 1,estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'a':
                j =0
                while j < len(estado_final):
                    
                    estado_final[j]= [estado_final[j][0] -1,estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'w':
                
                j =0
                estado_final[3] = estado_final_w[3]
                estado_final[2] = estado_final_w[2]
                estado_final[1] = estado_final_w[1]
                estado_final[0] = estado_final_w[0]
               
                aconteceu_w = True
                

            i=i+1
        
        
        if aconteceu_w == False:
           
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            
            
            if superficie[x1] < superficie[x3]:
                estado_final[0] = [estado_final[0][0],superficie[x1] - 2]
                estado_final[1] = [estado_final[1][0],superficie[x1] - 1]
                estado_final[2] = [estado_final[2][0],superficie[x1] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x1]]
               
            else:
                estado_final[0] = [estado_final[0][0],superficie[x3] - 3]
                estado_final[1] = [estado_final[1][0],superficie[x3] - 2]
                estado_final[2] = [estado_final[2][0],superficie[x3] - 2]
                estado_final[3] = [estado_final[3][0],superficie[x3] - 1]

            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final) 
        else:
            
            superficie = self.ler_superficie_game()
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0]
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            
            
            
            if(superficie[x3] <= superficie[x2]) and (superficie[x3] <= superficie[x0]):
                estado_final[0] = [estado_final[0][0],superficie[x3] - 2]
                estado_final[1] = [estado_final[1][0],superficie[x3] - 2]
                estado_final[2] = [estado_final[2][0],superficie[x3] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x3] - 1]
            
            elif (superficie[x2] <= superficie[x3]) and (superficie[x2] <= superficie[x0]):
                estado_final[0] = [estado_final[0][0],superficie[x2] - 2]
                estado_final[1] = [estado_final[1][0],superficie[x2] - 2]
                estado_final[2] = [estado_final[2][0],superficie[x2] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x2] - 1]
                
            elif (superficie[x0] < superficie[x3]) and (superficie[x0] < superficie[x2]):
                estado_final[0] = [estado_final[0][0],superficie[x0] - 1]
                estado_final[1] = [estado_final[1][0],superficie[x0] - 1]
                estado_final[2] = [estado_final[2][0],superficie[x0]]
                estado_final[3] = [estado_final[3][0],superficie[x0]]
                
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final)

            
            
    def possiveis_Z(self):
        lista = [['a','a'],['a'],[''],['d'],['d','d'],['d','d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],['w','d','d','d'],['d','d','d','d']]
        return lista
    
    def play_Z(self,açao):
        estado_inicial = [[4, 2], [3, 3], [4, 3], [3, 4]]  
        estado_final_w = [[5, 3], [4, 2], [4, 3], [3, 2]]  
        i=0
        estado_final = estado_inicial
        aconteceu_w = False
        while i < len(açao):
            if açao[i] == 'd':
                j =0
                while j < len(estado_final):
                    estado_final[j]= [estado_final[j][0] + 1,estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'a':
                j =0
                while j < len(estado_final):
                    estado_final[j]= [estado_final[j][0] -1,estado_final[j][1]]
                    j = j+1
            
            elif açao[i] == 'w':
                estado_final[0] = estado_final_w[0]
                estado_final[1] = estado_final_w[1]
                estado_final[2] = estado_final_w[2]
                estado_final[3] = estado_final_w[3]
                aconteceu_w = True
                
            i=i+1
        
        if aconteceu_w == False:
           
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 

            if superficie[x2] >= superficie[x3]:
                estado_final[0] = [estado_final[0][0],superficie[x3] - 3]
                estado_final[1] = [estado_final[1][0],superficie[x3] - 2]
                estado_final[2] = [estado_final[2][0],superficie[x3] - 2]
                estado_final[3] = [estado_final[3][0],superficie[x3] - 1] 
            else:
                estado_final[0] = [estado_final[0][0],superficie[x2] - 2]
                estado_final[1] = [estado_final[1][0],superficie[x2] - 1]
                estado_final[2] = [estado_final[2][0],superficie[x2] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x2]]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final) 
        else:
            
            superficie = self.ler_superficie_game()
            x3 = estado_final[3][0] 
            x1 = estado_final[1][0]
            x0 = estado_final[0][0] 
            x2 = estado_final[2][0] 
            
            if(superficie[x0] <= superficie[x2]) and (superficie[x0] <= superficie[x3]):
                estado_final[0] = [estado_final[0][0],superficie[x0] - 1]
                estado_final[1] = [estado_final[1][0],superficie[x0]-2]
                estado_final[2] = [estado_final[2][0],superficie[x0]-1]
                estado_final[3] = [estado_final[3][0],superficie[x0]-2]
            
            elif (superficie[x2] <= superficie[x0]) and (superficie[x2] <= superficie[x3]):
                estado_final[0] = [estado_final[0][0],superficie[x2]-1]
                estado_final[1] = [estado_final[1][0],superficie[x2]-2]
                estado_final[2] = [estado_final[2][0],superficie[x2]-1]
                estado_final[3] = [estado_final[3][0],superficie[x2]-2]
            else:
                estado_final[0] = [estado_final[0][0],superficie[x3] ]
                estado_final[1] = [estado_final[1][0],superficie[x3] -1]
                estado_final[2] = [estado_final[2][0],superficie[x3]]
                estado_final[3] = [estado_final[3][0],superficie[x3] -1]
                
           
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final) 

    def possiveis_L(self):
        lista =  [['a','a','a'],['a','a'],['a'],[''],['d'],['d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],
                    ['w','w','a','a'],['w','w','a'],['w','w'],['w','w','d','d','d'],['w','w','d','d'],['w','w','d'],
                    ['w','w','w'],['w','w','w','a','a'],['w','w','w','a'],['w','w','w','d','d','d'],['w','w','w','d','d'],['w','w','w','d'],['d','d','d'],
                    ['w','d','d','d'],['w','w','d','d','d','d']]
                    
        return lista

    def play_L(self,açao,num):
        estado_inicial = [[4, 2], [4, 3], [4, 4], [5, 4]] 
        estado_final_1w= [[5, 3], [4, 3], [3, 3], [3, 4]] 
        estado_final_2w= [[4, 4], [4, 3], [4, 2], [3, 2]] 
        estado_final_3w= [[3, 3], [4, 3], [5, 3], [5, 2]] 

        i=0
        estado_final = estado_inicial
        aconteceu_w = 0
    
        
        while i < len(açao):
            
            if açao[i] == 'd':
                j =0
                while j < len(estado_final):
                    estado_final[j]= [estado_final[j][0] + 1,estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'a':
                j =0
                while j < len(estado_final):
                    estado_final[j]= [estado_final[j][0] -1,estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'w':
                
                if self.contador_auxiliar == 0:
                    
                    estado_final[3] = estado_final_1w[3]
                    estado_final[2] = estado_final_1w[2]
                    estado_final[1] = estado_final_1w[1]
                    estado_final[0] = estado_final_1w[0]
                    
                elif  self.contador_auxiliar ==1:

                    estado_final[0] = estado_final_2w[0]
                    estado_final[1] = estado_final_2w[1]
                    estado_final[2] = estado_final_2w[2]
                    estado_final[3] = estado_final_2w[3] 
                elif   self.contador_auxiliar ==2:
                    estado_final[0] = estado_final_3w[0]
                    estado_final[1] = estado_final_3w[1]
                    estado_final[2] = estado_final_3w[2]
                    estado_final[3] = estado_final_3w[3]
                    

                self.contador_auxiliar = self.contador_auxiliar +1
                aconteceu_w = aconteceu_w +1
            
            i=i+1
       
        if aconteceu_w == 0:
           
            superficie = self.ler_superficie_game()
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            temp = [superficie[x2]] + [superficie[x3]]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1
            
            estado_final[0] = [estado_final[0][0],min-3]
            estado_final[1] = [estado_final[1][0],min - 2]
            estado_final[2] = [estado_final[2][0],min - 1]
            estado_final[3] = [estado_final[3][0],min - 1]
            
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final) 
        elif aconteceu_w == 1:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
        
            if superficie[x0] <= superficie[x1] and superficie[x0] < superficie[x3]:
                estado_final[0] = [estado_final[0][0],superficie[x0] - 1]
                estado_final[1] = [estado_final[1][0],superficie[x0] - 1]
                estado_final[2] = [estado_final[2][0],superficie[x0] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x0]]
               
            elif superficie[x1] <= superficie[x0] and superficie[x1] <superficie[x3]:
                
                estado_final[0] = [estado_final[0][0],superficie[x1] - 1]
                estado_final[1] = [estado_final[1][0],superficie[x1] - 1]
                estado_final[2] = [estado_final[2][0],superficie[x1] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x1]]
            else:
                estado_final[0] = [estado_final[0][0],superficie[x3] - 2]
                estado_final[1] = [estado_final[1][0],superficie[x3] - 2]
                estado_final[2] = [estado_final[2][0],superficie[x3] -2]
                estado_final[3] = [estado_final[3][0],superficie[x3]-1]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final)
        
        elif aconteceu_w == 2:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            
            
            if superficie[x0] <= superficie[x3] + 1:
                estado_final[0] = [estado_final[0][0],superficie[x0] - 1]
                estado_final[1] = [estado_final[1][0],superficie[x0] - 2]
                estado_final[2] = [estado_final[2][0], superficie[x0] - 3]
                estado_final[3] = [estado_final[3][0],superficie[x0] - 3]
            else:
                
                estado_final[0] = [estado_final[0][0],superficie[x3] + 1]
                estado_final[1] = [estado_final[1][0],superficie[x3]]
                estado_final[2] = [estado_final[2][0],superficie[x3] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x3] - 1]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final)
        elif aconteceu_w == 3:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 

            temp = [superficie[x0]] + [superficie[x1]] + [superficie[x2]]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1

            estado_final[0] = [estado_final[0][0],min - 1]
            estado_final[1] = [estado_final[1][0],min - 1]
            estado_final[2] = [estado_final[2][0],min - 1]
            estado_final[3] = [estado_final[3][0],min - 2]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final)


    def possiveis_J(self):
        lista = [['a','a','a'],['a','a'],['a'],[''],['d'],['d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],
                ['w','w','a','a'],['w','w','a'],['w','w'],['w','w','d'],['w','w','d','d']
                ,['w','w','w','a','a'],['w','w','w','a'],['w','w','w'],['w','w','w','d'],['w','w','w','d','d'],['w','w','w','d','d','d'],['d','d','d'],
                ['w','d','d','d'],['w','w','d','d','d','d']]

        return lista

    def play_J(self,açao,num):
        estado_inicial = [[4, 2], [5, 2], [4, 3], [4, 4]] 
        estado_final_1w = [[5, 3], [5, 4], [4, 3], [3, 3]] 
        estado_final_2w = [[4, 4], [3, 4], [4, 3], [4, 2]] 
        estado_final_3w = [[3, 3], [3, 2], [4, 3], [5, 3]] 
        i=0
        estado_final = estado_inicial
        aconteceu_w = 0
    
        
        while i < len(açao):
            
            if açao[i] == 'd':
                j =0
                while j < len(estado_final):
                    estado_final[j]= [estado_final[j][0] + 1,estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'a':
                j =0
                while j < len(estado_final):
                    estado_final[j]= [estado_final[j][0] -1,estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'w':
                
                if self.contador_auxiliar == 0:
                    estado_final[3] = estado_final_1w[3]
                    estado_final[2] = estado_final_1w[2]
                    estado_final[1] = estado_final_1w[1]
                    estado_final[0] = estado_final_1w[0]
                    
                elif  self.contador_auxiliar ==1:
                    estado_final[0] = estado_final_2w[0]
                    estado_final[1] = estado_final_2w[1]
                    estado_final[2] = estado_final_2w[2]
                    estado_final[3] = estado_final_2w[3]
                     
                elif   self.contador_auxiliar ==2:
                    
                    estado_final[0] = estado_final_3w[0]
                    estado_final[1] = estado_final_3w[1]
                    estado_final[2] = estado_final_3w[2]
                    estado_final[3] = estado_final_3w[3]
                    

                self.contador_auxiliar = self.contador_auxiliar +1
                aconteceu_w = aconteceu_w +1
            
            i=i+1
       
        if aconteceu_w == 0:
           
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            if superficie[x3] <= superficie[x1] + 1:
                estado_final[0] = [estado_final[0][0],superficie[x3] - 3]
                estado_final[1] = [estado_final[1][0],superficie[x3] - 3]
                estado_final[2] = [estado_final[2][0],superficie[x3] - 2]
                estado_final[3] = [estado_final[3][0],superficie[x3] - 1]
            else:
                estado_final[0] = [estado_final[0][0],superficie[x1] - 1]
                estado_final[1] = [estado_final[1][0],superficie[x1] - 1]
                estado_final[2] = [estado_final[2][0],superficie[x1]]
                estado_final[3] = [estado_final[3][0],superficie[x1] + 1]
            
            
            proxima_ronda_game = (self.game) + (estado_final) 
             
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final) 
        elif aconteceu_w == 1:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            if superficie[x3] <= superficie[x2] and superficie[x3] < superficie[x1]:
                
                estado_final[0] = [estado_final[0][0], superficie[x3] - 1]
                estado_final[1] = [ estado_final[1][0],superficie[x3]]
                estado_final[2] = [ estado_final[2][0],superficie[x3] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x3] - 1]
               
            elif superficie[x2] <= superficie[x3] and superficie[x2] < superficie[x1]:
                
                estado_final[0] = [estado_final[0][0],superficie[x2] - 1]
                estado_final[1] = [estado_final[1][0],superficie[x2]]
                estado_final[2] = [estado_final[2][0],superficie[x2] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x2] - 1]
            else:
                
                estado_final[0] = [estado_final[0][0], superficie[x1] - 2]
                estado_final[1] = [estado_final[1][0],superficie[x1] - 1]
                estado_final[2] = [estado_final[2][0],superficie[x1] - 2]
                estado_final[3] = [estado_final[3][0],superficie[x1] - 2]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final)
        
        elif aconteceu_w == 2:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            
            y_superficie1 = superficie[x1]
            y_superficie0 = superficie[x0]
            
            temp = [superficie[x0]] + [superficie[x1]]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1

           
            estado_final[0] = [estado_final[0][0],min - 1]
            estado_final[1] = [estado_final[1][0],min - 1]
            estado_final[2] = [estado_final[2][0],min - 2]
            estado_final[3] = [estado_final[3][0],min - 3]

            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final)
        elif aconteceu_w == 3:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 

            temp = [ superficie[x0]] + [superficie[x2]] + [superficie[x3]]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1

            
            estado_final[0] = [estado_final[0][0],min - 1]
            estado_final[1] = [estado_final[1][0],min - 2]
            estado_final[2] = [estado_final[2][0],min - 1]
            estado_final[3] = [estado_final[3][0],min - 1]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final)
    
    def possiveis_T(self):
        lista = [['a','a','a'],['a','a'],['a'],[''],['d'],['d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],
                ['w','w','a','a'],['w','w','a'],['w','w'],['w','w','d'],['w','w','d','d'],['w','w','d','d','d'],
                ['w','w','w','a','a'],['w','w','w','a'],['w','w','w'],['w','w','w','d'],['w','w','w','d','d'],['w','w','w','d','d','d'],['d','d','d'],
                ['w','d','d','d'],['w','w','d','d','d','d']]
        return lista
    
    def play_T(self,açao,num):
        estado_inicial = [[4, 2], [4, 3], [5, 3], [4, 4]] 
        estado_final_1w= [[5, 3], [4, 3], [4, 4], [3, 3]] 
        estado_final_2w= [[4, 4], [4, 3], [3, 3], [4, 2]] 
        estado_final_3w= [[3, 3], [4, 3], [4, 2], [5, 3]] 
 
        
        i=0
        estado_final = estado_inicial
        aconteceu_w = 0
    
        
        while i < len(açao):
            
            if açao[i] == 'd':
                j =0
                while j < len(estado_final):
                    aux = estado_final[j]
                    aux[0]= aux[0] + 1
                    estado_final[j]= [aux[0],estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'a':
                j =0
                while j < len(estado_final):
                    aux = estado_final[j]
                    aux[0]= aux[0] -1
                    estado_final[j]= [aux[0],estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'w':
                if self.contador_auxiliar == 0:
                    estado_final[0] = estado_final_1w[0]
                    estado_final[1] = estado_final_1w[1]
                    estado_final[2] = estado_final_1w[2]
                    estado_final[3] = estado_final_1w[3]
                    
                elif  self.contador_auxiliar ==1:
                    estado_final[0] = estado_final_2w[0]
                    estado_final[1] = estado_final_2w[1]
                    estado_final[2] = estado_final_2w[2]
                    estado_final[3] = estado_final_2w[3]
                    
                elif   self.contador_auxiliar ==2:
                    estado_final[0] = estado_final_3w[0]
                    estado_final[1] = estado_final_3w[1]
                    estado_final[2] = estado_final_3w[2]
                    estado_final[3] = estado_final_3w[3]
                    
                self.contador_auxiliar = self.contador_auxiliar +1
                aconteceu_w = aconteceu_w +1
            
            i=i+1
       
        if aconteceu_w == 0:
           
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 

            if superficie[x3] <= superficie[x2]:
                estado_final[0] = [estado_final[0][0],superficie[x3] - 3]
                estado_final[1] = [estado_final[1][0],superficie[x3] - 2]
                estado_final[2] = [estado_final[2][0],superficie[x3] - 2]
                estado_final[3] = [estado_final[3][0],superficie[x3] - 1]
               
            else:
                estado_final[0] = [estado_final[0][0],superficie[x2] - 2]
                estado_final[1] = [estado_final[1][0],superficie[x2] - 1]
                estado_final[2] = [estado_final[2][0],superficie[x2] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x2]]

            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final) 
        elif aconteceu_w == 1:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            
            if superficie[x0] <= superficie[x3] and superficie[x0] < superficie[x2]:
                estado_final[0] = [estado_final[0][0],superficie[x0] - 1]
                estado_final[1] = [estado_final[1][0],superficie[x0] - 1]
                estado_final[2] = [estado_final[2][0],superficie[x0]]
                estado_final[3] = [estado_final[3][0],superficie[x0] - 1]
               
            elif superficie[x3] <= superficie[x0] and superficie[x3] < superficie[x2]:
                estado_final[0] = [estado_final[0][0],superficie[x3] - 1]
                estado_final[1] = [estado_final[1][0],superficie[x3] - 1]
                estado_final[2] = [estado_final[2][0],superficie[x3]]
                estado_final[3] = [estado_final[3][0],superficie[x3] - 1]

            else:
                estado_final[0] = [estado_final[0][0],superficie[x2] - 2]
                estado_final[1] = [estado_final[1][0],superficie[x2] - 2]
                estado_final[2] = [estado_final[2][0],superficie[x2] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x2] - 2]


            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final)
        
        elif aconteceu_w == 2:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            
            if superficie[x0] <= superficie[x2] :
                estado_final[0] = [estado_final[0][0],superficie[x0] - 1]
                estado_final[1] = [estado_final[1][0],superficie[x0] - 2]
                estado_final[2] = [estado_final[2][0],superficie[x0] - 2]
                estado_final[3] = [estado_final[3][0],superficie[x0] - 3]

            else:
                estado_final[0] = [estado_final[0][0],superficie[x2]]
                estado_final[1] = [estado_final[1][0],superficie[x2] - 1]
                estado_final[2] = [estado_final[2][0],superficie[x2] - 1]
                estado_final[3] = [estado_final[3][0],superficie[x2] - 2]

            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final)
        elif aconteceu_w == 3:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            
            temp = [superficie[x0]] + [superficie[x1]] + [superficie[x3]]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1

            estado_final[0] = [estado_final[0][0],min - 1]
            estado_final[1] = [estado_final[1][0],min - 1]
            estado_final[2] = [estado_final[2][0],min - 2]
            estado_final[3] = [estado_final[3][0],min - 1]
                   
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1,x2,x3,estado_final)
        
    
    def escolha_melhor_jogada(self):   
        i=1
        melhor_jogada = ['',1000]
        
        while i< len(self.lista_acao_mais_altura):
           
            if self.lista_acao_mais_altura[i] < melhor_jogada[1]:
                melhor_jogada[0]= self.lista_acao_mais_altura[i-1]
                melhor_jogada[1]= self.lista_acao_mais_altura[i]
            i = i+2
        
        
        return melhor_jogada[0]

    def preencher_lista_alturas(self,açao,proxima_ronda_game,x0,x1,x2,x3,estado_final):
        aux0 = self.ler_superficie_game1(proxima_ronda_game)

        

        ####buracoss
        aux1 = self.ler_superficie_game()
        self.aux0=aux0
        self.aux1 = aux1
        buracos = sum(aux0)-sum(aux1)
        
       
       
       
        ####bumpinesss
        auxiliar = aux0[1:]
        i=0
        bumpiness = 0
        while i < len(auxiliar)-1:
            bumpiness = bumpiness + abs(auxiliar[i] - auxiliar[i+1])

            i=i+1
       
        
        
        
        ###Pontos###
        aux2 = self.ler_superficie_game1(proxima_ronda_game)
        y0 = estado_final[0][1]
        y1 = estado_final[1][1]
        y2 = estado_final[2][1]
        y3 = estado_final[3][1]
        pontos = 0
        
        soma = self.linhas_feitas(proxima_ronda_game,y0,y1,y2,y3,x0,x1,x2,x3)
        
        if soma==36:
            pontos = 25
            
            # print("44444444444444444444444444444444444444444444444444444444444")
        elif soma == 27:
            
            # print('33333333333333333333333333333333333333333333333333333333333333')
            pontos = 16
        elif soma == 18:
            
            # print('22222222222222222222222222222222222222222222222222222222')
            pontos = 9
        elif soma == 9:
            
            # print('111111111111111111111111111111111111111111111111111111111111111111')
            pontos = 5
        
       
       
       
        
        total = self.constante_altura * (30 -min(y0,y1,y2,y3)) + self.constante_buracos * buracos + self.bumpiness * bumpiness + self.tetris * pontos
        # total = self.constante_altura * (30 -min(y0,y1,y2,y3))
        self.lista_acao_mais_altura = self.lista_acao_mais_altura + [açao] + [total]
             
    
    def linhas_feitas(self,proxima_ronda_game,y0,y1,y2,y3,x0,x1,x2,x3):
       
        grid = [[1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0]]
        i=0
        while i < len(proxima_ronda_game):
            
            grid[proxima_ronda_game[i][1]][proxima_ronda_game[i][0]] = 1
            i=i+1
        grid[y0][x0]=1
        grid[y1][x1]=1
        grid[y2][x2]=1
        grid[y3][x3]=1
        auxiliar = [y0,y1,y2,y3]
        auxiliar = set(auxiliar)
        soma =0
        
        for x in auxiliar:
            if sum(grid[x][:]) ==9 :
                soma = soma + sum(grid[x][:])
    
        return soma
        
            
    



async def agent_loop(server_address="localhost:8000", agent_name="student"):
    async with websockets.connect(f"ws://{server_address}/player") as websocket:

        # Receive information about static game properties
        await websocket.send(json.dumps({"cmd": "join", "name": agent_name}))



        agente = Agent("98266")
        while True:
            try:
                atual = Game()
                while True:
                    state = json.loads(
                        await websocket.recv()  
                    )  # receive game update, this must be called timely or your game will get out of sync with the server
                    
                    key = agente.nextAction(state)
                    

                
                
                    
                        

                    await websocket.send(
                        json.dumps({"cmd": "key", "key": key})
                    )  # send key command to server - you must implement this send in the AI agent
                    break
            except websockets.exceptions.ConnectionClosedOK:
                print("Server has cleanly disconnected us")
                return
# DO NOT CHANGE THE LINES BELLOW
# You can change the default values using the command line, example:
# $ NAME='arrumador' python3 client.py
loop = asyncio.get_event_loop()
SERVER = os.environ.get("SERVER", "localhost")
PORT = os.environ.get("PORT", "8000")
NAME = os.environ.get("NAME", getpass.getuser())
loop.run_until_complete(agent_loop(f"{SERVER}:{PORT}", NAME))
        
            
    
