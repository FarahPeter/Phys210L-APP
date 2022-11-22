#TODO: Multi Threading for the primeCheck not working somehow



import tkinter as tk 
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
#from PIL import Image,ImageTk
import PIL.Image
import PIL.ImageTk
from datetime import datetime
from datetime import date
import glob, os
import random
import math
import webbrowser
import threading
import tkinter.messagebox
from scientificCal import *







def writeToFile(Text,fileName):
    if (len(glob.glob("*.txt"))>9):
        popupmsg("Can not have more than 10 notes","Warnning!","250x100")
        return()
    f = open(fileName+".txt", "a")
    f.write(Text[0:])
    f.close()
    #open and read the file after the appending:
    #f = open(fileName+".txt", "r")
    #print(f.read())
    
def readFromFile():
    def ref():
        window.destroy()
        readFromFile()
    def refreshAndDel(filetodel):
        os.remove(filetodel)
        ref()
        
    

    window = tk.Tk()
    window.title('Update Notes')
    window.geometry("307x375")
    window.resizable(width=0, height=0)
    rows=0
    shoose0=tk.Button(window)
    shoose1=tk.Button(window)
    shoose2=tk.Button(window)
    shoose3=tk.Button(window)
    shoose4=tk.Button(window)
    shoose5=tk.Button(window)
    shoose6=tk.Button(window)
    shoose7=tk.Button(window)
    shoose8=tk.Button(window)
    shoose9=tk.Button(window)
    del0=tk.Button(window)
    del1=tk.Button(window)
    del2=tk.Button(window)
    del3=tk.Button(window)
    del4=tk.Button(window)
    del5=tk.Button(window)
    del6=tk.Button(window)
    del7=tk.Button(window)
    del8=tk.Button(window)
    del9=tk.Button(window)
    filearray=[]
    for file in glob.glob("*.txt"):
         filearray.append(file)
         f = open(file, "r")
         if (rows==0):
             shoose0=tk.Button(window, text=file+": " + str(f.read())[0:10], width=35,pady=5,fg="black",bg="#54FA9B")#,command=lambda: os.system("notepad.exe "+file))
             del0=tk.Button(window, text="Remove", width=6,pady=5,fg="black",bg="Red")#,command=lambda: refreshAndDel(file))
         elif (rows==1):
             shoose1=tk.Button(window, text=file+": " + str(f.read())[0:10], width=35,pady=5,fg="black",bg="#54FA9B")#,command=lambda: os.system("notepad.exe "+file))
             del1=tk.Button(window, text="Remove", width=6,pady=5,fg="black",bg="Red")#,command=lambda: refreshAndDel(file))
         elif (rows==2):
             shoose2=tk.Button(window, text=file+": " + str(f.read())[0:10], width=35,pady=5,fg="black",bg="#54FA9B")#,command=lambda: os.system("notepad.exe "+file))
             del2=tk.Button(window, text="Remove", width=6,pady=5,fg="black",bg="Red")#,command=lambda: refreshAndDel(file))
         elif (rows==3):
             shoose3=tk.Button(window, text=file+": " + str(f.read())[0:10], width=35,pady=5,fg="black",bg="#54FA9B")#,command=lambda: os.system("notepad.exe "+file))
             del3=tk.Button(window, text="Remove", width=6,pady=5,fg="black",bg="Red")#,command=lambda: refreshAndDel(file))
         elif (rows==4):
             shoose4=tk.Button(window, text=file+": " + str(f.read())[0:10], width=35,pady=5,fg="black",bg="#54FA9B")#,command=lambda: os.system("notepad.exe "+file))
             del4=tk.Button(window, text="Remove", width=6,pady=5,fg="black",bg="Red")#,command=lambda: refreshAndDel(file))
         elif (rows==5):
             shoose5=tk.Button(window, text=file+": " + str(f.read())[0:10], width=35,pady=5,fg="black",bg="#54FA9B")#,command=lambda: os.system("notepad.exe "+file))
             del5=tk.Button(window, text="Remove", width=6,pady=5,fg="black",bg="Red")#,command=lambda: refreshAndDel(file))
         elif (rows==6):
             shoose6=tk.Button(window, text=file+": " + str(f.read())[0:10], width=35,pady=5,fg="black",bg="#54FA9B")#,command=lambda: os.system("notepad.exe "+file))
             del6=tk.Button(window, text="Remove", width=6,pady=5,fg="black",bg="Red")#,command=lambda: refreshAndDel(file))
         elif (rows==7):
             shoose7=tk.Button(window, text=file+": " + str(f.read())[0:10], width=35,pady=5,fg="black",bg="#54FA9B")#,command=lambda: os.system("notepad.exe "+file))
             del7=tk.Button(window, text="Remove", width=6,pady=5,fg="black",bg="Red")#,command=lambda: refreshAndDel(file))
         elif (rows==8):
             shoose8=tk.Button(window, text=file+": " + str(f.read())[0:10], width=35,pady=5,fg="black",bg="#54FA9B")#,command=lambda: os.system("notepad.exe "+file))
             del8=tk.Button(window, text="Remove", width=6,pady=5,fg="black",bg="Red")#,command=lambda: refreshAndDel(file))
         elif (rows==9):
             shoose9=tk.Button(window, text=file+": " + str(f.read())[0:10], width=35,pady=5,fg="black",bg="#54FA9B")#,command=lambda: os.system("notepad.exe "+file))
             del9=tk.Button(window, text="Remove", width=6,pady=5,fg="black",bg="Red")#,command=lambda: refreshAndDel(file))
            
         rows=rows+1
         f.close()
    if (len(filearray)>0):
        shoose0['command']=lambda: os.system("notepad.exe "+filearray[0])
        del0['command']=lambda: refreshAndDel(filearray[0])
        shoose0.grid (row=0,column=0)
        del0.grid (row=0,column=1)
    if (len(filearray)>1):
        shoose1['command']=lambda: os.system("notepad.exe "+filearray[1])
        del1['command']=lambda: refreshAndDel(filearray[1])
        shoose1.grid (row=1,column=0)
        del1.grid (row=1,column=1)
    if (len(filearray)>2):
        shoose2['command']=lambda: os.system("notepad.exe "+filearray[2])
        del2['command']=lambda: refreshAndDel(filearray[2])
        shoose2.grid (row=2,column=0)
        del2.grid (row=2,column=1)
    if (len(filearray)>3):
        shoose3['command']=lambda: os.system("notepad.exe "+filearray[3])
        del3['command']=lambda: refreshAndDel(filearray[3])
        shoose3.grid (row=3,column=0)
        del3.grid (row=3,column=1)
    if (len(filearray)>4):
        shoose4['command']=lambda: os.system("notepad.exe "+filearray[4])
        del4['command']=lambda: refreshAndDel(filearray[4])
        shoose4.grid (row=4,column=0)
        del4.grid (row=4,column=1)
    if (len(filearray)>5):
        shoose5['command']=lambda: os.system("notepad.exe "+filearray[5])
        del5['command']=lambda: refreshAndDel(filearray[5])
        shoose5.grid (row=5,column=0)
        del5.grid (row=5,column=1)
    if (len(filearray)>6):
        shoose6['command']=lambda: os.system("notepad.exe "+filearray[6])
        del6['command']=lambda: refreshAndDel(filearray[6])
        shoose6.grid (row=6,column=0)
        del6.grid (row=6,column=1)
    if (len(filearray)>7):
        shoose7['command']=lambda: os.system("notepad.exe "+filearray[7])
        del7['command']=lambda: refreshAndDel(filearray[7])
        shoose7.grid (row=7,column=0)
        del7.grid (row=7,column=1)
    if (len(filearray)>8):
        shoose8['command']=lambda: os.system("notepad.exe "+filearray[8])
        del8['command']=lambda: refreshAndDel(filearray[8])
        shoose8.grid (row=8,column=0)
        del8.grid (row=8,column=1)
    if (len(filearray)>9):
        shoose9['command']=lambda: os.system("notepad.exe "+filearray[9])
        del9['command']=lambda: refreshAndDel(filearray[9])
        shoose9.grid (row=9,column=0)
        del9.grid (row=9,column=1)
    
    refresh=tk.Button(window, text="Refresh", width=5,pady=5,fg="black",bg="blue",command=lambda: ref())
    refresh.grid (row=rows+1,column=0,columnspan=2)
    window.mainloop()

    
    
def random_exclusion(start, stop, excluded) -> int:
    """Function for getting a random number with some numbers excluded"""
    excluded = set(excluded)
    value = random.randint(start, stop - len(excluded)) # Or you could use randrange
    for exclusion in tuple(excluded):
        if value < exclusion:
            break
        value += 1
    return value

#Most efficent way to check for primenumbers
def primecheck(numberToCheck,Certainty=0.99999):
    if (numberToCheck<2):
        return (False,1)
    elif (numberToCheck==2):
        return (True,1)
    elif (numberToCheck%2==0):
        return (False,1)
    else:
        q=numberToCheck-1
        k=0
        while(True):
            if (q%2==0):
                q=int(q/2)
                k=k+1
            else:
                break
        t=-int(math.log10(1-Certainty)/math.log10(4))+1
        excludeFroma=[]
        for i in range (t):
            maybePrime=False
            if (len(excludeFroma)<numberToCheck-4):
                a=random_exclusion(2,numberToCheck-2,excludeFroma)
            else:
                return (True,1)
            excludeFroma.append(a)
            if ((a**q) % numberToCheck ==1):
                maybePrime=True
            else:
                for j in range (0,k):
                    if(((a**((2**j) * q)) % numberToCheck )==numberToCheck-1):
                        maybePrime=True
            if (maybePrime==False):
                return (False,1)
        return (True,1-4**-t)#return if prime or not with the certainty of the awnser







def ErrorUncertaintyRounding(e):#to the first significant bit
    e=e+0.000000000001
    if (e>=1):
        i=0
        while (True):
            if (e*10**i < 10):
                if (int (e*10**i) ==1 or int(e*10**i)==2):
                    return (round(e*10**i,1) * 10**(abs(i)))
                else:
                    return (round(e*10**i,0)* 10**(abs(i)))
            i=i-1
    i=0
    while (True):
        if (e*10**i >= 1):
            if (int (e*10**i) ==1 or int(e*10**i)==2):
                return (round(e,i+1))
            else:
                return (round(e,i))
        i=i+1

def MatchValueRoundingWithErrorRounding(value,roudedError):#match rouding of value with the rounding of error
    value=value+0.000000000001
    stringRoudedError=str (roudedError)
    if (roudedError<1):
        return (round(value,len(stringRoudedError)-2))
    else:
        poww=0
        for i in range (len(stringRoudedError)):
            if (stringRoudedError[i]=='.'):
                poww=i
                break
        return ((round(value*10**-poww,1))*10**poww)

        
def BestEstimateAndUncertainty(a):#takes an array of all mesurments and gives the average and the standard deviation of the mean
    average=0
    l=len(a)
    for i in range (l):
        average=average+a[i]
    average=average/l
    uncertainty=0
    for i in range (l):
        uncertainty=uncertainty+((a[i]-average)**2)
    uncertainty=((uncertainty)/(l*(l-1)))**(1/2)
    uncertainty=ErrorUncertaintyRounding(uncertainty)
    average=MatchValueRoundingWithErrorRounding(average,uncertainty)
    return([average,uncertainty])
    
def PropagationOfUncertainties():
    print("                                 2                2                2  0.5")
    print("Uncertainty of F = [ (dF * uncX)^  +  (dF * uncY)^  +  (dF * uncz)^  ]^")    
    print("                      dx               dy               dz")

def AcceptableMesurmentComparedToExperimental(roundedValue,roundedError,mesuredValue): #checks if the mesured value is in the range of best estimated value +- 2 uncertainty
    if (mesuredValue <= roundedValue + 2*roundedError and mesuredValue >= roundedValue - 2*roundedError):
        return ("Accepted")
    return("Rejected")

def CompareTwoExperimentalResults(roundedValue1,roundedError1,roundedValue2,roundedError2): #check if one of 2 experimental best estimate with their ranges fits inside the other 
    if (roundedValue1+2*roundedError1 <= roundedValue2+2*roundedError2 and roundedValue1-2*roundedError1 >= roundedValue2-2*roundedError2 ):
        return("Overlap")
    if (roundedValue2+2*roundedError2 <= roundedValue1+2*roundedError1 and roundedValue2-2*roundedError2 >= roundedValue1-2*roundedError2 ):
        return("Overlap")
    return("Do not Fully Overlap")

def LinearLineOfBestFit(y,x):#with correlation coeficient 0<= r <= 1 and uncertainties for a and b
    if (len(y)!=len(x)):
        print("Unmatshed length of X and Y")
        return ([None,None,None,None,None])
    try:
        l=len(y)
        AverageOfy=0
        AverageOfx=0
        for i in range (l):
            AverageOfy=AverageOfy+y[i]
            AverageOfx=AverageOfx+x[i]
        AverageOfy=AverageOfy/l
        AverageOfx=AverageOfx/l
        
        
        ANumerator=0
        ADenomenator=0
        for i in range (l):
            ANumerator=ANumerator+((y[i]-AverageOfy)*(x[i]-AverageOfx))
            ADenomenator=ADenomenator+(x[i]-AverageOfx)**2
        a=ANumerator/ADenomenator
        b=AverageOfy-a*AverageOfx
        
        r=0 #correlation coef
        for i in range (l):
            r=r+( (y[i] - AverageOfy)**2 )
        r=ANumerator/(ADenomenator*r)**0.5
        
        
        sumOfxTwo=0
        sumOfx=0
        for i in range (l):
            sumOfxTwo=sumOfxTwo+ x[i]**2
            sumOfx=sumOfx+x[i]
        delta=l*sumOfxTwo -(sumOfx)**2
        
        sume=0
        for i in range (l):
            sume=sume + (a*x[i] + b-y[i])**2
        
        uncA= ( ((l)/(l-2)) * sume/delta  )**0.5 #uncertainty with B
        uncB= ( (1/(l-2)) * sume*sumOfxTwo/delta)**0.5
        uncA=ErrorUncertaintyRounding(uncA)
        uncB=ErrorUncertaintyRounding(uncB)
        
        # return line of best fit = ax+b
        # return corellation coeficient = r
        #returns uncertainties with a and b = uncA, uncB
        return ([a,b,r,uncA,uncB]) 
    except ZeroDivisionError:
        print("Line estimate for one point is not definned")
        return("error")












#for error messages
def popupmsg(msg,tit="Warning!",size="300x80"):

    popup = tk.Tk()
    popup.geometry(size)
    popup.wm_title(tit)
    popup.resizable(width=0, height=0)
    label = tk.Label(popup, text=msg, font="NORM_FONT", wraplength=500)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="OK", command = popup.destroy)
    B1.pack()
    popup.mainloop()    




# plot function is created for 
# plotting the graph in 
# tkinter window
def plot(a,b,x,y,whoCalled):
     
    def plotNow(a,b,x,y):
        # the figure that will contain the plot
        fig = Figure(figsize = (4, 4),
                     dpi = 110)
      
        # adding the subplot
        plot1 = fig.add_subplot(111)
        # plotting the graph
        plot1.scatter(x,y,label = "Points",color="blue")
        plot1.plot(x,y,label = "Points",color="blue")
        if (a!='a' and  b!='a'):
            yy=[0]*len(x)
            for i in range (len(x)):
                yy[i]=a*x[i]+b
            plot1.plot(x,yy,label = "Best Fit",color="red")
            
      
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,master = window)  
        canvas.draw()
      
        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()
        
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,window)
        toolbar.update()
      
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()
    
    
    # the main Tkinter window
    window = tk.Tk()
      
    # setting the title 
    if (whoCalled=="bestFit"):
        window.title('Linear best fit and raw plot')
    elif(whoCalled=="plots"):
        window.title('Raw plot')
    # dimensions of the main window
    window.geometry("500x500")
    window.resizable(width=0, height=0)
      
    # displays the plot
    plotNow(a,b,x,y)
      
    # place the button 
    # in main window
      
    # run the gui
    window.mainloop()



def DisplayImage(x):
    p=tk.Toplevel()
    p.wm_title("Phys210L Cheat sheet #"+x)
    p.geometry("750x700")
    canvas= Canvas(p,width=750,height=700)
    canvas.pack(anchor='center')
    im= PIL.Image.open(str(x)+".PNG")
    resized_image= im.resize((700,700))
    new_image= PIL.ImageTk.PhotoImage(resized_image)
    canvas.create_image(10,10, anchor=NW, image=new_image)
    p.mainloop()



def iExit():
    iExit = tkinter.messagebox.askyesno("Exit","Do you want to exit ?")
    if iExit > 0:
        master.destroy()
        return












def check(whoCalled,inputt=""):
    if (whoCalled=="clearOutput"):
         output['text']=""
         return()
    if (whoCalled=="clear"):
         inputt.delete(0,'end')
         output['text']=""
         return()
    else:
        try:
            if (len(inputt)==0 and whoCalled!="errorPropagation"):
                 popupmsg("Needed input")
                 return()
        
            def checkonestringinput(inn):
                dot=0
                if (inn==''):
                    popupmsg("Invalid Input")
                    return("Invalid")
                for i in inn:
                    if (i!='0' and i!='1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9' and i!='.' and i!='-'):
                        popupmsg("Invalid Input")
                        return("Invalid")
                    if (i=='.'):
                        if(dot>0):
                            popupmsg("Invalid Input")
                            return ("Invalid")
                        dot=dot+1
                return("Valide")
                            
                # if (inn[0]=='.' or inn[ len(inn)-1]=='.'):
                #     popupmsg("Invalid Input")
            
            
            if (whoCalled=="roundError"):
                check=checkonestringinput(inputt)
                if (check=="Invalid"):
                    return()
                res=ErrorUncertaintyRounding(float(inputt))
                if (res==10**-12):
                    output['text']=("Error= 0")
                else:
                    output['text']=("Error=" + str(res))
            
            elif (whoCalled=="errorPropagation"):
                popupmsg("Uncertainty of F = [(df/dx *uncX)^2 + (df/dy *uncY)^2 + (df/dZ *uncZ)^2 +...]^0.5","Error propagation Formula","500x100")
           
            elif (whoCalled=="CheckPrime"):
                a=[0,0]
                twoInputs=0
                ends=0
                for i in range (len(inputt)):
                    if (inputt[i]==','):
                        twoInputs=twoInputs+1
                        check=checkonestringinput(inputt[0:i:1])
                        if (check=="Invalid"):
                            return()
                        check=checkonestringinput(inputt[i+1:len(inputt):1])
                        if (check=="Invalid"):
                            return()
                        ends=i
                if(twoInputs!=1):
                    check=popupmsg("Check Prime only takes 2 inputs ex: 17,0.999","Warning!","500x80")
                    return()
                a[0]=float(inputt[0:ends:1])
                a[1]=float(inputt[ends+1:len(inputt):1])
                if (int(a[0])!=a[0]):
                    check=popupmsg("Check Prime first input is an integer ex: 17,0.98","Warning!","500x80")
                    return()
                if ( a[1]>1 or a[1]<0):
                    check=popupmsg("Check Prime second input is between 0 and 1 ex: 17,0.95","Warning!","500x80")
                    return()
                res= primecheck(int(abs(a[0])),a[1])
                #res=[0,0]
                #t1 = threading.Thread(target=primecheck, args=(int(a[0]),a[1],))
                #t1.start()
                #t1.join()
                if (res[0]==True):
                    output['text']=(str(int(abs(a[0])))+" is a prime number with certainty:"+str(res[1]))
                elif (res[0]==False):
                    output['text']=(str(int(abs(a[0])))+" is a composite number with certainty: 1")
                
            elif (whoCalled=="roundValue"):
                a=[0,0]
                twoInputs=0
                ends=0
                for i in range (len(inputt)):
                    if (inputt[i]==','):
                        twoInputs=twoInputs+1
                        check=checkonestringinput(inputt[0:i:1])
                        if (check=="Invalid"):
                            return()
                        check=checkonestringinput(inputt[i+1:len(inputt):1])
                        if (check=="Invalid"):
                            return()
                        ends=i
                if(twoInputs!=1):
                    check=popupmsg("round value only takes 2 inputs ex: 1.5,2.2","Warning!","500x80")
                    return()
                a[0]=float(inputt[0:ends:1])
                a[1]=float(inputt[ends+1:len(inputt):1])
                
                res= MatchValueRoundingWithErrorRounding(a[0],a[1])
                output['text']=("Value=" + str(res))
                
            elif (whoCalled=="bestEstimateAndUncertainty" or whoCalled=="bestFit" or whoCalled=="plots" ):
                a=[]
                start=0
                inputt=inputt+","
                for i in range (len(inputt)):
                    if (inputt[i]==','):
                        check=checkonestringinput(inputt[start:i:1])
                        if (check=="Invalid"):
                            return()
                        a.append(float(inputt[start:i:1]))
                        start=i+1
                if (whoCalled=="bestEstimateAndUncertainty"):
                        if (len(a)<2):
                            popupmsg("At least 2 values needed")
                            return ("")
                        res=BestEstimateAndUncertainty(a)
                        if (res[1]==10**-12):
                            output['text']=("Best estimate=" + str(res[0])+" ; " +"Uncertainty= 0")
                        else:
                            output['text']=("Best estimate=" + str(res[0])+" ; " +"Uncertainty=" + str(res[1]))
                        
                elif(whoCalled=="bestFit" or whoCalled=="plots"):
                    if (len(a)%2!=0):
                        popupmsg("best Fit / PLot should have same Xs and Ys ex:0,1,1,2 x=[0,1] y=[1,2]","Warning!","700x80")
                        return ("")
                    if (len(a)<6):
                        popupmsg("At least 3 points needed")
                        return ("")
                    if (whoCalled=="bestFit"):
                        d=int(len(a)/2)
                        x=[0]*d
                        y=[0]*d    
                        for i in range (d):
                            x[i]=a[i]
                            y[i]=a[i+d]
                        res=LinearLineOfBestFit(y,x)
                        if (res=="error"):
                            popupmsg("Can not fit this input")
                            return()
                        if(res[3]==10**-12 and res[4]==10**-12):
                            output['text']=("Line of best fit(aX+b)=" + str(MatchValueRoundingWithErrorRounding(res[0],res[3]))+"X + " + str(MatchValueRoundingWithErrorRounding(res[1],res[4])) + " ; Corellation coeficient r="+ str(round(float(res[2]),5))+ " ; Uncertainties of a= 0" + " ; Uncertainties of b= 0")
                        elif(res[3]==10**-12):
                            output['text']=("Line of best fit(aX+b)=" + str(MatchValueRoundingWithErrorRounding(res[0],res[3]))+"X + " + str(MatchValueRoundingWithErrorRounding(res[1],res[4])) + " ; Corellation coeficient r="+ str(round(float(res[2]),5))+ " ; Uncertainties of a= 0" + " ; Uncertainties of b="+ str(res[4]))
                        elif(res[4]==10**-12):
                            output['text']=("Line of best fit(aX+b)=" + str(MatchValueRoundingWithErrorRounding(res[0],res[3]))+"X + " + str(MatchValueRoundingWithErrorRounding(res[1],res[4])) + " ; Corellation coeficient r="+ str(round(float(res[2]),5))+ " ; Uncertainties of a="+ str(res[3]) + " ; Uncertainties of b= 0")
                        else:
                            output['text']=("Line of best fit(aX+b)=" + str(MatchValueRoundingWithErrorRounding(res[0],res[3]))+"X + " + str(MatchValueRoundingWithErrorRounding(res[1],res[4])) + " ; Corellation coeficient r="+ str(round(float(res[2]),5))+ " ; Uncertainties of a="+ str(res[3])+ " ; Uncertainties of b="+ str(res[4]))
                        plot(res[0],res[1],x,y,whoCalled)
                    elif(whoCalled=="plots"):
                        d=int(len(a)/2)
                        x=[0]*d
                        y=[0]*d    
                        for i in range (d):
                            x[i]=a[i]
                            y[i]=a[i+d]
                        output['text']=""
                        plot("a","a",x,y,whoCalled)
                        
            
            elif(whoCalled=="compareExVm"):
                a=[]
                start=0
                inputt=inputt+","
                onlyThreeIn=0
                for i in range (len(inputt)):
                    if (inputt[i]==','):
                        check=checkonestringinput(inputt[start:i:1])
                        if (check=="Invalid"):
                            return()
                        a.append(float(inputt[start:i:1]))
                        start=i+1
                        onlyThreeIn=onlyThreeIn+1
                if (onlyThreeIn!=3):
                    popupmsg("Compare mesurment to experiment takes only 3 values as such: roundedValue,roundedError,mesuredValue","Warning!","600x100")
                    return ("")
                res=AcceptableMesurmentComparedToExperimental(a[0],a[1],a[2])
                output['text']=res
                
            elif(whoCalled=="compareExVEx"):
                a=[]
                start=0
                inputt=inputt+","
                onlyFourIn=0
                for i in range (len(inputt)):
                    if (inputt[i]==','):
                        check=checkonestringinput(inputt[start:i:1])
                        if (check=="Invalid"):
                            return()
                        a.append(float(inputt[start:i:1]))
                        start=i+1
                        onlyFourIn=onlyFourIn+1
                if (onlyFourIn!=4):
                    popupmsg("Compare experiment to experiment takes only 4 values as such: roundedValue1,roundedError1,roundedValue2,roundedError2","Warning!","600x100")
                    return ("")
                res=CompareTwoExperimentalResults(a[0],a[1],a[2],a[3])
                output['text']=res
        except:
            popupmsg("Something went wrong! Check your input. You can check the help option in the menu bar for the format of inputs of each operation.","Warning!","600x100")
            return ("")




#UI
master = tk.Tk()
master.wm_title("Phys210L Calculator")
master.geometry("450x300")
# photo = PhotoImage(file = "LOGO.png")
# master.iconphoto(False, photo)
#master.minsize(450, 300)
# set maximum window size value
#master.maxsize(450, 300)
master.resizable(width=0, height=0)


#master.columnconfigure(index=1, weight=1)
#master.rowconfigure(index=7, weight=3)

roundError=tk.Button(master, text="Round Error", width=20,pady=5,fg="black",bg="#263D42",command=lambda: check("roundError",inputt.get()))
roundError.grid (row=1,column=0)

roundValue=tk.Button(master, text="Round value", width=20,pady=5,fg="black",bg="#263D42",command=lambda: check("roundValue",inputt.get()))
roundValue.grid  (row=1,column=1)

bestEstimateAndUncertainty=tk.Button(master,text="Best estimate",width=20,pady=5,fg="black",bg="#263D42",command=lambda: check("bestEstimateAndUncertainty",inputt.get()))
bestEstimateAndUncertainty.grid  (row=1,column=2)

bestFit=tk.Button(master, text="Best fit",width=20,pady=5,fg="black",bg="#263D42",command=lambda: check("bestFit",inputt.get()))
bestFit.grid  (row=2,column=0)

plots=tk.Button(master,text="Plot",width=20,pady=5,fg="black",bg="#263D42",command=lambda: check("plots",inputt.get()))
plots.grid   (row=2,column=1)

compareExVm=tk.Button(master, text="Compare mes vs xp",width=20,pady=5,fg="black",bg="#263D42",command=lambda: check("compareExVm",inputt.get()))
compareExVm.grid  (row=2,column=2)

compareExVEx=tk.Button(master, text="Compare xp vs xp",width=20,pady=5,fg="black",bg="#263D42",command=lambda: check("compareExVEx",inputt.get()))
compareExVEx.grid  (row=3,column=0)

errorPropagation=tk.Button(master,text="Error propagation",width=20,pady=5,fg="black",bg="#263D42",command=lambda: check("errorPropagation"))
errorPropagation.grid   (row=3,column=1)

CheckPrime=tk.Button(master, text="Check Prime", width=20,pady=5,fg="black",bg="#263D42",command=lambda: check("CheckPrime",inputt.get()))#threading.Thread(target=check, args=("CheckPrime",inputt.get())).start())
CheckPrime.grid (row=3,column=2)

creatNote=tk.Button(master, text="Create Note", width=20,pady=5,fg="black",bg="light green",command=lambda: writeToFile(str(inputt.get()),str( date.today().strftime("%b-%d-%Y"))+"__"+str(datetime.now().strftime("%H-%M-%S"))))
creatNote.grid (row=4,column=0)

updateNote=tk.Button(master, text="Update Notes", width=20,pady=5,fg="black",bg="light green",command=lambda: readFromFile())
updateNote.grid (row=4,column=1)

# exitt=tk.Button(master,text="Exit",width=20,pady=5,fg="black",bg="Red",command=lambda: master.destroy())
# exitt.grid   (row=4,column=2)

scientificCal=tk.Button(master, text="Scientific calculator", width=20,pady=5,fg="black",bg="green",command=lambda: scientificCalculator())
scientificCal.grid (row=4,column=2)

clearOutput=tk.Button(master,text="Clear Output",width=20,fg="black",bg="pink",command=lambda: check("clearOutput"))
clearOutput.grid   (row=5,column=1)

clearInput=tk.Button(master,text="Clear Input",width=20,fg="black",bg="pink",command=lambda: inputt.delete(0,'end') )
clearInput.grid   (row=5,column=2)

clear=tk.Button(master,text="Clear",width=20,fg="black",bg="pink",command=lambda: check("clear",inputt))
clear.grid   (row=5,column=0)




inputt = tk.Entry(master,width=74)
inputt.grid(row=0, column=0,columnspan = 3)

# placeholder1=output =tk.Label(master,text="")
# placeholder1.grid(row=0,column=2)
# placeholder2=output =tk.Label(master,text="")
# placeholder2.grid(row=1,column=2)
# placeholder3=output =tk.Label(master,text="")
# placeholder3.grid(row=2,column=2)
# placeholder4=output =tk.Label(master,text="")
# placeholder4.grid(row=3,column=2)
# placeholder5=output =tk.Label(master,text="")
# placeholder5.grid(row=4,column=2)
# placeholder6=output =tk.Label(master,text="")
# placeholder6.grid(row=5,column=2)
# placeholder7=output =tk.Label(master,text="")
# placeholder7.grid(row=6,column=2)

output =tk.Label(master,text="",fg="black",pady=0, padx=10, font=10,wraplength=400)
output.grid(row=6,column=0,columnspan = 3)


menubar = tk.Menu(master)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Round Error",command=lambda: popupmsg("Takes a float number as input and rounds it to the first significant number, except if the first significant number is 1 or 2 then keeps 2 significant digits","More info about Round Error","500x130"))
helpmenu.add_command(label="Round value",command=lambda: popupmsg("Takes 2 float numbers as inputs ex of input: 1.5888,0.21 And rounds the first one(the value) to match the precision of the second one(the uncertainty)","More info about Round value","600x120"))
helpmenu.add_command(label="Best estimate",command=lambda: popupmsg("Takes as inputs all mesurments ex: 1.5,2.6,3.7,5.5 and gives the average and the standard deviation of the mean (the uncertainty)","More info about Best estimate","600x100"))
helpmenu.add_command(label="Best fit",command=lambda: popupmsg("Takes as inputs all values of x flowed by all values of y ex: 1,2,3,2,4,6 where x1=1 x2=2 x3=3 and y1=2 y2=4 y3=6 And gives the slope and y intercept of the linear line of best fit and their errors, and the correlation coeficient r between x and y, and plots the values of y against x according to the inputed values and the line of best fit","More info about Best fit","600x200"))
helpmenu.add_command(label="Plot",command=lambda: popupmsg("Takes as inputs all values of x flowed by all values of y ex: 1,2,3,2,4,6 where x1=1 x2=2 x3=3 and y1=2 y2=4 y3=6 And plots the values of y against x according to the inputed values","More info about Plot","600x130"))
helpmenu.add_command(label="Compare mes vs xp",command=lambda: popupmsg("Takes as input roundedValue,roundedError,mesuredValue ex: 2.2,0.5,2.3 And checks if the mesured value is in the range of best estimated value +- 2*uncertainty","More info about Compare mesurment vs experiment","600x120"))
helpmenu.add_command(label="Compare xp vs xp",command=lambda: popupmsg("Takes as inputs roundedValue1,roundedError1,roundedValue2,roundedError2 ex: 2.2,0.5,2.6,0.4 And check if one of 2 experimental best estimate with their ranges fits inside the other","More info about Compare experiment vs experiment","600x150"))
helpmenu.add_command(label="Error propagation",command=lambda: popupmsg("Gives The formula of error propagation inside function (no input needed)","More info about Error propagation","500x80"))
helpmenu.add_command(label="Check Prime",command=lambda: popupmsg("Takes as input the integer number to check for primality and the certainty of the awnser needed, ex: 17,0.9999","More info about Check Prime","500x100"))
helpmenu.add_command(label="Creat Note",command=lambda: popupmsg("Takes any input and saves it as a txt","More info about Save Note","300x80"))
helpmenu.add_command(label="Update Notes",command=lambda: popupmsg("Update or delete taken notes","More info about Update Notes","300x80"))
helpmenu.add_command(label="Scientific Calculator",command=lambda: popupmsg("Open scientific calculator. This is a 3rd party app","More info about Scientific Calculator","500x100"))
helpmenu.add_separator()
helpmenu.add_command(label="Exit",command=lambda: iExit())
menubar.add_cascade(label="Help", menu=helpmenu)

sheets=tk.Menu(menubar, tearoff=0)
sheets.add_command(label="1",command=lambda: DisplayImage("1"))
sheets.add_command(label="2",command=lambda: DisplayImage("2"))
sheets.add_command(label="3",command=lambda: DisplayImage("3"))
menubar.add_cascade(label="Cheat sheets", menu=sheets)

aboutmenu=tk.Menu(menubar, tearoff=0)
aboutmenu.add_command(label="Course Sylabus",command=lambda:webbrowser.open('https://www.aub.edu.lb/fas/physics/Documents/phys%20210L.pdf'))
aboutmenu.add_command(label="App functionality",command=lambda: popupmsg("This app is to help in calculations in the Phys210L course at AUB","App Functionality","500x80"))
aboutmenu.add_command(label="Version",command=lambda: popupmsg("Last Updated 22/11/2022\n \n V1.1","Version","200x120"))
aboutmenu.add_command(label="About",command=lambda: popupmsg("By Peter Farah","About","200x80"))
menubar.add_cascade(label="About", menu=aboutmenu)

contact=tk.Menu(menubar, tearoff=0)
contact.add_command(label="Report Bug",command=lambda: popupmsg("Send an email to psf04@mail.aub.edu","Report Bug"))
contact.add_command(label="GitHub",command=lambda:webbrowser.open('https://github.com/FarahPeter?tab=repositories'))
menubar.add_cascade(label="Contact", menu=contact)


master.config(menu=menubar)
master.mainloop()

