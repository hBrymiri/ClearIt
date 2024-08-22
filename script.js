// Define the word you want to look up
const word = 'code';

// Construct the API URL with the specified word
const apiUrl = `https://api.api-ninjas.com/v1/dictionary?word=${word}`;

// Define your API key
const apiKey = 'YOUR_API_KEY';

// Make a GET request to the API with the necessary API key
fetch(apiUrl, {
    method: 'GET',
    headers: {
        'X-Api-Key': apiKey
    }
})
.then(response => {
    if (response.ok) {
        // Parse the JSON response
        return response.json();
    } else {
        throw new Error('Network response was not ok');
    }
})
.then(data => {
    // Print the parsed JSON data
    console.log(data);
})
.catch(error => {
    // Print an error message if the request failed
    console.error('There was a problem with the fetch operation:', error);
});
