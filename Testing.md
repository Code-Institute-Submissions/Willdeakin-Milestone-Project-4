## TESTING

### User Stories

For this website there are  two types of users; the customer who is looking to purchase fitness equipment/supplements
in an easy and convenient way and the shop owner whose goal is to provide users with this service in a satisfactory manner.

Customer User Stories
| As a user I want to  	|   So I can	|
|---	|---	|
|   View products	|  TC1 	|
|  View product details	|   See a description of the product and decide if it's right for me |
|  Add items to my bag	|   Buy multiple items at once |
|  Easily acces the cost of my shopping bag at all times 	|   Monitor the cost of my items |
|  Sort products in the store 	|  Easily find a product that suits my needs	|
|  Search for a product	|   Quickly find exactly what I'm looking for	|
|  Easily acces my shopping bag	|   Make sure the items that I want are in my bag	|
|  Adjust the number of items or completely remove items from my bag	|   Make sure that only the items I want are in my bag	|
|  Have a secure payment process	|   Comfortably pay for my items without any worries	|
|  View the details of my purchase in the checkout	|   Make sure that it matches my bag	|
|  Get confirmation of my purchase	|   Be sure my order was received	|
|  Be able to register and login to an account	|   Make my purchases easier	|
|  Update and save a change in my details	|   Keep using my account if these details change	|
|  Change my password if I've forgotten	|   Retrieve my account	|



### Defensive programming

Some app pages are only accessible to authorised users and/or superusers for security of data.

**Product Management** Pages are only accessible by the SuperUser (as they are checked by a superuser request) and all links to these pages are hidden to regular users. The Product Management pages include add_product.html and edit_product.html.

**My Profile** page is only available for registered users.

**Blog Comments** Can be posted by anyone but will only be displayed if a superuser approves them.