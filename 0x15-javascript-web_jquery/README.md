## 0x15. Javascript - Web JQuery

**What you should learn from this project**

       At the end of this project you are expected to be able to explain to
       anyone, without the help of Google:

* Why jQuery make front-end programming so easy (don’t forget to tweet today,
  with the hashtag #ilovejquery :))
* How to select HTML elements in Javascript
* How to select HTML elements with jQuery
* What are differences between ID, class and tag name selectors
* How to modify an HTML element style
* How to get and update an HTML element content
* How to modify the DOM
* How to make a GET request with jQuery Ajax
* How to make a POST request with jQuery Ajax
* How to listen/bind to DOM events
* How to listen/bind to user events

**Import jQuery**

	 <head>
	     <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    	 </head>


**0. No jQuery**

     Write a Javascript script that updates the text color of the HTML tag
     `HEADER` to red (`#FF0000`):

* You must use `document.querySelector` to select the HTML tag
* You can’t use the jQuery API

**1. With jQuery**

     Write a Javascript script that updates the text color of the HTML tag
     HEADER to red (#FF0000):

* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

**2. Click and turn red**

     Write a Javascript script that updates the text color of the HTML tag
     HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:

* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

**3. Add `.red` class**

     Write a Javascript script that adds the class red to the HTML tag
     HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:

* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

**4. Toggle classes**

     Write a Javascript script that toggles the class of the HTML tag
     HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_header:

* The HEADER tag must always have one class: red or green, never both in the
  same time, never empty.
* If the current class is red, when the user click on DIV#toggle_header, the
  class must be updated to green ; and the reverse.
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

**5. List of elements**

     Write a Javascript script that adds a LI element to a list when the user
     clicks on the tag DIV#add_item:

* The new element must be: <li>Item</li>
* The new element must be added to UL.my_list
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API