

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

Django form handling process:-

Django's form handling uses all of the same techniques  performs any actions required including reading data from the models, then generates and returns an HTML page (from a template, into which we pass a context containing the data to be displayed). What makes things more complicated is that the server also needs to be able to process data provided by the user, and redisplay the page if there are any errors.

A process flowchart of how Django handles form requests is shown below, starting with a request for a page containing a form (shown in green).

<img width="1025" height="766" alt="image" src="https://github.com/user-attachments/assets/32cfd659-d426-46fa-8699-bf9e928b65b2" />

Based on the diagram above, the main things that Django's form handling does are:

1) Display the default form the first time it is requested by the user.

2)  The form may contain blank fields if you're creating a new record, or it may be pre-populated with initial values (for example, if you are changing a record, or have useful default initial values).
    The form is referred to as unbound at this point, because it isn't associated with any user-entered data (though it may have initial values). 
    Receive data from a submit request and bind it to the form.

3)  Binding data to the form means that the user-entered data and any errors are available when we need to redisplay the form.
    Clean and validate the data.

4)  Cleaning the data performs sanitization of the input fields, such as removing invalid characters that might be used to send malicious content to the server, and converts them into consistent Python types.
    Validation checks that the values are appropriate for the field (for example, that they are in the right date range, aren't too short or too long, etc.)
    If any data is invalid, re-display the form, this time with any user populated values and error messages for the problem fields.

5)  If all data is valid, perform required actions (such as save the data, send an email, return the result of a search, upload a file, and so on).

Form:

The Form class is the heart of Django's form handling system. It specifies the fields in the form, their layout, display widgets, labels, initial values, valid values, and (once validated) the error messages associated with invalid fields. The class also provides methods for rendering itself in templates using predefined formats (tables, lists, etc.) or for getting the value of any element (enabling fine-grained manual rendering).

Declaring a Form:

The declaration syntax for a Form is very similar to that for declaring a Model, and shares the same field types (and some similar parameters). This makes sense because in both cases we need to ensure that each field handles the right types of data, is constrained to valid data, and has a description for display/documentation.

Forms.py:

    assign important values for input like Unit_to_convert_to,Unit_to_convert_from,values




    def clean_Unit_to_convert_from(self):
        given=self.cleaned_data['Unit_to_convert_from']

        try:
            ureg.parse_units(given)
        except Exception:
            raise ValidationError("Invalid units")
        return given
    
    def clean_Unit_to_convert_to(self):
        given=self.cleaned_data['Unit_to_convert_to']
        try:
            ureg.parse_units(given)
        except Exception:
            raise ValidationError("Invalid units")
        return given






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

