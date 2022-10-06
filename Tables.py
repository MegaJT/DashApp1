import pandas as pd
import numpy as np
df=pd.read_excel('Data.xlsx')
df['SIMPLE SCORE']=(df['Q1_1_SCORE-Q1_1_SCORE']+
df['Q1_2_SCORE-Q1_2_SCORE']+
df['Q1_3_SCORE-Q1_3_SCORE']+
df['Q1_4_SCORE-Q1_4_SCORE']+
df['Q1_6_SCORE-Q1_6_SCORE']+
df['Q2_5_SCORE-Q2_5_SCORE'])/6

df['QUICK SCORE']=(df['Q2_1_SCORE-Q2_1_SCORE']+
df['Q2_2_SCORE-Q2_2_SCORE']+
df['Q2_6_SCORE-Q2_6_SCORE']+
df['Q2_3_SCORE-Q2_3_SCORE']+
df['Q2_4_SCORE-Q2_4_SCORE']+
df['Q2_5_SCORE-Q2_5_SCORE'])/6

df['TRUST SCORE']=(df['Q3_1_SCORE-Q3_1_SCORE']+
df['Q3_2_SCORE-Q3_2_SCORE']+
df['Q3_3_SCORE-Q3_3_SCORE']+
df['Q3_4_SCORE-Q3_4_SCORE']+
df['Q3_5_SCORE-Q3_5_SCORE']+
df['Q3_6_SCORE-Q3_6_SCORE'])/6

df['WORTH SCORE']=(df['Q4_2_SCORE-Q4_2_SCORE']+
df['Q4_3_SCORE-Q4_3_SCORE'])/2

df['OVERALL SCORE']=(df['SIMPLE SCORE']+df['QUICK SCORE']+df['TRUST SCORE']+df['WORTH SCORE'])/4

Branch_List=list(df['Branch_Name'].unique())



#print("Type Branch list - "+str(type(Branch_List)))
def Score_Generator(Branch_Name):
    Overall=df[df['Branch_Name']==Branch_Name]['OVERALL SCORE'].mean()
    Simple=df[df['Branch_Name']==Branch_Name]['SIMPLE SCORE'].mean()
    Quick=df[df['Branch_Name']==Branch_Name]['QUICK SCORE'].mean()
    Trust=df[df['Branch_Name']==Branch_Name]['TRUST SCORE'].mean()
    Worth=df[df['Branch_Name']==Branch_Name]['WORTH SCORE'].mean()
    return Overall,Simple,Quick,Trust,Worth

def Branch_Name():
    Branch_Name=list(df['Branch_Name'].unique())
    return Branch_Name

def Score_Generator_Dict():
    Global_Overall_Score=round(df['OVERALL SCORE'].mean())
    branch_score_dict={}
    for  items in Branch_List:
        branch_score_dict[items]=round(df[df['Branch_Name']==items]['OVERALL SCORE'].mean())
    return branch_score_dict,Global_Overall_Score



def Easy_To_Handle_Score(Branch_Name):
    E_to_H_Branch=df[df['Branch_Name']==Branch_Name]['Q1_5_SCORE-Q1_5_SCORE'].mean()
    E_to_H_Overall=df['Q1_5_SCORE-Q1_5_SCORE'].mean()
    return round(E_to_H_Branch,2),round(E_to_H_Overall,2)


def DataTables():
    df2=pd.DataFrame()
    df2=pd.pivot_table(data=df,values=['Q1_1_SCORE-Q1_1_SCORE',
    'Q1_2_SCORE-Q1_2_SCORE',
    'Q1_3_SCORE-Q1_3_SCORE',
    'Q1_4_SCORE-Q1_4_SCORE',
    'Q1_5_SCORE-Q1_5_SCORE',
    'Q1_6_SCORE-Q1_6_SCORE',
    'Q2_1_SCORE-Q2_1_SCORE',
    'Q2_2_SCORE-Q2_2_SCORE',
    'Q2_3_SCORE-Q2_3_SCORE',
    'Q2_4_SCORE-Q2_4_SCORE',
    'Q2_5_SCORE-Q2_5_SCORE',
    'Q2_6_SCORE-Q2_6_SCORE',
    'Q3_1_SCORE-Q3_1_SCORE',
    'Q3_2_SCORE-Q3_2_SCORE',
    'Q3_3_SCORE-Q3_3_SCORE',
    'Q3_4_SCORE-Q3_4_SCORE',
    'Q3_5_SCORE-Q3_5_SCORE',
    'Q3_6_SCORE-Q3_6_SCORE',
    'Q4_2_SCORE-Q4_2_SCORE',
    'Q4_3_SCORE-Q4_3_SCORE'],index="Branch_Name",aggfunc=np.mean)
    df2=df2.round()


    df2['Simple Score Summary']=round(df2[['Q2_1_SCORE-Q2_1_SCORE','Q2_1_SCORE-Q2_1_SCORE','Q1_3_SCORE-Q1_3_SCORE','Q1_4_SCORE-Q1_4_SCORE','Q1_6_SCORE-Q1_6_SCORE']].mean(axis=1))
    df2['Quick Score Summary']=round(df2[['Q1_1_SCORE-Q1_1_SCORE',
                                    'Q2_2_SCORE-Q2_2_SCORE',
                                    'Q2_2_SCORE-Q2_2_SCORE',
                                    'Q2_6_SCORE-Q2_6_SCORE',
                                    'Q2_3_SCORE-Q2_3_SCORE',
                                    'Q2_4_SCORE-Q2_4_SCORE',
                                    'Q2_5_SCORE-Q2_5_SCORE']].mean(axis=1))
    df2['Trust Score Summary']=round(df2[['Q3_1_SCORE-Q3_1_SCORE'
                                    ,'Q3_2_SCORE-Q3_2_SCORE'
                                    ,'Q3_3_SCORE-Q3_3_SCORE'
                                    ,'Q3_4_SCORE-Q3_4_SCORE'
                                    ,'Q3_5_SCORE-Q3_5_SCORE'
                                    ,'Q3_6_SCORE-Q3_6_SCORE'
                                    ]].mean(axis=1))
    df2['Worth Score Summary']=round(df2[['Q4_2_SCORE-Q4_2_SCORE'
                                    ,'Q4_3_SCORE-Q4_3_SCORE'
                                    ]].mean(axis=1))

    df2=df2.drop(['Q1_5_SCORE-Q1_5_SCORE'],axis=1)

    df2=df2[['Simple Score Summary','Q2_1_SCORE-Q2_1_SCORE','Q2_1_SCORE-Q2_1_SCORE','Q1_3_SCORE-Q1_3_SCORE','Q1_4_SCORE-Q1_4_SCORE','Q1_6_SCORE-Q1_6_SCORE'
        ,'Quick Score Summary','Q1_1_SCORE-Q1_1_SCORE',
                                    'Q2_2_SCORE-Q2_2_SCORE',
                                    'Q2_2_SCORE-Q2_2_SCORE',
                                    'Q2_6_SCORE-Q2_6_SCORE',
                                    'Q2_3_SCORE-Q2_3_SCORE',
                                    'Q2_4_SCORE-Q2_4_SCORE',
                                    'Q2_5_SCORE-Q2_5_SCORE',
            'Trust Score Summary','Q3_1_SCORE-Q3_1_SCORE'
                                    ,'Q3_2_SCORE-Q3_2_SCORE'
                                    ,'Q3_3_SCORE-Q3_3_SCORE'
                                    ,'Q3_4_SCORE-Q3_4_SCORE'
                                    ,'Q3_5_SCORE-Q3_5_SCORE'
                                    ,'Q3_6_SCORE-Q3_6_SCORE'
            ,'Worth Score Summary','Q4_2_SCORE-Q4_2_SCORE'
                                    ,'Q4_3_SCORE-Q4_3_SCORE']]

    df2.rename(columns={'Q1_1_SCORE-Q1_1_SCORE':"Was it easy to find the desired branch online?"
    ,'Q2_1_SCORE-Q2_1_SCORE':"Was it easy to find the desired branch?"
    ,'Q1_2_SCORE-Q1_2_SCORE':"Was it easy to find a parking space for your car Infront of the branch ?"
    ,'Q3_1_SCORE-Q3_1_SCORE':"Was the information online correct with regards to working hours when you reached the branch?"
    ,'Q3_2_SCORE-Q3_2_SCORE':"What best describes the appearance of the branch?"
    ,'Q2_2_SCORE-Q2_2_SCORE':"Was there a queue in front of you?"
    ,'Q2_6_SCORE-Q2_6_SCORE':"How long did it take from the moment you entered the branch to your turn?"
    ,'Q3_3_SCORE-Q3_3_SCORE':"What best describes the SALES CONSULTANT's appearance"
    ,'Q3_4_SCORE-Q3_4_SCORE':"What best describes SALES CONSULTANT's level of friendliness throughout your interaction:"
    ,'Q1_3_SCORE-Q1_3_SCORE':"What best describes the manner in which the SALES CONSULTANT responds to your questions:"
    ,'Q1_4_SCORE-Q1_4_SCORE':"Everything I needed was in the store"
    ,'Q2_4_SCORE-Q2_4_SCORE':"Was the time the employee told you to deliver the shipment right for you?"
    ,'Q1_6_SCORE-Q1_6_SCORE':"Pricing"
    ,'Q4_2_SCORE-Q4_2_SCORE':"Was the price right for you?"
    ,'Q4_3_SCORE-Q4_3_SCORE':"Compared to the service you received today, do you think the amount you paid was worth it?"
    ,'Q2_3_SCORE-Q2_3_SCORE':"How long did the sales consultant take to finish your request ?"
    ,'Q3_5_SCORE-Q3_5_SCORE':"What best describes the manner in which the overall sales process was handled:"
    ,'Q1_5_SCORE-Q1_5_SCORE':"Zajil made it easy to handle my transaction"
    ,'Q2_5_SCORE-Q2_5_SCORE':"Was the package delivered on time?"
    ,'Q3_6_SCORE-Q3_6_SCORE':"Was the package delivered in full and unbroken?"},inplace=True)


    df2['Average']=round(df2[['Simple Score Summary','Quick Score Summary','Trust Score Summary','Worth Score Summary']].mean(axis=1))


    dff=df2.T
    dff.reset_index(inplace=True)

    return dff  
