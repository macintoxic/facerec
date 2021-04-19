# simple_loopback.py
from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np
#import cv2
#from mtcnn import MTCNN
import streamlit as st
from streamlit_webrtc import webrtc_streamer, ClientSettings, VideoTransformerBase, WebRtcMode

print("TF Version:", tf.__version__)
#print("CV2 Version:", cv2.__version__)


WEBRTC_CLIENT_SETTINGS = ClientSettings(
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
)

st.header("Face detect demo")
rtc = webrtc_streamer(key="example", client_settings=WEBRTC_CLIENT_SETTINGS)


dir(rtc)
print(__name__)



