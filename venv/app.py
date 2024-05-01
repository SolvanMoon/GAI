from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY=""
openai.api_key=OPENAI_API_KEY


@app.route('/generate_story', methods=['POST'])
def generate_story():
    try:
        # Get data from POST request
        data = request.json

        # Use the OpenAI API to generate the story
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",  # or "text-davinci-002" based on the available engines at the time
            prompt=f"Title: {data['title']}\n"
                   f"Genre: {data['genre']}\n"
                   f"Characters: {', '.join(data['characters'])}\n"
                   f"Ending: {data['ending']}\n"
                   f"Write a story in {data['words']} words:",
        )

        # Extract the story from the API response
        story = response.choices[0].text.strip() if response.choices else "No story was generated."

        # Return the story as JSON
        return jsonify({'story': story})

    except Exception as e:
        # If an error occurs, print it and return a JSON error response
        print(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)