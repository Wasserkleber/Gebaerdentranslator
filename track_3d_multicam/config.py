import os
import numpy as np

current_file_directory = os.path.dirname(os.path.abspath(__file__))
video_folder=os.path.join(current_file_directory,'videos')

cam1_video1_file=os.path.join(video_folder,'cam1_video1.mp4')
cam1_video2_file=os.path.join(video_folder,'cam1_video2.mp4')
cam2_video1_file=os.path.join(video_folder,'cam2_video1.mp4')
cam2_video2_file=os.path.join(video_folder,'cam2_video2.mp4')
cam3_video1_file=os.path.join(video_folder,'cam3_video1.mp4')
cam3_video2_file=os.path.join(video_folder,'cam3_video2.mp4')

cam_video_files=[cam1_video1_file,
                 cam1_video2_file,
                 cam2_video1_file,
                 cam2_video2_file,
                 cam3_video1_file,
                 cam3_video2_file]

cam1_video1_red_points_file=os.path.join(video_folder,'cam1_video1_red_points.pkl')
cam1_video2_red_points_file=os.path.join(video_folder,'cam1_video2_red_points.pkl')
cam2_video1_red_points_file=os.path.join(video_folder,'cam2_video1_red_points.pkl')
cam2_video2_red_points_file=os.path.join(video_folder,'cam2_video2_red_points.pkl')
cam3_video1_red_points_file=os.path.join(video_folder,'cam3_video1_red_points.pkl')
cam3_video2_red_points_file=os.path.join(video_folder,'cam3_video2_red_points.pkl')

cam_video_red_points_files=[cam1_video1_red_points_file,
                 cam1_video2_red_points_file,
                 cam2_video1_red_points_file,
                 cam2_video2_red_points_file,
                 cam3_video1_red_points_file,
                 cam3_video2_red_points_file]


cam1_video1_green_points_file=os.path.join(video_folder,'cam1_video1_green_points.pkl')
cam1_video2_green_points_file=os.path.join(video_folder,'cam1_video2_green_points.pkl')
cam2_video1_green_points_file=os.path.join(video_folder,'cam2_video1_green_points.pkl')
cam2_video2_green_points_file=os.path.join(video_folder,'cam2_video2_green_points.pkl')
cam3_video1_green_points_file=os.path.join(video_folder,'cam3_video1_green_points.pkl')
cam3_video2_green_points_file=os.path.join(video_folder,'cam3_video2_green_points.pkl')

cam_video_green_points_files=[cam1_video1_green_points_file,
                 cam1_video2_green_points_file,
                 cam2_video1_green_points_file,
                 cam2_video2_green_points_file,
                 cam3_video1_green_points_file,
                 cam3_video2_green_points_file]

cam1_video1_limits=(50,600,366,830)
cam1_video2_limits=(86,580,426,850)
cam2_video1_limits=(417,690,510,788)
cam2_video2_limits=(33,510,365,790)
cam3_video1_limits=(7,560,415,990)
cam3_video2_limits=(54,520,302,737)

cam_video_limits=[cam1_video1_limits,
                 cam1_video2_limits,
                 cam2_video1_limits,
                 cam2_video2_limits,
                 cam3_video1_limits,
                 cam3_video2_limits]


cam1_video1_red_color=np.array((4,34,221),dtype=float)
cam1_video2_red_color=np.array((11,28,180),dtype=float)
cam2_video1_red_color=np.array((15,20,130),dtype=float)
cam2_video2_red_color=np.array((10,10,120),dtype=float)
cam3_video1_red_color=np.array((20,5,130),dtype=float)
cam3_video2_red_color=np.array((20,5,130),dtype=float)

cam_video_red_color=[cam1_video1_red_color,
                 cam1_video2_red_color,
                 cam2_video1_red_color,
                 cam2_video2_red_color,
                 cam3_video1_red_color,
                 cam3_video2_red_color]

cam1_video1_green_color=np.array((5,150,115),dtype=float)
cam1_video2_green_color=np.array((20,100,60),dtype=float)
cam2_video1_green_color=np.array((75,150,140),dtype=float)
cam2_video2_green_color=np.array((10,87,70),dtype=float)
cam3_video1_green_color=np.array((10,87,70),dtype=float)
cam3_video2_green_color=np.array((60,84,30),dtype=float)

cam_video_green_color=[cam1_video1_green_color,
                 cam1_video2_green_color,
                 cam2_video1_green_color,
                 cam2_video2_green_color,
                 cam3_video1_green_color,
                 cam3_video2_green_color]

