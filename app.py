import streamlit as st, pandas as pd, joblib, os, plotly.express as px
st.set_page_config(page_title='Student Dashboard',layout='wide')
if not os.path.exists('model.pkl'):
    import train
model=joblib.load('model.pkl')
st.title('🎓 Student Performance Prediction System')
c1,c2=st.columns(2)
with c1:
    attendance=st.slider('Attendance %',40,100,75)
    study_hours=st.slider('Study Hours',1,10,5)
    quiz=st.slider('Quiz Score',0,100,65)
with c2:
    assignment=st.slider('Assignment Score',0,100,70)
    gpa=st.slider('Previous GPA',0.0,10.0,7.5,0.1)
data={'attendance':attendance,'study_hours':study_hours,'quiz_score':quiz,'assignment_score':assignment,'previous_gpa':gpa}
if st.button('Predict Now'):
    df=pd.DataFrame([data])
    prob=float(model.predict_proba(df)[0][1])
    pred=int(prob>=0.5)
    st.metric('Pass Probability',f'{prob*100:.1f}%')
    if pred:
        st.success('Likely PASS')
    else:
        st.error('At Risk Student')
    fig=px.bar(x=list(data.keys()),y=list(data.values()),title='Student Metrics')
    st.plotly_chart(fig,use_container_width=True)
    pie=px.pie(values=[prob,1-prob],names=['Pass','Risk'],title='Probability Split')
    st.plotly_chart(pie,use_container_width=True)
