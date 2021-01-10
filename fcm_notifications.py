from pyfcm import FCMNotification
from extensions import fcmApiKey

push_service = FCMNotification(api_key=fcmApiKey)

def sendNotifications(fcmToken):
    registration_id = fcmToken
    message_title = "Uwaga!"
    message_body = "Wcześniej spotkałeś osobę chorą na COVID-19. Jesteś w strefie ryzyka zakażenia. Uważaj na siebie!"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    print(result)
