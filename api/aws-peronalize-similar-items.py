from rest_framework.response import Response
import boto3
import environ

class CredentialsHandler:
    def __init__(self):
        self.env = environ.Env()
        self.env.read_env()
    
    def getEnv_str(self, value):
        return self.env(value)


class AmazonPersonalizeSimilarItems(APIView):

    def get(self, request, *args, **kwargs):
            ch = CredentialsHandler()

            campaignArn = ch.getEnv_str('AWS_PERSONALIZE_CAMPAIGN_ARN_SIMILAR_ITEMS')
            aws_access_key_id=ch.getEnv_str('AWS_PERSONALIZE_ACCESS_KEY')
            aws_secret_access_key=ch.getEnv_str('AWS_PERSONALIZE_SECRET_ACCESS_KEY')


            personalize_rt = boto3.client('personalize-runtime', region_name='us-east-2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
            
            prod_ref = kwargs['prod_ref'].upper()
            response = personalize_rt.get_recommendations(campaignArn=campaignArn, itemId=prod_ref)

            items_response = response['itemList']

            similar_items_ids = []
            for item in items_response:
                for value in item.values():
                    similar_items_ids.append(value)

            data = {
                'prodRefs': similar_items_ids
            }

            return Response(data)