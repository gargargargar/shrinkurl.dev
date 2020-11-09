# shrinkurl
shrinkurl is a url shortening service created using Flask and PostgreSQL. This app is running live at `https://shrinkurl-demo.herokuapp.com/`.

# Setup

1. Please clone this repository and install the requirements using `pip install -r requirements.txt`. (Using a virtual environment is recommended.)
2. Once the repository is cloned, please create a local PostgreSQL database and include the url to the database as the environment variable `DATABASE_URL`.
3. Run `db.py` to create a table in the specified database from step 2.
4. Finally, run `app.py` to launch the application.

# Future plans
- Use SQLAlchemy to handle SQL queries instead of using plain text SQL queries.
- Create more sophisticated HTML pages.
- Deploy the webapp on a custom domain.
