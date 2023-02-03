import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator.set_service_url(url)
translator.set_disable_ssl_verification(True)

def english_to_french(englishText):
    try:
        json_french_text = translator.translate(text=englishText, model_id='en-fr').get_result()
        translations = json_french_text['translations'][0]
        french_text = translations['translation']
    except:
        french_text = None
    return french_text

def french_to_english(frenchText):
    try:
        json_english_text = translator.translate(text=frenchText, model_id='fr-en').get_result()
        translations = json_english_text['translations'][0]
        english_text = translations['translation']
    except:
        english_text = None
    return english_text
