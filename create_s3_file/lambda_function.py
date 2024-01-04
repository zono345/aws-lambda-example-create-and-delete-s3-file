import boto3
import json
import logging

# ロガーの設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # AWS S3クライアント
    s3_client = boto3.client('s3')

    # S3バケット名、ファイルパス、ファイルに書き込む内容
    bucket_name = 'test-example-20240104'
    file_path = 'parent/child/test_sample.txt'
    content = 'これはテストサンプルです'

    # ファイルを作成してアップロード
    try:
        # 指定されたS3パスに内容を書き込む
        s3_client.put_object(Bucket=bucket_name, Key=file_path, Body=content)
        message = f"ファイル '{file_path}' がバケット '{bucket_name}' に正常に作成されました。"
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