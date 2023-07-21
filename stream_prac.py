import streamlit as st
import pandas as pd

st.title("Zechariah's Page")
st.write("Hello")
':smile:'
':frown:'
':scream:'
name=st.text_input('Your name:')
if name:
	st.write(f'Hello {name}')

x=st.number_input('Enter a number',min_value=1,max_value=99)
st.divider()
clicked=st.button('Click me')
if clicked:
	st.write(':ghost:')
st.divider()
cities=["argentina", 'morroco','phila']

check=st.checkbox("Check me")  #you can add value=true to start at beginning
st.divider()

y=st.radio("Cities",cities)  #index=1 to preselect, key='your_city'
if y:
	st.write(f"You chose {y}") #st.session_state.your_city

box=st.selectbox("City",cities)
if box:
		st.write("Great choice :ghost: ")

st.divider()
j=st.slider('x',min_value=12,max_value=73,step=3)  #value=15
st.write(f'x is {j}')

st.divider()
uploaded_file=st.file_uploader('Upload a file') #type=['txt','xlsx']
if uploaded_file:
	st.write(uploaded_file)
	if uploaded_file.type=='text/plain':
		from io import StringIO
		stringio=StringIO(uploaded_file.getvalue().decode('utf=8'))
		string_data=stringio.read()
		st.write(string_data)
	elif uploaded_file=='text/csv':
		import pandas as pandas
		df=pd.read_csv(uploaded_file)
		st.write(df)
	else:
		import pandas as pd
		df=pd.read_excel(uploaded_file)
		st.write(df)
st.divider()

# pic=st.camera_input('Take a photo')
# if pic:
# 	st.image(pic)
# st.image('https://pixabay.com/photos/checkmate-chess-boar')  needs jpg file

my_select_box=st.sidebar.selectbox('Select',cities)

left_column, right_column=st.columns(2)
with left_column:
	st.write("HELLO")

right_column.write("Goodbye")
right_column.header("A cat")
left_column.markdown("Not a cat")