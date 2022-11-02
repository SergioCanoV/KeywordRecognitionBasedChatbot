<h1>Keyword Recognition Based Chatbot</h1>

<h2>Description</h2>
Project consists of a simple chatbot that learns from a text file to answer questions about the movie "Lord of the Rings: The Fellowship of the Ring".  The text was obtained semi-automatically with web scraping and manually organizing some of the text.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>NLTK</b>
- <b>BeautifulSoup</b>
- <b>Sklearn</b>

<h2>Environments Used </h2>

- <b>Windows 11</b>

<h2>Program walk-through:</h2>

<p align="center">
Obtaining the information of the movie <br/>
<img src="https://i.imgur.com/Hd8NMRc.png" height="80%" width="80%" alt="Keyword Recognition Based Chatbot"/>
<br />
<br />
Cleaning the data and storing it in a .txt file:  <br/>
<img src="https://i.imgur.com/vpojNGH.png" height="80%" width="80%" alt="Keyword Recognition Based Chatbot"/>
<br />
<br />
Opening the .txt created, calling the stopwords and defining tokenizers: <br/>
<img src="https://i.imgur.com/wETGrDW.png" height="80%" width="80%" alt="Keyword Recognition Based Chatbot"/>
<br />
<br />
Creating function for preprocessing the text:  <br/>
<img src="https://i.imgur.com/1rCQrcU.png" height="80%" width="80%" alt="Keyword Recognition Based Chatbot"/>
<br />
<br />
Create the greetings function:  <br/>
<img src="https://i.imgur.com/s3BUS1e.png" height="80%" width="80%" alt="Keyword Recognition Based Chatbot"/>
<br />
<br />
Create response function with TfidVectorizer considering that the .txt file is long  <br/>
<img src="https://i.imgur.com/5TpiJUd.png" height="80%" width="80%" alt="Keyword Recognition Based Chatbot"/>
<br />
<br />
Execution class to run the code:  <br/>
<img src="https://i.imgur.com/TeU6iBp.png" height="80%" width="80%" alt="Keyword Recognition Based Chatbot"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
