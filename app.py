from routes.create_update_routes import createUpdateRoutes
from routes.report_routes import reportRoutes
from routes.scholarship_admin_routes import scholarshipAdminRoutes
from routes.student_routes import student
from routes.util_routes import utilRoutes
from routes.view_routes import view
from routes.main_routes import main
from routes.home_pages import homePages
from flask import Flask

app = Flask(__name__)


app.register_blueprint(main)
app.register_blueprint(homePages)
app.register_blueprint(createUpdateRoutes)
app.register_blueprint(reportRoutes)
app.register_blueprint(scholarshipAdminRoutes)
app.register_blueprint(student)
app.register_blueprint(utilRoutes)
app.register_blueprint(view)

if __name__ == '__main__':
    app.run(debug=True)
