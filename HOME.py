import streamlit as st
import pandas as pd
from matplotlib import image
import os

# Set page configuration
st.set_page_config(
    page_title='Open Pubs Application',
    page_icon=':beer:',
    layout='wide',
    initial_sidebar_state='auto'
)

# Main title
st.title("Welcome to :red[Open Pub Application!] 🍻🍻 ")

os.chdir("D:/ML & AI (Resources & Work)/5.INNOMATICS INTERNSHIP/5. ML & MLOPS/P17_FIND_NEAREST_PUB/resources")

# Image
IMAGE_PATH = os.path.join("images", "drink_together.jpg")
img = image.imread(IMAGE_PATH)
st.image(img,use_column_width=True)

# Header
st.subheader("If you're on vacation in the United Kingdom and looking for pubs to visit, you've come to the right place. Google Maps may be down, but we have all the pub locations you need at your fingertips.")
st.subheader("Using data from https://www.getthedata.com/open-pubs, we've created a web application that allows you to easily find pubs near you.")
st.subheader("Simply enter your current location , and we'll show you all the pubs in the area. You can filter the results by distance, rating, and more to find the perfect pub for you and your friends..")
st.subheader("We hope you enjoy using our pub finder web app and discovering all the great pubs that the United Kingdom has to offer!")

DATA_PATH = os.path.join("data", "cleaned.csv")

st.header(":green[DataFrame]")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.header(":red[Details of the Dataset]")
st.markdown("**Select on sidebar to view the details:**")
section = st.sidebar.radio('Select a section to view', ['Head', 'Tail', 'Columns', 'Shape', 'Descriptive Statistics', 'Data Types', 'Missing Values'])

# Display the first few rows of the dataset
if section == 'Head':
    st.subheader('First 5 rows')
    st.write(df.head())

# Display the last few rows of the dataset
elif section == 'Tail':
    st.subheader('Last 5 rows')
    st.write(df.tail())

# Display the columns of the dataset
elif section == 'Columns':
    st.subheader('Columns')
    st.write(df.columns)

# Display the shape of the dataset
elif section == 'Shape':
    st.subheader('Shape')
    st.write(df.shape)
    
# Display descriptive statistics for each variable
elif section == 'Descriptive Statistics':
    st.subheader('Descriptive Statistics')
    st.write(df.describe())

# Display data types
elif section == 'Data Types':
    st.subheader('Data Types')
    st.write(df.dtypes)

# Display missing values
elif section == 'Missing Values':
    st.subheader('Missing Values')
    st.write(df.isnull().sum())

st.subheader(":violet[Top 10 Locations :] ")
IMAGE_PATH_2 = os.path.join("images", "pubs_by_location.png")
img = image.imread(IMAGE_PATH_2)
st.image(img,use_column_width=True)


st.subheader(":green[Feel free to connect with me :]")
# Add LinkedIn and GitHub links
link = '[![Title](https://camo.githubusercontent.com/5e3d78e5310a41c0667e07077cf93596229de398b154b83885dc068874ed5365/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c696e6b6564696e2d2532333145373742352e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465)](https://www.linkedin.com/in/tushar-goel04/)'
st.markdown(link,unsafe_allow_html=True)
link2 = '[![Title](https://camo.githubusercontent.com/b2d1ae072c968dbeaf2232f0e1071ae5a7b218b11caec1ae5c69c10ef370a3cc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d2532333234323932652e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)](https://github.com/TusharGoel13)'
st.markdown(link2,unsafe_allow_html=True)
