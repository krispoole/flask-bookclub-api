from api import app, db
from api.models import user
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType

# This is a subsitute for ariadne.constants import PLAYGROUND_HTML
# because that is no longer supported in ariadne
from ariadne.explorer import ExplorerPlayground

from flask import request, jsonify
from api.queries.user_query import resolve_users

# Added this to match current API structure with ariadne
PLAYGROUND_HTML = ExplorerPlayground(title="Book Club API").html(None)

query = ObjectType("Query")

query.set_field("users", resolve_users)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code