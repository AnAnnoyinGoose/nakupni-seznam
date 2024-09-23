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

if __name__ == "main.py":
  main()
