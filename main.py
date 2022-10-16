import tkinter as tk
import co2_funs as co2
from PIL import ImageTk, Image

#import convertions    

def energyuse():
    #label for renewable percent widget 
    renewable_label = tk.Label(window, text = 'Percent renewable your household uses', font=('calibre',10, 'bold'), background = '#90FBAD', width = 40, height = 2)

    #creating a entry for the renewable input
    renewable_var = 0 
    renewable_entry = tk.Entry(window,textvariable = renewable_var, font=('calibre',10,'normal'))

    #placement of the boxes on the screen
    renewable_label.grid(row=0,column=0)
    renewable_entry.grid(row=0,column=1)


    #label for energy type
    type_label = tk.Label(window, text = 'Natural gas (type "gas") or coal (type "coal")',
     font=('calibre',10, 'bold'),background = '#90FBAD', width = 50, height = 2)

    #creating a entry for the energy type
    type_var = 1 
    type_entry = tk.Entry(window,textvariable = type_var, font=('calibre',10,'normal'))

    #placement of the boxes on the screen
    type_label.grid(row=1,column=0)
    type_entry.grid(row=1,column=1)

    #label for power useage 
    energyuse_label = tk.Label(window, text = 'Amount of energy your household uses per year (in KWH)', font=('calibre',10, 'bold'), background = '#90FBAD', width = 50, height = 2)

    #creating a entry for the power useage 
    energyuse = 2
    energyuse_entry = tk.Entry(window,textvariable = energyuse, font=('calibre',10,'normal'))

    #placement of the boxes on the screen
    energyuse_label.grid(row=2,column=0)
    energyuse_entry.grid(row=2,column=1)



def car():
    #label for miles driven by car 
    miles_label = tk.Label(window, text = 'Miles you drive per day', font=('calibre',10, 'bold'), background = '#90FBAD', width = 40, height = 2)

    #creating a entry for the miles driven by car 
    miles_var = 3 
    miles_entry = tk.Entry(window,textvariable = miles_var, font=('calibre',10,'normal'))

    #placement of the boxes on the screen
    miles_label.grid(row=3,column=0)
    miles_entry.grid(row=3,column=1)

    #label for power useage 
    MPG_label = tk.Label(window, text = 'MPG of the car you drive', font=('calibre',10, 'bold'), background = '#90FBAD', width = 40, height = 2)

    #creating a entry for the power useage 
    MPG = 4
    MPG_entry = tk.Entry(window,textvariable = MPG, font=('calibre',10,'normal'))

    #placement of the boxes on the screen
    MPG_label.grid(row=4,column=0)
    MPG_entry.grid(row=4,column=1)

def flighttime():
    #label for hours spent on plane
    time_label = tk.Label(window, text = 'Hours you fly per year', font=('calibre',10, 'bold'), background = '#90FBAD', width = 40, height = 2)

    #creating a entry for the miles driven by car 
    time_var = 5 
    time_entry = tk.Entry(window,textvariable = time_var, font=('calibre',10,'normal'))

    #placement of the boxes on the screen
    time_label.grid(row=5,column=0)
    time_entry.grid(row=5,column=1)

def food():
    #label for hours spent on plane
    redmeat_label = tk.Label(window, text = 'Pounds of red meat you eat per day', font=('calibre',10, 'bold'), background = '#90FBAD', width = 40, height = 2)

    #creating a entry for the miles driven by car 
    redmeat_var = 6 
    redmeat_entry = tk.Entry(window,textvariable = redmeat_var, font=('calibre',10,'normal'))

    #placement of the boxes on the screen
    redmeat_label.grid(row=6,column=0)
    redmeat_entry.grid(row=6,column=1)


def consumption():
    #label for hours spent on plane
    money_label = tk.Label(window, text = 'Dollars you spend on clothes per week', font=('calibre',10, 'bold'), background = '#90FBAD', width = 40, height = 2)

    #creating a entry for the miles driven by car 
    money_var = 7 
    money_entry = tk.Entry(window,textvariable = money_var, font=('calibre',10,'normal'))

    #placement of the boxes on the screen
    money_label.grid(row=7,column=0)
    money_entry.grid(row=7,column=1)


def laundry():
    #label for hours spent on plane
    loads_label = tk.Label(window, text = 'Loads of laundry per week', font=('calibre',10, 'bold'), background = '#90FBAD', width = 40, height = 2)

    #creating a entry for the miles driven by car 
    loads_var = 8 
    loads_entry = tk.Entry(window,textvariable = loads_var, font=('calibre',10,'normal'))

    #placement of the boxes on the screen
    loads_label.grid(row=8,column=0)
    loads_entry.grid(row=8,column=1)


def shower():
    #label for hours spent on plane
    shower_label = tk.Label(window, text = 'Minutes in shower per day', font=('calibre',10, 'bold'), background = '#90FBAD', width = 40, height = 2)

    #creating a entry for the miles driven by car 
    shower_var = 9 
    shower_entry = tk.Entry(window,textvariable = shower_var, font=('calibre',10,'normal'))

    #placement of the boxes on the screen
    shower_label.grid(row=9,column=0)
    shower_entry.grid(row=9,column=1)


def carbonCALC():
    renewable_entry = tk.Entry(window,textvariable = 0)
    type_entry = tk.Entry(window,textvariable = 1)
    energyuse_entry = tk.Entry(window,textvariable = 2)
    miles_entry = tk.Entry(window,textvariable = 3)
    MPG_entry = tk.Entry(window,textvariable = 4)
    airtime_entry = tk.Entry(window,textvariable = 5)
    redmeat_entry = tk.Entry(window,textvariable = 6)
    money_entry = tk.Entry(window,textvariable = 7)
    loads_entry = tk.Entry(window,textvariable = 8)
    shower_entry = tk.Entry(window,textvariable = 9)



    try:

        co2number = co2.electricity(type_entry.get(), float(energyuse_entry.get()), float(renewable_entry.get())) + co2.car(float(MPG_entry.get()), float(miles_entry.get())) + co2.flight(float(airtime_entry.get()))+ co2.food(float(redmeat_entry.get()))  + co2.clothes(float(money_entry.get())) + co2.laundry(int(loads_entry.get()))+ co2.shower(int(shower_entry.get()))

        if co2number > 14515: 
            CO2_label = tk.Label(window, text = "Your carbon footprint per year is " + str(co2number)  + "kg. This is more than the average person. Do better." , font=('calibre',10, 'bold'))
        else:
            CO2_label = tk.Label(window, text = "Your carbon footprint per year is " + str(co2number) + "kg. This is less than the average person. Good job!.", font=('calibre',10, 'bold'))
        CO2_label.place(relx = 0.3, rely = 0.7)
    except:

        CO2_label = tk.Label(window, text = "There was a error in your inputs. Please check them.", font=('calibre',10, 'bold'))
        CO2_label.place(relx = 0.3, rely = 0.7)
            

    #CO2_entry = tk.Entry(window,textvariable = 4)
    #CO2_label = tk.Label(window, text = CO2_entry.get(), font=('calibre',10, 'bold'))
    #CO2_label.grid(row = 12, column = 3)
    #print(type(CO2_entry.get()))
    





if __name__ == '__main__': 
    #creating the window 
    window = tk.Tk()

    #Names the window 
    window.title("Carbon footprint calculator")
    title = tk.Label(window, text = 'Carbon Emmission per Year Calculator', font=('calibre',15, 'bold'), background = '#90FBAD', width = 80, height = 20)
    title.place(relx = -0.3, rely = 0.5)

    #Background color of the window 
    window.configure(background = '#90FBAD')

    #Sets the sizes of the windows 
    window.minsize(width=800, height=600)
    window.maxsize(width=800, height=600)



    #function calls
    energyuse()
    car()
    flighttime()
    food()
    consumption()
    laundry()
    shower()

    #amount CO2 in one year
    CO2 = tk.Entry(window,textvariable = 4, font=('calibre',10,'normal'))

    tk.Button(window, text = 'Calulate', command=carbonCALC).grid(row = 10, column = 0)

   #Import Image into App
    image = ImageTk.PhotoImage(Image.open('Earth.jpg'))
    labelWidget = tk.Label(window, image = image)
    labelWidget.place(relx = 0.7, rely = 0.7)


    #Main loop for the window 
    window.mainloop()

   
    

