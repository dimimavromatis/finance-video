from moviepy import *
"""
video = VideoFileClip("Part01.mp4")

voiceover = AudioFileClip("Part01Audio.mp4")  # or .wav

video_with_voiceover = video.with_audio(voiceover)

video_with_voiceover.write_videofile("Part01_final.mp4", codec="libx264", audio_codec="aac")
"""


"""
video_part02 = VideoFileClip("Part02.mp4")

audio_part02 = AudioFileClip("Part02Audio.mp4")

video_part02_final = video_part02.with_audio(audio_part02)

video_part02_final.write_videofile("Part02_final.mp4", codec="libx264", audio_codec="aac")

#video_final = VideoFileClip("Part02.mp4")
#video_cut = video_final.with_section_cut_out(55, 58)
#video_cut.write_videofile("Part02_final.mp4", codec="libx264", audio_codec="aac")

video_part02 = VideoFileClip("Part02.mp4")

audio_part02 = AudioFileClip("Part02Audio.mp4")

video_part02_final = video_part02.with_audio(audio_part02)

video_part02_final.write_videofile("Part02_final.mp4", codec="libx264", audio_codec="aac")

video_final = VideoFileClip("Part02_final.mp4")
video_cut = video_final.with_section_cut_out(55, 58)
video_cut.write_videofile("Part02_final_cut.mp4", codec="libx264", audio_codec="aac")
"""

video_1 = VideoFileClip("Part01_final.mp4")
video_2 = VideoFileClip("Part02_final_cut.mp4")

final_clip = concatenate_videoclips([video_1, video_2])
final_clip.write_videofile("Dimi_final.mp4", codec="libx264", audio_codec="aac")

video_1.close()
video_2.close()
final_clip.close()
