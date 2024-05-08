import unittest
import os
from src.utils.video_downloader import VideoDownloader


class VideoDownloaderTest(unittest.TestCase):

    def test_video_download_with_correct_url(self):
        tempfile_path = "../static/"
        video_file_name = "demo_video_test"
        if not os.path.isdir(tempfile_path):
            os.mkdir(tempfile_path)

        VideoDownloader.download_video_from_url("https://www.youtube.com/watch?v=u57LMno2Icg",
                                                f"{tempfile_path}{video_file_name}")
        result = os.path.exists(tempfile_path + "/" + video_file_name + ".mp4")
        self.assertTrue(result)

    def test_video_download_with_wrong_url(self):
        tempfile_path = "../static/"
        video_file_name = "video_name"
        if not os.path.isdir(tempfile_path):
            os.mkdir(tempfile_path)

        VideoDownloader.download_video_from_url("WrongURL",
                                                f"{tempfile_path}{video_file_name}")
        result = os.path.exists(tempfile_path + "/" + video_file_name + ".mp4")
        self.assertFalse(result)

