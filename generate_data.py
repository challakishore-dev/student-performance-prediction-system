import pandas as pd, numpy as np
np.random.seed(42)
n=1500
df=pd.DataFrame({
'attendance':np.random.randint(40,100,n),
'study_hours':np.random.randint(1,10,n),
'quiz_score':np.random.randint(20,100,n),
'assignment_score':np.random.randint(20,100,n),
'previous_gpa':np.round(np.random.uniform(4,10,n),2)
})
score=(df['attendance']*0.25+df['study_hours']*3+df['quiz_score']*0.2+df['assignment_score']*0.2+df['previous_gpa']*4)
df['pass']=(score>score.median()).astype(int)
df.to_csv('students.csv',index=False)
print(df['pass'].value_counts())
