from ollama import Client


class Summarization:

    @staticmethod
    def summarization_using_mistral(transcription):
        # Replace with your desired prompt
        prompt = f"Summarize the following text: {transcription}"

        # Create a client instance
        client = Client()

        # Send the prompt to Mistral model
        response = client.generate(model="mistral:instruct", prompt=prompt)

        # Print the Mistral generated response
        return response['response']
