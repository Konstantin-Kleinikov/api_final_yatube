 API Final Yatube

This project is a REST API for the Yatube social network. It allows users 
to create posts, comment on posts, follow other users, and manage groups 
(communities).

## Features
- User authentication using JWT
- CRUD operations for posts, comments, follow and groups
- Follow/unfollow functionality
- Pagination and permissions

## Installation
1. Clone the repository:  
git clone https://github.com/Konstantin-Kleinikov/api_final_yatube


2. Navigate to the project directory:  
cd api_final_yatube


3. Create and activate a virtual environment:  
python -m venv venv  
source venv/bin/activate # On Windows: venv\Scripts\activate


4. Install dependencies:  
python3 -m pip install --upgrade pip  
pip install -r requirements.txt  


5. Populate initial data into database:  
Go to _postman_collection_ folder and run command `bash set_up_data.sh` 
in Bash Terminal.


6. Make migrations:  
python manage.py migrate  


7. Import predefined API requests into Postman:  
Go to Postman and import collection from file 
_postman_collection_\ _API_for_yatube.postman_collection.json_.

## Usage
Run the development server:  
python manage.py runserver  

Review the API documentation at http://127.0.0.1:8000/redoc/.

Access the API at `http://127.0.0.1:8000/api/v1/`.

### API-request examples
1. Create a Post with Group  
The POST request for authorized user to url http://127.0.0.1:8000/api/v1/posts/  
with body  
```json
{
    "text": "Post with group (Example)",
} 
```
should create a new post in database and respond with status **201 Created**. 


## Testing
Run tests using:  
pytest


