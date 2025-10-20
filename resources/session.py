from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import SessionSchema
from storage import load_sessions, save_sessions

blp = Blueprint("Sessions", "sessions", description="Operations on sessions")

@blp.route("/sessions/<string:session_id>")
class SessionResource(MethodView):
    @blp.response(200, SessionSchema)
    def get(self, session_id):
        sessions = load_sessions()
        for session in sessions:
            if session["session_id"] == session_id:
                return session
        abort(404, message="Session not found")

    @blp.arguments(SessionSchema)
    @blp.response(200, SessionSchema)
    def put(self, updated_session, session_id):
        sessions = load_sessions()
        for index, session in enumerate(sessions):
            if session["session_id"] == session_id:
                # Update the session in place
                sessions[index] = updated_session
                save_sessions(sessions)
                return updated_session
        abort(404, message="Session not found")

    @blp.response(204)
    def delete(self, session_id):
        sessions = load_sessions()
        for index, session in enumerate(sessions):
            if session["session_id"] == session_id:
                del sessions[index]
                save_sessions(sessions)
                return
        abort(404, message="Session not found")


@blp.route("/sessions")
class SessionsList(MethodView):
    @blp.response(200, SessionSchema(many=True))
    def get(self):
        return load_sessions()

    @blp.arguments(SessionSchema)
    @blp.response(201, SessionSchema)
    def post(self, new_session):
        sessions = load_sessions()
        if any(s["session_id"] == new_session["session_id"] for s in sessions):
            abort(400, message="Session ID already exists")
        sessions.append(new_session)
        save_sessions(sessions)
        return new_session
