import streamlit as st


st.set_page_config(
    page_title="Gallery",
    layout="wide"
)
st.title('AB Travel Gallery')

st.info('All the pictures you find on this site are captured by me using an iPhone 13 Pro. Below is a gallery with some of the best ones.')

'---'

with st.expander('Map'):
    ...

with st.sidebar:
    st.subheader('Configuration')
    st.slider('Number of pictures per row', 2, 5, 3, 1)
    st.toggle('Show locations', False)

