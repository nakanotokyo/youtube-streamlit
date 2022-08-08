import streamlit as st
import time



st.title('test')

st.write('interactive widget')

'start'

latest_iteration = st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)


'Done'
#left_column, right_column = st.beta_columns(2)

#col1, col2, col3 = st.columns(2)

#col1.button('右カラムに文字を表示')

#expander = st.expander('問合せ')
#expander.write('問合せ内容を書く')

#text= st.text_input('あなたの趣味を教えてください')
#condition = st.slider('あなたの今の調子は？',0,100,50)

#'コンディション:' , condition
#'あなたの趣味:' , text


#option= st.selectbox(

	#'あなたが好きな数字を教えてください。',
	#list(range(1,11))

#)

#'あなたの好きな数字は、' , option , 'です。'

#if st.checkbox('Show Image'):
	#img = Image.open('sample.jpg')
	#st.image(img, caption="test",use_column_width=True)

