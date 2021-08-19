import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import time
#https://github.com/matsuzonikof/my1stRepository.git
#my1sttoken
#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
st.title("Streamlit 超入門")
st.write("DataFrame")
df = pd.DataFrame({
    "1列目": [1,2,3,4],
    "2列目": [10,20,30,40]
})

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns = ["lat","lon"]
)
#st.map(df)
#st.line_chart(df)
#st.area_chart(df)
st.write("プログレスバーの表示")
"Start!!"
latest_iteration = st.empty()
bar= st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}%')
    bar.progress(i+1)
    time.sleep(0.01)
"Done!"

st.write("インタラクティブ　ウィジェット")
left_column, right_column = st.columns(2)
if left_column.button("右カラムに文字を表示"):
    right_column.write("ここは右カラム")
expander = st.expander("問い合わせ")
expander.write("問い合わせの回答")


option= st.sidebar.selectbox(
    "あなたの好きな数字を教えてください",
    list(range(1,10))
)
"あなたの好きな数字は",option,"です"

text = st.sidebar.text_input("あなたの趣味は？")
"あなたの趣味：",text

condition = st.sidebar.slider("あなたの調子は？",0,100,50)
"あなたの調子：",condition



st.write("Display Image")

if st.checkbox('Show Image'):
    img=Image.open('/Users/matsukurayoshinori/Downloads/名称未設定のデザイン.png')
    st.image(img,caption='people',use_column_width=True)
#st.write(df) #ピクセルで大きさ指定できない
#st.dataframe(df.style.highlight_min(axis=0,color="#008000"), width = 400, height = 400) #動的
#st.table(df) #静的
"""
# 章
## 節
### 項

```python
import streamlit as st
import pandas as pd
import numpy as np
```
"""
