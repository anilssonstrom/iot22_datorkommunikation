import paho.mqtt.client as mqtt
from typing import Any, Optional


def on_connect(client: type[mqtt.Client], userdata: Any, flags: Optional[dict], rc: int):
    """ Anropas när vi ansluter till brokern """
    # rc = result code
    print(f"Connected to server, with result code {rc}")

    # Om vi lyckades ansluta, gör subscribe till en topic
    client.subscribe(topic="test/topic")


def on_message(client: type[mqtt.Client], userdata: Any, message: type[mqtt.MQTTMessage]):
    """ Anropas när vi får ett meddelande från brokern """
    print(f"Topic: {message.topic}, Message: {message.payload.decode('utf-8')}")


def main():
    client = mqtt.Client()

    # Ställ in vad som händer när klienten anslutit eller tagit emot meddelanden
    client.on_connect = on_connect
    client.on_message = on_message

    # Sätt användarnamn och lösenord
    client.username_pw_set(username='client', password='test')

    # Ställ in Last Will and Testament
    client.will_set('test/topic', 'Goodbye cruel world!')

    # Anslut till en broker
    client.connect(host='localhost', port=1883, keepalive=60)

    # Lyssna på trafik
    client.loop_forever()


if __name__ == '__main__':
    main()
