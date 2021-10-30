## TESTING

### User Stories

For this website there are  two types of users; the customer who is looking to purchase fitness equipment/supplements
in an easy and convenient way and the shop owner whose goal is to provide users with this service in a satisfactory manner.




### Defensive programming

Some app pages are only accessible to authorised users and/or superusers for security of data.

**Product Management** Pages are only accessible by the SuperUser (as they are checked by a superuser request) and all links to these pages are hidden to regular users. The Product Management pages include add_product.html and edit_product.html.

**My Profile** page is only available for registered users.

**Blog Comments** Can be posted by anyone but will only be displayed if a superuser approves them.