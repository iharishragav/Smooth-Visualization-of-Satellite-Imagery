

 # Smooth Visualization of Satellite Imagery
 
 This project is a web application that provides a smooth visualization of satellite imagery by interpolating between two images.
 
 ## Features
 
 -   **Satellite Image Fetching:** The application fetches satellite imagery from a specified URL.
 -   **Image Interpolation:** It uses a deep learning model to interpolate between two satellite images, creating a smooth video transition.
 -   **Web-based Visualization:** The application provides a web interface to display the generated video.
 
 ## Technologies Used
 
 -   **Frontend:**
     -   HTML
     -   CSS
     -   JavaScript
 -   **Backend:**
     -   Flask (Python)
     -   OpenCV
     -   NumPy
     -   PyTorch (for the interpolation model)
 
 ## Project Structure
 
 The project is divided into two main components:
 
 -   **`frontend/`:** Contains the client-side code for the web interface.
     -   `client-processing/`: The main interface for the application.
     -   `server-processing/`: An alternative interface.
 -   **`server/`:** Contains the backend Flask server and the image processing logic.
     -   `app.py`: The main Flask application file.
     -   `generator.py`: Contains the image interpolation logic.
     -   `model.py`: The deep learning model for interpolation.
     -   `IFRNet_S_Vimeo90K.pth`: The pre-trained model weights.
 
 ## How it Works
 
 1.  The user provides two timestamps and a bounding box through the web interface.
 2.  The frontend sends a request to the backend Flask server.
 3.  The server fetches the corresponding satellite images from the specified URL.
 4.  The server uses the pre-trained deep learning model to interpolate between the two images, generating a sequence of frames.
 5.  The frames are then encoded into a video file.
 6.  The video is sent back to the frontend and displayed to the user.
 
 ## Getting Started
 
 ### Prerequisites
 
 -   Python 3.x
 -   Flask
 -   OpenCV
 -   NumPy
 -   PyTorch
 -   imageio
 
 ### Installation
 
 1.  Clone the reposito git clone https://github.com/iharishragav/Smooth-Visualization-of-Satellite-Imagery.
2.  Install the required Python packag pip install -r requirements.
3.  Run the Flask serv cd serve python app
4.  Open the `frontend/client-processing/index.html` file in your web browser.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an iss
 # Smooth Visualization of Satellite Imagery
 
 This project is a web application that provides a smooth visualization of satellite imagery by interpolating between two images.
 
 ## Features
 
 -   **Satellite Image Fetching:** The application fetches satellite imagery from a specified URL.
 -   **Image Interpolation:** It uses a deep learning model to interpolate between two satellite images, creating a smooth video transition.
 -   **Web-based Visualization:** The application provides a web interface to display the generated video.
 
 ## Technologies Used
 
 -   **Frontend:**
     -   HTML
