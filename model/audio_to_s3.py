import os


def audio_to_s3(audio_file_number):
    os.system('aws s3 mv /tmp/test.mp3 s3://brodys-audio-files/test{}.mp3'.format(audio_file_number))
