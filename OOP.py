#class in oop - is the blue print of an object


# class Animal:
#     Name="Cat"
#     age = 12;
#     color=' black'
#     def dislay(self):
#         print('Name:', self.Name,'Age:', self.age,"Color", self.color)

# cat1 =Animal();
# cat1.dislay()

# class Rectangle:
#         legnth = 7;
#         width =9
#         area =0
#         def calculateArea(self):
#             self.area = self.legnth*self.width
#         def DisplayArea(self):
#             print('the area of rectangle =', self.area)
# rec1 = Rectangle();
# rec1.calculateArea();
# rec1.DisplayArea();
            

class Square:
      side=32
      area=0
      peri=0
      def calculateArea(self):
          self.area= self.side*self.side
      def calculateperi(self):
          self.peri= self.side+self.side+self.side+self.side
      def DisplayArea(self):
          print('the area of square =', self.area)     
      def Displayperi(self):
          print("the perimeter of square =", self.peri)
Squ1=Square();
Squ1.calculateArea();
Squ1.calculateperi();
Squ1.DisplayArea();
Squ1.Displayperi();
 

        
    
