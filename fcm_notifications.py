from pyfcm import FCMNotification
from extensions import fcmApiKey

push_service = FCMNotification(api_key=fcmApiKey)

def sendNotification(fcmToken):
    registration_id = fcmToken
    message_title = "DANGEROUS"
    message_body = "Jestes w strefie ryzyka zakazenia COVID-19. Uwazaj na siebie!"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    print(result)