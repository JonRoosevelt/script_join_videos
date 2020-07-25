import sys
import os
import uuid
import subprocess
from pathlib import Path
import ffmpeg


class JoinVideos:
    def __init__(self, path, extension='webm', output_name=f'{uuid.uuid4()}.webm'):
        self.path = path
        self.extension = f'.{extension}'
        self.output_name = Path(f'{self.path}/{output_name}')

    def safe_spaces(self, _string):
        _string = str(_string)
        return _string.replace(' ', '\\ ')

    def get_videos(self):
        videos = []
        try:
            for r, d, f in os.walk(self.path):
                for video in f:
                    if self.extension in video:
                        file_path = self.safe_spaces(
                            os.path.join(self.path, video))
                        import pdb
                        pdb.set_trace()
                        videos.append(open(Path(file_path)))
        except FileNotFoundError as ex:
            print(ex)
            print(file_path)
        videos.sort()
        return videos

    def join_videos(self, videos):
        import pdb
        pdb.set_trace()
        return ffmpeg.concat(videos).node
    # def get_videos(self):
    #     videos = []
    #     try:
    #         with open('input.txt', 'a') as file:
    #             for r, d, f in os.walk(self.path):
    #                 for video in f:
    #                     if self.extension in video:
    #                         file_path = self.safe_spaces(
    #                             os.path.join(self.path, video))
    #                         videos.append(file_path)
    #                         file.write(f'file {file_path}\n')
    #             file.close()
    #     except FileNotFoundError as ex:
    #         print(ex)
    #         print(file_path)
    #     videos.sort()
    #     return videos

    # def join_videos(self, videos):
    #     output = self.safe_spaces(self.output_name)
    #     return f'ffmpeg -f concat -safe 0 -i input.txt -c copy {output}'

    def write_videofile(self, joined_videos):
        output = self.safe_spaces(self.output_name)
        ffmpeg.output(join_videos, output)

    def clean_input(self):
        os.remove('input.txt')

    def run(self):
        videos = self.get_videos()
        joined_videos = self.join_videos(videos)
        self.write_videofile(joined_videos).run()


if __name__ == '__main__':
    join_videos = JoinVideos(path=sys.argv[1]).run()
