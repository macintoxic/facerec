# simple_loopback.py
from matplotlib import pyplot as plt
import tensorflow as tf
#from mtcnn import MTCNN
import numpy as np
#import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer



print("TF Version:", tf.__version__)
#print("CV2 Version:", cv2.__version__)

st.header("WebRTC demo")
webrtc_streamer(key="example")


print(__name__)
