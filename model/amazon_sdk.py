from __future__ import print_function
import time
import boto3


def run_transcribe(audio_file_number):
    transcribe = boto3.client('transcribe')
    job_name = "test{}".format(audio_file_number)
    job_uri = "s3://brodys-audio-files/{}.mp3".format(job_name)
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',
        LanguageCode='en-US',
        Settings={'ShowAlternatives': True,
                  'MaxAlternatives': 10}
    )
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Not ready yet...")
        time.sleep(5)
    return status['TranscriptionJob']['Transcript']['TranscriptFileUri']
