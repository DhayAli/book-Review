Book Review API 
A simple Django REST Framework project for for a book review system,Supports user registration, login, book management (admin-only), and review submission (authenticated Users)

How to Run the Project Locally :
1 Clone the repository:
git clone <your-repo-url>
cd bookreview
2 Create and activate a virtual environment
3 Install dependencies:
pip install -r requirements.txt
4 Apply migrations:
python manage.py migrate
5 Create superuser (for admin access):
python manage.py createsuperuser
6 Run the development server: 
python manage.py runserver
