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
| personaluser | edit_profile.html | ![screenshot](documentation/validation/html/htmlval7.png) | Pass: No error found |
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

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Tutor List | Tutor Profile | Tutor Add | Tutor Edit | Booking | Booking Success | Profile | Profile Edit | Contact | Contact Success | Register | Login | Sign Out | Email Verification | Email Verification Success | Reset Password | Reset Password Confirmation | Reset Password Key | Reset Password Key Success | Error | 403 | 404 | 500 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/chrome1.png) | ![screenshot](documentation/browsers/chrome2.png) | ![screenshot](documentation/browsers/chrome3.png) | ![screenshot](documentation/browsers/chrome4.png) | ![screenshot](documentation/browsers/chrome5.png) | ![screenshot](documentation/browsers/chrome6.png) | ![screenshot](documentation/browsers/chrome7.png) | ![screenshot](documentation/browsers/chrome8.png) | ![screenshot](documentation/browsers/chrome9.png) | ![screenshot](documentation/browsers/chrome10.png) | ![screenshot](documentation/browsers/chrome11.png) | ![screenshot](documentation/browsers/chrome12.png) | ![screenshot](documentation/browsers/chrome14.png) | ![screenshot](documentation/browsers/chrome23.png) | ![screenshot](documentation/browsers/chrome13.png) | ![screenshot](documentation/browsers/chrome16.png) | ![screenshot](documentation/browsers/chrome15.png) | ![screenshot](documentation/browsers/chrome17.png) | ![screenshot](documentation/browsers/chrome18.png) | ![screenshot](documentation/browsers/chrome19.png) | ![screenshot](documentation/browsers/chrome22.png) | ![screenshot](documentation/browsers/chrome21.png) | ![screenshot](documentation/browsers/chrome20.png) | ![screenshot](documentation/browsers/chrome24.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/firefox1.png) | ![screenshot](documentation/browsers/firefox2.png) | ![screenshot](documentation/browsers/firefox3.png) | ![screenshot](documentation/browsers/firefox5.png) | ![screenshot](documentation/browsers/firefox4.png) | ![screenshot](documentation/browsers/firefox6.png) | ![screenshot](documentation/browsers/firefox7.png) | ![screenshot](documentation/browsers/firefox8.png) | ![screenshot](documentation/browsers/firefox9.png) | ![screenshot](documentation/browsers/firefox10.png) | ![screenshot](documentation/browsers/firefox11.png) | ![screenshot](documentation/browsers/firefox17.png) | ![screenshot](documentation/browsers/firefox13.png) | ![screenshot](documentation/browsers/firefox12.png) | ![screenshot](documentation/browsers/firefox14.png) | ![screenshot](documentation/browsers/firefox15.png) | ![screenshot](documentation/browsers/firefox18.png) | ![screenshot](documentation/browsers/firefox16.png) | ![screenshot](documentation/browsers/firefox19.png) | ![screenshot](documentation/browsers/firefox20.png) | ![screenshot](documentation/browsers/firefox23.png) | ![screenshot](documentation/browsers/firefox22.png) | ![screenshot](documentation/browsers/firefox21.png) | X | Works as expected |
| Edge | ![screenshot](documentation/browsers/edge1.png) | ![screenshot](documentation/browsers/edge2.png) | ![screenshot](documentation/browsers/edge4.png) | ![screenshot](documentation/browsers/edge3.png) | ![screenshot](documentation/browsers/edge5.png) | ![screenshot](documentation/browsers/edge6.png) | ![screenshot](documentation/browsers/edge7.png) | ![screenshot](documentation/browsers/edge8.png) | ![screenshot](documentation/browsers/edge9.png) | ![screenshot](documentation/browsers/edge10.png) | ![screenshot](documentation/browsers/edge11.png) | ![screenshot](documentation/browsers/edge14.png) | ![screenshot](documentation/browsers/edge15.png) | ![screenshot](documentation/browsers/edge12.png) | ![screenshot](documentation/browsers/edge16.png) | ![screenshot](documentation/browsers/edge17.png) | ![screenshot](documentation/browsers/edge18.png) | ![screenshot](documentation/browsers/edge19.png) | ![screenshot](documentation/browsers/edge20.png) | ![screenshot](documentation/browsers/edge23.png) | ![screenshot](documentation/browsers/edge21.png) | ![screenshot](documentation/browsers/edge22.png) | ![screenshot](documentation/browsers/edge13.png) | X | Works as expected |
| Safari | ![screenshot](documentation/browsers/safari1.png) | ![screenshot](documentation/browsers/safari2.png) | ![screenshot](documentation/browsers/safari3.png) | ![screenshot](documentation/browsers/safari4.png) | ![screenshot](documentation/browsers/safari5.png) | ![screenshot](documentation/browsers/safari6.png) | ![screenshot](documentation/browsers/safari7.png) | ![screenshot](documentation/browsers/safari8.png) | ![screenshot](documentation/browsers/safari9.png) | ![screenshot](documentation/browsers/safari10.png) | ![screenshot](documentation/browsers/safari11.png) | ![screenshot](documentation/browsers/safari13.png) | ![screenshot](documentation/browsers/safari23.png) | ![screenshot](documentation/browsers/safari12.png) | ![screenshot](documentation/browsers/safari14.png) | ![screenshot](documentation/browsers/safari15.png) | ![screenshot](documentation/browsers/safari16.png) | ![screenshot](documentation/browsers/safari17.png) | ![screenshot](documentation/browsers/safari18.png) | ![screenshot](documentation/browsers/safari19.png) | ![screenshot](documentation/browsers/safari21.png) | ![screenshot](documentation/browsers/safari20.png) | ![screenshot](documentation/browsers/safari22.png) | X | Works as expected |

---

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Browser | Home | Tutor List | Tutor Profile | Tutor Add | Tutor Edit | Booking | Booking Success | Profile | Profile Edit | Contact | Contact Success | Register | Login | Sign Out | Email Verification | Email Verification Success | Reset Password | Reset Password Confirmation | Reset Password Key | Reset Password Key Success | Error | 403 | 404 | 500 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Apple MacMini | ![screenshot](documentation/responsiveness/desktop1.png) | ![screenshot](documentation/responsiveness/desktop2.png) | ![screenshot](documentation/responsiveness/desktop3.png) | ![screenshot](documentation/responsiveness/desktop4.png) | ![screenshot](documentation/responsiveness/desktop5.png) | ![screenshot](documentation/responsiveness/desktop6.png) | ![screenshot](documentation/responsiveness/desktop7.png) | ![screenshot](documentation/responsiveness/desktop8.png) | ![screenshot](documentation/responsiveness/desktop9.png) | ![screenshot](documentation/responsiveness/desktop10.png) | ![screenshot](documentation/responsiveness/desktop11.png) | ![screenshot](documentation/responsiveness/desktop12.png) | ![screenshot](documentation/responsiveness/desktop14.png) | ![screenshot](documentation/responsiveness/desktop23.png) | ![screenshot](documentation/responsiveness/desktop13.png) | ![screenshot](documentation/responsiveness/desktop16.png) | ![screenshot](documentation/responsiveness/desktop15.png) | ![screenshot](documentation/responsiveness/desktop17.png) | ![screenshot](documentation/responsiveness/desktop18.png) | ![screenshot](documentation/responsiveness/desktop19.png) | ![screenshot](documentation/responsiveness/desktop22.png) | ![screenshot](documentation/responsiveness/desktop21.png) | ![screenshot](documentation/responsiveness/desktop20.png) | ![screenshot](documentation/responsiveness/desktop24.png) | Works as expected |
| Apple iPad Air | ![screenshot](documentation/responsiveness/tablet1.png) | ![screenshot](documentation/responsiveness/tablet2.png) | ![screenshot](documentation/responsiveness/tablet3.png) | ![screenshot](documentation/responsiveness/tablet4.png) | ![screenshot](documentation/responsiveness/tablet5.png) | ![screenshot](documentation/responsiveness/tablet6.png) | ![screenshot](documentation/responsiveness/tablet7.png) | ![screenshot](documentation/responsiveness/tablet8.png) | ![screenshot](documentation/responsiveness/tablet9.png) | ![screenshot](documentation/responsiveness/tablet10.png) | ![screenshot](documentation/responsiveness/tablet11.png) | ![screenshot](documentation/responsiveness/tablet12.png) | ![screenshot](documentation/responsiveness/tablet13.png) | ![screenshot](documentation/responsiveness/tablet14.png) | ![screenshot](documentation/responsiveness/tablet15.png) | ![screenshot](documentation/responsiveness/tablet16.png) | ![screenshot](documentation/responsiveness/tablet17.png) | ![screenshot](documentation/responsiveness/tablet18.png) | ![screenshot](documentation/responsiveness/tablet19.png) | ![screenshot](documentation/responsiveness/tablet20.png) | ![screenshot](documentation/responsiveness/tablet21.png) | ![screenshot](documentation/responsiveness/tablet22.png) | ![screenshot](documentation/responsiveness/tablet23.png) | ![screenshot](documentation/responsiveness/tablet24.png) | Works as expected |
| Google Nexus 4 | ![screenshot](documentation/responsiveness/mobile1.png) | ![screenshot](documentation/responsiveness/mobile2.png) | ![screenshot](documentation/responsiveness/mobile4.png) | ![screenshot](documentation/responsiveness/mobile3.png) | ![screenshot](documentation/responsiveness/mobile5.png) | ![screenshot](documentation/responsiveness/mobile6.png) | ![screenshot](documentation/responsiveness/mobile7.png) | ![screenshot](documentation/responsiveness/mobile8.png) | ![screenshot](documentation/responsiveness/mobile9.png) | ![screenshot](documentation/responsiveness/mobile10.png) | ![screenshot](documentation/responsiveness/mobile11.png) | ![screenshot](documentation/responsiveness/mobile12.png) | ![screenshot](documentation/responsiveness/mobile13.png) | ![screenshot](documentation/responsiveness/mobile14.png) | ![screenshot](documentation/responsiveness/mobile15.png) | ![screenshot](documentation/responsiveness/mobile16.png) | ![screenshot](documentation/responsiveness/mobile17.png) | ![screenshot](documentation/responsiveness/mobile18.png) | ![screenshot](documentation/responsiveness/mobile19.png) | ![screenshot](documentation/responsiveness/mobile20.png) | ![screenshot](documentation/responsiveness/mobile21.png) | ![screenshot](documentation/responsiveness/mobile22.png) | ![screenshot](documentation/responsiveness/mobile23.png) | ![screenshot](documentation/responsiveness/mobile24.png) | Works as expected |

---

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/mobile1.png) | ![screenshot](documentation/lighthouse/desktop1.png) | Some minor and warnings |
| Tutor List | ![screenshot](documentation/lighthouse/mobile2.png) | ![screenshot](documentation/lighthouse/desktop2.png) | Some minor and warnings |
| Tutor Profile | ![screenshot](documentation/lighthouse/mobile3.png) | ![screenshot](documentation/lighthouse/desktop3.png) | Some minor and warnings |
| Tutor Add | ![screenshot](documentation/lighthouse/mobile4.png) | ![screenshot](documentation/lighthouse/desktop4.png) | Some minor warnings |
| Tutor Edit | ![screenshot](documentation/lighthouse/mobile5.png) | ![screenshot](documentation/lighthouse/desktop5.png) | Some minor warnings |
| Booking | ![screenshot](documentation/lighthouse/mobile6.png) | ![screenshot](documentation/lighthouse/desktop6.png) | Some minor warnings |
| Profile | ![screenshot](documentation/lighthouse/mobile7.png) | ![screenshot](documentation/lighthouse/desktop7.png) | Some minor warnings |
| Contact | ![screenshot](documentation/lighthouse/mobile8.png) | ![screenshot](documentation/lighthouse/desktop8.png) | Some minor warnings |
| Sign Out | ![screenshot](documentation/lighthouse/mobile9.png) | ![screenshot](documentation/lighthouse/desktop9.png) | Some minor warnings |
| Register | ![screenshot](documentation/lighthouse/mobile10.png) | ![screenshot](documentation/lighthouse/desktop10.png) | Some minor warnings |
| Login | ![screenshot](documentation/lighthouse/mobile11.png) | ![screenshot](documentation/lighthouse/desktop11.png) | Some minor warnings |
| Reset Password | ![screenshot](documentation/lighthouse/mobile12.png) | ![screenshot](documentation/lighthouse/desktop12.png) | Some minor warnings |
| 403 | ![screenshot](documentation/lighthouse/mobile13.png) | ![screenshot](documentation/lighthouse/desktop13.png) | Some minor warnings |
| 404 | ![screenshot](documentation/lighthouse/mobile14.png) | ![screenshot](documentation/lighthouse/desktop14.png) | Some minor warnings |

---

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | The page is expected to reload after submitting an incorrect email address and display the alert message stating, "Invalid email address. Please enter a valid email." | Deliberately input test@test without .com. | The feature behaved as expected, reloading and displaying the error alert message. | Test concluded and passed | ![screenshot](documentation/defprog/defprog1.png) |
| | The page is expected to reload after submitting an already subscribed email address and display the alert message stating, "You have already subscribed to our newsletter!" | Deliberately input test@test.com, which was already previously subscribed. | The feature behaved as expected, reloading and displaying the error alert message. | Test concluded and passed | ![screenshot](documentation/defprog/defprog2.png) |
| Register | | | | | |
| | The page is expected to redirect the logged user back to the Home page when attempting to brute force the URL of the Register page. | Brute forces the URL of the Register page when logged in. | The feature behaved as expected and redirected the logged user/superuser back to the Home page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog3.png) |
| | The signup form is expected to display the illegible first name, illegible last name, and incorrect email address inline error messages and prevent the form from submitting. | Deliberately input the illegible first name, illegible last name, and incorrect email address. | The feature behaved as expected and displayed the inline errors. Apostrophes and hyphens are allowed because some name may contain, for example, Ava-May and O'Shea. | Test concluded and passed | ![screenshot](documentation/defprog/defprog6.png) |
| Login | | | | | |
| | The page is expected to redirect the logged user back to the Home page when attempting to brute force the URL of the Login page. | Brute forces the URL of the Login page when logged in. | The feature behaved as expected and redirected the logged user/superuser back to the Home page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog4.png) |
| Sign Out | | | | | |
| | The page is expected to redirect the logged-out user or guest back to the Home page when attempting to brute force the Sign Out page URL. | Brute forces the URL of the Sign Out page when logged out or guest access. | The feature behaved as expected and redirected the logged-out user/guest back to the Home page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog5.png) |
| User Profile | | | | | |
| | The page is expected to redirect the logged-out user or guest to the Login page when attempting to brute force the User Profile page URL. | Brute forces the URL of the User Profile page when logged out or guest access. | The feature behaved as expected and redirected the logged-out user/guest to the Login page. If the login is validated, it redirects the logged-in user to the User Profile page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog7.png) |
| | The change name form is expected to display the illegible first name and illegible last name inline error messages and prevent the form from submitting. | Deliberately input the illegible first name and illegible last name. | The feature behaved as expected and reloaded the page to display inline error messages instead of submitting the form. | Test concluded and passed | ![screenshot](documentation/defprog/defprog8.png) |
| | The page is expected to redirect the logged-out user or guest to the Login page when attempting to brute force the User Profile's edit name page URL. | Brute forces the URL of the User Profile's edit name page when logged out or guest access. | The feature behaved as expected and redirected the logged-out user/guest to the Login page. If the login is validated, it redirects the logged-in user to the User Profile's edit name page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog9.png) |
| | The page is expected to redirect the logged-out user or guest to the Login page when attempting to brute force the User Profile's the delete user modal URL. | Brute forces the URL of the User Profile's the delete user modal page when logged out or guest access. | The feature behaved as expected and redirected the logged-out user/guest to the Login page. If the login is validated, it redirects the logged-in user to the User Profile's page instead of deleting the account to prevent accidental deletion through brute forcing the account deletion URL. | Test concluded and passed | ![screenshot](documentation/defprog/defprog10.png) |
| Tutor | | | | | |
| | The page is expected to redirect the logged-out user or guest to the 403 forbidden page when attempting to brute force the Add a New Tutor page URL. | Brute forces the URL of the Add a New Tutor page when logged out or guest access. | The feature behaved as expected and redirected the logged-out user/guest to the 403 forbidden page and offered the logged-out user/guest a button to return back to the Home page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog11.png) |
| | The page is expected to redirect the logged-out user or guest to the 403 forbidden page when attempting to brute force the Edit a Tutor page URL. | Brute forces the URL of the Edit Tutor page when logged out or guest access. | The feature behaved as expected and redirected the logged-out user/guest to the 403 forbidden page and offered the logged-out user/guest a button to return back to the Home page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog12.png) |
| | The page is expected to redirect the logged-out user or guest to the 403 forbidden page when attempting to brute force the Delete a Tutor modal URL. | Brute forces the URL of the Delete Tutor modal when logged out or guest access. | The feature behaved as expected and redirected the logged-out user/guest to the 403 forbidden page and offered the logged-out user/guest a button to return back to the Home page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog13.png) |
| | The page is expected to redirect the logged-in non-superuser user to the 403 forbidden page when attempting to brute force the Add a New Tutor page URL. | Brute forces the URL of the Add a New Tutor page from the logged-in non-superuser user. | The feature behaved as expected and redirected the logged-in non-superuser user to the 403 forbidden page and offered the logged-in non-superuser user a button to return back to the Home page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog14.png) |
| | The page is expected to redirect the logged-in non-superuser user to the 403 forbidden page when attempting to brute force the Edit Tutor page URL. | Brute forces the URL of the Edit Tutor page from the logged-in non-superuser user. | The feature behaved as expected and redirected the logged-in non-superuser user to the 403 forbidden page and offered the logged-in non-superuser user a button to return back to the Home page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog15.png) |
| | The page is expected to redirect the logged-in non-superuser user to the 403 forbidden page when attempting to brute force the Delete a Tutor modal URL. | Brute forces the URL of the Delete a Tutor modal from the logged-in non-superuser user. | The feature behaved as expected and redirected the logged-in non-superuser user to the 403 forbidden page and offered the logged-in non-superuser user a button to return back to the Home page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog16.png) |
| | The Add a New Tutor form is expected to display the illegible first name, illegible last name, and incorrect email address inline error messages and prevent the form from submitting. | Deliberately input the illegible first name, illegible last name, and incorrect email address. | The feature behaved as expected, displayed the inline errors and prevented the superuser from adding a new tutor. Apostrophes and hyphens are allowed because some names may contain, for example, Ava-May and O'Shea. | Test concluded and passed | ![screenshot](documentation/defprog/defprog17.png) |
| | The Edit Tutor form is expected to display the illegible first name, illegible last name, and incorrect email address inline error messages and prevent the form from submitting. | Deliberately input the illegible first name, illegible last name, and incorrect email address. | The feature behaved as expected, displayed the inline errors and prevented the superuser from updating the tutor. Apostrophes and hyphens are allowed because some names may contain, for example, Ava-May and O'Shea. | Test concluded and passed | ![screenshot](documentation/defprog/defprog18.png) |
| Booking | | | | | |
| | The page is expected to redirect the logged-out user or guest to the Login page when attempting to brute force the booking success page URL. | Brute forces the URL of the booking success page when logged out or guest access. | The feature behaved as expected and redirected the logged-out user/guest to the Login page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog19.png) |
| | The page is expected to display the error page after the logged-out user is logged back in and attempts to brute force the URL of someone's booking confirmation (success) page. | Brute forces the URL of someone's booking success page while the user is logged in, but the booking is not theirs. | The feature behaved as expected and displayed the error message stating, "Booking not found". | Test concluded and passed | ![screenshot](documentation/defprog/defprog20.png) |
| | The page is expected to display the error page after the logged-in user attempts to brute force the URL of someone's booking confirmation (success) page. | Brute forces the URL of someone's booking success page while the logged-in user attempts to view someone else's booking. | The feature behaved as expected and displayed the error message stating, "Booking not found". | Test concluded and passed | ![screenshot](documentation/defprog/defprog21.png) |
| | The page is expected to display the error page after the logged-in superuser user attempts to brute force the URL of someone's booking confirmation (success) page. | Brute forces the URL of someone's booking success page while the logged-in superuser attempts to view someone else's booking. | The feature behaved as expected and displayed the error message stating, "Booking not found". | Test concluded and passed | ![screenshot](documentation/defprog/defprog22.png) |
| | The page is expected to redirect the logged-out user or guest to the Login page when attempting to brute force the booking create page URL. | Brute forces the URL of the booking creation page when logged out or guest access. | The feature behaved as expected and redirected the logged-out user/guest to the Login page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog25.png) |
| | The page is expected to display the error page after the logged-out non-superuser or superuser is logged back in after the Login redirection and attempts to brute force the URL of the booking creation page directly without viewing the tutor profile and booking from there first. | Brute forces the URL of the booking creation page after successfully signing in on the Login redirection page. | The feature behaved as expected and displayed the error message stating, "No tutor selected. Please select a tutor first". | Test concluded and passed | ![screenshot](documentation/defprog/defprog23.png) |
| | The page is expected to display the error page after the non-superuser or superuser who has already logged in attempts to brute force the URL of the booking creation page directly from the Home page without viewing the tutor profile and booking from there first. | Brute forces the URL of the booking creation page directly from the Home page without viewing the tutor profile and booking from there first. | The feature behaved as expected and displayed the error message stating, "No tutor selected. Please select a tutor first". | Test concluded and passed | ![screenshot](documentation/defprog/defprog24.png) |
| Contact | | | | | |
| | The contact form is expected to display the illegible full name and incorrect email address inline error messages and prevent the form from submitting. | Deliberately input the illegible full name and incorrect email address. | The feature behaved as expected, displayed the inline errors and prevented the superuser from submitting the form. Apostrophes and hyphens are allowed because some names may contain, for example, Ava-May and O'Shea. | Test concluded and passed | ![screenshot](documentation/defprog/defprog26.png) |
| | The contact form message is expected to stop inputting after the character limit hits 1,000 characters. | Deliberately input the message to reach the 1,000 characters limit and attempt to continue typing thereafter. | The feature behaved as expected and stopped inputting any more characters after hitting the 1,000 characters limit. | Test concluded and passed | ![screenshot](documentation/defprog/defprog27.png) |
| Django admin panel | | | | | |
| | The page is expected to display the normal login page when the logged-out user or guest attempts to brute force the URL of the Django admin panel. | Brute forces the URL of the Django admin panel. | The feature behaved as expected and displayed the normal login page. | Test concluded and passed | ![screenshot](documentation/defprog/defprog28.png) |
| | The login page is expected to display the error message when the non-superuser user attempts to log in to the Django admin panel, preventing the non-superuser user from logging in to the Django admin panel. | Log in to the Django admin panel using non-superuser login credentials. | The feature behaved as expected, prevented the non-superuser from logging in to the Django admin panel, and displayed the error message. | Test concluded and passed | ![screenshot](documentation/defprog/defprog29.png) |
| | The login page is expected to display the error message and stop the logged-in non-superuser user from accessing the Django admin panel when attempting to brute force the URL of the Django admin panel. | Brute forces the URL of the Django admin panel while logged in as a non-superuser user. | The feature behaved as expected, prevented the non-superuser from accessing the Django admin panel, and displayed the error message. | Test concluded and passed | ![screenshot](documentation/defprog/defprog30.png) |

---

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to create an account, so that I can access tutoring services. | ![screenshot](documentation/ustesting/feature1.png) |
| As a new site user, I would like to browse available tutors, so that I can find the right match for my learning needs. | ![screenshot](documentation/ustesting/feature2.png) |
| As a new site user, I would like to book a tutoring session, so that I can start learning programming with a sign language tutor. | ![screenshot](documentation/ustesting/feature3.png) |
| As a returning site user, I would like to view my booking history, so that I can keep track of my past sessions. | ![screenshot](documentation/ustesting/feature4.png) |
| As a returning site user, I would like to check tutor profiles' date and time availability, so that I can book new sessions as per my schedule. | ![screenshot](documentation/ustesting/feature5a.png) ![screenshot](documentation/ustesting/feature5b.png) ![screenshot](documentation/ustesting/feature5c.png) |
| As a returning site user, I would like to update my profile information, so that my details remain current. | ![screenshot](documentation/ustesting/feature6.png) |
| As a site administrator, I should be able to manage user accounts, so that I can ensure a secure and efficient platform. | ![screenshot](documentation/ustesting/feature7.png) |
| As a site administrator, I should be able to monitor tutor availability, so that I can maintain an up-to-date list of available sessions. | ![screenshot](documentation/ustesting/feature8.png) |
| As a site administrator, I should be able to handle booking requests, so that I can ensure smooth scheduling and session management. | ![screenshot](documentation/ustesting/feature9.png) |

---

### GitHub **Issues**

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3ARoBizMan%2FSignCoding%20label%3Abug&label=bugs)](https://github.com/RoBizMan/SignCoding/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

[![GitHub closed issues](https://img.shields.io/github/issues-closed/RoBizMan/SignCoding)](https://github.com/RoBizMan/SignCoding/issues?q=is%3Aissue+is%3Aclosed)

All previously closed/fixed bugs can be tracked [here](https://github.com/RoBizMan/SignCoding/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [Hamburger icon not transforming into X icon when opening the menu](https://github.com/RoBizMan/SignCoding/issues/28) | Closed |
| [Footer nav links clickable area is full width instead of within text area](https://github.com/RoBizMan/SignCoding/issues/29) | Closed |
| [Images order stacked incorrectly in smaller screens](https://github.com/RoBizMan/SignCoding/issues/30) | Closed |
| [Sign Up & Login buttons in the landing page are stacked each other in smaller screens](https://github.com/RoBizMan/SignCoding/issues/31) | Closed |
| [Element div not allowed as child of element button for menu toggler in the mobile view](https://github.com/RoBizMan/SignCoding/issues/32) | Closed |
| [End tag h2 seen, but there were open elements in the index.html](https://github.com/RoBizMan/SignCoding/issues/33) | Closed |
| [Profile picture does not restore to the default image upon the page reload to display the error](https://github.com/RoBizMan/SignCoding/issues/34) | Closed |
| [Django's default allauth signup form does not prevent users from submitting the form with the already registered email](https://github.com/RoBizMan/SignCoding/issues/35) | Closed |
| [The terminal output shows the error "<The file path> SyntaxWarning: invalid escape sequence '\s'"](https://github.com/RoBizMan/SignCoding/issues/36) | Closed |
| [The terminal output shows the error "<The file path> UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'tutor.models.Tutor'> QuerySet. paginator = Paginator(tutors_list, 5)"](https://github.com/RoBizMan/SignCoding/issues/37) | Closed |
| [Session time slots initialise before picking the date from the session date](https://github.com/RoBizMan/SignCoding/issues/38) | Closed |
| [Login page does not display the error message](https://github.com/RoBizMan/SignCoding/issues/39) | Closed |
| [Pagination number displays {{ num }} instead of the actual page number](https://github.com/RoBizMan/SignCoding/issues/40) | Closed |
| [Today's date that is already past all available time slots are displaying in the session date datetime picker widget](https://github.com/RoBizMan/SignCoding/issues/41) | Closed |
| [Fully booked status not displaying properly](https://github.com/RoBizMan/SignCoding/issues/42) | Closed |
| [Booking form Submit/Cancel button width overflow in the mobile view](https://github.com/RoBizMan/SignCoding/issues/43) | Closed |
| [Booking Confirmation sends out the email with (no subject)](https://github.com/RoBizMan/SignCoding/issues/44) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/RoBizMan/SignCoding)](https://github.com/RoBizMan/SignCoding/issues)


Any remaining open issues can be tracked [here](https://github.com/RoBizMan/SignCoding/issues).

No open issues so far.

## Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of.