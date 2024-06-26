import streamlit as st
import time
import matplotlib as plt
import os
from transformers import pipeline
# zaczynamy od zaimportowania bibliotek

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.title('Tlumaczenie z jezyka angielskiego na niemiecki. Streamlit')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

st.header('Tlumaczenie z jezyka angielskiego na niemiecki')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

st.subheader('O Streamlit')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.
st.write('Instrukcja - Wybierz opcje z rozwijanej listy i pisz w pole slowo po angielsku a otrzymasz tlumaczenie na niemiecki')

st.header('Przetwarzanie języka naturalnego')
st.image('gr.jpg', caption="image")

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tlumaczenie z angielskiego na niemiecki",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("sentiment-analysis", model="t5-base")
        answer = classifier(text)
        st.write(answer)

if option == "Tlumaczenie z angielskiego na niemiecki":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("translation_en_to_de", model="t5-base")
        answer = classifier(text)
        st.write(answer)

st.write('s22865')
