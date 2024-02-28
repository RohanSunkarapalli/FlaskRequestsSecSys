# FlaskRequestsSecSys

Designing and using web services using Flask framework, and REST APIs.

Instructions to execute the program -

app.py -

Open a terminal or command prompt and navigate to the project folder. Create a virtual environment by running the command python -m venv venv. Activate the virtual environment by running the command source venv/bin/activate on Mac/Linux or .\venv\Scripts\activate on Windows. Install the required packages by running the command pip install -r requirements.txt. Start the Flask development server by running the command - python app.py. The server should now be running on http://127.0.0.1:5000/

client.py -

To test on the client side, open another terminal and go to the directory where client file is located. Before running the client program, install requests library by running the command - pip install requests Now, run the python script by using the following command -

python client.py
Usage -

To test the API endpoints, you can use a web browser or a tool like Postman.

Greeting endpoint -

This endpoint returns a greeting message with the name provided as a query parameter. To test it, open a web browser or Postman and navigate to http://127.0.0.1:5000/api/greeting?name=Rohan Sunkarapalli (replace John with your name or any other name you want). You should see a JSON response with a greeting message.

Sum endpoint -

This endpoint returns the sum of two numbers provided as query parameters. To test it, open a web browser or Postman and navigate to http://127.0.0.1:5000/api/sum?a=2&b=3 (replace 2 and 3 with any two integers you want). You should see a JSON response with the sum of the two numbers.

Countries endpoint -

This endpoint returns a list of countries provided as a list. To test it, open a web browser or Postman and navigate to http://127.0.0.1:5000/api/countries. You should see a JSON response with List of the countries.
