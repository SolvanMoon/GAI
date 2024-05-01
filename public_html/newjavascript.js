function AddCharacters(){
    var input = document.createElement('input');
    input.type = 'text';
    input.name = 'characters';
    input.required = true;
    document.getElementById('characters-section').appendChild(input);
}

function DeleteCharacters(){
    var section = document.getElementById('characters-section');
    if (section.children.length > 4) {  // Assuming 4 is the number of initial children (label + 2 buttons + 1 input)
        section.removeChild(section.lastChild);
}
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('story-input-form');
    form.addEventListener('submit', function(e) {
        e.preventDefault();  // Prevent the default form submission

        // Gather form data
        const formData = {
            title: document.getElementById('InpTitle').value,
            genre: document.getElementById('InpGenre').value,
            characters: Array.from(document.getElementsByName('characters')).map(input => input.value),
            ending: document.getElementById('InpEnding').value,
            words: document.getElementById('InpWords').value
        };

        // Send the data using fetch to your server endpoint
        fetch('http://127.0.0.1:5000/generate_story', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            // Display the generated story
            document.getElementById('geratedSt').innerText = data.story;
            console.log(data.story);
        })
        .catch(error => console.error('Error:', error));
    });
});