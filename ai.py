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
        '''
        This function generates a movie recommendation based on the user's input using the OpenAI API.
        Args:
        input (str): The user input .
        Returns:
            str: A movie recommendation with its release date.
        '''
        try:        
            completion=self.client.chat.completions.create(

                model = self.model,
            messages = [
            {"role": "system",
            "content": "You are a recommendation assistant that only provides suggestions for movies not TV shows. No matter what the user asks, your answer should always be a recommendation for a movie and release date "},
            {"role": "user", "content": input}
            ]

            )

            return completion.choices[0].message.content
        except Exception as e:
            print(e)
    def recomdation_tvshow(self,input):
        '''
        This function generates a tvshow recommendation based on the user's input using the OpenAI API.
        Args:
        input (str): The user input.
        Returns:
            str: tvshow recommendation with its release date.
        '''
        try:        
            completion=self.client.chat.completions.create(

                model = self.model,
            messages = [
            {"role": "system",
            "content": "You are a recommendation assistant that only provides suggestions for tvshow not movie. No matter what the user asks, your answer should always be a recommendation for a tvshow and release date."},
            {"role": "user", "content": input}
            ]

            )

            return completion.choices[0].message.content
        except Exception as e:
            print(e)

        

        