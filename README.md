# Django News API

## Overview
A Django-based backend that serves news articles, featuring a RESTful API for CRUD operations,  and advanced search functionalities.

## Features
- **RESTful API**: Offers endpoints for fetching news articles.
- **Search**: Allows searching for articles by keywords.
- **Filtering**: Supports filtering articles by source, category, etc.

## Getting Started

### Prerequisites

- Python 3.x
- pip
- Virtualenv (optional)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/dekkicheamine27/Django_News_API.git
cd Django_News_API
```

2. **Set up a virtual environment (Optional)**
```bash
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Configuring the PostgreSQL Database

1. Install PostgreSQL
Ensure PostgreSQL is installed and running on your system. Create a new database and user for this project.

2. **Install psycopg2**
```
pip install psycopg2
```

4. **Modify settings.py**
Open news_dashboard/settings.py and find the DATABASES setting. Replace the default configuration with your PostgreSQL database configuration:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
3. **Apply Migrations**
```
python manage.py migrate
```

5. **Run the Server**
```
python manage.py runserver
```

After starting the server, the API will be available at:
```
http://localhost:8000/
```

### Periodically fetch articles and store them
1. Open news_dashboard/settings.py and find NEWSAPI_KEY . Replace the default value by your newsapi.org API KEY:
```
NEWSAPI_KEY = '<your news api key>'
```
   
2.run this task to fetch and store articles every 1 hour:
```
python3 manage.py periodic_fetch_news
```



### Setting up the PostgreSQL Database

Before running the server, ensure you have PostgreSQL installed and running. Create a database for the project and update the `DATABASES` configuration in `settings.py` with your database credentials.

Refer to the PostgreSQL documentation for detailed instructions on creating a database and managing users.




   
