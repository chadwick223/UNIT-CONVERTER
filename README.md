

🧮 Unit Converter (Django Project)
https://roadmap.sh/projects/unit-converter

A simple Django web application that converts units (length, weight, height) using a single reusable Django form and pint for unit conversion.
This project does not use a database — the entire conversion happens through forms and backend logic.

🚀 Features

No database required

One single form reused across all pages

Validates units using pint

Supports:
✔ Length
✔ Weight
✔ Height

Uses clean Django GET/POST workflow

Each page displays the result on the same view


<img width="1025" height="766" alt="image" src="https://github.com/user-attachments/assets/32cfd659-d426-46fa-8699-bf9e928b65b2" />


📂 Project Structure


<img width="613" height="446" alt="image" src="https://github.com/user-attachments/assets/1246bb2a-e55c-4afe-989f-9c0d86133741" />


🧾 How It Works
1️⃣ User loads the page (GET request)

Browser sends a GET request

Django returns an empty (unbound) form

User sees blank input fields for value + units

This is where Django creates the form without any data.

2️⃣ User submits the form (POST request)

Browser sends a POST request with the user input

Django receives the form data

form.is_valid() checks:

value is a float

units are valid pint units

If valid:

pint performs the conversion

result is sent back to the same page

If invalid:

Django returns the same form with error messages

Preview images
<img width="1914" height="1079" alt="Screenshot 2025-12-05 225606" src="https://github.com/user-attachments/assets/2488faae-4af2-4a38-8e82-d5be67d1ae0c" />

