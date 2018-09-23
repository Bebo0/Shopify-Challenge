import graphene
from api.schema import Query as lineitem_query

class Query(lineitem_query):
	pass

schema = graphene.Schema(query=Query)