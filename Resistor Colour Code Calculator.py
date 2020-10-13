import tkinter as tk

#functions
def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

def create_resistor(band1, band2, band3, band4, band5):
    neutral_colour = (214,214,214)
    #clear canvas to start
    c.delete(tk.ALL)
    #wire at start
    c.create_rectangle(0, 60, 50, 90, fill=rgb_to_hex(neutral_colour)) 
    #wire at end
    c.create_rectangle(350, 60, 400, 90, fill=rgb_to_hex(neutral_colour))
    #front wide section
    c.create_rectangle(50, 10, 110, 140, fill=rgb_to_hex(neutral_colour))
    #end wide section
    c.create_rectangle(290, 10, 350, 140, fill=rgb_to_hex(neutral_colour))
    #middle body
    c.create_rectangle(110, 30, 290, 120, fill=rgb_to_hex(neutral_colour))
    #first band
    c.create_rectangle(80, 10, 100, 140, fill=rgb_to_hex(band1))
    #second band
    c.create_rectangle(120, 30, 140, 120, fill=rgb_to_hex(band2))
    #third band
    c.create_rectangle(170, 30, 190, 120, fill=rgb_to_hex(band3))
    #fourth band
    c.create_rectangle(220, 30, 240, 120, fill=rgb_to_hex(band4))
    #fifth band
    c.create_rectangle(300, 10, 320, 140, fill=rgb_to_hex(band5))

#tkinter setup
root = tk.Tk()
root.title("Resistance Colour Code Calculator")

#variable setup
init_value = 100
mult_value = 1.0
toler_value = 0.01
ohms = 100.0
minimum = 99.0
maximum = 101.0

#canvas section
colour_codes = {'Black': (0,0,0),
                'Brown': (163,44,46),
                'Red': (252,13,27),
                'Orange': (253,164,41),
                'Yellow': (255,253,56),
                'Green': (15,127,18),
                'Blue': (11,36,251),
                'Violet': (127,14,127),
                'Gray': (128,128,128),
                'White': (255,255,255),
                'Gold': (254,214,49),
                'Silver': (192,192,192)
    }

c = tk.Canvas(root, width=400, height=150)

c.pack()

create_resistor(colour_codes['Brown'], colour_codes['Black'], colour_codes['Black'], colour_codes['Black'], colour_codes['Brown'])

#options section
dropdown_area = tk.Frame(root)
dropdown_area.pack()

    #dropdown labels
digit1Label = tk.Label(dropdown_area, text="Digit 1", font='Arial 14 bold')
digit1Label.grid(row=0, column=0)

digit2Label = tk.Label(dropdown_area, text="Digit 2", font='Arial 14 bold')
digit2Label.grid(row=0, column=1)

digit3Label = tk.Label(dropdown_area, text="Digit 3", font='Arial 14 bold')
digit3Label.grid(row=0, column=2)

multLabel = tk.Label(dropdown_area, text="Multiplier", font='Arial 14 bold')
multLabel.grid(row=0, column=3)

tolerLabel = tk.Label(dropdown_area, text="Tolerance", font='Arial 14 bold')
tolerLabel.grid(row=0, column=4)

    #dropdown lists
digit1List = [
    "Brown: 1",
    "Red: 2",
    "Orange: 3",
    "Yellow: 4",
    "Green: 5",
    "Blue: 6",
    "Violet: 7",
    "Gray: 8",
    "White: 9"
    ]

otherDigitsList = [
    "Black: 0",
    "Brown: 1",
    "Red: 2",
    "Orange: 3",
    "Yellow: 4",
    "Green: 5",
    "Blue: 6",
    "Violet: 7",
    "Gray: 8",
    "White: 9"
    ]

multList = [
    "Black: x1",
    "Brown: x10",
    "Red: x100",
    "Orange: x1K",
    "Yellow: x10K",
    "Green: x100K",
    "Blue: x1M",
    "Violet: x10M",
    "Gray: x100M",
    "White: x1G",
    "Gold: ÷10",
    "Silver: ÷100"
    ]

tolerList = [
    "Brown: 1%",
    "Red: 2%",
    "Orange: 3%",
    "Yellow: 4%",
    "Green: 0.5%",
    "Blue: 0.25%",
    "Violet: 0.10%",
    "Gray: 0.05%",
    "Gold: 5%",
    "Silver: 10%"
    ]

    #dropdowns
digit1Var = tk.StringVar(dropdown_area)
digit1Var.set(digit1List[0])

digit2Var = tk.StringVar(dropdown_area)
digit2Var.set(otherDigitsList[0])

digit3Var = tk.StringVar(dropdown_area)
digit3Var.set(otherDigitsList[0])

multVar = tk.StringVar(dropdown_area)
multVar.set(multList[0])

tolerVar = tk.StringVar(dropdown_area)
tolerVar.set(tolerList[0])

digit1DropDown = tk.OptionMenu(dropdown_area, digit1Var, *digit1List)
digit1DropDown.grid(row=1, column=0)

digit2DropDown = tk.OptionMenu(dropdown_area, digit2Var, *otherDigitsList)
digit2DropDown.grid(row=1, column=1)

digit3DropDown = tk.OptionMenu(dropdown_area, digit3Var, *otherDigitsList)
digit3DropDown.grid(row=1, column=2)

multDropDown = tk.OptionMenu(dropdown_area, multVar, *multList)
multDropDown.grid(row=1, column=3)

tolerDropDown = tk.OptionMenu(dropdown_area, tolerVar, *tolerList)
tolerDropDown.grid(row=1, column=4)

    #dropdown tracer
def callback(*args):
    # get number from digits
    init_value = int(digit1Var.get().split(': ')[1] + digit2Var.get().split(': ')[1] + digit3Var.get().split(': ')[1])
    
    # get multiplier
    multTemp = multVar.get().split(': ')[1]
    if multTemp[0] == "÷":
        mult_value = 1/(int(multTemp.split("÷")[1]))
    else:
        multTemp = multTemp.split("x")[1]
        if multTemp[-1] == 'K':
            mult_value = int(multTemp.split('K')[0])*1000
        elif multTemp[-1] == 'M':
            mult_value = int(multTemp.split('M')[0])*1000000
        elif multTemp[-1] == 'G':
            mult_value = int(multTemp.split('G')[0])*1000000000
        else: mult_value = int(multTemp)

    # get tolerance as decimal
    toler_value = float(tolerVar.get().split(': ')[1].split('%')[0])*0.01

    # calculating resultant values
    ohms = init_value*mult_value
    minimum = ohms - (ohms*toler_value)
    maximum = ohms + (ohms*toler_value)

    #setting display labels
    def numToNumAndLetter(num):
        if num < 1000:
            return str(float(num))
        elif num < 1000000:
            return str(num/1000) + 'K'
        elif num < 1000000000:
            return str(num/1000000) + 'M'
        else:
            return str(num/1000000000) + 'G'

    ohmsValueLabel.configure(text=numToNumAndLetter(ohms)+" Ω")

    minValueLabel.configure(text=numToNumAndLetter(minimum)+" Ω")

    maxValueLabel.configure(text=numToNumAndLetter(maximum)+" Ω")
    
    tolerValueLabel.configure(text= "±" + tolerVar.get().split(': ')[1])
    
    #setting resistor graphic colours
    global colour_codes
    create_resistor(colour_codes[digit1Var.get().split(':')[0]],
                    colour_codes[digit2Var.get().split(':')[0]],
                    colour_codes[digit3Var.get().split(':')[0]],
                    colour_codes[multVar.get().split(':')[0]],
                    colour_codes[tolerVar.get().split(':')[0]])

digit1Var.trace('w', callback)
digit2Var.trace('w', callback)
digit3Var.trace('w', callback)
multVar.trace('w', callback)
tolerVar.trace('w', callback)

#value display labels
spacer = tk.Label(root, text=' ')
spacer.pack()

results_frame = tk.Frame(root)
results_frame.pack()

ohmsLabel = tk.Label(results_frame, text="Resistance: ", font='Calibri 14 bold')
ohmsLabel.grid(row=0,column=0)

ohmsValueLabel = tk.Label(results_frame, text="100.0 Ω")
ohmsValueLabel.grid(row=0,column=1)

tolerLabel = tk.Label(results_frame, text="Tolerance: ", font='Calibri 14 bold')
tolerLabel.grid(row=1,column=0)

tolerValueLabel = tk.Label(results_frame, text="±1%")
tolerValueLabel.grid(row=1,column=1)

minLabel = tk.Label(results_frame, text="Minimum: ", font='Calibri 14 bold')
minLabel.grid(row=2,column=0)

minValueLabel = tk.Label(results_frame, text="99.0 Ω")
minValueLabel.grid(row=2,column=1)

maxLabel = tk.Label(results_frame, text="Maximum: ", font='Calibri 14 bold')
maxLabel.grid(row=3,column=0)

maxValueLabel = tk.Label(results_frame, text="101.0 Ω")
maxValueLabel.grid(row=3,column=1)

#main loop
tk.mainloop()
