class Seznam:
  data = []
  def add(self, inp):
    self.data.append(inp)
  def rem(self, inp):
        try:
          self.data.remove(inp)
        except Exception as E:
          print(E)
s = Seznam()

def main():
  run = 1

if __name__ == "main.py":
  main()
