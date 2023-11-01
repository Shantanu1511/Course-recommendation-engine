import streamlit as st
import pickle
import pandas as pd

similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(course):
    course_index = data[data['Title'] == course].index[0]
    distances = similarity[course_index]
    courses = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendation = []

    for i in courses:

        recommendation.append(data.iloc[i[0]]['Title'])
        recommendation.append(data.iloc[i[0]]['Link'])
    return recommendation


df = pickle.load(open('course.pkl','rb'))
data = pd.DataFrame(df)
st.title('Course Recommendation System')

course_list = st.selectbox('Select the course you like to learn',(data['Title'].values))

if st.button('Recommend'):
    recommendations = recommend(course_list)
    for i in recommendations:
        st.markdown(i)