from ollama import Client


class Summarization:

    @staticmethod
    def summarization_using_mistral(transcription):
        # Replace with your desired prompt
        prompt = (
            f"Provide a concise summary of the minutes of this meeting transcription, including the following details: "
            f"MoM Title, MoM created date, Meeting organizer name, Attendees list, Topic of discussion/meeting, Agenda, "
            f"Notes, Tasks, and Additional Info. Ensure to include relevant points. "
            f"If an attendee is not found in the transcription, mark it as NA: {transcription}")
        try:
            # Replace with your desired prompt
            prompt = f"Summarize the following text: {transcription}"

        # Create a client instance
        client = Client()

        # Send the prompt to Mistral model
        response = client.generate(model="mistral:instruct", prompt=prompt)

        # Print the Mistral generated response
        return response['response']
