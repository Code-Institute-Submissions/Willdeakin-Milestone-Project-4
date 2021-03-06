# Milestone-Project-4
My last Code Institute milestone project concerning Django Frameworks

The full link is available [here](https://milestone-project-4-willdeakin.herokuapp.com/) and the full url is https://milestone-project-4-willdeakin.herokuapp.com/

## Purpose of the website

### Who is this website for?
This is a website for people wanting to buy equipment for their home gym. 
It should be user friendly such that the customer can easily access the products available and the website owner can add/edit these products easily also.

### What does it do?
The website owner can add products in the store view for purchase using stripe payments. 
The purchasing experience follows a standard format of adding to bag, going to checkout from the bag and checking out with delivery details and stripe payments.

## User Experience Design

## UX 5 Planes

### Strategy Plane
The goal of the website is to create a fully functional e-commerce application using Django Frameworks. 
Users can register, log in and add delivery information to their
profiles to expedite the checkout process.
The blog app adds functionality to the application, as in the blog app customers can interact further with the store, receiving tips for fitness and exercise. 
The comment section in the blog app allows for the community to interact further, commenting on how these blogs have helped them in their fitness journeys.

### Scope Plane
Here is the list of required features and functions. CRUD (Create, Read, Update, and Delete) functions are implemented in the store view for owners product management.

- A simple and effective landing page with multiple call-to-action buttons.
- The store app shows all the available products, shown in an easy to follow and appealing manner.
- A search bar is available for the user and store owner to find a particular product
- Sorting buttons under the search bar are available and helpful for the user sort the products by their criteria.
- A bag app is created for the user to see what they've added to their shopping bag and adjust the quantity of any products.
- Register and login pages are available in the navbar for the customer to keep a profile.
- A product management page is a more accessible alternative for the site owner adding, deleting or editing products than in the admin view.
- The profile app saves users delivery details to expedite the checkout process and keeps a history of the customer's previous purchases.
### Structure Plane

#### Header and navigation
The Navbar is consistent through the whole website and consists of:

- A nav button which opens access to all nav elements, which is on the left of the navbar.
- The bag icon and total on the right of the navbar, which is a link to the bag app.
- The navbar itself opens on the left of the page and is the full height of the screen.
- The home button which is a link to the home app/ landing page.
- A store button, which is a link to the store app with no sorting.
- A register and a login button, both of which are links to the register and login pages respectively and allow the user to log in to the website.
- A logout button which is a link to the profile app and is only available to users who are logged in to an account.
- A profile button which is a link to the profile app.
- A blog button which is a link to the blog app.

#### Search and Sorting
Below the navbar in some apps is a section which contains a searchbar and sort buttons. 

#### Landing Page

Landing page consists of the navbar and three sections, two of which contain a call-to-action button which redirect the user to either the blog or store app.
The page is split into three columns which are responsive and on large screens can all be seen at once; a carousel with images, a short section explaining the blog app functionality and a featured product from the store app.

#### Store page

This page features all products in the store.
Each product is represented with an image, category, name, price and product details button.
By clicking the image or product details button user is redirected to the product detail page.
When logged in as an admin, there is also a button redirecting to the add products page and each product also has a button which redirects to the edit products page.

#### Product Detail Page

This page is headed by the product name and split into two main parts.
On the left is an image of the product, larger than shown in the store view.

On the right there is:
- The product price
- A description of the product
- A quantity form with + and - buttons to adjust the quantity added to the bag
- A keep shopping button which redirects user to the store page
- An add to bag button which adds the product and its quantity to the bag

#### Shopping bag page

This page is headed by the word bag and consists mostly of a list of products in the bag. 

Each list row consists of:
- The product image
- The product name 
- The product price
- A quantity form with + and - buttons to adjust the quantity in the bag, with an update button to commit the change
- A remove button to remove the item from the bag
- The product subtotal

Underneath the list of bag products is:
- A bag total
- A keep shopping button which redirects customer to the store app
- A checkout button which redirects user to the checkout app

#### Checkout pages
The checkout Page, this page consists of:
- A form on the left which customer needs to fill in with their delivery details 
- An order summary on the right, containing items from the bag.


Upon clicking the **Complete Order** button, the user is redirected to the checkout success page.

The checkout success page, this page consists of:
- A confirmation message with the order summary.
- Button on the bottom of the page which will redirect the user back to the store.

#### Register/ Login/ Logout Pages
The register page consists of a form in which the user needs to enter their email, username and password to create new account.

The login page consists of a form in which the user needs to type in their username and password and is then redirected to the
home page.

The logout page gives user an option to log out from their account

#### Profile Page
The profile page contains 2 main parts:
- The form on the left which allows the user to add delivery details to expedite the checkout process.
- The order history on the right which allows the user to see their previous purchases

#### Blog Page

The blog page features blog posts displayed as cards showing a short exerpt from the blog and a button to open in its own page. 
each card is formatted as:
- Title
- Name of author and time submitted
- Exerpt
- Read more button

The blog details page features the full blog post with all of its details. 
This page also features the comments section just below.
Each blog comment, similar to the blogs themsselves, show the name of the author and the date and time published.

The comment form consists of 3 mandatory fields and a button:
- Name: for the user to submit their name.
- Email: where the user needs to add an email in the correct format.
- Body: where the user writes their comment.
- Submit button: submits the user's comment.

Administrator of the website needs to approve each one of the comments in the admin view. 
If the comment is not approved it will not be displayed.

### Surface Plane
The website has been designed with an emphasis on the store app.
Throughout the website the colour scheme stays consistent with white, black and 2 accenting shades of green and brown for most elements throughout each app.

#### Typography
I have used Playfair Display from google fonts to style the page headings in brown.


### Skeleton Plane
This website has been designed to be accessible and aesthetic at all screen sizes.

Wireframes are linked here:
- [Home Page](/readme_testing_media/Home.png)
- [Store](/readme_testing_media/Store.png)
- [Profile](/readme_testing_media/Profile.png)
- [Login/ Register](/readme_testing_media/Login_Register.png)
- [Bag](/readme_testing_media/Bag.png)
- [Blog](/readme_testing_media/Blog.png)
- [Checkout](/readme_testing_media/Checkout.png)

The application is similar to the wireframes in all pages. 
The most major difference between the application and wireframes is that the navbar in the application isn't the same, with it displaying on the left of the screen rather than the top in the navbar.
## Features

### Existing features
- Full CRUD functionality 
- Log In, Log Out, Register functions 

- Full **Stripe** integration
- Database querying and sorting all the available products
- Fully functional Blog section with enabled but supervised user comments

### Features left for future implementation
- Adding more images for the same product
- more social features for the blogs section
- Membership/ subscription model for discounted products etc.
- Wishlist for customers


## Technologies used

* [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
* [CSS3](https://en.wikipedia.org/wiki/CSS) for style
* [Python](https://www.python.org/) for backend development
* [Django](https://www.djangoproject.com/) for frameworks
* [PostgreSQL](https://www.postgresql.org//) as the database for the website
* [Git](https://git-scm.com/) for version control
* [GitHub](https://github.com/) as a remote repository
* [Bootstrap](https://getbootstrap.com/) for main frame and styling
* [JavaScript](https://www.javascript.com/) For functionality of some parts of website
* [Heroku](https://www.heroku.com/) For deployment of the website
* [Coolors](https://coolors.co/) For help creating a colour scheme

## Resources


* [My Fitness Pal](https://blog.myfitnesspal.com/) for blogs posted in the blog view
* [pixabay](https://pixabay.com/) for images with free license
* [Argos](https://www.argos.co.uk/) for products and product images used in the store view
* [musclesquad](https://musclesquad.com/) for products and product images used in the store view
* [bulk](https://www.bulk.com/uk/) for products and product images used in the store view
* [myprotein](https://www.myprotein.com/) for products and product images used in the store view
* [gravity fitness ](https://www.gravityfitness.co.uk/shop/) for products and product images used in the store view
* [Code Institute](https://codeinstitute.net/) course materials
* [Stackoverflow](https://stackoverflow.com/) general help and pointers
* [Youtube](https://www.youtube.com/) general help and pointers
* [W3schools](https://www.w3schools.com/) general help and pointers
* [Am I Responsive](http://ami.responsivedesign.is/) for a responsive image in Read Me
* [Google](https://www.google.ie/) general help
* [DJANGOCENTRAL](https://djangocentral.com/) for help with blog application
* [Google Fonts](https://fonts.google.com/) for the font used throughout the website
* [Font Awesome](https://fontawesome.com/) for icons
* [Stripe](https://stripe.com/ie) for help with payments integration
* [AmazonWebServices-AWS](https://aws.amazon.com/) for hosting static and media files

## Testing
Testing has been documented in [Testing.md](/Testing.md)

## Version Control

### Git and GitHub

I used [GitHub](https://github.com/) as a remote repository and development environment. To produce this project with version control I:

* Created a new repository on GitHub named Milestone-Project-4
* Git add .; to add all files to the staging area
* Git commit -m "*message detailing the changes from the last version*"; to commit changes from the staging area to the local repository
* Git push; to push committed changes from the local repository to the Github repository
* Work is now committed to the master branch

## Deployment

This project requires back-end technologies, so for the deployment I used [Heroku](https://www.heroku.com/), a cloud platform where users can host their projects.
For the purpose of this project the free version was suitable. A PostgreSQL database was selected from free Heroku addons. 
For hosting of static files and media files I used an AWS S3 bucket on a free plan.
During most of development, all media and static files were stored in the github repository and the database used was the sqlite3 database which is installed with django.

Heroku setup:
- I created a new app by clicking on *New* and then *Create new app*
- I named the new app milestone-project-4-willdeakin and chose the region europe
- Provision PostgreSQL database from heroku add-ons

Steps I took before deployment:

- I connected my the PostgreSQL database by changing the DEFAULT_DATABASE in my settings to DATABASE_URL and setting the environment variable in Heroku to the PostgreSQL URL
- I imported the database fixtures by creating a file db.json with all the information in, which I then moved across using python3 manage.py loaddata
- I Installed gunicorn via pip3 install, allowing it to act as a webserver
- I froze all requirements using pip2 freeze > requirements.txt so that Heroku could load all dependencies upon deployment
- I created a Procfile such that Heroku knows the necessary details to deploy correctly
- I disabled collectstatic so no static files were added, as these are going in the AWS S3 bucket.
- I added the host name of my Heroku app to settings.py

Before enabling automatic deploys, I had to set Config Vars in settings for the database URL, stipe keys etc.
After adding all the necessary Config Vars, I enabled automatic deploys such that every subsequent push in my linked GitHub would push to Heroku also.
- Every time the app deploys, this is seen in the Activity tab.



## Database
During the development **sqlite3** database was used which is installed with **Django**.

All databases were created by adding to the models.py file in their respective apps then using CLI to make migrations and migrate.

For deployment(production), a PostgreSQL database is provided by Heroku as an add-on.

Fixtures for the products are taken from the **Code Institute** course material and altered
to better fit this project. 



## Credits

Code for the navbar, as stated in style.css, is adapted from a youtube [tutorial](https://youtu.be/HbBMp6yUXO0), opting to use the mobile/ left nav.

Thanks to my mentor Spencer for his help and advice throughout

