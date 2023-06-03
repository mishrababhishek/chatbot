# JITBot - College Enquiry Chatbot 🤖
JIT Bot is a chatbot application designed specifically for college enquiries. It provides information about various aspects of the college, such as courses, admissions, faculty, facilities, and more. This documentation provides an overview of the project structure, installation instructions, usage guidelines, testing information, contribution guidelines, and licensing details.

## Project Structure 📁

```bash
+---backend
|   +---app
|   |       app.py
|   |       greetings.py
|   |       spelling_fix.py
|   |
|   +---data
|   |       data.py
|   |       generate_data.py
|   |       intends.json
|   |       querys.json
|   |       raw_data.json
|   |       related.json
|   |       responses.json
|   |
|   +---models
|   |   |   interpreter.py
|   |   |
|   |   +---saved
|   |   |       default_lemmatize.json
|   |   |       default_stem.json
|   |   |       new_lemmatize.json
|   |   |       new_stem.json
|   |   |       test.json
|   |   |
|   |   +---sequence_to_vector
|   |   |       seq2vec.py
|   |   |       utils.py
|   |   |
|   |   +---vector_to_class
|   |           utils.py
|   |           vec2class.py
|   |
|   +---tests
|           interpreter_test.py
|
+---frontend
    +---public
    |       background.png
    |       favicon.ico
    |       index.html
    |       logo192.png
    |       logo512.png
    |       manifest.json
    |       robots.txt
    |
    +---src
        |   App.css
        |   App.jsx
        |   App.test.js
        |   index.css
        |   index.js
        |   logo.svg
        |   reportWebVitals.js
        |   setupTests.js
        |
        +---api
        |       chatApi.js
        |
        +---components
            +---chat
            |       chat.css
            |       chat.jsx
            |
            +---chatbox
            |       chatbox.css
            |       chatbox.jsx
            |
            +---info
                    info.css
                    info.jsx
```
## Description 😀
To install and set up the JIT Bot project locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/mishrababhishek/chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd chatbot
   ```
3. Set up the backend:  
Install the required Python dependencies: 
   ```bash
   python backend/requirements.py
   ```
4. Set up the Frontend:  
Install the required Node.js packages using yarn: 
   ```bash
   cd frontend
   yarn install
   ```
## Usage 🚀
To use the JIT Bot application, follow these steps:

1. Start the backend server:
   ```bash
   cd backend
   python main.py
   ```
   This will start the backend server.

2. Start the frontend development server:
   ```bash
   cd frontend
   yarn start
   ```
   This will start the frontend development server at http://localhost:3000, and the JIT Bot application can be accessed through this URL.

3. Interact with the JIT Bot by typing in your college-related queries and receiving responses in real-time.

## Contributing 🤝
Contributions to JIT Bot are welcome! If you would like to contribute, please follow these guidelines:

* Fork the repository and create a new branch for your feature or bug fix.
* Ensure that your code follows the project's coding style and conventions.
* Write clear commit messages and provide a detailed description of your changes.
* Open a pull request, and your contribution will be reviewed by the project maintainers.

## License ⚖️
The JIT Bot project is licensed under the MIT License. Please see the [LICENSE](https://github.com/mishrababhishek/chatbot/blob/master/LICENSE) file for more details.

Feel free to customize and expand upon this documentation according to your project's specific requirements and features.
