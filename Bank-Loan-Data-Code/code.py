# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank = pd.DataFrame(bank_data,index=None,columns=None)

categorial_var = bank.select_dtypes(include = 'object')
print(categorial_var)

numrical_var = bank.select_dtypes(include='number')
print(numrical_var)

banks = bank.drop(columns = 'Loan_ID')
banks.isnull().sum()

bank_mode = banks.mode().iloc[0]

banks.fillna(bank_mode, inplace=True)

avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'], values=['LoanAmount'],aggfunc=np.mean)

loan_approved_se = banks.loc[(banks['Self_Employed']=='Yes') & (banks['Loan_Status'] =='Y'), ['Loan_Status']].count()
loan_approved_nse = banks.loc[(banks['Loan_Status']=='No') & (banks['Loan_Status'] =='N'), ['Loan_Status']].count()

percentage_se = (loan_approved_se * 100/ 614)
percentage_se=percentage_se[0]
percentage_nse = (loan_approved_nse * 100/ 614)
pecentage_nse = percentage_nse[0]

loan_term = banks['Loan_Amount_Term'].apply(lambda x:int(x)/12)

big_loan_term = len(loan_term[loan_term>=25])
print(big_loan_term)

columns_to_show = ['ApplicantIncome', 'Credit_History']
loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby[columns_to_show]

mean_values = loan_groupby.agg([np.mean])
print(mean_values)


