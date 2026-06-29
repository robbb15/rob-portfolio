import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Rob's Portfolio", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/c041abab-c20e-4e2d-a6e3-7c08a1e9a822/X9grPOFV5F.json")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.subheader("Hi, I am Rob Andre Catapang :wave:")
st.title("A Computer Engineering Graduate from the Technological Institute of the Philippines - Quezon City")
st.write("I am a Computer Engineering graduate from the Technological Institute of the Philippines - Quezon City. I have a strong passion for technology and innovation, and I am always eager to learn and grow in the field of computer engineering. My goal is to contribute to the development of cutting-edge technologies that can make a positive impact on society.")
st.write("[Learn More >](https://www.linkedin.com/in/rob-andre-catapang-aa5a43389/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a Computer Engineering graduate with a strong passion for technology and innovation. I have experience in various programming languages and technologies, including Python, C++, Java, HTML and web development. . 
            My goal is to contribute to the development of cutting-edge technologies that can make a positive impact on society.
            """
        )
        st.write("[Facebook account >](https://www.facebook.com/robcaaat)")

with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


#---Contact Form---#
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/robcatapang15@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()