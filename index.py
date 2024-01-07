<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text-to-Speech</title>
</head>
<body>
    <h1>Text-to-Speech</h1>
    <form action="/generate" method="post">
        <label for="text">Enter text:</label>
        <textarea id="text" name="text" rows="4" cols="50"></textarea>
        <br>
        <button type="submit">Generate Audio</button>
    </form>
    {% if audio_generated %}
        <br>
        <a href="/download" download="output.mp3">Download Audio</a>
    {% endif %}
</body>
</html>
