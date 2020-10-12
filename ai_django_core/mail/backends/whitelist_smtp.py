import re

from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend as SMTPEmailBackend

EMAIL_BACKEND_DOMAIN_WHITELIST = getattr(settings, 'EMAIL_BACKEND_DOMAIN_WHITELIST', [])
EMAIL_BACKEND_REDIRECT_ADDRESS = getattr(settings, 'EMAIL_BACKEND_REDIRECT_ADDRESS')
REGEX = r'^[\w\-\.]+@(%s)$' % '|'.join(x for x in EMAIL_BACKEND_DOMAIN_WHITELIST).replace('.', r'\.')


class WhitelistEmailBackend(SMTPEmailBackend):
    """
    Man kann über die folgenden Settings konfigurieren, ob Mails an _alle_ Adressen verschickt werden.
    Wenn nicht, dann kann eine Umleitung an ein Postfach mit CATCHALL konfiguriert werden.

    EMAIL_BACKEND = 'ai_django_core.mail.backends.whitelist_smtp.WhitelistEmailBackend'
    EMAIL_BACKEND_DOMAIN_WHITELIST = ['ambient-innovation.com']
    EMAIL_BACKEND_REDIRECT_ADDRESS = '%s@testuser.ambient-innovation.com'

    Wenn EMAIL_BACKEND_REDIRECT_ADDRESS gesetzt ist, wird eine Mail an xy.z@example.com umgeleitet an:
    xy.z_example.com@testuser.ambient-innovation.com
    """

    @staticmethod
    def whitify_mail_adresses(mail_adress_list):
        allowed_recipients = []
        for to in mail_adress_list:
            if re.search(REGEX, to):
                allowed_recipients.append(to)
            elif EMAIL_BACKEND_REDIRECT_ADDRESS:
                # sende nicht erlaubte Mails an die angegebene Redirect-Adresse (mit CATCHALL)
                allowed_recipients.append(EMAIL_BACKEND_REDIRECT_ADDRESS % to.replace('@', '_'))
        return allowed_recipients

    def send_messages(self, email_messages):
        """
        Checks if email-recipients are in allowed domains and cancels if not.
        Uses regular smtp-sending afterwards.
        """
        for email in email_messages:
            allowed_recipients = self.whitify_mail_adresses(email.to)
            email.to = allowed_recipients
        super().send_messages(email_messages)
