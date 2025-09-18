from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import PromptTemplate
load_dotenv()
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
import streamlit as st
hf_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token

st.markdown(
    """
    <h1 style='display: flex; align-items: center;'>
        <img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJUAAACUCAMAAACtIJvYAAAAjVBMVEX///8AjeUAiuf///1yr93f8PYAiOIAjecAi+Ydj9yTv+EAhuMAgNve8PsAgN3j8PkhkuTT5vPZ6fMAhdmiyucAg+TC3e3q8vnM4fAAf9Ywk+Hz9/uOv+jZ8PWEuObu+vik0ehGm9/A2fCz1esAettbpd2Bv+Q1lt/k+Phlq91Gn90yldjN6PK+3+tztuKdjWr4AAAEoElEQVR4nO2bDXOiMBCGCQE2NFZR0daPSq1aq/X6/3/eBRBYxNbRbCw3l7czdCbQ5OlmSTZL4jhWVlZWVlZWVlZWVlZWVlZW/7s4z67qt4ZQTURQWa0kFVLVk1flvMQLT1eL+IWIKPvXZqtw7QpXV0Kuw1VCAqWoko0UjEQggk1C0IeKahC6NEwZlxv2KWzFl4RQDJi7138TOV9IQihFxaSnb6xeSAmVcsHwUZvqXQI1lZxrU22JXj9EJULd1zCZEJtKUbGJ7qD1EQB1Dyp/9zWN5VMOC4VcbargX6GCzDnaRSVkdxh2Rq4GFz2V2MYfqvywUya71WLEVOks5vM8Kn0NbrYWta1gmQaT+c/qZixaKtVj47S+tEplrc2towaxrcSmqo074xuhqKlq8yr3o3ZQjV4xVRK24x2UMaZ6itpB5dbCyLb4FWyL+tI3cTFsBRUw+ZUvztPruNMOWyk3ClZ5hZz7nzdHqeRjO+vuBmmNT/FQsHaM7enoDsF0M597W51FBn3MoCIF4UoXdCIsY7Fou6K+3ETqCkcwqAMeC7MEjoBv6Mn9qsr7yMKz5KgscrNQUI4me8/zdvthV4pzPU1uK++h1DyfcOSiKtqky6rp/FD89Ue8D86MH+RUz9WtWT45j1DWIJbQ/fJ5OdJyJ1lFbsNc5FTj6tZTmDXXPVRFcxn+OU3JJrvGC3Nvqs6fMl9carY/zTWRryYwVZRSQQfl7uar9Hraor+Fe1JlRd3Kr/jhfGsPsj5CkFMhb29SfZtOPwkPzVLBKZXTcKq89CSLSb7yukxVhF+43TeTPQgQYSqWe/sZWyVO7ZsNH0yN2uoClbLQLF6u1+vh1wDXkizN2goNA+epdt10igGpInxUvBHmqNhFKu4d/RrkHi+zF+69qbBRHosVBrBO1YdcTUV368Ggaav3qnW1+i+a5mravhMV72W3lK1QC8vCf4C5u/I15M7r6BepkmkRtajob4mavicVnFL1ospWYovmaZNUjEXIhXuZr8AEUQ3QhAdTVM0dqYIGVd9S/Ug1RONVHzthjcrgyGCprqCCKQoFHvORAVM94/ztFjUdm/QrmPYQVSenmmGq0tsBalRmbYWpujnVE6JiZcQCbImq+VWqMaJKZ5yy7TtSNXsQZ5UFpnpoJZXJ+OosFWsBFRoGcr9i2FZvZRoNMqryhlkqvEbo594efU9VySgVw7Y6XEFl2NvPUVUtvFVPMrEvi82uJs7ZitWo4DeoYIqGzEOn2YO/Q7VF+25yKhGip5+xX23QDbN+xUIkkRdtURFKsNeejQzmGbLNU4WOqeE0wV4Jb7xAz4LRTFH9W0PRWRik/j+UxUZzfSf6+WPON3fTj4z+5YYvUBnYq6ZNldz6bfknqkmiu2X09u+431Gp8UXTVI7zPrrc0HVUECx481PBdfIjYmOBiHzd7ffpjl/CXZDpGOF657Py12F96myWa2K5nwTnFLjTDyk3/Qq1/CY4pMCdZBMIIi7Idt3THJ1IVuFaah9QcF2yEwrO8dvMS6x9mMPzstMcZGdMCE+r0J3IIWQiqsnKysrKysrKysrKysrKysrq39ZftldWxEBs6ucAAAAASUVORK5CYII=' width='40' style='margin-right:10px'>
        LinkedIn Post Generator
    </h1>
    """,
    unsafe_allow_html=True
)

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
)
model = ChatHuggingFace(llm=llm)
prompt = PromptTemplate(
    template = ''' You are an expert linkdin post writer who help people write a high quality linkdin post accordign to people choice.
    Here are the user prefrences and you have to write linkdin post according to that.

--Write a linkdin post on topic: "{topic}"  in {style} way.

--Include emojis: {emoji}.

--Include headings and points: {headings}.

--Include Hastags at end of post: {hastag}.

--Keep the post length {length} overall.

--Keep the post engaging and interesting to read.
--Make sure the post is easy to read and understand.

    ''',input_variables=['topic','style','emoji','headings','hastag','length']
)
st.header("Genrate LinkedIn post in seconds🕛⏩")
st.title("Customize your post below: ")
# Topic:
topic = st.text_input("Enter your topic:")

if st.button("Submit"):
    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic to proceed.")
        st.stop()
    else:
        st.success(f"✅ Topic submitted: {topic}")
# Style:
st.write("Select a style of post: ")
style = st.selectbox(
    'Professional',
    ("Professional", "Custom_style", "Casual", "Storytelling",
     "Educational / Tutorial", "Cheat-Sheet", "Opinion",
     "Inspirational", "Question / Discussion")
     
)
if style == "Custom_style":
  style = st.text_input("Enter your custom style: ")
else:
  style = style 
# Emoji: 
use_emoji = st.checkbox("Include emojis👍 in the post?")
emoji = "Yes" if use_emoji else "No"

# Headings and points:
headings = st.checkbox("Include headings and points in the post?")
if headings:
    headings = 'Yes'
else:
    headings = 'No'
# Hastags:
hastag = st.checkbox("Include Hastags in the post?")
if hastag:
    hastag = 'Yes'
else:
    hastag = 'No'
# Length:
length = st.selectbox(
    "Choose the length of the post:",
    ("Short (100-200 words)", "Medium (200-400 words)", "Long (400-600 words)")
)
prompt1 = prompt.format(topic=topic,style=style,emoji=emoji,headings=headings,hastag=hastag,length=length)
result = model.invoke(prompt1)
if st.button("Generate Post"):
    st.write("### Generated Linkdin Post:")

    st.write(result.content)




