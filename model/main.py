from audio_to_s3 import audio_to_s3
from audio_generator import audio_generator
from alter_pitch import pitch_increase
from amazon_sdk import run_transcribe
from audio_file_number import get_audio_file_number, save_audio_file_number

import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("phrase", help="enter a phrase that you want to alter and transcribe")
    args = parser.parse_args()
    audio_file_num = get_audio_file_number()
    if audio_file_num is None:
        audio_file_number = input("What is the current number of tests you've run? (e.g. '0') ")
        try:
            audio_file_num = int(audio_file_number)
        except TypeError as err:
            print('Invalid input')
            exit(1)
    audio_generator(args.phrase)
    pitch_increase(input_file='/tmp/test.mp3', output_file='/tmp/test.mp3')
    audio_to_s3(audio_file_num)
    aws_url = run_transcribe(audio_file_num)
    filename = "/tmp/transcribe_output{}.json".format(audio_file_num)
    print(aws_url)
    os.system('wget -O {} "{}"'.format(filename, aws_url))
    print('\nOutput has been transcribed and downloaded to {}'.format(filename))
    save_audio_file_number(audio_file_num + 1)
