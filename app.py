import streamlit as st
import pickle

animes = pickle.load(open("anime.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))
st.header("Anime Recommeder System")
selectvalue = st.selectbox("Select Anime",animes)

def Recommender(selectvalue):
    Index_of_anime = animes[animes["Name"] == selectvalue].index[0]
    Similarity_score = similarity[Index_of_anime]
    Sorted_scores = sorted(list(enumerate(Similarity_score)),reverse = True,key= lambda x: x[1]) [1:6]
    Recommended_Anime = []
    for i in Sorted_scores:
        Recommended_Anime.append(animes.iloc[i[0]].Name)
    return Recommended_Anime
        
if st.button("Show Recommended"):
    anime_re = Recommender(selectvalue)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(anime_re[0])
    with col2:
        st.text(anime_re[1])
    with col3:
        st.text(anime_re[2])
    with col4:
        st.text(anime_re[3])
    with col5:
        st.text(anime_re[4])
