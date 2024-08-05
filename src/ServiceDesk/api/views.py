import random

import requests
import datetime
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApplicationFormSerializer
from ServiceDesk.models import ApplicationForm
from .custom_decorator import limit_rate


class ApplicationFormCreateAPIView(generics.CreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer

    @limit_rate(num_requests=3, period=3600)
    def create(self, request, *args, **kwargs):
        import re

        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                self.perform_create(serializer)

                PHONE_REGEX = re.compile(r'^\+?[1-9]\d{1,14}$')
                EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

                if not PHONE_REGEX.match(request.data['number_or_email']) and not EMAIL_REGEX.match(request.data['number_or_email']):
                    return Response({'error': 'Неправильный email или номер телефона'}, status=status.HTTP_400_BAD_REQUEST)



                bot_token = '7414126400:AAGzT4FIlTF5AFfL2VLecXLHOsRvb0DWPaA'
                chat_id = '860389338'
                message = (
                    f'Номер заявки: {random.randint(1000, 9999)}\n'
                    f"Имя: {request.data['name']}\n"
                    f"Контакты: {request.data['number_or_email']}\n"
                    f"Вопрос по услуге/ам: {', '.join(request.data['service_titles'])}\n"
                    f"Комментарий: {request.data['review']}\n"
                    f"Создано в: {datetime.datetime.now().strftime('Дата: %D, время: %H:%M')}"
                )
                url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
                requests.post(url)

                headers = self.get_success_headers(serializer.data)
                responce_201 = {
                    "message": "Your request has been successfully submitted! Manager will contact you soon.",
                }

                return Response(responce_201, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            responce_400 = {
                "message": "Your request has not been successfully submitted! Please try again later.",
                "error": str(e)
            }
            return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)
