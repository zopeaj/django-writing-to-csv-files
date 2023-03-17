from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views.decorators import api_view
from csvwrites.core.business.abstracts.csvWriterService import CsvWriterService
from rest_framework import status
import csv
# Create your views here.


csvWriterService = CsvWriterService()

@api_view(['POST'])
def write_csv(request):
    if request.POST:
        data = request.data["datas"]
        if data is not None:
            filename = csvWriterService.writeData(data)
            if filename:
                response = Response(status=status.HTTP_200_OK, content_type="application/csv")
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
            return Response({"detail": "Error creating file"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "No content found for given data"}, status=status.HTTP_400_BAD_REQUEST)


