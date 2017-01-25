# -*- coding: utf-8 -*-
import json

def hello(event, context):
    body = [
 	u"us-east-1", 2012
    ]
    body = \
	u"us-east-1	米国東部（バージニア北部）" + "\r\n" + \
        u"us-east-2	米国東部 (オハイオ)" + "\r\n" + \
        u"us-west-1	米国西部（北カリフォルニア）" + "\r\n" + \
	u"us-west-2	米国西部（オレゴン）" + "\r\n" + \
        u"ca-central-1	カナダ (中部)" + "\r\n" + \
        u"eu-west-1	欧州（アイルランド）" + "\r\n" + \
        u"eu-central-1	欧州（フランクフルト）" + "\r\n" + \
        u"eu-west-2	欧州 (ロンドン)" + "\r\n" + \
        u"ap-northeast-1	アジアパシフィック（東京）" + "\r\n" + \
        u"ap-northeast-2	アジアパシフィック (ソウル)" + "\r\n" + \
        u"ap-southeast-1	アジアパシフィック（シンガポール）" + "\r\n" + \
        u"ap-southeast-2	アジアパシフィック（シドニー）" + "\r\n" + \
        u"ap-south-1	アジアパシフィック (ムンバイ)" + "\r\n" + \
        u"sa-east-1	南米 (サンパウロ)" + "\r\n"

    response = {
        "statusCode": 200,
        "body": body
    }

    return response

if __name__ == '__main__':
   result = hello(None, None)
   print(result)
