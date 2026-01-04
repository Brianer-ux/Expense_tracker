# \# Expense Tracker API

# A RESTful backend API built with Django and Django REST Framework that allows users to track expenses, organize them into categories, and view spending analytics. This project was developed as a backend capstone project and demonstrates real-world API design, authentication, database relationships, filtering, and analytics.

# 

# \## Features

# \- User registration and token-based authentication  

# \- Create, read, update, and delete expenses (CRUD)  

# \- Expense categorization  

# \- Filter expenses by date range and category  

# \- Analytics endpoints:

# &nbsp; - Total expense summary

# &nbsp; - Category-wise expense breakdown  

# \- Secure, user-specific data access  

# \- RESTful API design with proper HTTP status codes  

# 

# \## Tech Stack

# \- Framework: Django  

# \- API Framework: Django REST Framework (DRF)  

# \- Authentication: Token Authentication  

# \- Database: SQLite (default Django database)  

# \- Language: Python 3  

# 

# \## Database \& Relationships

# \- \*\*User\*\*: Each user has many expenses and categories (one-to-many).  

# \- \*\*Category\*\*: Belongs to a user; an expense must have one category.  

# \- \*\*Expense\*\*: Belongs to a user and is linked to one category.  

# \- Relationships ensure all data is \*\*user-specific\*\*, preventing cross-user access.

# 

# \## Project Structure

# expense\_tracker/

# ├── expense\_tracker/        # Project settings and configuration

# │   ├── \_\_init\_\_.py

# │   ├── asgi.py

# │   ├── settings.py

# │   ├── urls.py

# │   └── wsgi.py

# ├── expenses/               # Core application

# │   ├── migrations/

# │   ├── \_\_init\_\_.py

# │   ├── admin.py

# │   ├── apps.py

# │   ├── models.py

# │   ├── serializers.py

# │   ├── views.py

# │   ├── urls.py

# │   └── tests.py

# ├── manage.py

# ├── db.sqlite3

# ├── requirements.txt

# └── README.md

# 

# \## Authentication

# This API uses token-based authentication.  

# Register a new user: POST /api/register/  

# Login and obtain token: POST /api/login/  

# Include the token in request headers: Authorization: Token your\_token\_here

# 

# \## API Endpoints

# 

# \### Expenses

# | Method | Endpoint | Description |

# |--------|---------|------------|

# | GET    | /api/expenses/ | List all user expenses |

# | POST   | /api/expenses/ | Create a new expense |

# | GET    | /api/expenses/<id>/ | Retrieve a specific expense |

# | PUT    | /api/expenses/<id>/ | Update an expense |

# | DELETE | /api/expenses/<id>/ | Delete an expense |

# 

# \### Filters

# Filter expenses by date range: GET /api/expenses/?start\_date=2025-01-01\&end\_date=2025-01-31  

# Filter expenses by category: GET /api/expenses/?category=Food  

# Filters can be combined: GET /api/expenses/?category=Food\&start\_date=2025-01-01\&end\_date=2025-01-31

# 

# \### Analytics

# | Method | Endpoint | Description |

# |--------|---------|------------|

# | GET    | /api/expenses/summary/ | Total spending summary |

# | GET    | /api/expenses/category-breakdown/ | Category-wise totals |

# 

# Sample Response for Total Summary:  

# GET /api/expenses/summary/  

# ```json

# {

# &nbsp; "total\_expenses": 3300,

# &nbsp; "total\_categories": 4

# }



# 



