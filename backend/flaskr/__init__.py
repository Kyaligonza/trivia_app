import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random


from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  #cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE')
      return response

  QUESTIONS_PER_PAGE = 10

  def paginate_questions(request, response):
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    
    current_questions = response[start:end]

    return current_questions
  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def get_categories():
    headings = Category.query.order_by(Category.id).all()
    categoriesx = [item.format() for item in headings]
    categories = [item["type"] for item in categoriesx]
    
    return jsonify({
      'success':True,
      'categories':categories,
      'number_categories':len(Category.query.all())

    })

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def get_questions():
    questions = Question.query.all()
    response = []

    for question in questions:
      if question.category is None:
         questions_data = { 
        'answer': question.answer,
        'category': question.category,
        'difficulty':question.difficulty,
        'id': question.id,
        'question':question.question
      }
      else:
         questions_data = { 
        'answer': question.answer,
        'category': (question.category -1),
        'difficulty':question.difficulty,
        'id': question.id,
        'question':question.question
      }
      response.append(questions_data)

    current_questions = paginate_questions(request, response)

    headings = Category.query.order_by(Category.id).all()
    categoriesx = [item.format() for item in headings]
    categories = [item["type"] for item in categoriesx]
    

    if len(current_questions) == 0: 
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'categories': categories,
      'total_questions': len(Question.query.all())
    })


  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 
  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:

      item = Question.query.filter(Question.id == question_id).one_or_none()

      if item is None:
        abort(404)

      else:
        item.delete()

        return jsonify({
          'success':True,
          'item_deleted':question_id
        })
    except:
      abort(422)

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def create_question():

    body = request.get_json()
    try:
        new_question = body.get("question",None)
        new_answer = body.get("answer",None)
        new_category = body.get("category",None)
        new_difficulty = body.get("difficulty",None)
        search = body.get("searchTerm",None)

        if search:
          search_response = Question.query.filter(Question.question.ilike(f'%{search}%'))
          response = []

          for question in search_response:
            if question.category is None:
              questions_data = { 
              'answer': question.answer,
              'category': question.category,
              'difficulty':question.difficulty,
              'id': question.id,
              'question':question.question
            }
            else:
              questions_data = { 
              'answer': question.answer,
              'category': (question.category -1),
              'difficulty':question.difficulty,
              'id': question.id,
              'question':question.question
            }
            response.append(questions_data)
          
          possible_questions = paginate_questions(request,response)
          # add the categories
          headings = Category.query.order_by(Category.id).all()
          categoriesx = [item.format() for item in headings]
          categories = [item["type"] for item in categoriesx]
          
          return jsonify({
            'success':True,
            'questions':possible_questions,
            'categories':categories,
            'suggested_nb':len(possible_questions)
          })
        else:

          
          new_category = int(new_category) +1

          question = Question(question=new_question,answer=new_answer,category=new_category,difficulty=new_difficulty)

          question.insert()

          return jsonify({
            'success':True,
            'Total_questions': len(Question.query.all())
          })
    except:
      abort(422)

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def get_by_category(category_id):

    try:

      cat_questions = Question.query.filter(Question.category==(category_id+1)).all()
      response = []
      for question in cat_questions:
        questions_data = { 
                  'answer': question.answer,
                  'category': (question.category -1),
                  'difficulty':question.difficulty,
                  'id': question.id,
                  'question':question.question
                }
                
        response.append(questions_data)

      current_questions = paginate_questions(request, response)
      

      if len(current_questions) == 0:
        abort(404)
      
      else:

        return jsonify({
          'success': True,
          'questions':current_questions,
          'total_questions': len(Question.query.all())
        })
    except:
      abort(422)

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route( '/quizzes', methods=['POST']) 
  def get_next_question():

  
    body = request.get_json()
    previous_questions = body.get('previous_questions')
    quiz_category = body.get("quiz_category")
    
    try:

      question1 = Question.query.filter(Question.category==(int(quiz_category['id'])+1)).filter(Question.id.notin_(previous_questions)).all()
      question2 = [q.format() for q in question1]
      if len(question2) >0:

        question = random.choice(question2)
        previous_questions.append(question)

        return jsonify({
          'success': True,
          'question':question,
          'previous_questions':previous_questions
        })
      else:
        return jsonify({
          'success':True,
          'previous_questions':previous_questions
        })
    except:
      abort(400)

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(400)
  def bad_request(error):
        return jsonify({
            'success':False,
            'error': 400,
            'message':'Bad request'
        }),400

  @app.errorhandler(404)
  def not_found(error):
        return jsonify({
            'success':False,
            'error': 404,
            'message':'item not found'
        }),404

  @app.errorhandler(405)
  def method_not_allowed(error):
        return jsonify({
            'success':False,
            'error': 405,
            'message':'Method is not allowed for this endpoint'
        }),405

  @app.errorhandler(422)
  def unprocessable(error):
        return jsonify({
            'success':False,
            'error': 422,
            'message':'something amiss try again'
        }),422
  

  
  return app

    