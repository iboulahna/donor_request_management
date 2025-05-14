from prometheus_client import start_http_server, Summary
import time

# Create a metric to track request processing time
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Start the Prometheus server to collect metrics
start_http_server(8000)


@app.route('/handle_request', methods=['POST'])
@REQUEST_TIME.time()  # Track time taken by the request
def handle_request():
    data = request.json
    query = data.get("query")
    # Process the query
    response = augment_response(query)
    return jsonify({"response": response})

from flask_migrate import Migrate
from app.models.donor_model import db

# pip install Flask-Migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


# flask db init
# flask db migrate -m "Create donor table"
# flask db upgrade