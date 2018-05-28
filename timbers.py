from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():

    """ This method to be used by the REPL to permit database instances and models to be shared in a shell context
    Example usage: From the cli: 
    flask shell
    -- Now you are in a REPL with database access and the models too
    """

    return {'db': db, 'User': User, 'Post': Post}

