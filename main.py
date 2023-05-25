from api import app, db
from api.models import user
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType

# This is a subsitute for ariadne.constants import PLAYGROUND_HTML
# because that is no longer supported in ariadne
from ariadne.explorer import ExplorerPlayground

from flask import request, jsonify
from api.queries.user_queries import resolve_user, resolve_users
from api.queries.book_queries import resolve_book, resolve_books
from api.queries.review_queries import resolve_review, resolve_reviews

from api.mutations.user_mutations import resolve_create_user, resolve_delete_user
from api.mutations.book_mutations import resolve_create_book, resolve_delete_book
from api.mutations.review_mutations import resolve_create_review, resolve_delete_review

with app.app_context():
    db.create_all()
    
# Added this to match current API structure with ariadne
PLAYGROUND_HTML = ExplorerPlayground(title="Book Club API").html(None)

query = ObjectType("Query")

query.set_field("user", resolve_user)
query.set_field("users", resolve_users)
query.set_field("book", resolve_book)
query.set_field("books", resolve_books)
query.set_field("review", resolve_review)
query.set_field("reviews", resolve_reviews)

mutation = ObjectType("Mutation")
mutation.set_field("createUser", resolve_create_user)
mutation.set_field("deleteUser", resolve_delete_user)
mutation.set_field("createBook", resolve_create_book)
mutation.set_field("deleteBook", resolve_delete_book)
mutation.set_field("createReview", resolve_create_review)
mutation.set_field("deleteReview", resolve_delete_review)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
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