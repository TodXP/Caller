import vidstream

import threading


receiver = vidstream.AudioReceiver('192.168.68.69', 9999)
receive_thread = threading.Thread(target=receiver.start_server)

sender = vidstream.AudioSender('192.168.68.74', 5555)
sender_thread = threading.Thread(target=sender.start_stream)

receive_thread.start()
sender_thread.start()