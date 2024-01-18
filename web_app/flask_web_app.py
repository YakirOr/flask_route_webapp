from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Postgres parameters
db_params = {
    'host': os.environ.get('DATABASE_HOST'),
    'database': os.environ.get('POSTGRES_DATABASE'),
    'user': os.environ.get('POSTGRES_USERNAME'),
    'password': os.environ.get('POSTGRES_PASSWORD')
}


@app.route('/number_of_tables', methods=["GET"])
def get_table_count():
    """Route to get the number of tables in the database."""
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Execute the query to get the number of tables in the Postgres database
        cursor.execute("SELECT count(*) FROM information_schema.tables;")
        table_count = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return jsonify({'table_count': table_count})

    except Exception as e:
        return jsonify({'error': f'An error occurred while fetching table count: {e}'})


@app.route('/health', methods=["GET"])
def health_check():
    """Route for health check of the service."""
    try:
        # Retrieve the container name from environment variable
        container_name = os.environ.get('FLASK_CONTAINER_NAME', 'container_name_not_set')
    except KeyError:
        container_name = 'container_name_not_set'

    # Return a health response
    return jsonify({
        'status': 'Healthy!',
        'container': container_name
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    