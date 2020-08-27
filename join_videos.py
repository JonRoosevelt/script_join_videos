import os
import shutil
import subprocess
import sys
import uuid
from pathlib import Path


class JoinVideos:
    def __init__(self, path, extension='webm', output_name=uuid.uuid4()):
        self.base_folder = Path(path)
        self.output_folder = self.base_folder.joinpath('output')
        self.output_name = self.base_folder.joinpath(
            'output', f'{output_name}.webm')
        self.extension = extension

    def safe_spaces(self, _str):
        return str(_str).replace(' ', '\ ')

    def get_videos_list(self):
        videos = []
        try:
            for r, d, f in os.walk(self.base_folder):
                f.sort()
                for video in f:
                    if '.webm' in video:
                        file_path = self.safe_spaces(
                            self.base_folder.joinpath(video))
                        videos.append(file_path)
            return videos
        except FileNotFoundError as ex:
            print(ex)
            print(file_path)

    def get_command(self, videos_list):
        output = self.safe_spaces(self.output_name)
        log = self.safe_spaces(self.output_folder.joinpath('log.txt'))
        return f'mkvmerge -o {output} {" + ".join(videos_list)}'

    def run(self):
        videos_list = self.get_videos_list()
        command = self.get_command(videos_list)
        subprocess.run(command, shell=True, check=True)


if __name__ == '__main__':
    JoinVideos(path=sys.argv[1]).run()
