<!DOCTYPE html><html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Flashcard Generator</title>
</head>
<body><h1>AI Flashcard Generator</h1>

<p>
    An AI-powered flashcard generator that creates question-and-answer
    flashcards based on a given topic, number of flashcards, and difficulty level.
</p>

<h2>Features</h2>
<ul>
    <li>Generate flashcards using AI</li>
    <li>Choose the topic and number of flashcards</li>
    <li>Select difficulty level</li>
    <li>Generate concise questions and answers</li>
    <li>Uses the Hugging Face Inference API</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li>Python 3.12.4</li>
    <li>Hugging Face Inference API</li>
    <li>Qwen/Qwen3-4B-Instruct-2507</li>
    <li>Hugging Face Hub</li>
    <li>Python-dotenv</li>
</ul>

<h2>How It Works</h2>

<p>
    The user enters a topic, number of flashcards, and difficulty level.
    The application sends this information to the Qwen model through the
    Hugging Face API and displays the generated flashcards.
</p>

<h3>Example</h3>

<pre>

Enter topic: Python Programming
Number of flashcards: 5
Difficulty: Beginner
</pre>

<h2>Setup</h2>

<p>Install the required packages:</p>

<pre>pip install huggingface_hub python-dotenv</pre>

<p>Create a <code>.env</code> file and add your Hugging Face API token:</p>

<pre>TOKEN=your_huggingface_token</pre>

<p>Run the application:</p>

<pre>python app.py</pre>

<h2>Security</h2>

<p>
    The API token is stored in <code>.env</code>. Make sure
    <code>.env</code> is included in <code>.gitignore</code> and is not
    uploaded to GitHub.
</p>

<h2>Future Improvements</h2>
<ul>
    <li>Add a web interface</li>
    <li>Save and export flashcards</li>
    <li>Add quiz functionality</li>
    <li>Add progress tracking</li>
</ul>

<h2>Author</h2>
<p>Your Name</p>

</body>
</html>
