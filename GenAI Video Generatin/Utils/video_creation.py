from moviepy.editor import *
import os

def create_video(script, image_paths, audio_path, output_file):
    clips = []
    duration = 5
    for img_path in image_paths:
        clip = ImageClip(img_path).set_duration(duration).resize(height=720)
        clips.append(clip)
    
    final_clip = concatenate_videoclips(clips, method="compose")
    audio = AudioFileClip(audio_path).set_duration(final_clip.duration)
    video = final_clip.set_audio(audio)

    output_path = f"output_videos/{output_file}"
    video.write_videofile(output_path, fps=24)
