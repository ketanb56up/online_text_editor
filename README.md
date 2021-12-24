# Text Editor

## Problem:

I have a follow up quiz. Imagine that every time a user uses our service we collect their JS fingerprint. For each user we will have several fingerprints (e.g. one one for when he connects from the browser on his desktop computer, another one from when he connects from the phone, etc). Now imagine we store the fingerprint in a dictionary like this:

```
USERS = {

  'user_1': [fp11, fp12, ...] # List of all fingerprints for user_1

  'user_2': [fp21, fp22, ...] # List of all fingerprints for user_2

  ....

  'user_n': [fpn1, fpn2, ...] # List of all fingerprint for user_n

}
```

We are not blocking users if we detect the same fingerprint is used from different accounts. However, I would like to have a Python function that given an username finds all the accounts opened by the same person.


def find_related_accounts(username: str) -> List[str]


Could you write the pseudocode or Python code (better) for this search? 


## Solution:
I have crated new URL for search user using username to finds all the accounts opened by the same person.
here is the link to test it,
please enter username at the end points of the below url to get the list of accounts opened by the same person.

```
localhost:8000/account/user_list/<username>
```

please check the code at **account/views.py**

```
class UsersByUsername(View):
    """
    UsersByUsername:
        Get User list username and its fingerprint
        :param username
    """

    def get(self, request, username):
        user = User.objects.filter(username=username)
        user_list = (
            User.objects.filter(user_agent=user.first().user_agent) if user else None
        )
        if user_list:
            return render(
                request, "account/all_user.html", context={"users": user_list}
            )
        else:
            return redirect("/")

```


## Configurations 


  It is best to use the python virtualenv tool to build locally:

  ```
  $ virtualenv-2.7 venv
  $ source venv/bin/activate
  $ mkdir Text Editor                  # for creating driectory
  $ cd text_editor                     # get in directory 
  $ git clone https://github.com/ketanb56up/Text Editor.git   
  $ pip3 install -r requirements.txt
  $ python manage.py runserver

  ```
  Then visit http://localhost:8000 to view the app. 


## requirements.txt 

```
     pip3 install -r requirments.txt
```

## FingerPrintJs Token in settings
  
  To configure the FingerPrintJS token in settings as variable `settings.py` file 
  ```  
  # FingerPrintJS Browser Token
  FINGER_PRINT_JS = '<BrowserID>' 
  ```

## Application Code

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
    localhost:8000//account/register   # for signup      
    localhost:8000/account/user_list/<username>   # for userlist with same fingerprint     
  ```