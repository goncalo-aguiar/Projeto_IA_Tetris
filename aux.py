from game import Game

class Agent:
    def __init__(self,n_mec):
        self.username = n_mec
        (self.l) = []
        self.iteracao = 0
        self.piece_atual= None
        self.game = None
        self.next_piece0 = None
        self.lista_jogadas_mais_pontos = None
        self.lista_alturas = None  #
        
    
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
        
        
        self.piece_atual = state['piece']
        self.game = state['game']
        next_pieces = state['next_pieces']
        self.next_piece0 = next_pieces[0]
        next_piece1 = next_pieces[1]
        next_piece2 = next_pieces[2]
            


        print("------------GAME--------")
        print(self.game)
        print("----------------------")
        print('\n')
        print("------------ATUAL--------")
        print(self.piece_atual)
        print("----------------------")
        print('\n')
        print("------------P1--------")
        print(self.next_piece0)
        print("----------------------")
        print('\n')
        print("------------P2--------")
        print(next_piece1)
        print("----------------------")
        print('\n')
        print("------------P3--------")
        print(next_piece2)
        print("----------------------")
        ##############################
        if self.piece_atual == None:         #sempre q a peça muda chama o search para a seguinte
            self.l = [] 
            self.piece_atual = self.next_piece0
            self.iteracao = 0
            self.lista_jogadas_mais_pontos = []
            self.lista_alturas = []
            self.search()
            
        #############################
        return self.jogar() # self.l é a lista que mete a peça a mexer(ou seja é passado para esta lista a jogada com melhor pontuação)
    

    ############################################FUnção que preeche a self.l com a jogada#########################
    def search(self):
        lista = ['','','','','','','','','','','','','','','','','','','','','','','','','','','']
        print(self.tipo_de_peca(self.piece_atual))
        if self.tipo_de_peca(self.piece_atual) == 'I':
            
            # (self.l).append(self.possiveis_I())
            (self.l).append('w')
            (self.l).append('d')
            (self.l).append('d')
            (self.l).append('d')
            
            
            
            
            
            
            
            (self.l).append(lista)
              
        elif self.tipo_de_peca(self.piece_atual) == 'J':
            (self.l).append('w')
            (self.l).append('w')
            (self.l).append('w')
            
            (self.l).append(lista)
        elif self.tipo_de_peca(self.piece_atual) == 'Square':
            # percorrer a lista de possiveis_Square e chamar a func play_Square para cada jogada possivel
            # depois meter a melhor jogada no self.l (que vem da self.lista_jogadas_mais_pontos )
            i=0
            lista_square = self.possiveis_Square()
            while i < len(lista_square):
                self.play_Square(lista_square[i])
                i =i+1
            jogada = self.escolha_melhor_jogada(self.lista_jogadas_mais_pontos)
            print('---------------------------------------------------------------------------------------------')
            print(jogada)
            
            (self.l) = [''] + jogada + lista 
            
            
            (self.l).append(lista)
        elif self.tipo_de_peca(self.piece_atual) == 'S':
            (self.l).append('w')
            (self.l).append('d')
            (self.l).append('d')
            
            
            (self.l).append(lista)
        elif self.tipo_de_peca(self.piece_atual) == 'L':
            (self.l).append('w')
            (self.l).append('w')
            (self.l).append('w')
            
            (self.l).append(lista)
        elif self.tipo_de_peca(self.piece_atual) == 'Z':
            (self.l).append('w')
            (self.l).append('a')
            
            
            
            
            (self.l).append(lista)  
        elif self.tipo_de_peca(self.piece_atual) == 'T':
            (self.l).append('w')
            (self.l).append('w')
            (self.l).append('w')
            (self.l).append('w')
            
            (self.l).append(lista)     
            
        else:
            
            
            (self.l).append(lista)
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
        lista = [['a'],['']['d','d','d'],['d','d'],['d'],['w','d','d','d','d'],
                  ['w','d','d','d'],['w','a','a','a'],['w','a','a'],['w','d','d'],['w','d'],['w'],['w','a']]
        return lista
    # def play_I(self,açao,superficie):
    #     return ???

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
        print("Superficie atual:")
        print(superficie)                        
        x0 = estado_final[0][0] 
        x1 = estado_final[1][0]
        y_superficie0 = superficie[x0]
        y_superficie1 = superficie[x1]
        if y_superficie0 <= y_superficie1:
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
        print("Game:")
        print(self.game)
        print("Estado FInal")
        print(estado_final)
        print("Proxima ronda game")
        print(proxima_ronda_game)
        # adiciona jogada e pontos respetivos à lista de jogadas possiveis mais pontos
        self.lista_jogadas_mais_pontos = self.lista_jogadas_mais_pontos + self.analisar_proxima_ronda(açao,proxima_ronda_game,x0,x1) 
        # jogada = self.escolha_melhor_jogada(self.lista_jogadas_mais_pontos)
        # return jogada
        ##########################################################
    ################################################################################################################################


    def analisar_proxima_ronda(self,açao,proxima_ronda_game,x,x2):
        aux0 = self.ler_superficie_game1(proxima_ronda_game)
        y0 = aux0[x]
        y1 = aux0[x2]
        self.lista_alturas = self.lista_alturas + min(y0,y1)
        pontos 
        # aux0 = self.ler_superficie_game1(proxima_ronda_game)
        # aux1= []
        # for num1,num2 in zip(aux0,aux0):
        #     aux1.append(num1*num2)
        # soma_todas_alturas_superficiais_next_game = sum(aux1)
        
        # # aux2 = self.ler_superficie_game()
        # # aux3= []
        # # for num1,num2 in zip(aux2,aux2):
        # #     aux3.append(num1*num2)
        # soma_todas_alturas_superficiais_game_atual = 900*9
        # # print("next " + str(soma_todas_alturas_superficiais_next_game) )
        # # print("atual " + str(soma_todas_alturas_superficiais_game_atual))
        # pontos = soma_todas_alturas_superficiais_game_atual -  soma_todas_alturas_superficiais_next_game
        # # print("pontos "+str(pontos))
        # # print("jogada "+str(açao))


        
        

        return [açao,pontos]
    
    def escolha_melhor_jogada(self,lista_jogadas):
        i=1
        melhor_jogada = ['',1]
        while i< len(lista_jogadas):
            if lista_jogadas[i] < melhor_jogada[1]:
                melhor_jogada[0]= lista_jogadas[i-1]
                melhor_jogada[1]= lista_jogadas[i]
            i = i+2
        
        return melhor_jogada[0]

    def possiveis_S(self):
        lista = [['a','a','a'],['a','a'],['a'],[''],['d'],['d','d'],['d','d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],['w','d','d','d']]
        return lista
    def possiveis_Z(self):
        lista = [['a','a'],['a'],[''],['d'],['d','d'],['d','d','d'],['d','d','d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],['w','d','d','d']]
        return lista
    def possiveis_L(self):
        lista =  [['a','a','a'],['a','a'],['a'][''],['d','d','d'],['d','d'],['d'],['w','d','d','d'],['w','d','d'],['w','d'],['w'],['w','a'],['w','a','a'],
                    ['w','w','a','a'],['w','w','a'],['w','w'],['w','w','d','d','d','d'],['w','w','d','d','d'],['w','w','d','d'],['w','w','d'],
                    ['w','w','w'],['w','w','w','a','a'],['w','w','w','a'],['w','w','w','d','d','d'],['w','w','w','d','d'],['w','w','w','d']]
        return lista
    def possiveis_J(self):
        lista = [['a','a','a'],['a','a'],['a'],[''],['d'],['d','d'],['d','d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],['w','d','d','d'],['w','w','a','a'],['w','w','a'],['w','w'],['w','w','d'],['w','w','d','d'],['w','w','d','d','d','d']
                ,['w','w','w','a','a'],['w','w','w','a'],['w','w','w'],['w','w','w','d'],['w','w','w','d','d'],['w','w','w','d','d','d']]
        return lista
    def possiveis_T(self):
        lista = [['a','a','a'],['a','a'],['a'],[''],['d'],['d','d'],['d','d','d'],['w','a','a'],['w','a'],['w'],['w','d'],['w','d','d'],['w','d','d','d'],
                ['w','w','a','a'],['w','w','a'],['w','w'],['w','w','d'],['w','w','d','d'],['w','w','d','d','d','d'],
                ['w','w','w','a','a'],['w','w','w','a'],['w','w','w'],['w','w','w','d'],['w','w','w','d','d'],['w','w','w','d','d','d']]
        return lista

