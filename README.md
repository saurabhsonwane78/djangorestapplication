# DJango Rest Application

1) To run the project
   use Pip install -r requirements.txt command

2) Api structure
   a) create a user - http://127.0.0.1:8000/signup
                   request type - post
                   parameters - username,password,email

   b) login a user - http://127.0.0.1:8000/login
                   request type - post
                   parameters - username,password
                   In Response we will get Token

   c) Get all posts - http://127.0.0.1:8000/api/posts/
                   request type - GET
                    parameters - Token

   d) Creates a new post - http://127.0.0.1:8000/api/posts/
                   request type - POST
                   parameters - Token, tittle,body,author

    e) Get single posts - http://127.0.0.1:8000/api/posts/<id>
                   request type - GET
                    parameters - Token

   
    f) Update single posts - http://127.0.0.1:8000/api/posts/<id>
                   request type - PUT
                    parameters - Token, tittle,body,author

    g) Deletes a single post - http://127.0.0.1:8000/api/posts/<id>
                   request type - DELETE
                    parameters - Token

   
