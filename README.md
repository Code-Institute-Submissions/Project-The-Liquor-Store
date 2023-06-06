# Introduction

The Liquor Store Web Application is a Flask-based web application that allows customers to conveniently browse and order a wide variety of liquor products. This application provides a user-friendly interface for customers to explore different categories of alcoholic beverages, select their preferred items, specify quantities, and provide essential contact and delivery information for a seamless ordering experience.

## Screenshot in Am I Responsive

![image](https://github.com/Imalsha0330/Project-The-Liquor-Store/assets/131761126/7264176c-a73d-466e-9eea-8dc3808b19f2)

## Features

![image](https://github.com/Imalsha0330/Project-The-Liquor-Store/assets/131761126/60efb91b-24c2-47e4-8a93-dcfcbca2abd7)

User-Friendly Menu: The application presents customers with an intuitive menu that categorizes liquor products into distinct sections such as hard liquor, red wine, white wine, and beer. Customers can easily browse through the available options within each category.

![image](https://github.com/Imalsha0330/Project-The-Liquor-Store/assets/131761126/29b17623-8b5b-4d6d-891c-e37e81b48c6f)

* Order Placement: Customers can select their desired item from the menu and specify the quantity they wish to order. The application calculates the total cost based on the selected item's price and quantity.
* Customer Information: Customers are required to provide their name, phone number, and address for delivery purposes. This information is securely stored and used to process and fulfill the orders.

![image](https://github.com/Imalsha0330/Project-The-Liquor-Store/assets/131761126/7631bc75-7638-45a1-a760-044d9f5e68a5)

Order Confirmation: After placing an order, customers receive an order confirmation with the details of their order, including the item name, quantity, and total cost. The confirmation also informs customers that their ID is being verified and assures them of prompt communication once the verification process is complete.

# Testing
* Tested on Google Chrome
* Tested on Internet Explore
* Tested Many options to get a correct value
* All the input bars are checked.
* Place order button and reset button checked.
* Checked the console for Errors.
* Checked on the WAVE and no Major Errors. 
* Checked the project in different sizes (320 - 1920) Screenshots below. 
![image](https://github.com/Imalsha0330/Project-The-Liquor-Store/assets/131761126/074ba7d8-2d5f-44ab-8ea5-d803fa05a7b3)
* 320
![image](https://github.com/Imalsha0330/Project-The-Liquor-Store/assets/131761126/eb3ad370-556c-47e1-a5ef-6d312cde0880)
* 1920

# Bugs founded.
* When calculating the total cost of an order, the application was not taking into account the quantity specified by the customer. As a result, the total displayed in the order confirmation was incorrect, showing only the base price of the selected item.
* I faced some difficulties with the CSS styling of the Liquor Store application. The styling was not appearing as intended, resulting in inconsistencies in the look and layout of the web pages. Text alignment, colors, and spacing needed adjustments to enhance the overall user experience.

## Bug Correction Summary
* To fix this bug, I modified the `calculate_total` function in the Flask application's code. I added a new parameter to the function, `quantity`, which represents the quantity selected by the customer. I then multiplied the price by the quantity to calculate the correct total.
* Created a new CSS file called style.css in the /static/CSS/ directory. Incorporated appropriate CSS rules and selectors into the style.css file to modify the styling elements. Added the style.css file to the /template/ folder of the application.

# Unfixed bugs
* No unfixed bugs.

# Languages Used
* Python 
* HTML
* CSS

# Accessibility in Lighthouse.
 
![image](https://github.com/Imalsha0330/Project-The-Liquor-Store/assets/131761126/e3e13f89-289b-4e28-8953-56fe1ebb85b9)

# Deployment
  
* This site was deployed via Heroku pages using the following steps:

* Created a Heroku account by visiting their website at https://www.heroku.com/.
* Installed the Heroku Command Line Interface (CLI) on my computer.
* Once logged in, clicked the "Create new app" button in the Heroku dashboard.
* Provided a name for my app and the other necessary details during the app creation process.
* After created the app, connected it to my GitHub repository from the Heroku dashboard.
* Selected the specific repository I want to connect to Heroku.
* In the settings section of the Heroku app, update the buildpack to use Python.
* Went back to the "Deploy" page in the Heroku dashboard and followed the instructions to deploy my app.
* After several minutes website will be live.

# Credits
  
 * Chatbot powered by OpenAI for helped to correct coding issues and provided assistance with English language queries.
  

