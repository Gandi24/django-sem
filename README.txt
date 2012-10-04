==================
SignedEmailMessage
==================

SignedEmailMessage is a django package modifying the original, built-in EmailMessage 
by adding a possibility to add signing certificats.

Typical usage might looks like this:
msg = SignedEmailMessage(
            subject, message_body, sender, recipient_list, attachments=attachments,
            from_key=from_key, from_cert=from_cert)

REQUIREMENTS
============

Django >= 1.1.1
M2Crypto >= 0.21.1


CONTRIBUTION
============

This package is fully dependent and bases on M2Crpyto.