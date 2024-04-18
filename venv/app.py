from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

@app.route('/generate_story', methods=['POST'])

def generate_story():
    data = request.json
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Title: {data['title']}\nGenre: {data['genre']}\nCharacters: {', '.join(data['characters'])}\nEnding: {data['ending']}\nWords: {data['words']}\nWrite a story:",
        max_tokens=int(data['words']),
        api_key=os.getenv('OPENAI_API_KEY')  # Use the API key from environment
    )
    return jsonify({'story': response.choices[0].text.strip()})