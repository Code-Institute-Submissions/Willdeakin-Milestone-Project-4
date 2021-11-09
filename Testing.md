## TESTING

### User Stories

For this website there are  two types of users; the customer who is looking to purchase fitness equipment/supplements
in an easy and convenient way and the shop owner whose goal is to provide users with this service in a satisfactory manner.

Customer User Stories
|   | As a user I want to  	|   So I can	|
|---    |---	|---	|
|1|  View product details	|   See a description of the product and decide if it's right for me |
|2|  Add items to my bag	|   Buy multiple items at once |
|3|  Easily access the cost of my shopping bag at all times 	|   Monitor the cost of my items |
|4|  Sort products in the store 	|  Easily find a product that suits my needs	|
|5|  Search for a product	|   Quickly find exactly what I'm looking for	|
|6|  Easily acces my shopping bag	|   Make sure the items that I want are in my bag	|
|7|  Adjust the number of items or completely remove items from my bag	|   Make sure that only the items I want are in my bag	|
|8|  Have a secure payment process	|   Comfortably pay for my items without any worries	|
|9|  View the details of my purchase in the checkout	|   Make sure that it matches my bag	|
|10|  Get confirmation of my purchase	|   Be sure my order was received	|
|11|  Be able to register and login to an account	|   Make my purchases easier	|
|12|  Update and save a change in my details	|   Keep using my account if these details change	|


Store Owner User Stories
|   | As a user I want to  	|   So I can	|
|---	|---	|---	|
|1|  Provide an e-commerce website that works	|   Take my business to the online space |
|2|  Be able to add, update and delete products from the store	|   Keep my store up to date with the products I offer |
|3|  Allow administrative access to certain people	|   Protect my store's sensitive material and get help managing my website |
|4|  Add blogs to my website 	|   Provide an extra service to my store and increase engagement with my store |

### Fulfilment of user stories
|   | Customer user stories fulfilment  	|
|---    |---	|
|1|  The user can press either the product image or a button to access the rpoduct details page	|
|2|  In the product details page there is an add to bag button with a form to allow the user to add multiple of the item	|
|3|  There is a bag total next to the bag link in the top corner at all times 	|
|4|  There are sort buttons available in the home and store views 	|
|5|  There is a search bar available in the home and store views	|
|6|  There is a	bag link in the top corner at all times |
|7|  In the bag view are an update button for the amount and a remove button to remove items from the bag	|
|8|  The checkout app uses stripe payments to securely handle payments	|
|9|  The checkout app features all of the items in the bag	|
|10|  There is a checkout success page which shows the payment has gone through and gives an order number	|
|11|  There are navbar links and corresponding pages to register/ login to an account	|
|12|  In the profile page there is a form for updating delivery details for the user	|


Store Owner User Stories
|   | Store owner user stories fulfilment 	|
|---	|---	|
|1|  My project is a functioning work which allows the customer to access the products available and place orders, with a simple and easy layout	|
|2|  When logged in as a superuser, the store owner can access each existing product to edit or delete, and there is a button at the top of the store page to add a new product also	|
|3|  The store owner can add new superusers in the admin view or approve existing users to become a superuser to allow administrative access	|
|4|  The store owner can add new blogs in the admin view and has access to edit and delete them also	|

### Code Validation

#### HTML

- All HTML pages have been run through the W3C Markup Validation Surface. 
All remaining errors are consequence of the django frameworks: errors for a missing DOCTYPE which is in the base or returning a bad vale for a url in {%%} brackets etc.

#### CSS

All CSS Pages have been run through the W3C CSS Validation Service, no errors were given and all warnings are listed below.

- -webkit-transition is a vendor extension
- ::-webkit-scrollbar is a vendor extended pseudo-element
- ::-webkit-scrollbar-track is a vendor extended pseudo-element
- ::-webkit-scrollbar-thumb is a vendor extended pseudo-element
Which have been ignored as these don't have any bearing on anything other than the side scroller, and if that doesn't work on any device/ browser it won't badly affect the website experience.

#### Javascript

Javascript files have been run through [JSHint](https://jshint.com/), 2 warnings were given from stripe-elements.js:
- Line 27	'template literal syntax' is only available in ES6 (use 'esversion: 6').
- Line 90	'template literal syntax' is only available in ES6 (use 'esversion: 6').
There are also 2 undefined variables $ and Stripe; $ is used in jquery and thus can be ignored, and Stripe is used for stripe functionality and can also be ignored.

#### Python

Python files have been run through [Extends Class Python Tester](https://extendsclass.com/python-tester.html) and a few files returned syntax errors; all of which were regarding f strings, which can be ignored.

#### Form Validation

All the forms are validated with HTML. Manual testing has been carried out for the forms to confirm they are working
correctly.

### Defensive programming

Some app pages are only accessible to authorised users and/or superusers for security of data.

**Product Management** Pages are only accessible by the SuperUser (as they are checked by a superuser request) and all links to these pages are hidden to regular users. The Product Management pages include add_product.html and edit_product.html.

**My Profile** page is only available for registered users.

**Blog Comments** Can be posted by anyone but will only be displayed if a superuser approves them.

## Browser testing


## Bugs, Errors, Issues and Fixes

- When using the W3C validator to validate my HTML, I received a number of errors regarding button elements sat inside anchor tags. 
I fixed this simply by removing the buttons and adding the lasses btn and regular-btn to my anchor tags.