import requests

def azure_translate(text):
    API_KEY = "YOUR_API_KEY"
    API_REGION = "YOUR_API_REGION"

    # Azure Translator Text API endpoint
    endpoint = "https://api.cognitive.microsofttranslator.com"
    headers = {"Ocp-Apim-Subscription-Key": API_KEY, "Ocp-Apim-Subscription-Region": API_REGION, "Content-type": "application/json"}
    params = {"api-version": "3.0", "from": "en", "to": "es"} # English to Spanish, other options: https://docs.microsoft.com/en-us/azure/cognitive-services/translator/language-support
    api_url = endpoint + "/translate"
    body = [{"text": text}]
    response = requests.post(api_url, headers=headers, params=params, json=body)
    return response.json()[0]["translations"][0]["text"]