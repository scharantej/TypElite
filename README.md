## Flask Application Design

### HTML Files
- **index.html:** The main page of the application. It presents the pretyping test, containing an input box and buttons to measure typing speed and accuracy.
- **results.html:** Displays the results of the pretyping test, showing the participant's typing speed and accuracy both before and after using the application.

### Routes
- **`/` (GET):** Renders the `index.html` page, displaying the pretyping test.
- **`/start-test` (POST):** Initiates the pretyping test. Records the participant's initial typing speed and accuracy.
- **`/end-test` (POST):** Ends the pretyping test. Records the participant's final typing speed and accuracy.
- **`/results` (GET):** Renders the `results.html` page, displaying the participant's typing speed and accuracy both before and after using the application.