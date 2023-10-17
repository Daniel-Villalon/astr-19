class favoriteAnimal():
  def print(self):
    print(f"Arms length(cm): {self.arms_len}\nLegs length(cm): {self.legs_len}\nNumber of eyes: {self.number_eyes}\nDoes it have a tail? {self.tail}\nIs it furry? {self.furry}")



  def __init__(self, armsL=43.18, legsL=43.18, N_eye=2, tail=True, furry=True):
    self.arms_len = armsL
    self.legs_len = legsL
    self.number_eyes = N_eye
    self.tail = tail
    self.furry = furry
    

def main():
    
  x = favoriteAnimal()
  x.print()

if __name__=="__main__":
  main()