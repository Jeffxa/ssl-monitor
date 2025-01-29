# Notify when the audit is finished 
if mode == 'audit': # type: ignore
    notification = Notify()
    notification.title = 'Audit is completed' # type: ignore
    notification.message = "The audit is done"
    notification.icon = './assets/images/graph.png'
    # notification.audio = "./assets/sound/uwu.wav"
    notification.send()
    exit()