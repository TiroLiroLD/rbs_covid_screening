import paho.mqtt.client as mqtt
import json
import time

risk_message = "Acesso NAO APROVADO.\n" \
               "Risco de contaminacao, procure assistencia medica"

no_risk_message = "Acesso APROVADO\n" \
                  "Sem risco identificado"


class ClientMQTT:
    __broker = "broker.emqx.io"

    def __init__(self):
        self.client = mqtt.Client('covid_robios')
        self.client.on_message = self.on_message
        # self.client.on_connect = self.on_connect
        # self.client.on_disconnect = self.on_disconnect

    def publish(self, message):
        self.client.connect(self.__broker)
        self.client.loop_start()
        self.client.subscribe("robios/covid_result")
        self.client.publish("robios/covid_result", json.dumps(message))
        time.sleep(2)
        self.client.loop_stop()
        self.client.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("connected - OK")
        else:
            print(f"Bad connection, code {rc}")

    def on_disconnect(self, client, userdata, flags, rc=0):
        print(f"Disconnected, code {rc}")

    def on_message(self, client, userdata, msg):
        # print(msg.topic)
        m_decode = str(msg.payload.decode("utf-8"))
        json_msg = json.loads(m_decode)
        if json_msg['risk']:
            print(risk_message)
        else:
            print(no_risk_message)

    def set_broker(self, broker):
        self.__broker = broker
