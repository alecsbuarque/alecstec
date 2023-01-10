import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Chanin Nantasenamat, Ph.D.')

st.info('Developer Advocate, Content Creator and ex-Professor with an interest in Data Science and Bioinformatics')

icon_size = 20

st_button('Youtube', 'https://youtube.com/@alecstec', 'Canal do Youtube', icon_size)
st_button('Instagram', 'https://instagram.com/alecstec', 'Me siga no instagram!', icon_size)
st_button('Tiktok', 'https://tiktok.com/@alecstec', 'Follow me on Twitter', icon_size)
