# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

GET '/questions'
- Fetches a dictionary of questions in which the keys are the categories,questions,success and total_questions; and the value is the corresponding list for categories and questions, string and int for success and total_questions respectively:
- Request Arguments: None
- Returns: An object with four keys, categories,success, total_questions and questions which contains list objects of key:value pairs represented below.
 
{
  "categories": [
    "Science", 
    "Art", 
    "Geography", 
    "History", 
    "Entertainment", 
    "Sports"
  ], 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 3, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      ......
    },
    {
      "answer": "Escher", 
      "category": 1, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 35
}

GET '/categories/<int:category_id>/questions'
- Fetches a dictionary of questions based on categories.
- Request Arguments: category_id
- Returns: An object with three keys,success, total_questions and questions which contains a list of key:value pairs represented below.
{
  "questions": [
    {
      "answer": "Escher", 
      "category": 1, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 1, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 1, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 1, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ], 
  "success": true, 
  "total_questions": 36
}

DELETE '/questions/<int:question_id>'
- Deletes a question using a question id.
- Request Arguments: question id
- Returns: An object with two keys, success and id of the question deleted, that contains an object of key:value pairs as follows. 

{
    "success":True,
    "item_deleted":24
}

POST '/questions'
C:\Users\hp>curl -X POST -H "Content-Type:application/json" -d "{  \"question\" : \"who is Frodo\",  \"answer\" : \"Baggins of course in Lord of the rings\",\"category\":4 }" http://localhost:5000/questions

- Creates a new question, which requires the question and answer text, 
  category, and difficulty score.
- Request Arguments: None
- Returns: An object with a two keys,success and total_questions that contains objects of key:value pairs represented below.

{
  "Total_questions": 36,
  "success": true
}

POST '/questions'
C:\Users\hp>curl -X POST -H "Content-Type:application/json" -d "{  \"searchTerm\":\"city\" }" http://localhost:5000/questions

- Retrieves question(s) based on a serach term, requires a string searchTerm to be provided.
- Request Arguments: None
- Returns: An object with four keys,success, categories, suggested_nb of questions and questions which contains a list of key:value pairs represented below.
{
  "categories": [
    "Science",
    "Art",
    "Geography",
    "History",
    "Entertainment",
    "Sports"
  ],
  "questions": [
    {
      "answer": "Agra",
      "category": 2,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Vancouver",
      "category": 2,
      "difficulty": 2,
      "id": 24,
      "question": "greatest city in the world"
    },
    {
      "answer": "rome",
      "category": 0,
      "difficulty": 4,
      "id": 27,
      "question": "Capital city of Italy?"
    }
  ],
  "success": true,
  "suggested_nb": 3
}

POST '/quizzes'
C:\Users\hp>curl -X POST -H "Content-Type:application/json" -d "{\"quiz_category\":"{\"id\":1,\"type\":\"Art\"}", \"previous_questions\":[]}" http://localhost:5000/quizzes

- Retrieves randomn question by category to play the quiz, requires quiz_category id and the list of previous_questions to be provided.
- Request Arguments: quiz_category id and a list of previous_questions.
- Returns: An object with three keys, success, question and previous_questions which contains a list of key:value pairs represented below.
{
  "previous_questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ],
  "question": {
    "answer": "Escher",
    "category": 2,
    "difficulty": 1,
    "id": 16,
    "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
  },
  "success": true
}
```
Error handling
Error messages will appear in the following format:
{
    "success":False,
    "error":404,
    "message":item not found
}
The API captures four errors types when the requests fail:
    .400: Bad request
    .404: Item not found
    .405: Method not allowed for this end point
    .422: Something amiss try again


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```