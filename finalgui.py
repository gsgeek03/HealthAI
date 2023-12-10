from tkinter import *
from tkinter import simpledialog
import pandas as pd
from tabulate import tabulate
import numpy as np
from sklearn.cluster import KMeans
import tkinter as tk
from tkinter import simpledialog
from tkinter import Entry, Label, Button, ttk
main_win = Tk()

def Weight_Loss():
    print(" Age : %s Years \n Weight: %s Kg \n Height: %s m \n" % (e1.get(), e3.get(), e4.get()))    
    
    ROOT = tk.Tk()
    
    ROOT.withdraw()
    
    USER_INP = simpledialog.askstring(title="Food Timing",
                                      prompt="Enter 1 for Breakfast, 2 for Lunch and 3 for Dinner")
    
    
    data=pd.read_csv('input.csv')
    
    
    Breakfastdata=data['Breakfast']
    BreakfastdataNumpy=Breakfastdata.to_numpy()
    
    Lunchdata=data['Lunch']
    LunchdataNumpy=Lunchdata.to_numpy()
    
    Dinnerdata=data['Dinner']
    DinnerdataNumpy=Dinnerdata.to_numpy()
    
    Food_itemsdata=data['Food_items']
    breakfastfoodseparated=[]
    Lunchfoodseparated=[]
    Dinnerfoodseparated=[]
    
    breakfastfoodseparatedID=[]
    LunchfoodseparatedID=[]
    DinnerfoodseparatedID=[]
    
    for i in range(len(Breakfastdata)):
      if BreakfastdataNumpy[i]==1:
        breakfastfoodseparated.append(Food_itemsdata[i])
        breakfastfoodseparatedID.append(i)
      if LunchdataNumpy[i]==1:
        Lunchfoodseparated.append(Food_itemsdata[i])
        LunchfoodseparatedID.append(i)
      if DinnerdataNumpy[i]==1:
        Dinnerfoodseparated.append(Food_itemsdata[i])
        DinnerfoodseparatedID.append(i)
        
        
    LunchfoodseparatedIDdata = data.iloc[LunchfoodseparatedID]
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.T
    val=list(np.arange(5,16))
    Valapnd=[0]+[4]+val
    LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.iloc[Valapnd]
    LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.T
    
    breakfastfoodseparatedIDdata = data.iloc[breakfastfoodseparatedID]
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
    val=list(np.arange(5,16))
    Valapnd=[0]+[4]+val
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.iloc[Valapnd]
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
    
    DinnerfoodseparatedIDdata = data.iloc[DinnerfoodseparatedID]
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
    val=list(np.arange(5,16))
    Valapnd=[0]+[4]+val
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.iloc[Valapnd]
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
    
    age=int(e1.get())
    weight=float(e3.get())
    height=float(e4.get())
    bmi = weight/(height**2) 
    
    for lp in range (0,80,10):
        test_list=np.arange(lp,lp+10)
        for i in test_list: 
            if(i == age):
                print('age is between',str(lp),str(lp+10))
                agecl=round(lp/20)    
   
    print("Your body mass index is: ", bmi)
    if ( bmi < 16):
        print("severely underweight")
        clbmi=4
    elif ( bmi >= 16 and bmi < 18.5):
        print("underweight")
        clbmi=3
    elif ( bmi >= 18.5 and bmi < 25):
        print("Healthy")
        clbmi=2
    elif ( bmi >= 25 and bmi < 30):
        print("overweight")
        clbmi=1
    elif ( bmi >=30):
        print("severely overweight")
        clbmi=0
    
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.to_numpy()
    LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.to_numpy()
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.to_numpy()
    ti=(clbmi+agecl)/2
    
    ## K-Means Based  Dinner Food
    Datacalorie=DinnerfoodseparatedIDdata[1:,1:len(DinnerfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0, n_init=10).fit(X)
    XValu=np.arange(0,len(kmeans.labels_))
    dnrlbl=kmeans.labels_
    
    ## K-Means Based  Lunch Food
    Datacalorie=LunchfoodseparatedIDdata[1:,1:len(LunchfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0, n_init=10).fit(X)
    XValu=np.arange(0,len(kmeans.labels_))
    lnchlbl=kmeans.labels_
    
    ## K-Means Based  Breakfast Food
    Datacalorie=breakfastfoodseparatedIDdata[1:,1:len(breakfastfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0, n_init=10).fit(X)
    XValu=np.arange(0,len(kmeans.labels_))
    brklbl=kmeans.labels_
    
    ## Reading of the Dataset
    datafin=pd.read_csv('inputfin.csv')
    
    dataTog=datafin.T

    bmicls=[0,1,2,3,4]
    agecls=[0,1,2,3,4]
    
    weightlosscat = dataTog.iloc[[1,2,7,8]]
    weightlosscat=weightlosscat.T
    weightgaincat= dataTog.iloc[[0,1,2,3,4,7,9,10]]
    weightgaincat=weightgaincat.T
    healthycat = dataTog.iloc[[1,2,3,4,6,7,9]]
    healthycat=healthycat.T
    weightlosscatDdata=weightlosscat.to_numpy()
    weightgaincatDdata=weightgaincat.to_numpy()
    healthycatDdata=healthycat.to_numpy()
    weightlosscat=weightlosscatDdata[1:,0:len(weightlosscatDdata)]
    weightgaincat=weightgaincatDdata[1:,0:len(weightgaincatDdata)]
    healthycat=healthycatDdata[1:,0:len(healthycatDdata)]
    
    weightlossfin=np.zeros((len(weightlosscat)*5,6),dtype=np.float32)
    weightgainfin=np.zeros((len(weightgaincat)*5,10),dtype=np.float32)
    healthycatfin=np.zeros((len(healthycat)*5,9),dtype=np.float32)
    
    t=0
    r=0
    s=0
    yt=[]
    yr=[]
    ys=[]
    for zz in range(5):
        for jj in range(len(weightlosscat)):
            valloc=list(weightlosscat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightlossfin[t]=np.array(valloc)
            yt.append(brklbl[jj])
            t+=1
            
        for jj in range(len(weightlosscat)):
            valloc=list(weightlosscat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightlossfin[r]=np.array(valloc)
            yr.append(lnchlbl[jj])
            r+=1
            
        for jj in range(len(weightlosscat)):
            valloc=list(weightlosscat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightlossfin[s]=np.array(valloc)
            ys.append(dnrlbl[jj])
            s+=1
            
    X_test=np.zeros((len(weightlosscat),6),dtype=np.float32)
    
    for jj in range(len(weightlosscat)):
        valloc=list(weightlosscat[jj])
        valloc.append(agecl)
        valloc.append(clbmi)
        X_test[jj]=np.array(valloc)*ti
        
  
    from sklearn.model_selection import train_test_split
        
    val=int(USER_INP)
    
    if val==1:
        X_train= weightlossfin
        y_train=yt
        
    elif val==2:
        X_train= weightlossfin
        y_train=yr 
        
    elif val==3:
        X_train= weightlossfin
        y_train=ys
        
    from sklearn.ensemble import RandomForestClassifier
    
    clf=RandomForestClassifier(n_estimators=100)
    
    clf.fit(X_train,y_train)
    
    y_pred=clf.predict(X_test)
    
    l= []
    print ('SUGGESTED FOOD ITEMS ::')
    for ii in range(len(y_pred)):
        if y_pred[ii]==2:
            l.appnd(Food_itemsdata[ii])

    import pandas as pd
    from tabulate import tabulate

    df = pd.read_csv('./dataset.csv')

    if len(l) == 0:
        l = ['Berries', 'Banana']

    tmp = np.char.lower(l)
    listnew = set()
    printed_rows = set()  
    columns_to_print = ['Meal_Id','Name', 'Disease', 'Diet', 'Veg_Non','Price']

    for i in df['description']:
        if not pd.isna(i):
            split_data = i.split(',')
            split_data_str = [str(item) for item in split_data]
            split_data_new = [s.encode('utf-8', 'replace') for s in split_data_str]
            common_values = [value for value in split_data_new if any(val in value.decode('utf-8', 'replace').lower() for val in tmp)]
            if common_values:
                selected_rows = df[df['description'] == i]
                row_tuple = tuple(selected_rows[columns_to_print].to_records(index=False)[0])
                
                if row_tuple not in printed_rows:
                    listnew.add(row_tuple)
                    printed_rows.add(row_tuple)

    
    columns = columns_to_print
    listnew = [pd.DataFrame([row], columns=columns) for row in listnew]

    new_disease = e6.get()  
    if new_disease == 'None':
        new_disease=""

    selected_diet_type = e5.get()
    if selected_diet_type == 'Both':
        selected_diet_type=""

    
    printed_meal_ids = set()

    for df_subset in listnew:
        subset_disease = df_subset['Disease'].iloc[0]

        if new_disease.lower() in subset_disease.lower() and selected_diet_type.lower() in df_subset['Veg_Non'].iloc[0].lower():
            corresponding_rows_indices = df[df['Name'].isin(df_subset['Name'])].index

            # Check and print only if the meal ID is not in printed_meal_ids
            for index in corresponding_rows_indices:
                meal_id = df.at[index, 'Name']
                if meal_id not in printed_meal_ids:
                    corresponding_row_subset = df.loc[[index], ['Name', 'Diet', 'Price']]
                    print(tabulate(corresponding_row_subset, headers='keys', tablefmt='pretty'))
                    printed_meal_ids.add(meal_id)
            

def Weight_Gain():
    print(" Age: %s\n Weight: %s\n Height: %s\n" % (e1.get(), e3.get(), e4.get()))
    
    
    import pandas as pd
    import numpy as np
    from sklearn.cluster import KMeans
    import tkinter as tk
    
    ROOT = tk.Tk()
    
    ROOT.withdraw()
   
    USER_INP = simpledialog.askstring(title="Food Timing",
                                      prompt="Enter 1 for Breakfast, 2 for Lunch and 3 for Dinner")
    
    data=pd.read_csv('input.csv')
    data.head(5)
    Breakfastdata=data['Breakfast']
    BreakfastdataNumpy=Breakfastdata.to_numpy()
    
    Lunchdata=data['Lunch']
    LunchdataNumpy=Lunchdata.to_numpy()
    
    Dinnerdata=data['Dinner']
    DinnerdataNumpy=Dinnerdata.to_numpy()
    
    Food_itemsdata=data['Food_items']
    breakfastfoodseparated=[]
    Lunchfoodseparated=[]
    Dinnerfoodseparated=[]
    
    breakfastfoodseparatedID=[]
    LunchfoodseparatedID=[]
    DinnerfoodseparatedID=[]
    
    for i in range(len(Breakfastdata)):
      if BreakfastdataNumpy[i]==1:
        breakfastfoodseparated.append(Food_itemsdata[i])
        breakfastfoodseparatedID.append(i)
      if LunchdataNumpy[i]==1:
        Lunchfoodseparated.append(Food_itemsdata[i])
        LunchfoodseparatedID.append(i)
      if DinnerdataNumpy[i]==1:
        Dinnerfoodseparated.append(Food_itemsdata[i])
        DinnerfoodseparatedID.append(i)
    
    LunchfoodseparatedIDdata = data.iloc[LunchfoodseparatedID]
    LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.T
    val=list(np.arange(5,15))
    Valapnd=[0]+val
    LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.iloc[Valapnd]
    LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.T
    
    breakfastfoodseparatedIDdata = data.iloc[breakfastfoodseparatedID]
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
    val=list(np.arange(5,15))
    Valapnd=[0]+val
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.iloc[Valapnd]
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
    
    
    DinnerfoodseparatedIDdata = data.iloc[DinnerfoodseparatedID]
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
    val=list(np.arange(5,15))
    Valapnd=[0]+val
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.iloc[Valapnd]
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
    
    age=int(e1.get())
    weight=float(e3.get())
    height=float(e4.get())
    bmi = weight/(height**2) 
    agewiseinp=0
    
    for lp in range (0,80,10):
        test_list=np.arange(lp,lp+10)
        for i in test_list: 
            if(i == age):
                print('age is between',str(lp),str(lp+10))
                tr=round(lp/20)  
                agecl=round(lp/20)    

    print("Your body mass index is: ", bmi)
    if ( bmi < 16):
        print("severely underweight")
        clbmi=4
    elif ( bmi >= 16 and bmi < 18.5):
        print("underweight")
        clbmi=3
    elif ( bmi >= 18.5 and bmi < 25):
        print("Healthy")
        clbmi=2
    elif ( bmi >= 25 and bmi < 30):
        print("overweight")
        clbmi=1
    elif ( bmi >=30):
        print("severely overweight")
        clbmi=0    
    val1=DinnerfoodseparatedIDdata.describe()
    valTog=val1.T
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.to_numpy()
    LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.to_numpy()
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.to_numpy()
    ti=(bmi+agecl)/2
    
    Datacalorie=DinnerfoodseparatedIDdata[1:,1:len(DinnerfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0, n_init=10).fit(X)
    XValu=np.arange(0,len(kmeans.labels_))
    dnrlbl=kmeans.labels_
    
    Datacalorie=LunchfoodseparatedIDdata[1:,1:len(LunchfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0, n_init=10).fit(X)
    XValu=np.arange(0,len(kmeans.labels_))
    lnchlbl=kmeans.labels_
    
    Datacalorie=breakfastfoodseparatedIDdata[1:,1:len(breakfastfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0, n_init=10).fit(X)
    XValu=np.arange(0,len(kmeans.labels_))
    brklbl=kmeans.labels_
    
    inp=[]
    datafin=pd.read_csv('inputfin.csv')
    datafin.head(5)
    dataTog=datafin.T
    bmicls=[0,1,2,3,4]
    agecls=[0,1,2,3,4]
    weightlosscat = dataTog.iloc[[1,2,7,8]]
    weightlosscat=weightlosscat.T
    weightgaincat= dataTog.iloc[[0,1,2,3,4,7,9,10]]
    weightgaincat=weightgaincat.T
    healthycat = dataTog.iloc[[1,2,3,4,6,7,9]]
    healthycat=healthycat.T
    weightlosscatDdata=weightlosscat.to_numpy()
    weightgaincatDdata=weightgaincat.to_numpy()
    healthycatDdata=healthycat.to_numpy()
    weightlosscat=weightlosscatDdata[1:,0:len(weightlosscatDdata)]
    weightgaincat=weightgaincatDdata[1:,0:len(weightgaincatDdata)]
    healthycat=healthycatDdata[1:,0:len(healthycatDdata)]
    
    weightlossfin=np.zeros((len(weightlosscat)*5,6),dtype=np.float32)
    weightgainfin=np.zeros((len(weightgaincat)*5,10),dtype=np.float32)
    healthycatfin=np.zeros((len(healthycat)*5,9),dtype=np.float32)
    t=0
    r=0
    s=0
    yt=[]
    yr=[]
    ys=[]
    for zz in range(5):
        for jj in range(len(weightgaincat)):
            valloc=list(weightgaincat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightgainfin[t]=np.array(valloc)
            yt.append(brklbl[jj])
            t+=1
        for jj in range(len(weightgaincat)):
            valloc=list(weightgaincat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightgainfin[r]=np.array(valloc)
            yr.append(lnchlbl[jj])
            r+=1
        for jj in range(len(weightgaincat)):
            valloc=list(weightgaincat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightgainfin[s]=np.array(valloc)
            ys.append(dnrlbl[jj])
            s+=1

    
    X_test=np.zeros((len(weightgaincat),10),dtype=np.float32)

   
    for jj in range(len(weightgaincat)):
        valloc=list(weightgaincat[jj])
        valloc.append(agecl)
        valloc.append(clbmi)
        X_test[jj]=np.array(valloc)*ti
    
    from sklearn.model_selection import train_test_split
    
    val=int(USER_INP)
    
    if val==1:
        X_train= weightgainfin
        y_train=yt
        
    elif val==2:
        X_train= weightgainfin
        y_train=yr 
        
    elif val==3:
        X_train= weightgainfin
        y_train=ys
    
   
    from sklearn.model_selection import train_test_split
    
    
    from sklearn.ensemble import RandomForestClassifier
    
    clf=RandomForestClassifier(n_estimators=100)
    
    clf.fit(X_train,y_train)
    
    y_pred=clf.predict(X_test)
    
    
    l=[]
    
    print ('SUGGESTED FOOD ITEMS ::')
    for ii in range(len(y_pred)):
        if y_pred[ii]==2:
            l.append(Food_itemsdata[ii])

    import pandas as pd
    from tabulate import tabulate

    df = pd.read_csv('./dataset.csv')

    if len(l) == 0:
        l = ['Berries', 'Banana']

    tmp = np.char.lower(l)
    listnew = set()
    printed_rows = set()  
    columns_to_print = ['Meal_Id','Name', 'Disease', 'Diet', 'Veg_Non','Price']

    for i in df['description']:
        if not pd.isna(i):
            split_data = i.split(',')
            split_data_str = [str(item) for item in split_data]
            split_data_new = [s.encode('utf-8', 'replace') for s in split_data_str]
            common_values = [value for value in split_data_new if any(val in value.decode('utf-8', 'replace').lower() for val in tmp)]
            if common_values:
                selected_rows = df[df['description'] == i]
                row_tuple = tuple(selected_rows[columns_to_print].to_records(index=False)[0])
                
                if row_tuple not in printed_rows:
                    listnew.add(row_tuple)
                    printed_rows.add(row_tuple)

    
    columns = columns_to_print
    listnew = [pd.DataFrame([row], columns=columns) for row in listnew]

    new_disease = e6.get()  
    if new_disease == 'None':
        new_disease=""

    selected_diet_type = e5.get()
    if selected_diet_type == 'Both':
        selected_diet_type=""

    
    printed_meal_ids = set()

    for df_subset in listnew:
        subset_disease = df_subset['Disease'].iloc[0]

        if new_disease.lower() in subset_disease.lower() and selected_diet_type.lower() in df_subset['Veg_Non'].iloc[0].lower():
            corresponding_rows_indices = df[df['Name'].isin(df_subset['Name'])].index

            # Check and print only if the meal ID is not in printed_meal_ids
            for index in corresponding_rows_indices:
                meal_id = df.at[index, 'Name']
                if meal_id not in printed_meal_ids:
                    corresponding_row_subset = df.loc[[index], ['Name', 'Diet', 'Price']]
                    print(tabulate(corresponding_row_subset, headers='keys', tablefmt='pretty'))
                    printed_meal_ids.add(meal_id)
                 

def Healthy():
    print(" Age: %s\n Weight: %s\n Height: %s\n" % (e1.get(), e3.get(), e4.get()))
    import pandas as pd
    import numpy as np
    from sklearn.cluster import KMeans
    import tkinter as tk
    
    ROOT = tk.Tk()
    
    ROOT.withdraw()
   
    USER_INP = simpledialog.askstring(title="Food Timing",
                                      prompt="Enter 1 for Breakfast, 2 for Lunch and 3 for Dinner")
    
    
    data=pd.read_csv('input.csv')
    data.head(5)
    Breakfastdata=data['Breakfast']
    BreakfastdataNumpy=Breakfastdata.to_numpy()
    
    Lunchdata=data['Lunch']
    LunchdataNumpy=Lunchdata.to_numpy()
    
    Dinnerdata=data['Dinner']
    DinnerdataNumpy=Dinnerdata.to_numpy()
    
    Food_itemsdata=data['Food_items']
    breakfastfoodseparated=[]
    Lunchfoodseparated=[]
    Dinnerfoodseparated=[]
    
    breakfastfoodseparatedID=[]
    LunchfoodseparatedID=[]
    DinnerfoodseparatedID=[]
    
    for i in range(len(Breakfastdata)):
      if BreakfastdataNumpy[i]==1:
        breakfastfoodseparated.append(Food_itemsdata[i])
        breakfastfoodseparatedID.append(i)
      if LunchdataNumpy[i]==1:
        Lunchfoodseparated.append(Food_itemsdata[i])
        LunchfoodseparatedID.append(i)
      if DinnerdataNumpy[i]==1:
        Dinnerfoodseparated.append(Food_itemsdata[i])
        DinnerfoodseparatedID.append(i)
    
    LunchfoodseparatedIDdata = data.iloc[LunchfoodseparatedID]
    LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.T
    val=list(np.arange(5,15))
    Valapnd=[0]+val
    LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.iloc[Valapnd]
    LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.T
    
    breakfastfoodseparatedIDdata = data.iloc[breakfastfoodseparatedID]
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
    val=list(np.arange(5,15))
    Valapnd=[0]+val
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.iloc[Valapnd]
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.T
    
    DinnerfoodseparatedIDdata = data.iloc[DinnerfoodseparatedID]
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
    val=list(np.arange(5,15))
    Valapnd=[0]+val
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.iloc[Valapnd]
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.T
    
    age=int(e1.get())
    weight=float(e3.get())
    height=float(e4.get())
    bmi = weight/(height**2) 
    agewiseinp=0
    
    for lp in range (0,80,10):
        test_list=np.arange(lp,lp+10)
        for i in test_list: 
            if(i == age):
                print('age is between',str(lp),str(lp+10))
                tr=round(lp/20)  
                agecl=round(lp/20)    
    
    print("Your body mass index is: ", bmi)
    if ( bmi < 16):
        print("severely underweight")
        clbmi=4
    elif ( bmi >= 16 and bmi < 18.5):
        print("underweight")
        clbmi=3
    elif ( bmi >= 18.5 and bmi < 25):
        print("Healthy")
        clbmi=2
    elif ( bmi >= 25 and bmi < 30):
        print("overweight")
        clbmi=1
    elif ( bmi >=30):
        print("severely overweight")
        clbmi=0    
    val1=DinnerfoodseparatedIDdata.describe()
    valTog=val1.T
    DinnerfoodseparatedIDdata=DinnerfoodseparatedIDdata.to_numpy()
    LunchfoodseparatedIDdata=LunchfoodseparatedIDdata.to_numpy()
    breakfastfoodseparatedIDdata=breakfastfoodseparatedIDdata.to_numpy()
    ti=(bmi+agecl)/2
    
    ## K-Means Based  Dinner Food
    Datacalorie=DinnerfoodseparatedIDdata[1:,1:len(DinnerfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=5, random_state=0,n_init=10).fit(X)
    XValu=np.arange(0,len(kmeans.labels_))
    dnrlbl=kmeans.labels_
    
    ## K-Means Based  lunch Food
    Datacalorie=LunchfoodseparatedIDdata[1:,1:len(LunchfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=4, random_state=0,n_init=10).fit(X)
    XValu=np.arange(0,len(kmeans.labels_))
    lnchlbl=kmeans.labels_
    
    ## K-Means Based  lunch Food
    Datacalorie=breakfastfoodseparatedIDdata[1:,1:len(breakfastfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0,n_init=10).fit(X)
    XValu=np.arange(0,len(kmeans.labels_))
    brklbl=kmeans.labels_
    inp=[]
    datafin=pd.read_csv('inputfin.csv')
    datafin.head(5)
    dataTog=datafin.T
    bmicls=[0,1,2,3,4]
    agecls=[0,1,2,3,4]
    weightlosscat = dataTog.iloc[[1,2,7,8]]
    weightlosscat=weightlosscat.T
    weightgaincat= dataTog.iloc[[0,1,2,3,4,7,9,10]]
    weightgaincat=weightgaincat.T
    healthycat = dataTog.iloc[[1,2,3,4,6,7,9]]
    healthycat=healthycat.T
    weightlosscatDdata=weightlosscat.to_numpy()
    weightgaincatDdata=weightgaincat.to_numpy()
    healthycatDdata=healthycat.to_numpy()
    weightlosscat=weightlosscatDdata[1:,0:len(weightlosscatDdata)]
    weightgaincat=weightgaincatDdata[1:,0:len(weightgaincatDdata)]
    healthycat=healthycatDdata[1:,0:len(healthycatDdata)]
    
    weightlossfin=np.zeros((len(weightlosscat)*5,6),dtype=np.float32)
    weightgainfin=np.zeros((len(weightgaincat)*5,10),dtype=np.float32)
    healthycatfin=np.zeros((len(healthycat)*5,9),dtype=np.float32)
    t=0
    r=0
    s=0
    yt=[]
    yr=[]
    ys=[]
    for zz in range(5):
        for jj in range(len(healthycat)):
            valloc=list(healthycat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            healthycatfin[t]=np.array(valloc)
            yt.append(brklbl[jj])
            t+=1
        for jj in range(len(healthycat)):
            valloc=list(healthycat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            healthycatfin[r]=np.array(valloc)
            yr.append(lnchlbl[jj])
            r+=1
        for jj in range(len(healthycat)):
            valloc=list(healthycat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            healthycatfin[s]=np.array(valloc)
            ys.append(dnrlbl[jj])
            s+=1

    X_test=np.zeros((len(healthycat)*5,9),dtype=np.float32)
    for jj in range(len(healthycat)):
        valloc=list(healthycat[jj])
        valloc.append(agecl)
        valloc.append(clbmi)
        X_test[jj]=np.array(valloc)*ti
    
    
    from sklearn.model_selection import train_test_split
    

    val=int(USER_INP)
    
    if val==1:
        X_train= healthycatfin
        y_train=yt
        
    elif val==2:
        X_train= healthycatfin
        y_train=yt 
        
    elif val==3:
        X_train= healthycatfin
        y_train=ys
        
    
    from sklearn.model_selection import train_test_split
    
    
    from sklearn.ensemble import RandomForestClassifier
    
    clf=RandomForestClassifier(n_estimators=100)
    
    clf.fit(X_train,y_train)
    
    y_pred=clf.predict(X_test)

    l=[]

    print ('SUGGESTED FOOD ITEMS ::')
    for ii in range(len(y_pred)):
        if y_pred[ii]==2:
            l.append(Food_itemsdata[ii])
            
    import pandas as pd
    from tabulate import tabulate

    df = pd.read_csv('./dataset.csv')

    if len(l) == 0:
        l = ['Berries', 'Banana']

    tmp = np.char.lower(l)
    listnew = set()
    printed_rows = set()  
    columns_to_print = ['Meal_Id','Name', 'Disease', 'Diet', 'Veg_Non','Price']

    for i in df['description']:
        if not pd.isna(i):
            split_data = i.split(',')
            split_data_str = [str(item) for item in split_data]
            split_data_new = [s.encode('utf-8', 'replace') for s in split_data_str]
            common_values = [value for value in split_data_new if any(val in value.decode('utf-8', 'replace').lower() for val in tmp)]
            if common_values:
                selected_rows = df[df['description'] == i]
                row_tuple = tuple(selected_rows[columns_to_print].to_records(index=False)[0])
                
                if row_tuple not in printed_rows:
                    listnew.add(row_tuple)
                    printed_rows.add(row_tuple)

    
    columns = columns_to_print
    listnew = [pd.DataFrame([row], columns=columns) for row in listnew]

    new_disease = e6.get()  
    if new_disease == 'None':
        new_disease=""

    selected_diet_type = e5.get()
    if selected_diet_type == 'Both':
        selected_diet_type=""

    
    printed_meal_ids = set()

    for df_subset in listnew:
        subset_disease = df_subset['Disease'].iloc[0]

        if new_disease.lower() in subset_disease.lower() and selected_diet_type.lower() in df_subset['Veg_Non'].iloc[0].lower():
            corresponding_rows_indices = df[df['Name'].isin(df_subset['Name'])].index

            # Check and print only if the meal ID is not in printed_meal_ids
            for index in corresponding_rows_indices:
                meal_id = df.at[index, 'Name']
                if meal_id not in printed_meal_ids:
                    corresponding_row_subset = df.loc[[index], ['Name', 'Diet', 'Price']]
                    print(tabulate(corresponding_row_subset, headers='keys', tablefmt='pretty'))
                    printed_meal_ids.add(meal_id)




Label(main_win,text="Age",font='Helvetica 12 bold').grid(row=1,column=0,sticky=W,pady=4)
Label(main_win,text="Weight",font='Helvetica 12 bold').grid(row=2,column=0,sticky=W,pady=4)
Label(main_win,text="Height", font='Helvetica 12 bold').grid(row=3,column=0,sticky=W,pady=4)
Label(main_win, text="veg/NonVeg", font='Helvetica 11 bold').grid(row=4, column=0, sticky=tk.W, pady=4)
Label(main_win, text="Condition", font='Helvetica 11 bold').grid(row=5, column=0, sticky=tk.W, pady=4)

e1 = Entry(main_win,bg="light grey")
e3 = Entry(main_win,bg="light grey")
e4 = Entry(main_win,bg="light grey")

veg_nonveg_var = tk.StringVar()
e5 = ttk.Combobox(main_win, values=["veg", "non-veg","Both"], textvariable=veg_nonveg_var, state="readonly")
e5.set("Veg")  # Set the default value
       
        # Create Combobox for "Condition"
condition_var = tk.StringVar()
e6 = ttk.Combobox(main_win, values=["heart_disease", "hypertension", "obesity","diabeties","kidney_disease","pregnancy","cancer","rickets","scurvy","anemia","goitre","eye_disease","None"], textvariable=condition_var, state="readonly")
e6.set("None")  # Set the default value

e1.focus_force() 
e1.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)


Button(main_win,text='Quit',font='Helvetica 8 bold',command=main_win.quit).grid(row=6,column=0,sticky=W,pady=4)
Button(main_win,text='Weight Loss',font='Helvetica 8 bold',command=Weight_Loss).grid(row=1,column=4,sticky=W,pady=4)
Button(main_win,text='Weight Gain',font='Helvetica 8 bold',command=Weight_Gain).grid(row=2,column=4,sticky=W,pady=4)
Button(main_win,text='Healthy',font='Helvetica 8 bold',command=Healthy).grid(row=3,column=4,sticky=W,pady=4)
main_win.geometry("600x250")
main_win.wm_title("DIET RECOMMENDATION SYSTEM")
main_win.mainloop()

