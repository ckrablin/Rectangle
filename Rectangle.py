from dataclasses import dataclass
@dataclass

class RectangleBorder:
  Height: int
  Width: int
  def getPerimeter(self):
      perimeter = self.Height * 2 + self.Width * 2
      return perimeter

  def getArea(self):
      area = self.Height * self.Width
      return area
  
  def getStr(self):
    side = ""
    width = "* " * self.Width + "\n"
    side += width
    for i in range(self.Height - 2):
        side += "* " + "  " * (self.Width - 2) + "* \n"
    side += width
    return side
def main():
    print("-"*20+"Rectangle Calculator"+"-"*20+"\n")
    
    again = "Y"
    while again.upper() == "Y":
      height = int(input("Height: "))
      width = int(input("Width: "))
      rectangle = RectangleBorder(height, width)
      
      print("Perimeter:", rectangle.getPerimeter())
      print("Area: ", rectangle.getArea())
      print(rectangle.getStr())
      again = input("Try Again? (y/n): ").upper()
    print("-"*40)
    print("Thank You for Using the System")
if __name__ == "__main__":
    main()