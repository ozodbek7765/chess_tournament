# Chess Tournament Backend System

## Setup

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the dependencies
4. Run the migrations
5. Create a superuser
6. Run the development server

```bash
git clone <repository-url>
cd chess_tournament
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
