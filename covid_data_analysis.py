#https://www.kaggle.com/imdevskp/covid19-corona-virus-india-dataset for data sets
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("/home/rithichariharan/Downloads/datasets_549966_1376803_complete.csv")


#print(df)
name=input("Enter the name of State/UT")

filt =(df["Name of State / UT"] ==name )

y= df[filt]
#print(df.shape)

#print(y)

tab1=y["Total Confirmed cases"]
print(df.shape)
ls =[]
ls1 =[]

for i in range(0,4307):
    try:
        x=i
        y=tab1[i]

        ls.insert(i,x)
        ls1.insert(i,y)
        a=len(ls1)
        #plt.plot(x,y)
        #plt.show()

    except:
        KeyboardInterrupt
#print(ls)
#print("end")
option=input("Enter whether you want a graph or the latest number")
if option=='graph':
    plt.plot(ls,ls1)
    plt.show()
    
elif option=='latest number':
    import pyttsx3
    engine = pyttsx3.init()
        
    engine.say(ls1[a-1])
    engine.runAndWait()  
