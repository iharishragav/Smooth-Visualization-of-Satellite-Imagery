import os
import requests
import numpy as np
import cv2
from flask import Flask, request, jsonify
from generator import interpolate
from imageio import mimsave

app = Flask(__name__)
from flask_cors import CORS
CORS(app)


def get_image(url):
    """
    Fetch an image from a URL and print its shape using OpenCV.

    Args:
        url (str): URL of the image.

    Returns:
        tuple: Shape of the image (height, width, channels).
    """
    try:
        # Fetch the image from the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for HTTP issues

        img_array = np.asarray(bytearray(response.content), dtype=np.uint8)

        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if image is None:
            print("Error: Unable to decode the image.")
            return None
        return image

    except Exception as e:
        print(f"Error fetching or processing the image: {e}")
        return None

def load_image(t1, t2, bbox):
    base_url = ("https://mosdac.gov.in/live_data/wms/live3RL1BSTD1km/products/Insat3r/3R_IMG/2024/10DEC/3RIMG_10DEC2024_{timestamp}_L1B_STD_V01R00.h5?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&FORMAT=image%2Fpng&TRANSPARENT=true&LAYERS=IMG_VIS&COLORSCALERANGE=46%2C538&BELOWMINCOLOR=extend&ABOVEMAXCOLOR=extend&transparent=true&format=image%2Fpng&STYLES=boxfill%2Fgreyscale&WIDTH=256&HEIGHT=256&CRS=EPSG%3A3857&BBOX={bbox}")
    
    images = []
    for timestamp in [t1, t2]:
        url = base_url.format(timestamp=timestamp, bbox = bbox)
        try:
            img = get_image(url)
            if img is not None:
                images.append(img)
            else:
                print(f"Failed to download image for timestamp {timestamp}.")
        except Exception as e:
            print(f"Error downloading image for timestamp {timestamp}: {e}")
            images.append(None)

    # Handle cases where downloads might fail
    img1 = images[0] if len(images) > 0 else None
    img2 = images[1] if len(images) > 1 else None

    return img1, img2


@app.route('/interpolate/', methods=['POST'])
def receive_data():
    data = request.json  
    timestamp = data.get('timestamp')
    bbox = data.get('bbox')
    req_id = data.get('req_id')
    img1,img2 = load_image(timestamp[0],timestamp[1],bbox)
    
    frames = interpolate(img1,img2)
    print(type(frames))
    print(len(frames))
    output_dir = os.path.join('static')
    os.makedirs(output_dir, exist_ok=True)
    video_path = os.path.join(output_dir, f"{req_id}.mp4")

    img_arr = []
    for img_index in range(1,31):
        img_arr.append(frames[img_index])

    try:
        # Save the video using mimsave
        mimsave(video_path, img_arr, fps=30)  # Adjust FPS as needed

        # Respond with the video path
        return jsonify({"message": "Video generated successfully", "video_path": video_path}), 200
    except Exception as e:
        print(f"Error saving video: {e}")
        return jsonify({"error": "Failed to save video"}), 500

    return jsonify(response), 200

@app.route('/hello',methods=['GET'])
def hello():
    return 'hi'

if __name__ == '__main__':
    app.run(debug=True)
