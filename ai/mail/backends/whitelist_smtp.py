# -*- coding: utf-8 -*-
import re

from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend as SMTPEmailBackend
from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend

EMAIL_BACKEND_DOMAIN_WHITELIST = getattr(settings, 'EMAIL_BACKEND_DOMAIN_WHITELIST', [])
REGEX = r'^[\w\-\.]+@(%s)$' % '|'.join(x for x in EMAIL_BACKEND_DOMAIN_WHITELIST).replace('.', '\.')


class EmailBackend(SMTPEmailBackend):
    def __init__(self, *args, **kwargs):
        self.console_backend = ConsoleEmailBackend(*args, **kwargs)
        super(EmailBackend, self).__init__(*args, **kwargs)

    def send_messages(self, email_messages):
        """
        Checks if email-recipients are in allowed domains and cancels if not.
        Uses regular smtp-sending afterwards.
        """
        for email in email_messages:
            allowed_recipients = []
            # unallowed_recipients = []
            for to in email.to:
                if re.search(REGEX, to):
                    allowed_recipients.append(to)
                else:
                    # sende nicht erlaubte Mails an den t-ped.biz Catchall
                    allowed_recipients.append("%s@t-ped.biz" % to.replace('@', '_'))
                    # unallowed_recipients.append(to)
            email.to = allowed_recipients
        super(EmailBackend, self).send_messages(email_messages)
        # self.console_backend.send_messages(email_messages)
