from comments.serializers import CommentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from classifier.classification import Classification
from classifier.classification_json import JSONClassificationResponse 


class CommentsSentiment(APIView):
    """
    Get comments sentiment polarity
    """
    def get(self, request, format=None):
        '''
        Single comment sentiment classification:
        QUERY_PARAMS:
        comment: string comment
        classifier_type: 'SVM' or 'MNB'   
        classes: 2 or 5
        '''
        comment = request.QUERY_PARAMS.get('comment', 'comentario no encontrado :(')
        classifier_type = request.QUERY_PARAMS.get('classifier_type','SVM')
        no_classes = int(request.QUERY_PARAMS.get('no_classes', 5))
        classify = Classification()
        sentiment = classify.classify_comment(comment, classifier_type=classifier_type, no_classes=no_classes)
    	serializer = CommentSerializer()
    	serialized = serializer.serialize({comment:sentiment})
        return Response(serialized)
    

    def post(self, request, format=None):
        '''
        Multiple comment sentiment classification:
        JSON_FORMAT:
        See JSON_FORMAT_for_REST_Service.txt for details on input/output json format
        '''
        serializer = CommentSerializer()
        print type(request.DATA)
        json_response = JSONClassificationResponse() 
        deserialized = serializer.deserialize(request.DATA)
        if deserialized:            
            return Response(json_response.classification_response(request.DATA), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    