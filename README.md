# 概要
- AWS Lambdaで動くPythonのサンプルコードとデプロイ用のスクリプトです。
- create_s3_file
    - S3にファイルを作成するサンプルコードです。
- delete_s3_file
    - S3のファイルを削除するサンプルコードです。

# Lambdaへ付与するIAMロールについて
- `lambda-s3-full-access` という名前のIAMロールを事前に作成してください。
- `lambda-s3-full-access` のポリシーには、以下のポリシーを付与してください。
  - AmazonS3FullAccess
  - AWSLambdaBasicExecutionRole