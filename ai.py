from openai import OpenAI
import os
from dotenv import load_dotenv
class Ai:
    def __init__(self):
        load_dotenv()
        self.model="gpt-4o-mini"
        self.client=OpenAI(api_key=os.getenv('api_key_ai'))
    def configure(self):
        load_dotenv()

    def recomdation_movie(self,input):
        try:        
            completion=self.client.chat.completions.create(

                model = self.model,
            messages = [
            {"role": "system",
            "content": "You are a recommendation assistant that only provides suggestions for movies not TV shows. No matter what the user asks, your answer should always be a recommendation for a movie "},
            {"role": "user", "content": input}
            ]

            )

            return completion.choices[0].message.content
        except Exception as e:
            print(e)
    def recomdation_tvshow(self,input):
        try:        
            completion=self.client.chat.completions.create(

                model = self.model,
            messages = [
            {"role": "system",
            "content": "You are a recommendation assistant that only provides suggestions for tvshow not movie. No matter what the user asks, your answer should always be a recommendation for a tvshow."},
            {"role": "user", "content": input}
            ]

            )

            return completion.choices[0].message.content
        except Exception as e:
            print(e)

        

        