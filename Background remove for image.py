from rembg import remove
import numpy as np
import cv2

# Load the image
input_path = 'C:/Users/Viswajith/Downloads/wp6390855-ms-dhoni-4k-desktop-wallpapers.jpg'
output_path = 'C:\Brackground remove for image\output_image10_no_bg.png'

# Read the image
input_image = cv2.imread(input_path)

# Remove the background
output_image = remove(input_image)

# Save the image with the background removed
cv2.imwrite(output_path, output_image)





#if you are using flask means change the file name at app.py
# pip install flask rembg opencv-python-headless numpy


# from flask import Flask, request, render_template, redirect, url_for, send_file
# from rembg import remove
# import cv2
# import numpy as np
# import os

# app = Flask(__name__)

# # Route to upload the image
# @app.route('/')
# def index():
#     return render_template('upload.html')

# # Route to handle the image upload and process background removal
# @app.route('/remove_bg', methods=['POST'])
# def remove_bg():
#     # Check if the POST request has the file part
#     if 'file' not in request.files:
#         return redirect(request.url)

#     file = request.files['file']
#     if file.filename == '':
#         return redirect(request.url)

#     if file:
#         # Save the uploaded file temporarily
#         input_image_path = os.path.join('uploads', file.filename)
#         file.save(input_image_path)

#         # Read the image with OpenCV
#         input_image = cv2.imread(input_image_path)

#         # Remove the background using rembg
#         output_image = remove(input_image)

#         # Define the output path
#         output_image_path = os.path.join('outputs', f'output_{file.filename}')

#         # Save the result image
#         cv2.imwrite(output_image_path, output_image)

#         # Return the processed image for download
#         return send_file(output_image_path, as_attachment=True)

# if __name__ == '__main__':
#     # Ensure uploads and outputs directories exist
#     os.makedirs('uploads', exist_ok=True)
#     os.makedirs('outputs', exist_ok=True)
#     app.run(debug=True, use_reloader=False)

