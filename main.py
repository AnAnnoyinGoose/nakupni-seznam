class Seznam:
  data = []
  def add(self, inp):
    self.data.append(inp)
  def rem(self, inp):
    try:
      self.data.remove(inp)
    except Exception as E:
      print(E)
  def list(self):
    if self.data:
      for idx, e in enumerate(self.data, 1):
        print(f"{idx}. - {e}")
    else: 
      print("Seznam je prázdný.")
  def help(self):
    print("1) Help msg.")
    print("2) Add element.")
    print("3) Remove element.")
    print("4) List all elements.")
    print("5) Exit program.")



s = Seznam()

def main():
  run = 1
  s.help()
  while run:
    try:
      m = int(input("> "))
    except Exception as E:
      continue
  if m in [1,2,3,4,5]:
    match m:
      case 1:
        s.help()
      case 2:
        e = input("Add an element: ")
        s.add(e)
      case 3:
        s.list()
        e = input("Specify element: ")
        s.rem(e)
      case 4:
        s.list()
      case 5:
        run = 0
      
  

if __name__ == "main.py":
  main()
