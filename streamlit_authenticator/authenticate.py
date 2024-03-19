# Import the required module
import pyttsx3
import streamlit as st
from IPython.display import Audio

def get_audio():
    # Create a string
    string = "Lorem Ipsum is simply dummy text " \
    	+ "of the printing and typesetting industry."
    
    # Initialize the Pyttsx3 engine
    engine = pyttsx3.init()
    
    # We can use file extension as mp3 and wav, both will work
    engine.save_to_file(string, 'speech.mp3')
    
    # Wait until above command is not finished.
    engine.runAndWait()

if __name__=='__main__':
    get_audio()
    st_audio_widget = Audio("speech.mp3", autoplay=True)
    
