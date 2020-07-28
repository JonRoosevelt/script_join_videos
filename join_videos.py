import sys
import os
import uuid
import subprocess
from pathlib import Path


class JoinVideos:
    def __init__(self, path, extension='webm', output_name=uuid.uuid4()):
        self.path = path
        self.extension = extension
        self.output_name = Path(f'{self.path}/{output_name}.{self.extension}')

    def safe_spaces(self, _string):
        _string = str(_string)
        return _string.replace(' ', '\\ ')

    def get_videos_list(self):
        videos = []
        try:
            with open(Path(f'{self.path}/input.txt').as_posix(), 'a') as file:
                for r, d, f in os.walk(self.path):
                    f.sort()
                    for video in f:
                        if f'.{self.extension}' in video:
                            file_path = self.safe_spaces(
                                os.path.join(self.path, video))
                            videos.append(file_path)
                            file.write(f'file {file_path}\n')
                file.close()
        except FileNotFoundError as ex:
            print(ex)
            print(file_path)

    def get_command(self):
        file_path = self.safe_spaces(self.path)
        output_name = self.safe_spaces(self.output_name)
        return f'ffmpeg -f concat -safe 0 -i {file_path}/input.txt -c copy {output_name} 2> {file_path}/log.txt'

    def run(self):
        self.get_videos_list()
        command = self.get_command()
        subprocess.run(command, shell=True, check=True)
        os.remove(Path(f'{self.path}/input.txt').as_posix())


if __name__ == '__main__':
    join_videos = JoinVideos(path=sys.argv[1]).run()
