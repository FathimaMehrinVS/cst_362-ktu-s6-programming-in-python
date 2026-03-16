'''
Write a GUI-based program that allows the user to convert amount in Indian Rupees to
amount in Euro. The interface should have labeled entry fields for these two values.
These components should be arranged in a grid where the labels occupy the first row and
the corresponding fields occupy the second row. At start-up, the Rupees field should
contain 0.0, and the Euro field should contain 0.0. The third row in the window contains
two command buttons, labeled R-&gt;E and E-&gt;R. When the user presses the first button,
the program should use the data in the Rupee field to compute the amount in Euro, which
should then be output in the Euro field. The second button should perform the inverse
function.
'''
from breezypythongui import EasyFrame
class A(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Rupee-Euro Converter")
        self.addLabel(text="Rupees",row=0,column=0)
        self.addLabel(text="Euro",row=0,column=1)
        self.rupee=self.addFloatField(value=0.0,row=1,column=0)
        self.euro=self.addFloatField(value=0.0,row=1,column=1)
        self.addButton(text="R->E",row=2,column=0,command=self.convertRtoE)
        self.addButton(text='E->R',row=2,column=1,command=self.convertEtoR)
    def convertRtoE(self):
        #function to convert rupee to euro
        rupees=self.rupee.getNumber()
        euro=rupees/106
        self.euro.setNumber(euro)
    def convertEtoR(self):
        #function to convert euro to rupee
        euro=self.euro.getNumber()
        rupees=euro*106
        self.rupee.setNumber(rupees)
u1=A()
u1.mainloop()