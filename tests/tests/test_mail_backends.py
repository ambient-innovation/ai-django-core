from django.core.mail import EmailMultiAlternatives
from django.test import TestCase, override_settings

from ai_django_core.mail.backends.whitelist_smtp import WhitelistEmailBackend


@override_settings(
    EMAIL_BACKEND='ai_django_core.mail.backends.whitelist_smtp.WhitelistEmailBackend',
    EMAIL_BACKEND_DOMAIN_WHITELIST=['valid.domain'],
    EMAIL_BACKEND_REDIRECT_ADDRESS='%s@testuser.valid.domain',
)
class MailBackendWhitelistBackendTest(TestCase):
    def test_whitify_mail_addresses_replace(self):
        email_1 = 'albertus.magnus@example.com'
        email_2 = 'thomas_von_aquin@example.com'
        processed_list = WhitelistEmailBackend.whitify_mail_addresses(mail_address_list=[email_1, email_2])

        self.assertEqual(len(processed_list), 2)
        self.assertEqual(processed_list[0], 'albertus.magnus_example.com@testuser.valid.domain')
        self.assertEqual(processed_list[1], 'thomas_von_aquin_example.com@testuser.valid.domain')

    def test_whitify_mail_addresses_whitelisted_domain(self):
        email = 'platon@valid.domain'
        processed_list = WhitelistEmailBackend.whitify_mail_addresses(mail_address_list=[email])

        self.assertEqual(len(processed_list), 1)
        self.assertEqual(processed_list[0], email)

    @override_settings(EMAIL_BACKEND_REDIRECT_ADDRESS='')
    def test_whitify_mail_addresses_no_redirect_configured(self):
        email = 'sokrates@example.com'
        processed_list = WhitelistEmailBackend.whitify_mail_addresses(mail_address_list=[email])

        self.assertEqual(len(processed_list), 0)

    def test_process_recipients_regular(self):
        mail = EmailMultiAlternatives(
            'Test subject', 'Here is the message.', 'from@example.com', ['to@example.com'], connection=None
        )

        backend = WhitelistEmailBackend()
        message_list = backend._process_recipients([mail])
        self.assertEqual(len(message_list), 1)
        self.assertEqual(message_list[0].to, ['to_example.com@testuser.valid.domain'])
