import streamlit as st
import requests
from streamlit_lottie import st_lottie

# ---- PAGE CONFIG ---- #
st.set_page_config(page_title="Rob's Portfolio", page_icon=":spider:", layout="wide")


# ---- LOAD ASSETS ---- #
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


lottie_coding = load_lottieurl("https://lottie.host/c041abab-c20e-4e2d-a6e3-7c08a1e9a822/X9grPOFV5F.json")
local_css("style/style.css")

# ---- HERO SECTION ---- #
left_column, right_column = st.columns((2, 1))

with left_column:
    st.subheader("Hi, I am Rob Andre Catapang :wave:")
    st.title("A Computer Engineering Graduate from Technological Institute of the Philippines - Quezon City")
    st.write(
        """
        I am a Computer Engineering graduate from Technological Institute of the Philippines - Quezon City.
        I have a strong passion for technology and innovation, and I am always eager to learn and grow in the field of computer engineering.
        My goal is to contribute to the development of cutting-edge technologies that can make a positive impact on society.
        """
    )
    st.write("[Learn More >](https://www.linkedin.com/in/rob-andre-catapang-aa5a43389/)")

with right_column:
    st.image("me.JPG", width=300)

# ---- WHAT I DO SECTION ---- #
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("What I do")
        # st.write("##")
        st.write(
            """
            I am a motivated and hardworking Computer Engineering graduate with a passion for 
            system administration, network management, and IT operations. I am seeking an entry-level 
            position where I can apply my academic foundation and technical skills while continuing 
            to learn and grow professionally.

             **System Administration & IT Operations**
            - Experienced in Windows Server and Ubuntu Linux environments
            - Skilled in network administration and analysis using Wireshark and Cisco Packet Tracer
            - Knowledgeable in TCP/IP fundamentals and network troubleshooting

             **Automation & Virtualization**
            - Hands-on experience with Ansible for IT automation
            - Proficient in Oracle VirtualBox for virtualization tasks

             **Programming & Scripting**
            - Developed projects using Python, C++, and Bash/Shell Scripting
            - Experienced in HTML/CSS for web development

             **Research**
            - Completed a Design of a Deep Learning Based Composition Classification System 
            For Abaca Bundle Using Multimodal Imaging


             **Design & Modeling**
            - Familiar with Figma, CAD Design, and Basic 3D Modeling
            """
        )

    with right_column:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_lottie(lottie_coding, height=300, key="coding")

# ---- EDUCATION SECTION ---- #
with st.container():
    st.write("---")
    st.header("My Education")
    # st.write("##")

    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Bachelor of Science in Computer Engineering")
        st.write("**Technological Institute of the Philippines - Quezon City**")
        st.write("2022 - 2025")
        st.write(
            """
            - Studied core subjects including Data Structures, Algorithms, 
              Computer Networks, and Operating Systems.
            - Gained hands-on experience in Python, C++, Java, and web development.
            - Completed capstone project focusing on classification between abaca and fake abaca(daratex).
            """
        )

    with right_column:
        st.subheader("Senior High School")
        st.write("**Marikina Catholic High School**")
        st.write("2020 - 2021")
        st.write(
            """
            - STEM Strand (Science, Technology, Engineering, and Mathematics)
            """
        )

    # st.write("##")
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Junior High School")
        st.write("**Marikina Catholic High School**")
        st.write("2016 - 2019")
        st.write(
            """
            - Active participant in school science and technology clubs.
            """
        )

    with right_column:
        st.subheader("Elementary School")
        st.write("**Marikina Catholic School**")
        st.write("2010 - 2015")
        st.write(
            """
            - Developed early interest in science and technology.
            """
        )

# ---- SKILLS SECTION ---- #
with st.container():
    st.write("---")
    st.header("My Skills")
    # st.write("##")

    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Technical Skills")

        st.write("Ubuntu/Linux")
        st.progress(70)

        st.write("C++")
        st.progress(30)

        st.write("Java")
        st.progress(30)

        st.write("HTML/CSS")
        st.progress(67)

        st.write("Python")
        st.progress(50)

        st.write("Ansible")
        st.progress(60)

        st.write("Oracle VirtualBox")
        st.progress(60)

        st.write("Cisco Packet Tracer")
        st.progress(60)

        st.write("Bash/Shell Scripting")
        st.progress(65)

    with right_column:
        st.subheader("Soft Skills")

        st.write("Team Collaboration")
        st.progress(85)

        st.write("Time Management")
        st.progress(85)

        st.write("Communication Skills")
        st.progress(75)

        st.write("Adaptability & Continuous Learning")
        st.progress(90)

        st.write("Technical Documentation")
        st.progress(95)


# ---- RESUME SECTION ---- #
with st.container():
    st.write("---")
    st.header("My Resume")
    # st.write("##")

    with open("ROB ANDRE CATAPANG resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="Rob_Catapang_Resume.pdf",
        mime="application/octet-stream"
    )


# ---- CONTACT SECTION ---- #
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    # st.write("##")

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
