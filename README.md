# UKRPoshta

This is a web application built with Django that allows you to Route, Village  and Directions

# Check it out!

[UKRPoshta](https://ukrposhta.onrender.com/)

## Characteristic
- Create, Update, Detail and Delete
- Add any Village to any Directions;
- Information about Directions;

## Local deployment instruction

To deploy the UKRPoshta project locally, please follow the steps below:
1. Clone the repository to your local machine: git clone https://github.com/Bohdan11Dii/UKRPoshta
2. Create a virtual environment: python -m venv env
3. Activate the virtual environment:
    - For Windows: .\env\Scripts\activate
    - For macOS and Linux: source env/bin/activate
4. Install the project dependencies: pip install -r requirements.txt
5. Apply database migrations: python manage.py migrate
6. Run the development server: python manage.py runserver
7. Open your web browser and access the Task Manager application at http://localhost:8000/.

### Environment Variables
In the root directory, you need to create an .env file and install all the necessary data that is written in the file .env_sample, namely
> SECRET_KEY: Your Django secret key
>
> DATABASE_URL: Your database url