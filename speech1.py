import streamlit as st
import docx
import pyttsx3
import gtts
import os

def main():
    # Initialize the converter
    engine = pyttsx3.init()
    newVoiceRate = 145
    engine.setProperty('rate',newVoiceRate)

    st.title("This is the title")
    st.sidebar.title("This is sidebar")
    upload_file = st.sidebar.file_uploader("Upload ur file here", type=['csv','xlsx','docx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('.docx'):
                doc = docx.Document(upload_file)

                doc_text=''
                for para in doc.paragraphs: 
                    doc_text += para.text
            else:
                return "incorrect file format"
            
            st.sidebar.success("file uploaded successfully")
            st.subheader("data below")
            #st.dataframe(doc_text)
            if st.button('docx file'): # display a button widget and use a short label ('.docx file') explaining to the user what this button is for
                st.write(doc_text) 

            #print doc contents
            #print(doc_text)

            # Convert text to speech
            #engine.say(doc_text)
            #engine.runAndWait()

            language = 'en'
            myobj = gtts.gTTS(text=doc_text, lang=language, slow=False)
            myobj.save("generated_speech_to_text.mp3")
            # play the stored audio
            os.system("generated_speech_to_text.mp3")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
