from moviepy.editor import VideoFileClip

def compress_gif(input_gif_path, output_gif_path):
    clip = VideoFileClip(input_gif_path)

    clip = clip.set_duration(clip.duration).set_fps(2)

    clip = clip.resize(height=640)

    clip.write_gif(output_gif_path, program="ImageMagick", fuzz=4, tempfiles=True)

compress_gif("./cpAdd.gif", "./cpAdd2.gif")
