# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| home | index.html | ![screenshot](documentation/validation/html/htmlval1.png) | Pass: No error found |
| tutor | tutors.html | ![screenshot](documentation/validation/html/htmlval2.png) | Pass: No error found |
| tutor | tutors_profile.html | ![screenshot](documentation/validation/html/htmlval3.png) | Pass: No error found |
| booking | booking_create.html | ![screenshot](documentation/validation/html/htmlval4.png) | Pass: No error found |
| booking | booking_success.html | ![screenshot](documentation/validation/html/htmlval5.png) | Pass: No error found |
| personaluser | my_profile.html | ![screenshot](documentation/validation/html/htmlval6.png) | Pass: No error found |
| personaluser | edit_profile.html | ![screenshot](documentation/validation/html/htmlval7) | Pass: No error found |
| contact | contact_form.html | ![screenshot](documentation/validation/html/htmlval8.png) | Pass: No error found |
| contact | contact_success.html | ![screenshot](documentation/validation/html/htmlval9.png) | Pass: No error found |
| templates | signup.html.html | ![screenshot](documentation/validation/html/htmlval11.png) | Pass: No error found |
| templates | logout.html | ![screenshot](documentation/validation/html/htmlval10.png) | Pass: No error found |
| templates | login.html | ![screenshot](documentation/validation/html/htmlval12.png) | Pass: No error found |
| templates | password_reset.html | ![screenshot](documentation/validation/html/htmlval13.png) | Pass: No error found |
| templates | verification_sent.html | ![screenshot](documentation/validation/html/htmlval17.png) | Pass: No error found |
| templates | password_reset_done.html | ![screenshot](documentation/validation/html/htmlval18.png) | Pass: No error found |
| templates | error.html | ![screenshot](documentation/validation/html/htmlval14.png) | Pass: No error found |
| templates | 403.html | ![screenshot](documentation/validation/html/htmlval15.png) | Pass: No error found |
| templates | 404.html | ![screenshot](documentation/validation/html/htmlval16.png) | Pass: No error found |
| templates | 500.html | ![screenshot](documentation/validation/html/htmlval19.png) | Pass: No error found |
| templates | password_reset_from_key.html | ![screenshot](documentation/validation/html/htmlval20.png) | 1 error: The allauth password reset from key form has known HTML validation error |
| templates | password_reset_from_key_done.html | ![screenshot](documentation/validation/html/htmlval21.png) | Pass: No error found |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | base.css | ![screenshot](documentation/validation/css/cssval1.png) | Pass: No error found |
| static | booking.css | ![screenshot](documentation/validation/css/cssval2.png) | Pass: No error found |
| static | contact.css | ![screenshot](documentation/validation/css/cssval3.png) | Pass: No error found |
| static | error.css | ![screenshot](documentation/validation/css/cssval4.png) | Pass: No error found |
| static | home.css | ![screenshot](documentation/validation/css/cssval5.png) | Pass: No error found |
| static | personaluser.css | ![screenshot](documentation/validation/css/cssval6.png) | Pass: No error found |
| static | tutor.css | ![screenshot](documentation/validation/css/cssval7.png) | Pass: No error found |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| booking | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/booking/admin.py) | ![screenshot](documentation/validation/python/pyval6.png) | All clear, no errors found |
| booking | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/booking/models.py) | ![screenshot](documentation/validation/python/pyval2.png) | All clear, no errors found |
| booking | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/booking/urls.py) | ![screenshot](documentation/validation/python/pyval3.png) | All clear, no errors found |
| booking | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/booking/views.py) | ![screenshot](documentation/validation/python/pyval4.png) | All clear, no errors found |
| booking | webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/booking/webhooks.py) | ![screenshot](documentation/validation/python/pyval5.png) | All clear, no errors found |
| contact | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/contact/admin.py) | ![screenshot](documentation/validation/python/pyval7.png) | All clear, no errors found |
| contact | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/contact/forms.py) | ![screenshot](documentation/validation/python/pyval8.png) | All clear, no errors found |
| contact | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/contact/models.py) | ![screenshot](documentation/validation/python/pyval9.png) | All clear, no errors found |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/contact/urls.py) | ![screenshot](documentation/validation/python/pyval10.png) | All clear, no errors found |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/contact/views.py) | ![screenshot](documentation/validation/python/pyval11.png) | All clear, no errors found |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/home/urls.py) | ![screenshot](documentation/validation/python/pyval12.png) | All clear, no errors found |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/home/views.py) | ![screenshot](documentation/validation/python/pyval13.png) | All clear, no errors found |
| newsletter | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/newsletter/admin.py) | ![screenshot](documentation/validation/python/pyval14.png) | All clear, no errors found |
| newsletter | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/newsletter/forms.py) | ![screenshot](documentation/validation/python/pyval15.png) | All clear, no errors found |
| newsletter | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/newsletter/models.py) | ![screenshot](documentation/validation/python/pyval16.png) | All clear, no errors found |
| newsletter | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/newsletter/urls.py) | ![screenshot](documentation/validation/python/pyval17.png) | All clear, no errors found |
| newsletter | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/newsletter/views.py) | ![screenshot](documentation/validation/python/pyval18.png) | All clear, no errors found |
| personaluser | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/personaluser/admin.py) | ![screenshot](documentation/validation/python/pyval19.png) | All clear, no errors found |
| personaluser | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/personaluser/forms.py) | ![screenshot](documentation/validation/python/pyval20.png) | All clear, no errors found |
| personaluser | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/personaluser/models.py) | ![screenshot](documentation/validation/python/pyval21.png) | All clear, no errors found |
| personaluser | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/personaluser/urls.py) | ![screenshot](documentation/validation/python/pyval22.png) | All clear, no errors found |
| personaluser | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/personaluser/views.py) | ![screenshot](documentation/validation/python/pyval23.png) | All clear, no errors found |
| signcoding | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/signcoding/urls.py) | ![screenshot](documentation/validation/python/pyval24.png) | All clear, no errors found |
| signcoding | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/signcoding/views.py) | ![screenshot](documentation/validation/python/pyval25.png) | All clear, no errors found |
| tutor | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/tutor/admin.py) | ![screenshot](documentation/validation/python/pyval26.png) | All clear, no errors found |
| tutor | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/tutor/forms.py) | ![screenshot](documentation/validation/python/pyval27.png) | All clear, no errors found |
| tutor | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/tutor/models.py) | ![screenshot](documentation/validation/python/pyval28.png) | All clear, no errors found |
| tutor | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/tutor/urls.py) | ![screenshot](documentation/validation/python/pyval29.png) | All clear, no errors found |
| tutor | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/RoBizMan/SignCoding/main/tutor/views.py) | ![screenshot](documentation/validation/python/pyval30.png) | All clear, no errors found |

---

