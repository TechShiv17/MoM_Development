import moviepy.editor
import logging


class VideoToAudioConverter:
    @staticmethod
    def audio_converter_from_video(video_path, output_audio_path):
        try:
            logging.info(f"\nLoading the YouTube Video from {video_path}")
            # Load the video file
            video_clip = moviepy.editor.VideoFileClip(video_path)

            logging.info("\nExtracting the audio from video")
            # Extract audio from the video
            audio_clip = video_clip.audio

            logging.info(f"\nSaving the audio to {output_audio_path} directory.")
            # Save the extracted audio to a file
            audio_clip.write_audiofile(output_audio_path)

            # Close the video and audio clips
            video_clip.close()
            audio_clip.close()

            logging.info("\nAudio extraction completed successfully.")

        except FileNotFoundError as e:
            logging.error(f"\nFile not found error: {e}")

        except Exception as e:
            logging.error(f"\nAn error occurred: {e}")
