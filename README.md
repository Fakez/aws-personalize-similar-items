# aws-personalize-similar-items
gets similar items from aws personalize using django rest framework

1. Add your AWS Personalize info to environment variables as ```AWS_PERSONALIZE_CAMPAIGN_ARN_SIMILAR_ITEMS```, ```AWS_PERSONALIZE_ACCESS_KEY``` and ```AWS_PERSONALIZE_SECRET_ACCESS_KEY```.

2. Implement files to your Django REST Framework API code.

3. Send your GET requests to the endpoint ```/api/getPersonalizeSimilarItems/<product_id>```.

4. Response will be in the JSON format like:
```
{
    'prodRefs': [list_of_similar_items_ids]
}
```


