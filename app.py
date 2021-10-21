import pickle
import streamlit as st
import pandas as pd
import requests

def fech_poster(movie_id):
    url='https://api.themoviedb.org/3/movie/{}?api_key=e922bef3e8e6658a9e934324346937c0&language=en-US'.format(movie_id)
    response=requests.get(url)
    data=response.json()
    return 'http://image.tmdb.org/t/p/w500/'+data['poster_path']


def recommend(movie):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(sm[index])),reverse=True,key = lambda x: x[1])
    names=[]
    poster=[]
    for i in distances[1:6]:
        names.append(new.iloc[i[0]].title)
        poster.append(fech_poster(new.iloc[i[0]].movie_id))
    return names,poster







st.title('Movie Recommendation System')


movies_dict=pickle.load(open('movie_dict.pkl','rb'))

new=pd.DataFrame(movies_dict)
sm=pickle.load(open('similarity.pkl','rb'))
option = st.selectbox('pelease select any movie from dropdown',new['title'].values)

if st.button('Recommend'):
    names,poster=recommend(option)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])

st.text('This app is made by Amit kumar')





