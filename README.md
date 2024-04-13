# Desafio-TuntsRocks-2024

## Code's Objective:

<p>Calculate the situation of each studant, registred in the Googel WorkSheet, based on the average of the three tests (P1, P2, P3).</p>

## What you need to run the code:

<ul>
  <li><a href='https://www.python.org/downloads/'>Python</a></li>
  <li><a href='https://docs.gspread.org/en/v6.0.0/'>gspread API</a></li>
  <br />Typing on CMD:
  
  ```
  pip install gspread
  ```
  
  <li>Internet access</li>
</ul>

## Running the code:

[how_to_run.webm](https://github.com/KevinFGR/Desafio-TuntsRocks-2024/assets/109561598/6570b0d8-ddb0-42ee-ac7b-c666c1cafa0b)


<ol>
  <li>Check you had installed correctly the Python and gspread</li>
  <li>Clone this repository in your computer</li>
  <br/> Type on your GIT Bash:
  
  ```
    git clone https://github.com/KevinFGR/Desafio-TuntsRocks-2024.git
  ```
  <li>Open your command prompt on the repository cloned</li>
  <li>Type: ...</li>

  ```
  py app.py
  ```
  <li>Wait the progam return the massage: "Worksheet successfully modified"</li>
</ol>

## GoogleSheet's access link:

```
https://docs.google.com/spreadsheets/d/13PW1hgkXhSs-qpwBvibQeXXT_q7cOWcPr3dAaV00k14/edit?usp=sharing
```

## Possible exceptions:
<p>If the code returns you a mensage like this ..</p>

![Error-image](https://github.com/KevinFGR/Desafio-TuntsRocks-2024/assets/109561598/4f967933-c7dc-46e1-80b2-4a1be0a1a1ee)

<p>Means the API exceeded the limit of request per minute. This is not a code problem, it just happens because the Google Cloud needs a paid version for unlimited uses.</p>
<p>When you get this message error you just have to wait some minutes and try again or create your own access to the Google API following this video's steps:</p>

```
https://www.youtube.com/watch?v=FDkknYBBbwQ
```
