from ollama import Client
import logging


class Summarization:

    @staticmethod
    def summarization_using_mistral(transcription):
        try:
            # Replace with your desired prompt
            prompt = f"Summarize the following text: {transcription}"

            # Create a client instance
            client = Client()

            # Send the prompt to Mistral model
            response = client.generate(model="mistral:instruct", prompt=prompt)

            # Print the Mistral generated response
            return response['response']

        except Exception as e:
            logging.error(f"\nAn error occurred during summarization using Mistral: {e}")
