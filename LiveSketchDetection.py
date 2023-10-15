#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[2]:


import cv2

# Function to apply sketch effect using Canny edge detection
def sketch(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to the grayscale image to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Use Canny edge detection to detect edges in the image
    edges = cv2.Canny(blurred, threshold1=10, threshold2=70)
    
#     # Invert the edges image to make the edges white and background black
    inverted_edges = cv2.bitwise_not(edges)
    
    # Create a blank white canvas of the same size as the original image
#     sketch_image = cv2.bitwise_not(image, image.copy(), mask=inverted_edges)
    ret, mask = cv2.threshold(edges,70,255,cv2.THRESH_BINARY_INV)
    
    return mask

# Open a connection to the first camera device (0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Apply sketch effect to the frame
    sketch_frame = sketch(frame)
    
    # Display the sketch frame
    cv2.imshow('Sketch', sketch_frame)
    
    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()


# In[ ]:




