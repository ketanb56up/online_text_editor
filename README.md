# online_text_editor

## Configurations 

---

  It is best to use the python virtualenv tool to build locally:

  ```
  $ virtualenv-2.7 venv
  $ source venv/bin/activate
  $ mkdir Text Editor                  # for creating driectory
  $ cd text_editor                     # get in directory 
  $ git clone https://github.com/ketanb56up/online_text_editor.git   
  $ pip3 install -r requirements.txt
  $ python manage.py runserver

  ```
  Then visit http://localhost:8000 to view the app. 


## requirements.txt 

---   
```
     pip3 install -r requirments.txt
```

## FingerPrintJs Token in settings
  
---
  To configure the FingerPrintJS token in settings as variable `settings.py` file 
  ```  
  # FingerPrintJS Browser Token
  FINGER_PRINT_JS = '<BrowserID>' 
  ```

## Application Code

---
 For Backend take a look in `account` directory in project in `models.py` and `views.py` file having all the mechanism 

 in frontend template we are using FingerPrintJs library `template/account/register.html`
 ```
  <script>
function initFingerprintJS() {
  FingerprintJS.load({
        <!-- finger_print_token is custom template tag which is giving the FingerprintJS token-->
        token: "{% finger_print_token %}",
  })
    .then((fp) => fp.get())
    .then((result) => {
        console.log(result.visitorId)
      document.getElementById("id_user_agent").value =
        result.visitorId;
    });
}


</script>
<script async onload="initFingerprintJS()"
        src="https://cdn.jsdelivr.net/npm/@fingerprintjs/fingerprintjs-pro@3/dist/fp.min.js"></script>

 ``` 



## Set up the project 

---
  **migrate** the data in database run command 
  ```
   python3 manage.py migrate   
  ```
  **Createsuperuser** 

  enter the value in terminal as per variable   
  ```
   python3 manage.py createsuperuser 
  ```
  
  **Start the Django's Server**
  ```
   ./manage.py runserver "or"
   python3 manage.py runserver   
  ```
  **Run test cases** 
  ```
   ./manage.py test <app_name>.tests  "or" 
   python3 manage.py test <app_name>.test    
  ```

## Routes
  currently, project having only 2 urls one for admin and other for sighup user 
  
  ```
    localhost:8000/admin      # for admin panel
    localhost:8000   # for signup/register user      
  ```
  
****
