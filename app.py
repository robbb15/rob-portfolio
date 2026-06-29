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

# ---- PARTICLE BACKGROUND ---- #
st.markdown("""
    <style>
    canvas {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        z-index: 0 !important;
        pointer-events: none !important;
    }
    </style>

    <canvas id="particle-canvas"></canvas>

    <script>
        const canvas = document.getElementById('particle-canvas');
        const ctx = canvas.getContext('2d');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });

        const particles = [];
        const count = 100;

        for (let i = 0; i < count; i++) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                radius: Math.random() * 3 + 1,
                dx: (Math.random() - 0.5) * 1.5,
                dy: (Math.random() - 0.5) * 1.5,
                opacity: Math.random() * 0.5 + 0.2
            });
        }

        function drawParticles() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            particles.forEach(p => {
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(76, 175, 80, ${p.opacity})`;
                ctx.fill();

                p.x += p.dx;
                p.y += p.dy;

                if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
                if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
            });

            // Draw lines between nearby particles
            particles.forEach((p1, i) => {
                particles.slice(i + 1).forEach(p2 => {
                    const dist = Math.hypot(p1.x - p2.x, p1.y - p2.y);
                    if (dist < 120) {
                        ctx.beginPath();
                        ctx.moveTo(p1.x, p1.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.strokeStyle = `rgba(76, 175, 80, ${0.3 * (1 - dist / 120)})`;
                        ctx.lineWidth = 0.5;
                        ctx.stroke();
                    }
                });
            });

            requestAnimationFrame(drawParticles);
        }

        drawParticles();
    </script>
""", unsafe_allow_html=True)

# ---- BACKGROUND ANIMATION ---- #
st.markdown("""
    <style>
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(
            135deg,
            #0a0a0a 0%,
            #0d1117 25%,
            #0a0a0a 50%,
            #111111 75%,
            #0a0a0a 100%
        );
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    </style>
""", unsafe_allow_html=True)

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
