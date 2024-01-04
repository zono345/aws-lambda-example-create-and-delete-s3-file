import boto3
import json
import logging

# ロガーの設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # AWS S3クライアントの初期化
    s3_client = boto3.client('s3')

    # バケット名とファイルパス
    bucket_name = 'test-example-20240104'
    file_path = 'parent/child/test_sample.txt'

    # ファイルの削除
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=file_path)
        message = f"ファイル '{file_path}' がバケット '{bucket_name}' から削除されました。"
        logger.info(message)
        return {
            'statusCode': 200,
            'body': json.dumps(message)
        }
    except Exception as e:
        error_message = f"エラー発生: {str(e)}"
        logger.error(error_message)
        return {
            'statusCode': 500,
            'body': json.dumps(error_message)
        }
