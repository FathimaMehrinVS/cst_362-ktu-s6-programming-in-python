'''
Write Python GUI program to take the birth date and output the age when a button is
pressed.
'''
from breezypythongui import EasyFrame
from datetime import date
class Age(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text="Input Year: ",row=0,column=0)
        self.year=self.addIntegerField(value=0,row=0,column=1)
        self.addLabel(text="Input Month: ",row=1,column=0)
        self.month=self.addIntegerField(value=0,row=1,column=1)
        self.addLabel(text="Input Day: ",row=2,column=0)
        self.day=self.addIntegerField(value=0,row=2,column=1)
        self.addLabel(text='Age',row=3,column=0)
        self.age=self.addIntegerField(value=0,row=3,column=1,state="readonly")
        self.addButton(text="Go",row=4,column=0,command=self.findage)
    def findage(self):
        year=self.year.getNumber()
        month=self.month.getNumber()
        day=self.day.getNumber()
        today=date.today()
        d=date(year,month,day)
        age=today.year-year-((today.month,today.day)<(month,day))
        self.age.setNumber(age)
u1=Age()
u1.mainloop()