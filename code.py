
import streamlit as st

st.title('Find whether the given number is odd or even.')
box = st.empty()

p = box.number_input('Enter The Number',step=1)

p=int(input())
if p>=0:
        if int(p)%2 == 0:
            print("Even number!")
        if int(p)%2 != 0:
            print("Odd Number!")
else:
    print(" Please Enter a valid Integer.")    
