####
# streamlit run d:\_Home\Programming\Python\StreamLit_Numerizer\app.py
# Deployment on https://huggingface.co/
# https://huggingface.co/spaces/stribizhev/numerizer_spacy
# https://www.youtube.com/watch?v=DpVt1WDTD9k
####
from typing_extensions import final
import streamlit as st # https://docs.streamlit.io/library/get-started/installation#install-streamlit-on-windows, pip install streamlit
import spacy
#import en_core_web_trf
from numerizer import numerize

st.title("Numerizer with Spacy test")

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_model():
    """Spacy model loading"""
    return spacy.load("en_core_web_sm")
    #return en_core_web_trf.load()

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def process_text(text: str):
    """Process text and create a Doc object"""
    nlp = load_model()
    return nlp(text)

st.markdown("Input Text")

input_text = st.text_input(label="Add text", value="Two plus two is four")

st.write(input_text)

doc = process_text(input_text)

numerized_parts = doc._.numerize()
#numerized_parts = doc._.numerize(labels=['MONEY'])

st.markdown("Numerized Sections:\n")
st.markdown(numerized_parts)
final_sentence = input_text
for key in numerized_parts.keys():
    final_sentence = final_sentence.replace(str(key), numerized_parts[key])

st.write("Output text")
st.write(final_sentence)