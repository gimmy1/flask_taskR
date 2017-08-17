from project import app
# never have true for production. True also prevents 500 error from popping up.
# app.run(debug=True)
app.run()
