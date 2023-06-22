### Imports
import streamlit as st

### LangChain



### UI
st.title('GamePlan')
st.subheader('Generative AI Managed Enterprise PLAtform Network')
st.markdown('---')

with st.sidebar:    
    mysidebar = st.selectbox('Select GamePlan', ['Cybersecurity', 'Tourguide', 'Data Science', 'Techwriter'])

if mysidebar == 'Cybersecurity':
    st.write('Cyber')

if mysidebar == 'Tourguide':
    st.write('Tour')

if mysidebar == 'Data Science':
    st.write('Python')
    
if mysidebar == 'Techwriter':
    st.write('Document')





