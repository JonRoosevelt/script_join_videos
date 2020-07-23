import sys, os
import uuid
import subprocess
from exceptions import *


class JoinVideos:
    def __init__(self, path, extension='webm', output_name=f'{uuid.uuid4()}.webm'):
        self.path = path
        self.extension = f'.{extension}'
        self.output_name = output_name

    def get_videos(self):
        try:
            folder = os.path.basename(os.path.normpath(self.path))
            videos = []
            for r, d, f in os.walk(self.path):
                for video in f:
                    if self.extension in video:
                        videos.append(os.path.join(self.path, video))
            return videos[::-1]
        except OSError as err:
            if error.errno == errno.ENOENT:  # File not found
                raise OSFileNotFoundException
            raise err

    def join_videos(self, videos):
        command_prefix = f'mkvmerge -o {self.path}/{self.output_name} -w '
        concat_video_string = ' + '.join(videos)
        return f'{command_prefix}{concat_video_string}'

    def run(self):
        videos = self.get_videos()
        joined_videos = self.join_videos(videos)
        print(joined_videos)
        return subprocess.run(joined_videos, shell=True, check=True)

if __name__ == '__main__':
    join_videos = JoinVideos(path=sys.argv[1]).run()
