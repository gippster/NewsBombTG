import requests

API_KEY = "2ceac2dc-86c8-4428-bed0-f59276f32d53"
headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": API_KEY
    }

#   63b409eb241a82001d51c782    Galina Ivanov       female
#   63b409f0241a82001d51c78e    Nadezhda Smirnoff   female
#   63b409ee241a82001d51c788    Pyotr Semenov       male


def ger_speakers():
    url = "https://api.genny.lovo.ai/api/v1/speakers"

    return requests.get(url, headers=headers).json()


def create_tts(text: str, speaker_id: str):
    url = "https://api.genny.lovo.ai/api/v1/tts"

    payload = {"speed": 1,
               "text": text,
               "speaker": speaker_id
               }

    return requests.post(url, json=payload, headers=headers).json()


def retrieve_tts(job_id: str):
    pass


def main():
   response = create_tts("Привет, дорогой", "63b409f0241a82001d51c78e")           #TTS requests via API for Free Users are blocked for security reasons.
                                                                                                #Please contact us at hello@lovo.ai if you wish to try out the API for free
   print(response)


if __name__ == '__main__':
    main()
