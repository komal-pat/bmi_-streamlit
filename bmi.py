import streamlit as st

h = st.number_input('enter height in meters')
w = st.number_input('enter weight in kgs')

try:
    bmi = w/h**2

    st.write(f"your bmi is:{bmi:.2f}")
    if bmi <18.5:
        st.warning('you are underweighted')
    elif bmi>18.5 and bmi<25:
        st.success('you have a good weight')
    elif bmi>25 and bmi<30:
        st.warning('overweight')
    else:
        st.info('obesity kills')
except Exception as e:
    st.write("enter valid numbers")

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
