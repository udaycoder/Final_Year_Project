import pickle
import numpy as np

from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar

model = pickle.load(open('MachineLearningModel.pkl', 'rb'))



def performPrediction(event):
    
    #perform tests on the loaded model

    inputInstance = []   #The input given by the user will be stored here
    
    inputInstance.append(int(val1.get()))
    inputInstance.append(int(val2.get()))
    inputInstance.append(int(val3.get()))
    inputInstance.append(int(val4.get()))
    inputInstance.append(int(val5.get()))
    inputInstance.append(int(val6.get()))
    inputInstance.append(int(val7.get()))
    inputInstance.append(int(val8.get()))
    inputInstance.append(int(val9.get()))
    inputInstance.append(int(val10.get()))
    inputInstance.append(int(val11.get()))
    inputInstance.append(int(val12.get()))
    inputInstance.append(int(val13.get()))
    inputInstance.append(int(val14.get()))
    inputInstance.append(int(val15.get()))
    inputInstance.append(int(val16.get()))
    inputInstance.append(int(val17.get()))
    inputInstance.append(int(val18.get()))
    inputInstance.append(int(val19.get()))
    inputInstance.append(int(val20.get()))

    inputInstance = np.array(inputInstance).reshape(1,-1)    #Reshaping the instance to be accepted by the model

    predictedOutputRating = float(model.predict(inputInstance)) #Return the Output rating to the user in the app
    
    output = str("The rating is ")+str(predictedOutputRating) 
    
    finalOutput.set(output)
    
    

root=Tk()

root.title("Tourist Destination Ratings Prediction")

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

finalOutput = StringVar()
 
Label(frame1,text="Tourist Destination Ratings Predictor").grid(row=0 , column = 10, sticky='N' , padx=4, pady = 10)

Label(frame1,text="Enter attributes in each of the below fields as 1 for present and 0 for absent and press on the submit button to get the result").grid(row=3 , column=10, sticky='N' , padx=4, pady = 10)

Label(frame2, width=9 ,text='Mountain').grid(row=4 ,column =0 , sticky='W' ,padx=1, pady = 4)
Label(frame2, width=9 ,text='Desert').grid(row=4 ,column =1 , sticky='W' ,padx=1, pady = 4)
Label(frame2, width=9 ,text='Waterfall').grid(row=4 ,column =2 , sticky='W' ,padx=1, pady = 4)
Label(frame2, width=9 ,text='Beach').grid(row=4 ,column =3 , sticky='W' ,padx=1, pady = 4)
Label(frame2, width=9 ,text='River').grid(row=4 ,column =4 , sticky='W' ,padx=1, pady = 4)
Label(frame2, width=9 ,text='Worship \n Place').grid(row=4 ,column =5 , sticky='W' ,padx=1, pady = 4)
Label(frame2, width=9 ,text='Climate').grid(row=4 ,column =6 , sticky='W' ,padx=1, pady = 4)
Label(frame2, width=9 ,text='Zoo').grid(row=4 ,column =7 , sticky='W' ,padx=1, pady = 4)
Label(frame2, width=9 ,text='Park').grid(row=4 ,column =8 , sticky='W' ,padx=1, pady = 4)
Label(frame2, width=9 ,text='Travel').grid(row=4 ,column =9 , sticky='W' ,padx=1, pady = 4)

val1=Entry(frame2, width=8 , textvariable=StringVar(frame2, value='0'))
val2=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val3=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val4=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val5=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val6=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val7=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val8=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val9=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val10=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))

val1.grid(row=5 ,column =0 , sticky='W' ,padx=1, pady = 1)
val2.grid(row=5 ,column=1, sticky='W' ,padx=1, pady = 1)
val3.grid(row=5 ,column=2 , sticky='W' ,padx=1, pady = 1)
val4.grid(row=5 ,column=3 , sticky='W' ,padx=1, pady = 1)
val5.grid(row=5 ,column=4 , sticky='W' ,padx=1, pady = 1)
val6.grid(row=5 ,column=5, sticky='W' ,padx=1, pady = 1)
val7.grid(row=5 ,column=6, sticky='W' ,padx=1, pady = 1)
val8.grid(row=5 ,column=7, sticky='W' ,padx=1, pady = 1)
val9.grid(row=5 ,column=8, sticky='W' ,padx=1, pady = 1)
val10.grid(row=5 ,column=9, sticky='W' ,padx=1, pady = 1)

Label(frame2, width=14 ,text='Archaelogical\n Site').grid(row=9 ,column =0 , sticky='W' ,padx=1, pady = 1)
Label(frame2, width=9 ,text='Festival').grid(row=9 ,column =1, sticky='W' ,padx=1, pady = 1)
Label(frame2, width=9 ,text='Pollution').grid(row=9 ,column =2 , sticky='W' ,padx=1, pady = 1)
Label(frame2, width=9 ,text='Tourist').grid(row=9 ,column =3, sticky='W' ,padx=1, pady = 1)
Label(frame2, width=9 ,text='Cuisine').grid(row=9 ,column =4, sticky='W' ,padx=1, pady = 1)
Label(frame2, width=9 ,text='Safety').grid(row=9 ,column =5, sticky='W' ,padx=1, pady = 1)
Label(frame2, width=9 ,text='Museum').grid(row=9 ,column =6, sticky='W' ,padx=1, pady = 1)
Label(frame2, width=9 ,text='Stadium').grid(row=9 ,column =7 , sticky='W' ,padx=1, pady = 1)
Label(frame2, width=9 ,text='Market').grid(row=9 ,column =8, sticky='W' ,padx=1, pady = 1)
Label(frame2, width=9 ,text='Concert').grid(row=9 ,column =9, sticky='W' ,padx=1, pady = 1)

val11=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val12=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val13=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val14=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val15=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val16=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val17=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val18=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val19=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))
val20=Entry(frame2, width=8 ,textvariable=StringVar(frame2, value='0'))

val11.grid(row=10 ,column=0, sticky='W' ,padx=1, pady = 4)
val12.grid(row=10,column=1, sticky='W' ,padx=1, pady = 4)
val13.grid(row=10,column=2, sticky='W' ,padx=1, pady = 4)
val14.grid(row=10,column=3, sticky='W' ,padx=1, pady = 4)
val15.grid(row=10,column=4, sticky='W' ,padx=1, pady = 4)
val16.grid(row=10,column=5, sticky='W' ,padx=1, pady = 4)
val17.grid(row=10,column=6, sticky='W' ,padx=1, pady = 4)
val18.grid(row=10,column=7, sticky='W' ,padx=1, pady = 4)
val19.grid(row=10,column=8, sticky='W' ,padx=1, pady = 4)
val20.grid(row=10,column=9, sticky='W' ,padx=1, pady = 4)

submitButton = Button(frame3,text="Submit")
submitButton.bind("<Button-1>",performPrediction)
submitButton.grid(row=12 , column=10, sticky='S' ,padx=4, pady = 4)


ratingsLabel = Label(frame3, textvariable = finalOutput)
ratingsLabel.grid(row=14, column=10 , padx=4, pady=4)

frame1.pack()
frame2.pack()
frame3.pack()


root.mainloop()

