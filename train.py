import os,joblib,pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report
if not os.path.exists('students.csv'):
    import generate_data
df=pd.read_csv('students.csv')
X=df.drop('pass',axis=1)
y=df['pass']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(n_estimators=300,random_state=42)
model.fit(X_train,y_train)
pred=model.predict(X_test)
print('Accuracy:',accuracy_score(y_test,pred))
print(classification_report(y_test,pred))
joblib.dump(model,'model.pkl')
print('Saved model.pkl')
