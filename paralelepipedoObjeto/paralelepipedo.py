class Paralelepipedo:
  comprimento = 0
  largura = 0
  altura = 0
  
  def limpa(self):
    self.comprimento = 0
    self.largura = 0
    self.altura = 0
  
  def show(self):
    print('-='*55)
    print('Dados de seu PARALELEPÍPEDO:')
    print(f'Altura = {self.altura}, Comprimento = {self.comprimento}, Largura = {self.largura}')
    print(f'Volume =  {self.volume():.2f}')
    print(f'Area extrena = {self.areaExterna():.2f}')
    print('-='*55) 
  
  def volume(self):
    return self.comprimento * self.largura *self.altura
  
  def areaExterna(self):
    return 2*self.comprimento*self.largura + 2*self.comprimento*self.altura + 2*self.largura*self.altura
  
  def novo(self, l1, l2, l3):
    self.comprimento = l1
    self.largura = l2
    self.altura = l3
    return True

