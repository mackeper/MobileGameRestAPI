from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from score.models import Score
from score.serializers import ScoreSerializer

@csrf_exempt
def score_list(request):
    """
    List all code scores, or create a new score.
    """
    if request.method == 'GET':
        scores = Score.objects.all()
        serializer = ScoreSerializer(scores, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ScoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def score_detail(request, pk):
    """
    Retrieve, update or delete a code score.
    """
    try:
        score = Score.objects.get(pk=pk)
    except Score.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ScoreSerializer(score)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ScoreSerializer(score, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        score.delete()
        return HttpResponse(status=204)