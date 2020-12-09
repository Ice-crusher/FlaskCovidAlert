from pyfcm import FCMNotification

#todo get this value from heroku CI
push_service = FCMNotification(api_key="AAAAujOMeAE:APA91bEVG034XkqY-UGjen3iLkkj1XUEkb7yEfudgKj5qyabvdD-gUJkeAg3tPPuXPAZRgGAuDY2eDTbfZ5NPqF__OchVvfnlBTvxz5EwM1XLifLxm528pygZCRCSRT2RQs5C3hOXJgQ")

def sendNotification(fcmToken):
    registration_id = fcmToken
    message_title = "DANGEROUS"
    message_body = "Jestes w strefie ryzyka zakazenia COVID-19. Uwazaj na siebie!"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    print(result)

#todo send FCM to multiply devices