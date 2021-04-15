import streamlit as st 

import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)







left_column, right_column = st.beta_columns(2)
button = left_column.button('右からむに文字を表示')
if button:
    right_column.write('ここは右からむ')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('回答1')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('回答2')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('回答3')



# text = st.text_input('あなたの趣味を教えてください',)
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味は', text,'です'
# 'コンディション：', condition







# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='toshi', use_column_width=True)

