import streamlit as st
from streamlit import session_state as ss
from random import shuffle

from utils.images import img_list


st.set_page_config(
    page_title="Game",
    layout="wide"
)

st.title('AB Travel Game')

st.info('All the pictures you find on this site are captured by me using an iPhone 13 Pro. Can you guess where the pictures are from?')

if 'game' not in ss:
    ss.game = False

if 'npic' not in ss:
    ss.npic = 0

if 'shuffle' not in ss:
    ss.shuffle = False

if 'guess' not in ss:
    ss.guess = False

if 'points' not in ss:
    ss.points = 0

if st.button('Start game', type='primary'):
    ss.game = True

if not ss.shuffle:
    shuffle(img_list)
    guess_options = []
    for i in range(1, 5):
        guess_options.extend(sorted(set([j[i] for j in img_list])))
    ss.shuffle = [img_list, guess_options]

img_list, guess_options = ss.shuffle

if ss.game:
    '---'
    st.subheader(f'Picture {ss.npic+1}/10')

    cols = st.columns([2.5, 1])

    img = img_list[ss.npic]

    with cols[0]:
        st.image(img[0])

    with cols[1]:
        if not ss.guess:
            st.write('**Take your guess below**  \nThe more specific, the more points. Possibilities include:  \n- Continent  \n- Country  \n- City  \n- Specific place/sight')
            guess = st.selectbox('Select guess', guess_options, index=None, placeholder='Guess...')
            btn_disabled = True if guess is None else False
            if st.button('Guess', type='primary', use_container_width=True, disabled=btn_disabled):
                ss.guess = guess
                st.rerun()
            '---'
            with st.expander('Reveal clue'):
                st.write('**Continent**  \nhh')

        else:

            st.write(f'**Your guess**  \n{ss.guess}')

            img_info = [img[i] for i in range(1, 5)[::-1]]
            st.write(f'**Correct answer**  \n{', '.join(img_info)}')

            points = 0
            if ss.guess in img_info:
                points = 4 - img_info.index(ss.guess)
            st.write(f'**Points**  \n{points}')

            'MAP MAP MAP'
            
            '---'

            if st.button('Next picture', type='primary', use_container_width=True):
                ss.points += points
                ss.npic += 1
                ss.guess = False
                st.rerun()
