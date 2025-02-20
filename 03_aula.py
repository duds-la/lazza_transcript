import streamlit as st
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = openai.OpenAI()

def transcreve_tab_mic():
    st.markdown('transcreve microfone')

def transcreve_tab_video():
    st.markdown('transcreve video')
    
def transcreve_tab_audio():
    prompt_input = st.text_input('(opcional) Digite seu prompt:', key='input_audio')
    arquivo_audio = st.file_uploader('Adicione um arquivo de áudio .mp3', type=['mp3'])

    if not arquivo_audio is None:
        transcricao = client.audio.transcriptions.create(
            model='whisper-1',
            language='pt',
            response_format='text',
            file=arquivo_audio,
            prompt=prompt_input
        )
        st.write(transcricao)

def main():
    st.header('Bem vindo ao Lazza transcipt', divider=True)
    st.markdown('### Transceva o que quiser!')
    tab_mic, tab_video, tab_audio = st.tabs(['Microfone', 'Video', 'Audio'])

    with tab_mic:
        transcreve_tab_mic()
    
    with tab_video:
        transcreve_tab_video()

    with tab_audio:
        transcreve_tab_audio()

if __name__ == '__main__':
    main()