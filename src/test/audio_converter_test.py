import unittest
import os
from src.utils.audio_converter import VideoToAudioConverter
from src.utils.video_downloader import VideoDownloader


class VideoToAudioConverterTest(unittest.TestCase):

    def test_audio_conversion_with_video(self):
        tempfile_path = "../static/"
        video_file_name = "demo_video_test"
        video_ext = ".mp4"
        audio_file_name = "demo_audio_test.mp3"

        if not os.path.isdir(tempfile_path):
            os.mkdir(tempfile_path)

        if os.path.exists(tempfile_path + "/" + video_file_name + ".mp4"):
            pass
        else:
            VideoDownloader.download_video_from_url("https://www.youtube.com/watch?v=u57LMno2Icg",
                                                    f"{tempfile_path}{video_file_name}")

        VideoToAudioConverter.audio_converter_from_video(f"{tempfile_path}{video_file_name}{video_ext}",
                                                         f"{tempfile_path}{audio_file_name}")
        result = os.path.exists(tempfile_path + "/" + audio_file_name)
        self.assertTrue(result)

