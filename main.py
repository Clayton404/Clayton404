import random


#Jogo da velha

class Jogo(object):
    
    def __init__(self):
        
        
        #Variables
        self.position = []
        self.a = []
        
        for a in range(1,3):
            self.position.append("a"+str(a))
   
     #   self.position = 0
        for b in range(1,3):
            self.position.append("b"+str(b))
     
    #    self.position = 0
        for c in range(1,3):
            self.position.append("c" + str(c))
    
     #   print(self.a)
        
        self.a = " "
        self.b = " "
        self.c = " "
        self.d = " "
        self.e = " "
        self.f = " "
        self.g = " "
        self.h = " "
        self.i = " "
        self.turn = 0
        self.cpu = None
        self.jg = []
        
        #Loop.game tik tok
        self.loopmv()
  
    def loopmv(self):
        rs = 1
        
        
        while True:
            
              self.jogador = str(input("1 - X \n 2 - O \n Jogador: "))
              if self.jogador == "X" or self.jogador == "x":
                           self.cpu = "O"
              elif self.jogador == "O" or self.jogador == "o":
                           self.cpu = "X"
              else:
                           print('Jogador invalido',self.jogador)
                           continue
              break
              
        while True:          
                
              
              self.creatTable()
              
              if self.turn == 0:
                  option = str(input("Jogador: "))
               
              elif self.turn >= 1:
                  print('Cpu Jogando',self.turn)
                  option = self.Inteligence()
              
                      
                  
              self.optionExe(option)
              if self.turn == 0:
                  self.turn += 1
              else:
                 self.turn = 0
                 rs+=1
              
            
              
    def creatTable(self):
      
       table = f'''                                                                      Victory        Lost
                                                                  ------------------------
                                                                  X |    0       |    0
                                                                  -------------------------
                                                                  O |    0       |    0
                                                                  --------------------- --
                       a     b     c                                                     
                          |     |     
                    1  {self.a}  |  {self.b}  |  {self.c}
                     _____|_____|_____
                          |     |     
                    2  {self.d}  |  {self.e}  |  {self.f}
                     _____|_____|_____
                          |     |     
                    3  {self.g}  |  {self.h}  |  {self.i} 
                          |     |     
       
      '''
       print(table)
    
    def  Inteligence(self):
       
        
        for i in self.position:
             if not i:
                 break
             for definitive in self.jg:
                    if i == definitive:
                           print("&")
                    else: 
                            self.defini.append(i)
                    break
                    
          
                   
                   
        print(self.defini)
       
        value =  random.choice(self.defini)
        
        return value
        
    def optionExe(self,opc):
               if self.turn == 0:
                   out = self.jogador
                   win = "Jogador"
               elif self.turn >= 1:
                   out = self.cpu
                   win ="Cpu"
        
               if opc == "a1":
                        if self.a == " ":
                            self.a = out
                            self.jg.append(opc)
                        else:
                            print('Posicao ja ocupada')
               elif opc == "b1":
                    
                       if self.b == " ":
                            self.b = out
                            self.jg.append(opc)
                       else:
                           print("Posicao ja ocupada")
               elif opc == "c1":
                        if self.c == " ":
                            self.c = out
                            self.jg.append(opc)
                        else:
                            print('Posicao ja ocupada')
               elif opc == "a2":
                        if self.d == " ":
                            self.d = out
                            self.jg.append(opc)
                        else:
                            print('Posicao ja ocupada')
               elif opc == "b2":
                        if self.e == " ":
                            self.e = out
                            self.jg.append(opc)
                        else:
                            print('Posicao ja ocupada')
               elif opc == "c2":
                        if self.f == " ":
                            self.f = out
                            self.jg.append(opc)
                        else:
                            print('Posicao ja ocupada')
               elif opc == "a3":
                        if self.g == " ":
                            self.g = out
                            self.jg.append(opc)
                        else:
                            print('Posicao ja ocupada')
               elif opc == "b3":
                        if self.h == " ":
                            self.h = out
                            self.jg.append(opc)
                        else:
                            print('Posicao ja ocupada')
               elif opc == "c3":
                        if self.i == " ":
                            self.i = out
                            self.jg.append(opc)
                        else:
                            print('Posicao ja ocupada')
               else:
                   
                   print("Invalido Ex:  a1")
                
                
               self.winner(out,win,opc)
                
    def winner(self,out,win,opc):
              
               if self.c == out and self.f== out and self.i== out:
                   print(f"\n\t\t\t\t\t{win} {out} venceu\n")
               elif self.b == out and self.e== out and self.h == out:
                   print(f"\n\t\t\t\t\t{win} {out} venceu\n")
               elif self.a == out and self.d== out and self.g == out:
                   print(f"\n\t\t\t\t\t{win} {out} venceu\n")
               elif self.a == out and self.b== out and self.c== out:
                   print(f"\n\t\t\t\t\t{win} {out} venceu\n")
               elif self.d == out and self.e== out and self.f == out:
                   print(f"\n\t\t\t\t\t{win} {out} venceu\n")
               elif self.g == out and self.h== out and self.i== out:
                   print(f"\n\t\t\t\t\t{win} {out} venceu\n")
               elif self.a == out and self.e== out and self.i == out:
                   print(f"\n\t\t\t\t\t{win} {out} venceu\n")
               elif self.c  == out and self.e== out and self.g== out:
                   print(f"\n\t\t\t\t\t{win} {out} venceu\n")
               elif self.c== out and self.f == out and self.i == out and self.b == out and self.e == out and self.h== out and self.b == out and self.e== out and self.h == out and self.a == out and self.d== out and self.g == out and self.a == out and self.b== out and self.c== out and self.d == out and self.e== out and self.f == out and self.g == out and self.h== out and self.i== out and self.a == out and self.e== out and self.i == out and self.c== out and self.e== out and self.g == out:
                  print("Empate")
              
                
               
               
      

if __name__ == "__main__":
    
    Jogo()
