TECHNOLOGIES USED:
    Python, Postgres, Django, VS Code, Postman

ABOUT THE PROJECT:

    -- The database name is 'think_bridge' and the table name is 'shop_bridge_inventory'
    -- The table is created via migrations in Django model
    -- The table fields are : name, price, description, image
    -- The table is exported to db.csv file in the same project root directory
    -- The images are saved in the media/images directory of project 
    -- The address of image is saved in table
    -- The app is 'shop_bridge' in 'think_bridge_test' project
    -- The app consists of two pages, one to show the list of inventories and one to show the detail of one selected inventory
    -- In the views, there are 4 apis namely:

        1. list_inventory ['GET'] => To get the list of the inventories in the table
        2. show_inventory ['GET'] => To show detail of one inventory when id given
        3. add_inventory ['POST'] => To add new inventory
        4. delete_inventory ['POST'] => To remove the inventory when id given

    -- The static folder consists of static files (css, js, fonts)
    -- Templates folder consists the html template for two pages
    -- tests folder has the test cases 
    -- pytest and cov is used for testing/coverage


TO RUN THE APPLICATION:
    -- In terminal, run "python manage.py runserver"
    -- Open the url in the browser "http://127.0.0.1:8000/inventory" 
    -- The first page will have all the inventories with their images, with the remove button for each to remove/delete the selected inventory, and a button on top to add new inventory
    -- The second page will be opened when clicked on any inventory in first page, that will show the detail/description of the inventory


