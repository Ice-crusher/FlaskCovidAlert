from pyfcm import FCMNotification
from extensions import fcmApiKey

push_service = FCMNotification(api_key=fcmApiKey)

def sendNotifications(fcmTokens):
    registration_ids = fcmTokens
    message_title = "Uwaga!"
    message_body = "Wcześniej spotkałeś osobę chorą na COVID-19. Jesteś w strefie ryzyka zakażenia. Uważaj na siebie!"
    result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
    print(result)
