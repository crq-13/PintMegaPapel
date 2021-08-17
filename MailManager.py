import os
from imbox import Imbox
import traceback
import Tools

host = "imap.gmail.com"
username = "cristian.rojas.quintero"
password = 'cris-3117619809'
dia = Tools.Get_fecha(dia=1)
download_folder = "Adjuntos/" + str(dia)

if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)

mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)

def Download_Attach(emailSender):
    messages = mail.messages(sent_from=str(emailSender))
    for (uid, message) in messages:
        #mail.mark_seen(uid)  # optional, mark message as read
        for idx, attachment in enumerate(message.attachments):
            try:
                att_fn = attachment.get('filename')
                download_path = f"{download_folder}/{att_fn}"
                print(download_path)
                with open(download_path, "wb") as fp:
                    fp.write(attachment.get('content').read())
                return download_path
            except:
                print(traceback.print_exc())

    mail.logout()
