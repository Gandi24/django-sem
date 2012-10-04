from M2Crypto import BIO, Rand, SMIME, X509
from django.core.mail import send_mail, EmailMessage, SafeMIMEMultipart
from email import message_from_string
import settings

def createsmime(msg, from_key, from_cert):
    """
    This part of code is a mix of code from:
    http://svn.osafoundation.org/m2crypto/trunk/doc/howto.smime.html
    """
    s = SMIME.SMIME()
    s.load_key(from_key, from_cert)

    sk = X509.X509_Stack()
    x509 = X509.load_cert(settings.AUTH_CERT)
    sk.push(x509)
    s.set_x509_stack(sk)

    msg_bio = BIO.MemoryBuffer(msg)
    p7 = s.sign(msg_bio)
    msg_bio = BIO.MemoryBuffer(msg) # Recreate coz sign() has consumed it.

    out = BIO.MemoryBuffer()
    s.write(out, p7, msg_bio)
    out.close()

    return out.read()

class SignedEmailMessage(EmailMessage):
    MIME_HEADERS = set((
        'mime-version',
        'content-id',
        'content-type',
        'content-disposition',
        'content-transfer-encoding',
        ))

    def __init__(self, *args, **kwargs):
        self.from_cert = kwargs.pop('from_cert', None)
        self.from_key = kwargs.pop('from_key', None)
        super(SignedEmailMessage, self).__init__(*args, **kwargs)

    def message(self):
        plain_msg = super(SignedEmailMessage, self).message()
        headers = dict()
        for k, v in plain_msg.items():
            if k.lower() not in self.MIME_HEADERS:
                headers[k] = v
                del plain_msg[k]
        if not self.attachments:
        # When attachment is added, message is automaticaly set to be SafeMIMEMultipart. We have to force it to do so.
            encoding = self.encoding or settings.DEFAULT_CHARSET
            body_msg = plain_msg
            msg = SafeMIMEMultipart(_subtype=self.mixed_subtype, encoding=encoding)
            if self.body:
                msg.attach(body_msg)
            plain_msg = msg
        message_body = createsmime(plain_msg.as_string(), self.from_key, self.from_cert)
        msg = message_from_string(message_body)
        for k, v in headers.items():
            msg[k] = v
        return msg