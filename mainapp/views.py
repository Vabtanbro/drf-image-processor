from django.shortcuts import render

import json
from rest_framework.generics import ListAPIView

from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from .models import ImgProject

from .serializer import ImageSerializer
from .utility_img import process_image




class ImageViewSet(ListAPIView):
    queryset = ImgProject.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        file = request.data.get('real_img',None)
        if file != None:
            try:
                image = ImgProject.objects.create(real_img=file)

                procesed_imgs = process_image(image.real_img.path)
                image.thum_img = procesed_imgs[0]
                image.medium_img = procesed_imgs[1]
                image.large_img = procesed_imgs[2]
                image.gray_img = procesed_imgs[3]

                serializer = self.get_serializer(image)
                #image.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                
            except Exception as _error:
                print(_error)

        return HttpResponse(json.dumps({'message': f"Not Uploaded "}), status=400)
        
        