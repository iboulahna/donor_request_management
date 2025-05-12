### **1. Speech-to-Text Integration**

import boto3

def transcribe_audio(audio_file_path):
    transcribe_client = boto3.client('transcribe', region_name='us-east-1')

    job_name = "transcription-job"
    job_uri = f"s3://your-bucket-name/{audio_file_path}"

    # Start transcription job
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',
        LanguageCode='en-US',
        OutputBucketName='your-output-bucket'
    )

    # Wait and fetch transcription result
    result = transcribe_client.get_transcription_job(
        TranscriptionJobName=job_name
    )
    return result['TranscriptionJob']['Transcript']['TranscriptFileUri']
