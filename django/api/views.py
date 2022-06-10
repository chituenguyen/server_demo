from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import BookSerializer
from .models import Book
from rest_framework.decorators import api_view
from django.http import JsonResponse

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        Book.objects.create(title=title, cover=cover)
        return HttpResponse({'message': 'Book created'}, status=200)


@api_view(['POST'])
def post_new(request):
    data = request.data
    book = Book.objects.create(

        title = data['title'],
        cover = data['cover']
    )
    book.save()
    return HttpResponse({'message':'Created'},status = 200)

def cal():
    return [1,2,3,4]
@api_view(['GET'])
def test(request):
    return JsonResponse({'foo':cal()})