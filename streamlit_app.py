from streamlit_extras.colored_header import colored_header
from streamlit_extras.mention import mention
from streamlit_extras.badges import badge
import streamlit as st
from lyzr import QABot
import configparser
import openai


st.set_page_config(layout="wide")
config = configparser.ConfigParser()
config.read("./config.ini")


MODEL = config["MODEL"]["LLM"]
MATCH_PERCENTAGE = config["DETAILED_PROMPTS"]["MATCH_PERCENTAGE"]
MISSING_SKILLS = config["DETAILED_PROMPTS"]["MISSING_SKILLS"]
GRAMMAR_MISTAKES = config["DETAILED_PROMPTS"]["GRAMMAR_MISTAKES"]
ONLINE_COURSES = config["DETAILED_PROMPTS"]["ONLINE_COURSES"]
SALARY = config["DETAILED_PROMPTS"]["SALARY"]
CAREER_ADVICE = config["DETAILED_PROMPTS"]["CAREER_ADVICE"]

MATCH_PERCENTAGE2 = config["SHORT_PROMPTS"]["MATCH_PERCENTAGE"]
MISSING_SKILLS2 = config["SHORT_PROMPTS"]["MISSING_SKILLS"]
GRAMMAR_MISTAKES2 = config["SHORT_PROMPTS"]["GRAMMAR_MISTAKES"]
ONLINE_COURSES2 = config["SHORT_PROMPTS"]["ONLINE_COURSES"]
SALARY2 = config["SHORT_PROMPTS"]["SALARY"]
CAREER_ADVICE2 = config["SHORT_PROMPTS"]["CAREER_ADVICE"]


if 'response' not in st.session_state:
    st.session_state['response'] = None


with st.sidebar:
    input_file = st.file_uploader("Upload Resume PDFs", type="pdf")
    job_description = st.text_area("Paste the Job Description")
    temperature = st.slider(label="Temperature: Default 0.5", min_value=0.1, max_value=2.0, value=0.5)
    openai.api_key = st.text_input("OpenAI API", type="password")
    output_format = st.radio("Output Scale", ["Short and Crispy", "Detailed"])
    choice = st.radio("Select the Query", [
        "Match Percentage",
        "Missing Skills in the Resume",
        "Grammatical error in the Resume",
        "Online Courses",
        "Salary Prediction",
        "Future Opportunities",
    ])


    submitBtn = st.button("Submit")
    llm_params = (
        {
            "model": MODEL, "temperature": temperature
        }
    )

    
    if submitBtn:
        if output_format == "Detailed":
            if choice == "Match Percentage":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=MATCH_PERCENTAGE
                )
                st.session_state['response'] = qa_bot.query(job_description)

            if choice == "Missing Skills in the Resume":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=MISSING_SKILLS
                )
                st.session_state['response'] = qa_bot.query(job_description)

            if choice == "Grammatical error in the Resume":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=GRAMMAR_MISTAKES
                )
                st.session_state['response'] = qa_bot.query(job_description)

            if choice == "Online Courses":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=ONLINE_COURSES
                )
                st.session_state['response'] = qa_bot.query(job_description)

            if choice == "Salary Prediction":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=SALARY
                )
                st.session_state['response'] = qa_bot.query(job_description)

            if choice == "Future Opportunities":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=CAREER_ADVICE
                )
                st.session_state['response'] = qa_bot.query(job_description)

        if output_format == "Short and Crispy":
            if choice == "Match Percentage":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=MATCH_PERCENTAGE2
                )
                st.session_state['response'] = qa_bot.query(job_description)

            if choice == "Missing Skills in the Resume":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=MISSING_SKILLS2
                )
                st.session_state['response'] = qa_bot.query(job_description)

            if choice == "Grammatical error in the Resume":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=GRAMMAR_MISTAKES2
                )
                st.session_state['response'] = qa_bot.query(job_description)

            if choice == "Online Courses":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=ONLINE_COURSES2
                )
                st.session_state['response'] = qa_bot.query(job_description)

            if choice == "Salary Prediction":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=SALARY2
                )
                st.session_state['response'] = qa_bot.query(job_description)

            if choice == "Future Opportunities":
                qa_bot = QABot.pdf_qa(
                    input_files=[input_file.name],
                    llm_params=llm_params,
                    system_prompt=CAREER_ADVICE2
                )
                st.session_state['response'] = qa_bot.query(job_description)


col1, col2 = st.columns([0.9, 0.1])

with col1:
    colored_header(
        label="Application Tracking System and Resume Analyser",
        description="Analyse the resume for insights and improvements",
        color_name="red-70",
    )
    if st.session_state.response is None:
        st.caption("Upload the resume and analyse it")
    else:
        st.code('Output: ')
        st.write(st.session_state['response'].response)

with col2:
    colored_header(
        label="Connect",
        description="",
        color_name="red-70",
    )
    badge(type="pypi", name="lyzr")
    badge(type="twitter", name="lyzrai")
    badge(type="github", name="LyzrCore/lyzr")
    badge(type="github", name="sabhashanki/lyzr_shankesh")
    mention(
        label="LinkedIn",
        icon="🔗",  
        url="https://www.linkedin.com/in/shankeshrajums",
    )
    mention(
        label="Lyzr SDK",
        icon="🔗", 
        url="https://docs.lyzr.ai/lyzr-sdk/opensource/",
    )


