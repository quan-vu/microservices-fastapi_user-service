from confluent_kafka import Producer

class UserRegisteredProducer():

    def __init__(self):
        self.p = Producer({'bootstrap.servers': 'localhost:9092'})

    def callback(self, err, msg):
        if err is not None:
            print("Failed to deliver message: {0}: {1}"
                .format(msg.value(), err.str()))
        else:
            print("Message produced: {0}".format(msg.value()))    

    def send(self, data):
        try:
            self.p.produce('user_registered', '{0}'.format(data), callback=self.callback)
            self.p.poll(0.5)
        except KeyboardInterrupt:
            pass

        self.p.flush(30)