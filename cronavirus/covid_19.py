from plyer import notification

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,#"E:\cronavirus\download.ico",
        timeout = 10
    )
if __name__ == " __main__":
    notifyMe("shishir","Lets stop the spread of this virus together")
