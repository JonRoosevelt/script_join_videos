import sys
import os
import uuid
import subprocess
from pathlib import Path
import shutil


class JoinVideos:
    def __init__(self, path, extension='webm', output_name=uuid.uuid4()):
        self.base_folder = Path(path)
        self.temp_folder = self.base_folder.joinpath('temp')
        self.output_folder = self.base_folder.joinpath('output')
        self.output_name = self.base_folder.joinpath(
            'output', f'{output_name}.mp4')
        self.extension = extension

    def create_output_folder(self):
        os.mkdir(os.path.join(self.base_folder, 'output'))

    def create_temp_folder(self):
        os.mkdir(os.path.join(self.base_folder, 'temp'))

    def safe_spaces(self, _str):
        return str(_str).replace(' ', '\ ')

    def convert_videos(self):
        try:
            for r, d, f in os.walk(self.base_folder):
                f.sort()
                for video in f:
                    if f'.{self.extension}' in video:
                        _input = self.safe_spaces(
                            self.base_folder.joinpath(video))
                        output = self.safe_spaces(
                            self.temp_folder.joinpath(video.replace('webm', 'mp4')))
                        subprocess.run(
                            f'ffmpeg -i {_input} -vcodec copy {output}', shell=True, check=True)
        except FileNotFoundError as ex:
            print(ex)
            print(_input)

    def set_videos_list(self):
        videos = []
        try:
            with self.temp_folder.joinpath('input.txt').open(mode='a') as file:
                for r, d, f in os.walk(os.path.join(self.base_folder, 'temp')):
                    f.sort()
                    for video in f:
                        if '.mp4' in video:
                            file_path = self.safe_spaces(
                                self.temp_folder.joinpath(video))
                            videos.append(file_path)
                            file.write(f'file {file_path}\n')
                file.close()
        except FileNotFoundError as ex:
            print(ex)
            print(file_path)

    def get_command(self):
        _input = self.safe_spaces(self.temp_folder.joinpath('input.txt'))
        output = self.safe_spaces(self.output_name)
        log = self.safe_spaces(self.output_folder.joinpath('log.txt'))
        return f'ffmpeg -f concat -safe 0 -i {_input} -c copy {output} 2> {log}'

    def setUp(self):
        self.create_temp_folder()
        self.create_output_folder()
        self.convert_videos()
        self.set_videos_list()

    def run(self):
        self.setUp()
        command = self.get_command()
        subprocess.run(command, shell=True, check=True)
        shutil.rmtree(self.temp_folder)


if __name__ == '__main__':
    join_videos = JoinVideos(path=sys.argv[1]).run()
