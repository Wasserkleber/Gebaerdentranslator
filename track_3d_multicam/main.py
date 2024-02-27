import cv2
import numpy as np
import pickle
from scipy.ndimage import binary_closing, binary_opening

from config import *

def read_video(file):
    cap = cv2.VideoCapture(file)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frames.append(frame)

    cap.release()
    frames_array = np.array(frames)
    
    return frames_array

def show_image_with_rgb_values(image):
    # Create a window to display the image
    cv2.namedWindow('Image')
    
    def on_mouse_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # Get RGB values of the selected pixel
            b, g, r = image[y, x]
            print(f"RGB values at ({x}, {y}): R={r}, G={g}, B={b}")

    # Set mouse callback function
    cv2.setMouseCallback('Image', on_mouse_event)

    # Display the image
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_mask(bool_mask):
    bool_mask_uint8 = bool_mask.astype(np.uint8)
    color_mask = np.ones((*bool_mask.shape, 3), dtype=np.uint8) * 255
    color_mask[bool_mask_uint8 == 0] = [0, 0, 0]

    # Create a window to display the image
    cv2.namedWindow('mask')
    def on_mouse_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"({x}, {y})")

    # Set mouse callback function
    cv2.setMouseCallback('mask', on_mouse_event)

    # Display the image
    cv2.imshow('mask', color_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def createMaskVideo(video,color, threshold):
    distances = np.linalg.norm(video - color, axis=-1)
    print(np.max(distances))
    print(np.min(distances))
    bool_array = distances < threshold
    return bool_array

def binary_closing_opening(bool_array):
    # Perform binary closing along the x and y axes
    closed_array = binary_closing(bool_array, structure=np.ones((1, 5, 5)))

    # Perform binary opening along the x and y axes
    opened_closed_array = binary_opening(closed_array, structure=np.ones((1, 5, 5)))

    return opened_closed_array

def find_objects_and_centers(binary_image):
    # Convert boolean array to uint8
    binary_image_uint8 = binary_image.astype(np.uint8)

    # Find connected components in the binary image
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image_uint8, connectivity=8)

    # Remove background (0th label)
    num_labels -= 1
    stats = stats[1:]
    centroids = centroids[1:]

    # Display the number of objects found
    print("Number of objects found:", num_labels)

    # Return the stats and centroids of the objects
    return stats, centroids

# Function to save the detected objects
def save_detected_objects(detected_objects, filename):
    with open(filename, 'wb') as f:
        pickle.dump(detected_objects, f)

# Function to load the detected objects
def load_detected_objects(filename):
    with open(filename, 'rb') as f:
        detected_objects = pickle.load(f)
    return detected_objects

def track_points():
    for i,cam_video_file in enumerate(cam_video_files):
        cam_video=read_video(cam_video_file)
        limits=cam_video_limits[i]
        cam_video=cam_video[0:10,limits[0]:limits[1],limits[2]:limits[3],:]   #safe RAM
        print(cam_video.shape)
        #show_image_with_rgb_values(cam_video[0,:,:,:])
        
        cam_video_red=createMaskVideo(cam_video,cam_video_red_color[i],50) 
        cam_video_red=binary_closing_opening(cam_video_red)
        #show_mask(cam_video_red[0,:,:])
        cam_video_red_points=[]
        for t in range(cam_video_red.shape[0]):
            stats, centroids = find_objects_and_centers(cam_video_red[t,:,:])
            cam_video_red_points.append((t,centroids))
        cam_video_red_points_file=cam_video_red_points_files[i]
        save_detected_objects(cam_video_red_points,cam_video_red_points_file)

        cam_video_green=createMaskVideo(cam_video,cam_video_green_color[i],50) 
        cam_video_green=binary_closing_opening(cam_video_green)
        #show_mask(cam_video_green[0,:,:])
        cam_video_green_points=[]
        for t in range(cam_video_green.shape[0]):
            stats, centroids = find_objects_and_centers(cam_video_green[t,:,:])
            cam_video_green_points.append((t,centroids))
        cam_video_green_points_file=cam_video_green_points_files[i]
        save_detected_objects(cam_video_green_points,cam_video_green_points_file)

def calculate_camera_positions():
    p1_2D=np.array((1,1))
    p2_2D=np.array((1,1))
    p3_2D=np.array((1,1))

    p1_3D=np.array((1,0,0))
    p2_3D=np.array((0,1,0))
    p3_3D=np.array((0,0,1))

    #camera model:
    #https://en.wikipedia.org/wiki/Camera_resectioning

if __name__ == "__main__":
    #track_points()
    calculate_camera_positions()