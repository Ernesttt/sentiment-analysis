from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.compat import BytesIO



class CommentSerializer(object):
	"""
	Serialize/Deserialize python natives into JSON format and viceversa
	"""
	def serialize(self, obj):
		#serialized = JSONRenderer().render(obj)
		return obj

	def deserialize(self, obj):
		#stream = BytesIO(obj)
		#deserialized =  JSONParser().parse(stream)
		return obj

# Here we can modify to serialize objects instead of python natives