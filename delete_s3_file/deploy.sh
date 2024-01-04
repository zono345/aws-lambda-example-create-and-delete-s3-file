#!/bin/bash

# Lambda関数の設定
FUNCTION_NAME="delete_s3_file"
ZIP_FILE="Lambda-Deployment.zip"
ROLE_ARN="arn:aws:iam::123499991234:role/lambda-s3-full-access"

# zipファイルの作成（既存のzipファイル、deploy.sh、response.txtを除外）
zip -r $ZIP_FILE . -x "*.zip" "*.sh" "response.txt"

# Lambda関数が存在するか確認
if aws lambda get-function --function-name $FUNCTION_NAME 2>&1 | grep -q 'ResourceNotFoundException'
then
    echo "Lambda関数が存在しません。新規作成します。"
    # Lambda関数を新規作成
    aws lambda create-function --function-name $FUNCTION_NAME \
                               --zip-file fileb://$ZIP_FILE \
                               --handler lambda_function.lambda_handler \
                               --runtime python3.8 \
                               --role $ROLE_ARN
else
    echo "Lambda関数が存在します。更新します。"
    # Lambda関数を更新
    aws lambda update-function-code --function-name $FUNCTION_NAME \
                                    --zip-file fileb://$ZIP_FILE
fi


### 補足説明 - デプロイ手順 ###
# (1)実行権限の付与
# chmod +x deploy.sh
# (2)デプロイ
# ./deploy.sh

### 補足説明 - 実行 ###
# (1)Lambda関数の実行
# aws lambda invoke --function-name delete_s3_file response.txt