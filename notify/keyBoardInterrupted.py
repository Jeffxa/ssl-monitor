# notify for monitor end with the task is interrupted form keyboard
if mode == 'monitor': # type: ignore
    notification = Notify()
    notification.title = 'Proccess Interrupted ' # type: ignore
    notification.message = "Key Board Interrupted."
    notification.icon = './assets/images/stop.png'
    # notification.audio = "./assets/sound/uwu.wav"
    notification.send()
    exit()
  