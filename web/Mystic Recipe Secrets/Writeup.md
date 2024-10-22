### Challenge title: Mystic Recipe Secrets

#### Points: 125-100

#### Flag:

```
 |  BUETCTF{$p3llb00k_of_3nchan73d_c00kies_82ded45e3}
```

#### Author: 
##### [C0d3HuNt3r](https://github.com/Shehabul-Islam-Sawraz)

### Challenge Description

---

The Guild of Culinary Magic entrusted me with their ancient recipe scrolls, and I’ve set up a magical portal for safe access. You can browse the spells (or recipes), and even add new ones if you're worthy. It's all sealed with powerful magic... or is it?

***Hint:*** 
- Search through all the enchanted scripts carefully
- Magical cookies can be altered, but don’t underestimate their simplicity

### Solution of Mystic Recipe Secrets

---

- The starting point is `index.html` or Home Page
  
- If we click on the 3 bar menu on the right we can see three pages: `Sorcerer's Portal`, `Arcane Cupcakes`, `Mystic Brownies`

- Going to the `Sorcerer's Portal`, we can see it's actually a login page
  
- If we check the URL path carefully, we can see we are on `adminLogin.html` page
 
- It refers that we want to login as the admin (as it was in the name of the link)
  
- However, the **username** field is already filled in as `Guest`
  
  - So, we can use the Browser DevTools: Inspect > modify the value of the **username** to **`admin`**
 
  - Going to the `Sources` tab under Devtools, we can find an `adminLogin.js` file
 
- In the JS file, we see that **`processLogin()`** takes our password and encodes it using **`encodePassword()`**, before putting it in as a cookie
 
- The function **`encodePassword()`** takes the character code of each character in our password and adds the letter `"b"` as a delimiter
 
- For now, we don't know what the password is, so let's put in something arbitrary, like `admin`
 
- Hitting enter, and we are taken to `adminEditor.html`
    - The page is blank, so we open DevTools again
    - As we can see, the DOM is basically empty, but we now have a new script tag - `editor.js` 
    - A single if statement checks if our cookie matches a very long string (clearly encoded by `encodePassword()`)
    - If so, it redirects us to `flag.html` 

- Naigating to `flag.html` from URL, we see that we have been deceived
    - However, upon inspecting the source, we see a handy  **`decodeDelight()`** function
    - This decodes and outputs the cookie `hiddenRecipe` which is currently an incorrect value  
    - Let's navigate back to adminEditor.html
    - Here, we can find that super long string and set it as our `hiddenRecipe` cookie
- Navigating back to `flag.html` and ***we see the flag***!!
- In other way, the flag can also be retrieved by replacing all the `b` with blank space, from the long string that we had got in `editor.js` and convert them from ASCII to text.
