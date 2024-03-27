# Python Engineering (Task 1)
Client Brief:
You are tasked with developing a QR code generator application. The application should allow users to generate QR codes for different types of data such as URLs, text, and contact information. The application should be built using Python, Flask for API development, Pydantic for data validation, and PostgreSQL for storing generated QR codes.

# Task Outline:
### 1. Setup:
Set up a virtual environment for your project.
Install Flask, Pydantic, and PostgreSQL dependencies.
Create a PostgreSQL database for storing QR code data.

### 3. QR Code Generation:
Implement endpoints for generating QR codes.
Accept input data from users such as URLs, text, or contact information.
Use Pydantic for validating input data.
Generate QR codes using a library like qrcode.

### 5. Save and Retrieve QR Codes:
Implement endpoints for saving and retrieving generated QR codes.
Store QR code images or data in the PostgreSQL database.
Ensure proper validation and error handling for saving and retrieving QR codes.

### 7. Data Types:
Support generating QR codes for different data types such as URLs, text, and contact information.
Implement validation to ensure the input data matches the specified data type.

### 9. QR Code Customisation:
Allow users to customise the appearance of generated QR codes (e.g., size, color).
Implement endpoints for specifying customisation options.

### 11. Testing:
Write unit tests to ensure the functionality of each endpoint.
Test edge cases such as invalid input data or unsupported data types.
Use testing frameworks like pytest for efficient testing.

### 12. Documentation:
Document your API endpoints using tools like Swagger or Flask-RESTful.
Provide clear instructions on how to use the API endpoints.

### 13. Deployment:
Deploy your application on Linode
Ensure proper security measures are in place, such as HTTPS encryption and secure database connections.

### 14. Bonus (Optional):
Add support for bulk QR code generation.
Deliverables:
Python code for the Flask API implementation.
SQL scripts for setting up the database schema.
Unit tests for the endpoint.
Documentation including API endpoints, data models, and usage instructions.
Deployed application accessible via a public URL (optional for bonus points).

## Evaluation Criteria:
Completion of each task according to the outlined requirements.
Code quality, including readability, modularity, and adherence to best practices.
Proper error handling and validation of user input.
Documentation clarity and completeness.
