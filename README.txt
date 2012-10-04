==================
SignedEmailMessage
==================

SignedEmailMessage is a django package modifying the original, built-in EmailMessage 
by adding a possibility to add signing certificats.

INITIAL ACTIONS
===============

1. Include SEM in your settings' installed apps.
INSTALLED_APPS = (
	...
	'SEM',
	...
	)

2. Add your authentication certificate to your settings.
AUTH_CERT = "resources/cert.pem"

This is the highest available cert in cery-chain.
 

TYPICAL USAGE
=============

from SEM import SEMail

msg = SEMail.SignedEmailMessage(
            subject, message_body, sender, recipient_list, attachments=attachments,
            from_key=from_key, from_cert=from_cert)
msg.send()


REQUIREMENTS
============

Django >= 1.1.1
M2Crypto >= 0.21.1


CONTRIBUTION
============

This package is fully dependent and bases on M2Crpyto.