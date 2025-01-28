from notifypy import Notify # type: ignore

if mode == 'monitor': # type: ignore

    notification = Notify()
    notification.title = 'Proccess Interrupted ' # type: ignore
    notification.message = "Key Board Interrupted."
    notification.icon = './assets/images/stop.png'
    # notification.audio = "./assets/sound/uwu.wav"
    notification.send()
    exit()
  