import os
from project import app
# never have true for production. True also prevents 500 error from popping up.
# app.run(debug=True)
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
