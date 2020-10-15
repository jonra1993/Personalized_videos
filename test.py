# import vogon
import vogon
import csv

print("holii")
config_file= "Project/config.json"
# config_file = "config.json"
path_dir= "Project"
video_path = "Project/assets/base_video.mp4"
print(type(config_file))
vogon.generate_preview(config_file,1,path_dir)

# vogon.generate_video(config_file,1,3,path_dir)
# vogon.generate_videos(config_file,False,None,path_dir,False)
# vogon.generate_videos_final(config_file,None,path_dir)
# vogon.get_video_duration(video_path)