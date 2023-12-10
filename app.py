import streamlit as st

def find_largest(num1, num2, num3):
  return max(num1, num2, num3)

st.title('Find the Largest Number')
num1 = st.number_input('Enter the first number', value=o.o)
num2 = st.number_input('Enter the second number', value=o.o)
num3 = st.number_input('Enter the third number', value=o.o)


if st.button('Find largest'):
  largest = find_largest(num1, num2, num3)
  st.success(f'The largest number is : {largest}')


