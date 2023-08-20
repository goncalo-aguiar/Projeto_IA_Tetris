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
        self.contador_auxiliar = 0
        
        
    
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
        # print(game)
        while i < len(game):
            aux = game[i]
            aux1 = aux[1]
            if max > aux1:
                max = aux1
            i= i+1
        return max
        
    
    def nextAction(self,state):
        
        if self.primeira_iter == 0:
            
            # self.piece_atual = state['piece']
            # self.game = state['grid']
            # next_pieces = state['next_pieces']
            # self.next_piece0 = next_pieces[0]
            # next_piece1 = next_pieces[1]
            # next_piece2 = next_pieces[2]
            # ##############################
            # if self.piece_atual == None:         #sempre q a peça muda chama o search para a seguinte
            #     self.l = [] 
            #     self.piece_atual = self.next_piece0
            #     self.iteracao = 0
            #     self.lista_acao_mais_altura = []
            #     self.search()
                
            # # #############################
            self.primeira_iter = self.primeira_iter +1
            # return self.jogar()
        else:

            
            self.piece_atual = state['piece']
            self.game = state['game']
            next_pieces = state['next_pieces']
            self.next_piece0 = next_pieces[0]
            next_piece1 = next_pieces[1]
            next_piece2 = next_pieces[2]
            ##############################
            if self.piece_atual == None:         #sempre q a peça muda chama o search para a seguinte
                self.l = [] 
                self.piece_atual = self.next_piece0
                self.iteracao = 0
                self.lista_acao_mais_altura = []
                self.search()
                
            #############################
            
            return 'w' # self.l é a lista que mete a peça a mexer(ou seja é passado para esta lista a jogada com melhor pontuação)
            

    ############################################FUnção que preeche a self.l com a jogada#########################
    def search(self):
        lista = ['','','','','','','','','','','','','','','','','','','','','','','','','','','']
        lista2 = ['s','s','s','s','s','s','s','s']
        print(self.tipo_de_peca(self.piece_atual))
        if self.tipo_de_peca(self.piece_atual) == 'I':
            
            
            # i=0
            # lista_I = self.possiveis_I()
            # while i < len(lista_I):
            #     self.play_I(lista_I[i])
            #     i =i+1
            # jogada = self.escolha_melhor_jogada()
            
            # (self.l) = jogada + lista2
            (self.l) = 'a'
            
        elif self.tipo_de_peca(self.piece_atual) == 'J':
            # i=0
            # lista_J = self.possiveis_J()
            # while i < len(lista_J):
            #     self.contador_auxiliar =0
            #     self.play_J(lista_J[i],i)
            #     i =i+1
            # jogada = self.escolha_melhor_jogada()
            
            # (self.l) = jogada + lista2
            (self.l) = 'a'
        elif self.tipo_de_peca(self.piece_atual) == 'Square':
            # percorrer a lista de possiveis_Square e chamar a func play_Square para cada jogada possivel
            # depois meter a melhor jogada no self.l (que vem da self.lista_jogadas_mais_pontos )
            # i=0
            # lista_square = self.possiveis_Square()
            # while i < len(lista_square):
            #     self.play_Square(lista_square[i])
            #     i =i+1
            # jogada = self.escolha_melhor_jogada()
            
            # (self.l) = jogada + lista2 
            (self.l) = 'a'
            
            
        elif self.tipo_de_peca(self.piece_atual) == 'S':
            
            # i=0
            # lista_S = self.possiveis_S()
            # while i < len(lista_S):
            #     self.play_S(lista_S[i])
            #     i =i+1
            # jogada = self.escolha_melhor_jogada()
            
            # (self.l) = jogada + lista2
            (self.l) = 'a'
            
        elif self.tipo_de_peca(self.piece_atual) == 'L':
            # i=0
            # lista_L = self.possiveis_L()
            # while i < len(lista_L):
            #     self.contador_auxiliar =0
            #     self.play_L(lista_L[i],i)
            #     i =i+1
            # jogada = self.escolha_melhor_jogada()
            
            # (self.l) = jogada + lista2
            (self.l) = 'a'

        elif self.tipo_de_peca(self.piece_atual) == 'Z':
            # i=0
            # lista_Z = self.possiveis_Z()
            # while i < len(lista_Z):
            #     self.play_Z(lista_Z[i])
            #     i =i+1
            # jogada = self.escolha_melhor_jogada()
            
            # (self.l) = [''] + jogada + lista2
            (self.l) = 'a'
              
        elif self.tipo_de_peca(self.piece_atual) == 'T':
            # i=0
            # lista_T = self.possiveis_T()
            # while i < len(lista_T):
            #     self.contador_auxiliar =0
            #     self.play_T(lista_T[i],i)
            #     i =i+1
            # jogada = self.escolha_melhor_jogada()
            
            # (self.l) = jogada + lista2
            (self.l) = 'a'

        #########################################################################################
            
            
        
        
    ##########Primeira peça(falta saber o que vamos fazer) e jogar as restantes com base nas iteraçoes
    def jogar(self): 
        lista = ['','','','','','','','','','','','','','','','','','','','','','','','','','','']
        
        if len(self.l) == 0:
            (self.l).append('a')
            (self.l).append('a')
            (self.l).append(lista)
       
        aux = (self.l)[self.iteracao]
        
        
        if (self.iteracao >= len(self.l) -1):
            return (self.l)[len(self.l)-1]
        self.iteracao = self.iteracao +1

            
        return aux
    ########################################################################
    def ler_superficie_game(self):
        max = [30,30,30,30,30,30,30,30,30]
        i=0
        j=0
        while i < len(self.game):
            aux = self.game[i]
            x = aux[0]
            y = aux[1]
            print("olaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            print(x)
            print(y)
            
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
           
            print(x)
            print(y)
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
        lista = [['a'],[''],['d','d','d'],['d','d'],['d'],['w','d','d','d','d'],
                  ['w','d','d','d'],['w','a','a','a'],['w','a','a'],['w','d','d'],['w','d'],['w'],['w','a']]
        return lista
    ###########################ESTA MAL ALGURES
    def play_I(self,açao):
        estado_inicial = [[2, 2], [3, 2], [4, 2], [5, 2]]
        i=0
        estado_final = estado_inicial
        aconteceu_w = False
        
        while i < len(açao):
            if açao[i] == 'd':
                j =0
                while j < len(estado_inicial):
                    aux = estado_final[j]
                    aux[0]= aux[0] + 1

                    estado_final[j]= [aux[0],estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'a':
                j =0
                while j < len(estado_inicial):
                    aux = estado_final[j]
                    aux[0]= aux[0] -1
                    estado_final[j]= [aux[0],estado_final[j][1]]
                    j = j+1

            elif açao[i] == 'w':
                j =0
                aux0 = estado_final[0]
                aux1 = estado_final[1]
                aux2 = estado_final[2]
                aux3 = estado_final[3]
                    
                aux0 = [aux0[0]+2,aux0[1]+1]
                aux1 = [aux1[0]+1,aux1[1]]
                aux2 = [aux2[0],aux2[1]-1]
                aux3 = [aux3[0]-1,aux3[1]-2]

                estado_final[0] = aux0 
                estado_final[1] = aux1
                estado_final[2] = aux2
                estado_final[3] = aux3

                aconteceu_w = True
                

            i=i+1
        

        if aconteceu_w == False:

            superficie = self.ler_superficie_game()
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0]
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0]

            y_superficie0 = superficie[x0]
            y_superficie1 = superficie[x1]
            y_superficie2 = superficie[x2]
            y_superficie3 = superficie[x3]
            
            temp = [y_superficie0] + [y_superficie1] + [y_superficie2] + [y_superficie3]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1
            
            i = 0
            while i<len(estado_final):
                aux = estado_final[i]
                aux[1]= min - 1
                estado_final[i]= [estado_final[i][0],aux[1]]
                i=i+1
            proxima_ronda_game = (self.game) + (estado_final)
            
            self.preencher_lista_alturas4(açao,proxima_ronda_game,x0,x1,x2,x3) 

        else:

            superficie = self.ler_superficie_game()
            x0 = estado_final[3][0] 
            

            y_superficie0 = superficie[x0]

            
            i = 0
            while i<len(estado_final):
                aux = estado_final[i]
                aux[1]=  y_superficie0 - 1 - i 
                estado_final[i]= [estado_final[i][0],aux[1]]
                i=i+1
            proxima_ronda_game = (self.game) + (estado_final)
            
            self.preencher_lista_alturas1(açao,proxima_ronda_game,x0) 

        
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
                    aux = estado_final[j]
                    aux[0]= aux[0] +1
                    estado_final[j]= [aux[0],estado_final[j][1]]
                    j = j+1
            elif açao[i] == 'a':
                j =0
                while j < len(estado_inicial):
                    aux = estado_final[j]
                    aux[0]= aux[0] -1
                    estado_final[j]= [aux[0],estado_final[j][1]]
                    j = j+1
            i=i+1
        ############POUSAR QUADRADO TENDO EM CONTA A SUPERFICIE E A JOGADA (d,a,w..)######################

        superficie = self.ler_superficie_game()                       
        x0 = estado_final[0][0] 
        x1 = estado_final[1][0]
        y_superficie0 = superficie[x0]
        y_superficie1 = superficie[x1]
        if y_superficie0 < y_superficie1:
            j=0
            while j < 2:
                aux = estado_final[j]
                aux[1]= y_superficie0 -2
                estado_final[j]= [estado_final[j][0],aux[1]]
                j = j+1

            while j < 4:
                aux = estado_final[j]
                aux[1]= y_superficie0 - 1
                estado_final[j]= [estado_final[j][0],aux[1]]
                j = j+1

        if y_superficie0 >= y_superficie1:
            j=0
            while j < 2:
                aux = estado_final[j]
                aux[1]= y_superficie1 -2
                estado_final[j]= [estado_final[j][0],aux[1]]
                j = j+1

            while j < 4:
                aux = estado_final[j]
                aux[1]= y_superficie1 - 1
                estado_final[j]= [estado_final[j][0],aux[1]]
                j = j+1
       
        proxima_ronda_game = (self.game) + (estado_final)
        
        # adiciona jogada e pontos respetivos à lista de jogadas possiveis mais pontos
        self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1) 
        # jogada = self.escolha_melhor_jogada(self.lista_jogadas_mais_pontos)
        
        
        ##########################################################
    ################################################################################################################################

    
    def preencher_lista_alturas4(self,açao,proxima_ronda_game,x0,x1,x2,x3):
        aux0 = self.ler_superficie_game1(proxima_ronda_game)
        y0 = aux0[x0]
        y1 = aux0[x1]
        y2 = aux0[x2]
        y3 = aux0[x3]
        self.lista_acao_mais_altura = self.lista_acao_mais_altura + [açao] + [min(y0,y1,y2,y3)]
    
    def preencher_lista_alturas3(self,açao,proxima_ronda_game,x0,x1,x2):
        aux0 = self.ler_superficie_game1(proxima_ronda_game)
        y0 = aux0[x0]
        y1 = aux0[x1]
        y2 = aux0[x2]
        self.lista_acao_mais_altura = self.lista_acao_mais_altura + [açao] + [min(y0,y1,y2)]

    
    def preencher_lista_alturas(self,açao,proxima_ronda_game,x,x2):
        aux0 = self.ler_superficie_game1(proxima_ronda_game)
        y0 = aux0[x]
        y1 = aux0[x2]
        self.lista_acao_mais_altura = self.lista_acao_mais_altura + [açao] + [min(y0,y1)]
    
    def preencher_lista_alturas1(self,açao,proxima_ronda_game,x0):
        aux0 = self.ler_superficie_game1(proxima_ronda_game)
        y0 = aux0[x0]
        self.lista_acao_mais_altura = self.lista_acao_mais_altura + [açao] + [y0]
        
    
    def escolha_melhor_jogada(self):
        i=1
        melhor_jogada = ['',0]
        print(self.lista_acao_mais_altura)
        while i< len(self.lista_acao_mais_altura):
            
            if self.lista_acao_mais_altura[i] > melhor_jogada[1]:
                melhor_jogada[0]= self.lista_acao_mais_altura[i-1]
                melhor_jogada[1]= self.lista_acao_mais_altura[i]
            i = i+2
        
        return melhor_jogada[0]

    def possiveis_S(self):
        lista = [['a','a','a'],['a','a'],['a'],[''],['d'],['d','d'],['d','d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],['w','d','d','d']]
        return lista
    
    def play_S(self,açao):
        estado_inicial = [[4, 2], [4, 3], [5, 3], [5, 4]]  
        
        i=0
        estado_final = estado_inicial
        aconteceu_w = False
        
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
                
                j =0
                aux0 = estado_final[3]
                aux1 = estado_final[2]
                aux2 = estado_final[1]
                aux3 = estado_final[0]
                    
                aux0 = [aux0[0]-2,aux0[1]-1]
                aux1 = [aux1[0]-1,aux1[1]-1]
                aux2 = [aux2[0],aux2[1]]
                aux3 = [aux3[0]+1,aux3[1]]

                estado_final[3] = aux0 
                estado_final[2] = aux1
                estado_final[1] = aux2
                estado_final[0] = aux3
               
                aconteceu_w = True
                

            i=i+1
        
        
        if aconteceu_w == False:
           
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            y_superficie3 = superficie[x3]
            y_superficie1 = superficie[x1]
            
            
            if y_superficie1 < y_superficie3:
                aux = estado_final[0]
                aux[1] = y_superficie1 - 2
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie1 - 1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie1 - 1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie1 
                estado_final[3] = [aux[0],aux[1]]
               
            else:
                aux = estado_final[0]
                aux[1] = y_superficie3 - 3
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie3 - 2
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie3 - 2
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie3 -1
                estado_final[3] = [aux[0],aux[1]]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x2) 
        else:
            
            superficie = self.ler_superficie_game()
            x3 = estado_final[3][0] 
            x2 = estado_final[2][0]
            x0 = estado_final[0][0] 
            
            

            y_superficie0 = superficie[x0]
            y_superficie2 = superficie[x2]
            y_superficie3 = superficie[x3]
            
            
            if(y_superficie3 <= y_superficie2) and (y_superficie3 <= y_superficie0):
                aux = estado_final[0]
                aux[1] = y_superficie3 - 2
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie3-2
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie3-1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie3-1
                estado_final[3] = [aux[0],aux[1]]
            
            elif (y_superficie2 <= y_superficie3) and (y_superficie2 <= y_superficie0):
                aux = estado_final[0]
                aux[1] = y_superficie2-2
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie2-2
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie2-1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie2-1
                estado_final[3] = [aux[0],aux[1]]

            elif (y_superficie0 < y_superficie3) and (y_superficie0 < y_superficie2):
                aux = estado_final[0]
                aux[1] = y_superficie0 - 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie0 -1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie0 
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie0
                estado_final[3] = [aux[0],aux[1]]
                
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas3(açao,proxima_ronda_game,x0,estado_final[1][0],x3) 

            
            
    def possiveis_Z(self):
        lista = [['a','a'],['a'],[''],['d'],['d','d'],['d','d','d'],['d','d','d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],['w','d','d','d']]
        return lista
    
    def play_Z(self,açao):
        estado_inicial = [[4, 2], [3, 3], [4, 3], [3, 4]]  
        
        i=0
        estado_final = estado_inicial
        aconteceu_w = False
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
                
                
                aux0 = estado_final[0]
                aux1 = estado_final[1]
                aux2 = estado_final[2]
                aux3 = estado_final[3]
                    
                aux0 = [aux0[0]+1,aux0[1]-1]
                aux1 = [aux1[0],aux1[1]]
                aux2 = [aux2[0]+1,aux2[1]+1]
                aux3 = [aux3[0],aux3[1]+2]

                estado_final[3] = aux0 
                estado_final[2] = aux1
                estado_final[1] = aux2
                estado_final[0] = aux3
               
                aconteceu_w = True
            i=i+1
        
        
        if aconteceu_w == False:
           
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            y_superficie3 = superficie[x3]
            y_superficie1 = superficie[x1]
            
            
            if y_superficie1 >= y_superficie3:
                aux = estado_final[0]
                aux[1] = y_superficie3 - 3
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie3 - 2
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie3 - 2
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie3 -1
                estado_final[3] = [aux[0],aux[1]]
               
            else:
                aux = estado_final[0]
                aux[1] = y_superficie1 - 2
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie1 - 1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie1 - 1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie1 
                estado_final[3] = [aux[0],aux[1]]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x2) 
        else:
            
            superficie = self.ler_superficie_game()
            x3 = estado_final[3][0] 
            x1 = estado_final[1][0]
            x0 = estado_final[0][0] 
            x2 = estado_final[2][0] 
            
            

            y_superficie0 = superficie[x0]
            y_superficie1 = superficie[x1]
            y_superficie3 = superficie[x3]
            
            
            if(y_superficie0 <= y_superficie1) and (y_superficie0 <= y_superficie3):
                aux = estado_final[0]
                aux[1] = y_superficie0 - 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie0-1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie0-2
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie0-2
                estado_final[3] = [aux[0],aux[1]]
            
            elif (y_superficie1 <= y_superficie0) and (y_superficie1 <= y_superficie3):
                aux = estado_final[0]
                aux[1] = y_superficie1-1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie1-1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie1-2
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie1-2
                estado_final[3] = [aux[0],aux[1]]

            elif (y_superficie3 < y_superficie0) and (y_superficie3 < y_superficie1):
                aux = estado_final[0]
                aux[1] = y_superficie3 
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie3 
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie3 -1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie3 -1
                estado_final[3] = [aux[0],aux[1]]
                
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas3(açao,proxima_ronda_game,x0,x2,x3) 

    def possiveis_L(self):
        lista =  [['a','a','a'],['a','a'],['a'],[''],['d'],['d','d'],['d','d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],['w','d','d','d'],
                    ['w','w','a','a'],['w','w','a'],['w','w'],['w','w','d','d','d','d'],['w','w','d','d','d'],['w','w','d','d'],['w','w','d'],
                    ['w','w','w'],['w','w','w','a','a'],['w','w','w','a'],['w','w','w','d','d','d'],['w','w','w','d','d'],['w','w','w','d']]
                    
        return lista

    def play_L(self,açao,num):
        estado_inicial = [[4, 2], [4, 3], [4, 4], [5, 4]] 
        
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
                    aux0 = estado_final[0]
                    aux1 = estado_final[1]
                    aux2 = estado_final[2]
                    aux3 = estado_final[3]
                        
                    aux0 = [aux0[0]+1,aux0[1]+1]
                    aux1 = [aux1[0],aux1[1]]
                    aux2 = [aux2[0]-1,aux2[1]-1]
                    aux3 = [aux3[0]-2,aux3[1]]

                    estado_final[3] = aux3 
                    estado_final[2] = aux2
                    estado_final[1] = aux1
                    estado_final[0] = aux0
                    
                elif  self.contador_auxiliar ==1:
                    
                    aux0 = estado_final[0]
                    aux1 = estado_final[1]
                    aux2 = estado_final[2]
                    aux3 = estado_final[3]
                        
                    aux0 = [aux0[0]-1,aux0[1]+1]
                    aux1 = [aux1[0],aux1[1]]
                    aux2 = [aux2[0]+1,aux2[1]-1]
                    aux3 = [aux3[0],aux3[1]-2]

                    estado_final[0] = aux0 
                    estado_final[1] = aux1
                    estado_final[2] = aux2
                    estado_final[3] = aux3
                    
                    
                elif   self.contador_auxiliar ==2:
                    
                    aux0 = estado_final[0]
                    aux1 = estado_final[1]
                    aux2 = estado_final[2]
                    aux3 = estado_final[3]
                        
                    aux0 = [aux0[0]-1,aux0[1]-1]
                    aux1 = [aux1[0],aux1[1]]
                    aux2 = [aux2[0]+1,aux2[1]+1]
                    aux3 = [aux3[0]+2,aux3[1]]

                    estado_final[0] = aux0 
                    estado_final[1] = aux1
                    estado_final[2] = aux2
                    estado_final[3] = aux3
                    

                self.contador_auxiliar = self.contador_auxiliar +1
                aconteceu_w = aconteceu_w +1
            
            i=i+1
       
        if aconteceu_w == 0:
           
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            y_superficie3 = superficie[x3]
            y_superficie2 = superficie[x2]
            
            temp = [y_superficie2] + [y_superficie3]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1
            
            aux = estado_final[0]
            aux[1] = min-3
            estado_final[0] = [aux[0],aux[1]]
            
            aux = estado_final[1]
            aux[1] = min - 2
            estado_final[1] = [aux[0],aux[1]]
            
            aux = estado_final[2]
            aux[1] = min - 1
            estado_final[2] = [aux[0],aux[1]]
            
            aux = estado_final[3]
            aux[1] = min - 1
            estado_final[3] = [aux[0],aux[1]]
            
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x3) 
        elif aconteceu_w == 1:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            y_superficie3 = superficie[x3]
            y_superficie1 = superficie[x1]
            y_superficie0 = superficie[x0]
            
            
            
            if y_superficie0 <= y_superficie1 and y_superficie0 < y_superficie3:
                aux = estado_final[0]
                aux[1] = y_superficie0 - 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie0 - 1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie0 - 1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie0
                estado_final[3] = [aux[0],aux[1]]
               
            elif y_superficie1 <= y_superficie0 and y_superficie1 < y_superficie3:
                
                aux = estado_final[0]
                aux[1] = y_superficie1 - 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie1 - 1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie1 - 1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie1
                estado_final[3] = [aux[0],aux[1]]
            else:
                aux = estado_final[0]
                aux[1] = y_superficie3 - 2
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie3 - 2
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie3 -2
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie3 -1
                estado_final[3] = [aux[0],aux[1]]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas3(açao,proxima_ronda_game,x0,x1,x2)
        
        elif aconteceu_w == 2:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            # print(estado_final)
            y_superficie3 = superficie[x3]
            y_superficie0 = superficie[x0]
            
            
            
            #NAO TENHO A CERTEZA
            if y_superficie0 <= y_superficie3 + 1:
                aux = estado_final[0]
                aux[1] = y_superficie0 - 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie0 - 2
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie0 - 3
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie0 - 3
                estado_final[3] = [aux[0],aux[1]]
            else:
                aux = estado_final[0]
                aux[1] = y_superficie3 + 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie3
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie3 - 1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie3 - 1
                estado_final[3] = [aux[0],aux[1]]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x2,x3)
        elif aconteceu_w == 3:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 


            y_superficie2 = superficie[x2]
            y_superficie1 = superficie[x1]
            y_superficie0 = superficie[x0]

            temp = [y_superficie0] + [y_superficie1] + [y_superficie2]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1

            aux = estado_final[0]
            aux[1] = min - 1
            estado_final[0] = [aux[0],aux[1]]
            
            aux = estado_final[1]
            aux[1] = min - 1
            estado_final[1] = [aux[0],aux[1]]
            
            aux = estado_final[2]
            aux[1] = min - 1
            estado_final[2] = [aux[0],aux[1]]
            
            aux = estado_final[3]
            aux[1] = min - 2
            estado_final[3] = [aux[0],aux[1]]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas3(açao,proxima_ronda_game,x0,x1,x3)


    def possiveis_J(self):
        lista = [['a','a','a'],['a','a'],['a'],[''],['d'],['d','d'],['d','d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],['w','d','d','d'],['w','w','a','a'],['w','w','a'],['w','w'],['w','w','d'],['w','w','d','d'],['w','w','d','d','d','d']
                ,['w','w','w','a','a'],['w','w','w','a'],['w','w','w'],['w','w','w','d'],['w','w','w','d','d'],['w','w','w','d','d','d']]

        return lista


    
    def play_J(self,açao,num):
        estado_inicial = [[4, 2], [5, 2], [4, 3], [4, 4]] 
        
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
                    aux0 = estado_final[0]
                    aux1 = estado_final[1]
                    aux2 = estado_final[2]
                    aux3 = estado_final[3]
                        
                    aux0 = [aux0[0]+1,aux0[1]+1]
                    aux1 = [aux1[0],aux1[1]+2]
                    aux2 = [aux2[0],aux2[1]]
                    aux3 = [aux3[0]-1,aux3[1]-1]

                    estado_final[3] = aux3 
                    estado_final[2] = aux2
                    estado_final[1] = aux1
                    estado_final[0] = aux0
                    
                elif  self.contador_auxiliar ==1:
                    
                    aux0 = estado_final[0]
                    aux1 = estado_final[1]
                    aux2 = estado_final[2]
                    aux3 = estado_final[3]
                        
                    aux0 = [aux0[0]-1,aux0[1]+1]
                    aux1 = [aux1[0]-1,aux1[1]-1]
                    aux2 = [aux2[0],aux2[1]]
                    aux3 = [aux3[0]+1,aux3[1]-1]

                    estado_final[0] = aux0 
                    estado_final[1] = aux1
                    estado_final[2] = aux2
                    estado_final[3] = aux3
                    
                    
                elif   self.contador_auxiliar ==2:
                    
                    aux0 = estado_final[0]
                    aux1 = estado_final[1]
                    aux2 = estado_final[2]
                    aux3 = estado_final[3]
                        
                    aux0 = [aux0[0]-1,aux0[1]-1]
                    aux1 = [aux1[0],aux1[1]-2]
                    aux2 = [aux2[0],aux2[1]]
                    aux3 = [aux3[0]-1,aux3[1]-1]

                    estado_final[0] = aux0 
                    estado_final[1] = aux1
                    estado_final[2] = aux2
                    estado_final[3] = aux3
                    

                self.contador_auxiliar = self.contador_auxiliar +1
                aconteceu_w = aconteceu_w +1
            
            i=i+1
       
        if aconteceu_w == 0:
           
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            y_superficie3 = superficie[x3]
            y_superficie1 = superficie[x1]
            
            if y_superficie3 <= y_superficie1 + 1:
                aux = estado_final[0]
                aux[1] = y_superficie3 - 3
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie3 - 3
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie3 - 2
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie3 - 1
                estado_final[3] = [aux[0],aux[1]]
            else:
                aux = estado_final[0]
                aux[1] = y_superficie3 - 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1] 
                aux[1] = y_superficie3 - 1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie3
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie3 + 1
                estado_final[3] = [aux[0],aux[1]]
            
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x1) 
        elif aconteceu_w == 1:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            y_superficie3 = superficie[x3]
            y_superficie2 = superficie[x2]
            y_superficie1 = superficie[x1]
            
            
            
            
            if y_superficie3 <= y_superficie2 and y_superficie3 < y_superficie1:
                aux = estado_final[0]
                aux[1] = y_superficie3 - 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie3
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie3 - 1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie3 - 1
                estado_final[3] = [aux[0],aux[1]]
               
            elif y_superficie2 <= y_superficie3 and y_superficie2 < y_superficie1:
                
                aux = estado_final[0]
                aux[1] = y_superficie2 - 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie2
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie2 - 1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie2 - 1
                estado_final[3] = [aux[0],aux[1]]
            else:
                aux = estado_final[0]
                aux[1] = y_superficie1 - 2
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie1 - 1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie1 - 2
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie1 - 2
                estado_final[3] = [aux[0],aux[1]]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas3(açao,proxima_ronda_game,x0,x2,x3)
        
        elif aconteceu_w == 2:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            # print(estado_final)
            y_superficie1 = superficie[x1]
            y_superficie0 = superficie[x0]
            
            temp = [y_superficie0] + [y_superficie1]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1

            aux = estado_final[0]
            aux[1] = min - 1
            estado_final[0] = [aux[0],aux[1]]
            
            aux = estado_final[1]
            aux[1] = min - 1
            estado_final[1] = [aux[0],aux[1]]
            
            aux = estado_final[2]
            aux[1] = min - 2
            estado_final[2] = [aux[0],aux[1]]
            
            aux = estado_final[3]
            aux[1] = min - 3
            estado_final[3] = [aux[0],aux[1]]

            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x1,x3)
        elif aconteceu_w == 3:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 


            y_superficie3 = superficie[x3]
            y_superficie2 = superficie[x2]
            y_superficie0 = superficie[x0]

            temp = [y_superficie0] + [y_superficie2] + [y_superficie3]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1

            aux = estado_final[0]
            aux[1] = min - 1
            estado_final[0] = [aux[0],aux[1]]
            
            aux = estado_final[1]
            aux[1] = min - 2
            estado_final[1] = [aux[0],aux[1]]
            
            aux = estado_final[2]
            aux[1] = min - 1
            estado_final[2] = [aux[0],aux[1]]
            
            aux = estado_final[3]
            aux[1] = min - 1
            estado_final[3] = [aux[0],aux[1]]
            
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas3(açao,proxima_ronda_game,x1,x2,x3)
    
    def possiveis_T(self):
        lista = [['a','a','a'],['a','a'],['a'],[''],['d'],['d','d'],['d','d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],['w','d','d','d'],
                ['w','w','a','a'],['w','w','a'],['w','w'],['w','w','d'],['w','w','d','d'],['w','w','d','d','d'],['w','w','d','d','d','d'],
                ['w','w','w','a','a'],['w','w','w','a'],['w','w','w'],['w','w','w','d'],['w','w','w','d','d'],['w','w','w','d','d','d']]
        return lista
    
    def play_T(self,açao,num):
        estado_inicial = [[4, 2], [4, 3], [5, 3], [4, 4]]  
        
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
                    aux0 = estado_final[0]
                    aux1 = estado_final[1]
                    aux2 = estado_final[2]
                    aux3 = estado_final[3]
                        
                    aux0 = [aux0[0]+1,aux0[1]+1]
                    aux1 = [aux1[0],aux1[1]]
                    aux2 = [aux2[0]-1,aux2[1]+1]
                    aux3 = [aux3[0]-1,aux3[1]-1]

                    estado_final[3] = aux3 
                    estado_final[2] = aux2
                    estado_final[1] = aux1
                    estado_final[0] = aux0
                    
                elif  self.contador_auxiliar ==1:
                    print(estado_final)
                    aux0 = estado_final[0]
                    aux1 = estado_final[1]
                    aux2 = estado_final[2]
                    aux3 = estado_final[3]
                        
                    aux0 = [aux0[0]-1,aux0[1]+1]
                    aux1 = [aux1[0],aux1[1]]
                    aux2 = [aux2[0]-1,aux2[1]-1]
                    aux3 = [aux3[0]+1,aux3[1]-1]

                    estado_final[0] = aux0 
                    estado_final[1] = aux1
                    estado_final[2] = aux2
                    estado_final[3] = aux3
                    print("novooooooooooooo")
                    print(estado_final)
                    
                elif   self.contador_auxiliar ==2:
                    print(estado_final)
                    aux0 = estado_final[0]
                    aux1 = estado_final[1]
                    aux2 = estado_final[2]
                    aux3 = estado_final[3]
                        
                    aux0 = [aux0[0]-1,aux0[1]-1]
                    aux1 = [aux1[0],aux1[1]]
                    aux2 = [aux2[0]+1,aux2[1]-1]
                    aux3 = [aux3[0]+1,aux3[1]+1]

                    estado_final[0] = aux0 
                    estado_final[1] = aux1
                    estado_final[2] = aux2
                    estado_final[3] = aux3
                    print('6xxxxxxxxxxxx')
                    print(estado_final)
                    

                self.contador_auxiliar = self.contador_auxiliar +1
                aconteceu_w = aconteceu_w +1
            
            i=i+1
       
        if aconteceu_w == 0:
           
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            y_superficie3 = superficie[x3]
            y_superficie2 = superficie[x2]
            
            
            
            if y_superficie3 <= y_superficie2:
                aux = estado_final[0]
                aux[1] = y_superficie3 - 3
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie3 - 2
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie3 - 2
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie3 -1
                estado_final[3] = [aux[0],aux[1]]
               
            else:
                aux = estado_final[0]
                aux[1] = y_superficie2 - 2
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie2 - 1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie2 - 1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie2 
                estado_final[3] = [aux[0],aux[1]]
            # print("000000000000000000000000")
            # print(estado_final)
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x0,x2) 
        elif aconteceu_w == 1:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            y_superficie3 = superficie[x3]
            y_superficie2 = superficie[x2]
            y_superficie0 = superficie[x0]
            
            
            
            if y_superficie0 <= y_superficie3 and y_superficie0 < y_superficie2:
                aux = estado_final[0]
                aux[1] = y_superficie0 - 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie0 - 1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie0 
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie0 -1
                estado_final[3] = [aux[0],aux[1]]
               
            elif y_superficie3 <= y_superficie0 and y_superficie3 < y_superficie2:
                
                aux = estado_final[0]
                aux[1] = y_superficie3 - 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie3 - 1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie3
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie3 -1
                estado_final[3] = [aux[0],aux[1]]
            else:
                aux = estado_final[0]
                aux[1] = y_superficie2 - 2
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie2 - 2
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie2 -1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie2 -2
                estado_final[3] = [aux[0],aux[1]]
            # print("11111111111111111111111111111")
            # print(estado_final)
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas3(açao,proxima_ronda_game,x0,x1,x3)
        
        elif aconteceu_w == 2:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            

            # print(estado_final)
            y_superficie2 = superficie[x2]
            y_superficie0 = superficie[x0]
            
            
            
            if y_superficie0 <= y_superficie2 :
                aux = estado_final[0]
                aux[1] = y_superficie0 - 1
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie0 - 2
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie0 -2
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie0 -3
                estado_final[3] = [aux[0],aux[1]]
            else:
                aux = estado_final[0]
                aux[1] = y_superficie2
                estado_final[0] = [aux[0],aux[1]]
                
                aux = estado_final[1]
                aux[1] = y_superficie2 - 1
                estado_final[1] = [aux[0],aux[1]]
                
                aux = estado_final[2]
                aux[1] = y_superficie2 -1
                estado_final[2] = [aux[0],aux[1]]
                
                aux = estado_final[3]
                aux[1] = y_superficie2 -2
                estado_final[3] = [aux[0],aux[1]]
            # print("2222222222222222222222222222")
            # print(estado_final)
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas(açao,proxima_ronda_game,x2,x3)
        elif aconteceu_w == 3:
            
            superficie = self.ler_superficie_game()
            
            x0 = estado_final[0][0] 
            x1 = estado_final[1][0] 
            x2 = estado_final[2][0] 
            x3 = estado_final[3][0] 
            # print(estado_final)

            y_superficie3 = superficie[x3]
            y_superficie1 = superficie[x1]
            y_superficie0 = superficie[x0]
            # print("sup0")
            # print(x0)
            # print(y_superficie0)
            # print("sup1")
            # print(x1)
            # print(y_superficie1)
            # print("sup3")
            # print(x3)
            # print(y_superficie3)
            
            temp = [y_superficie0] + [y_superficie1] + [y_superficie3]
            i = 0
            min = 30
            while i < len(temp):
                if temp[i]<min:
                    min = temp[i]
                i=i+1
            aux = estado_final[0]
            aux[1] = min-1
            estado_final[0] = [aux[0],aux[1]]
            
            aux = estado_final[1]
            aux[1] = min - 1
            estado_final[1] = [aux[0],aux[1]]
            
            aux = estado_final[2]
            aux[1] = min -2
            estado_final[2] = [aux[0],aux[1]]
            
            aux = estado_final[3]
            aux[1] = min -1
            estado_final[3] = [aux[0],aux[1]]
            
            
            print("3333333333333333333333")
            print(estado_final)
            proxima_ronda_game = (self.game) + (estado_final)    
            self.preencher_lista_alturas3(açao,proxima_ronda_game,x0,x2,x3)
             
            
            
    
