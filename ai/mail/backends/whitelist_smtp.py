# -*- coding: utf-8 -*-
import re

from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend as SMTPEmailBackend

EMAIL_BACKEND_DOMAIN_WHITELIST = getattr(settings, 'EMAIL_BACKEND_DOMAIN_WHITELIST', [])
REGEX = r'^[\w\-\.]+@(%s)$' % '|'.join(x for x in EMAIL_BACKEND_DOMAIN_WHITELIST).replace('.', '\.')


class WhitelistEmailBackend(SMTPEmailBackend):
    @staticmethod
    def whitify_mail_adresses(mail_adress_list):
        allowed_recipients = []
        for to in mail_adress_list:
            if re.search(REGEX, to):
                allowed_recipients.append(to)
            else:
                # sende nicht erlaubte Mails an den testuser.t-ped.de Catchall
                allowed_recipients.append("%s@testuser.t-ped.de" % to.replace('@', '_'))
        return allowed_recipients

    def send_messages(self, email_messages):
        """
        Checks if email-recipients are in allowed domains and cancels if not.
        Uses regular smtp-sending afterwards.
        """
        for email in email_messages:
            allowed_recipients = self.whitify_mail_adresses(email.to)
            email.to = allowed_recipients
        super(WhitelistEmailBackend, self).send_messages(email_messages)
