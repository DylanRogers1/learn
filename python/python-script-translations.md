# Chapter 1: Hello World

## English

Hi, welcome to The Open Project! In this video, we'll be going through the very basics of Python. We'll create a python program that prints "Hello world" to the console!

First, I want to really quickly discuss the document in front of me at the moment. Just so I don't babble on about the same thing for half an hour, I made a little document to go along with this tutorial. If you'd like to have a look at it, I'll leave a link to my GitHub page in the description, so you can have a look for yourself! Also, if you're a content creator, feel free to use this file to help you make your own Python tutorial - which you may find useful as you don't have to create 100% of the content yourself! Have a look at the document, it explains it all there.

I've also wrote a script for this tutorial, so feel free to read through that if you prefer reading articles to watching videos. The script will be on my GitHub, alongside the Python document, so you should be able to follow along if it helps. I also added custom subtitles to the video in lots of different languages, so check that out if you like subtitles! Anyway, I'm going on at this point, so let's get coding.

The first thing we want to do is to install Python. I'll leave a link in the description to download it. If you use Linux like me, just use your package manager to install `python3`. On Windows or MacOS, download the latest version at https://python.org. Once Python is installed, create a new Python file. A Python file has the `.py` extension. In my program, I'll create the `hello.py` file. Open this file in a text editor of your choice - VS Code, an IDE or just IDLE, the built in Python IDE.

Great - now the boring stuff is out the way, it's time to start programming! Inside `hello.py` (or whatever your Python file is called) copy the following code:

`print("Hello world")`

We can then run our code using the terminal. Open a new terminal and navigate to the folder containing the Python program. Once inside that folder, use the `python3` command to execute our code. In my case, I would type `python3 hello.py`. Note that on some devices - particularly Windows computers - `python3` is installed as `python` or `py`. Try all three commands and use the one that works! When we run our code, we get `Hello world` printed to the console!

Now we've successfully written and executed our code, let's explain what it all means. 

First we start by calling the `print` function. A function is basically a block / group of code that executes when we call it. In our case, when we call the `print` function, Python prints some text to the screen. We can call a function using by adding a pair of brackets `()` to the end of a function name. In our case, we call the `print` function by typing `print()`.

Inside these brackets we can add data, known as arguments. In our program, we pass "Hello world" as an argument. "Hello world" is what we call a string, which is basically just text. When we call `print`, it will print the given text to the console (terminal).

## Hindi

हाय, ओपन प्रोजेक्ट में आपका स्वागत है! इस वीडियो में, हम Python के मूल सिद्धांतों के बारे में जानेंगे। हम एक अजगर प्रोग्राम बनाएंगे जो कंसोल पर "हैलो वर्ल्ड" प्रिंट करता है!

सबसे पहले, मैं इस समय मेरे सामने दस्तावेज़ पर वास्तव में जल्दी से चर्चा करना चाहता हूं। बस इसलिए कि मैं आधे घंटे तक एक ही चीज़ के बारे में बात नहीं करता, मैंने इस ट्यूटोरियल के साथ जाने के लिए एक छोटा दस्तावेज़ बनाया। यदि आप इसे देखना चाहते हैं, तो मैं विवरण में अपने GitHub पृष्ठ का लिंक छोड़ दूँगा, ताकि आप स्वयं इसे देख सकें! इसके अलावा, यदि आप एक सामग्री निर्माता हैं, तो बेझिझक इस फ़ाइल का उपयोग अपने स्वयं के पायथन ट्यूटोरियल बनाने में मदद करने के लिए करें - जो आपको उपयोगी लग सकता है क्योंकि आपको स्वयं 100% सामग्री बनाने की आवश्यकता नहीं है! दस्तावेज़ पर एक नज़र डालें, यह वहां सब कुछ समझाता है।

मैंने इस ट्यूटोरियल के लिए एक स्क्रिप्ट भी लिखी है, इसलिए यदि आप वीडियो देखने के बजाय लेख पढ़ना पसंद करते हैं तो बेझिझक इसे पढ़ें। स्क्रिप्ट मेरे गिटहब पर, पायथन दस्तावेज़ के साथ होगी, इसलिए यदि यह मदद करता है तो आपको इसका पालन करने में सक्षम होना चाहिए। मैंने कई अलग-अलग भाषाओं में वीडियो में कस्टम उपशीर्षक भी जोड़े हैं, इसलिए देखें कि क्या आपको उपशीर्षक पसंद हैं! वैसे भी, मैं इस बिंदु पर जा रहा हूँ, तो चलिए कोडिंग करते हैं।

पहली चीज जो हम करना चाहते हैं वह है पायथन को स्थापित करना। मैं इसे डाउनलोड करने के लिए विवरण में एक लिंक छोड़ दूँगा। यदि आप मेरी तरह लिनक्स का उपयोग करते हैं, तो `python3` को स्थापित करने के लिए अपने पैकेज मैनेजर का उपयोग करें। Windows या MacOS पर, https://python.org से नवीनतम संस्करण डाउनलोड करें। एक बार पायथन स्थापित हो जाने के बाद, एक नई पायथन फ़ाइल बनाएँ। एक पायथन फ़ाइल में `.py` एक्सटेंशन होता है। अपने प्रोग्राम में, मैं `hello.py` फ़ाइल बनाऊँगा। इस फाइल को अपनी पसंद के टेक्स्ट एडिटर में खोलें - वीएस कोड, एक आईडीई या सिर्फ आईडीएलई, बिल्ट इन पायथन आईडीई।

बढ़िया - अब उबाऊ चीजें बाहर हो गई हैं, प्रोग्रामिंग शुरू करने का समय आ गया है! `Hello.py` के अंदर (या जो भी आपकी पायथन फ़ाइल कहलाती है) निम्नलिखित कोड की प्रतिलिपि बनाएँ:

`प्रिंट ("हैलो वर्ल्ड")`

फिर हम टर्मिनल का उपयोग करके अपना कोड चला सकते हैं। एक नया टर्मिनल खोलें और पायथन प्रोग्राम वाले फ़ोल्डर में नेविगेट करें। एक बार उस फ़ोल्डर के अंदर, हमारे कोड को निष्पादित करने के लिए `python3` कमांड का उपयोग करें। मेरे मामले में, मैं `python3 hello.py` टाइप करूंगा। ध्यान दें कि कुछ उपकरणों पर - विशेष रूप से विंडोज कंप्यूटर - `python3` को `python` या `py` के रूप में स्थापित किया गया है। सभी तीन आदेशों का प्रयास करें और जो काम करता है उसका उपयोग करें! जब हम अपना कोड चलाते हैं, तो हमें कंसोल पर 'हैलो वर्ल्ड' प्रिंट मिलता है!

अब हमने अपने कोड को सफलतापूर्वक लिख और निष्पादित कर लिया है, आइए बताते हैं कि इसका क्या अर्थ है।

सबसे पहले हम `प्रिंट` फ़ंक्शन को कॉल करके प्रारंभ करते हैं। एक फ़ंक्शन मूल रूप से कोड का एक ब्लॉक / समूह होता है जिसे हम कॉल करते समय निष्पादित करते हैं। हमारे मामले में, जब हम `प्रिंट` फ़ंक्शन कहते हैं, तो पायथन स्क्रीन पर कुछ टेक्स्ट प्रिंट करता है। हम फ़ंक्शन नाम के अंत में कोष्ठक `()` की एक जोड़ी जोड़कर फ़ंक्शन को कॉल कर सकते हैं। हमारे मामले में, हम `प्रिंट ()` टाइप करके `प्रिंट` फ़ंक्शन को कॉल करते हैं।

इन कोष्ठकों के अंदर हम डेटा जोड़ सकते हैं, जिसे तर्क के रूप में जाना जाता है। हमारे कार्यक्रम में, हम "हैलो वर्ल्ड" को एक तर्क के रूप में पास करते हैं। "हैलो वर्ल्ड" वह है जिसे हम एक स्ट्रिंग कहते हैं, जो मूल रूप से सिर्फ टेक्स्ट है। जब हम `प्रिंट` कहते हैं, तो यह दिए गए टेक्स्ट को कंसोल (टर्मिनल) पर प्रिंट करेगा।

## Dutch

Hallo, welkom bij The Open Project! In deze video gaan we door de basisprincipes van Python. We zullen een python-programma maken dat "Hallo wereld" naar de console afdrukt!

Ten eerste wil ik heel snel het document bespreken dat op dit moment voor me ligt. Om te voorkomen dat ik een half uur lang over hetzelfde blijf babbelen, heb ik een klein document gemaakt dat bij deze tutorial hoort. Als je het wilt bekijken, laat ik een link naar mijn GitHub-pagina achter in de beschrijving, zodat je het zelf kunt bekijken! Als je een maker van inhoud bent, voel je vrij om dit bestand te gebruiken om je te helpen bij het maken van je eigen Python-zelfstudie - wat misschien handig is omdat je niet 100% van de inhoud zelf hoeft te maken! Bekijk het document eens, daar wordt het allemaal uitgelegd.

Ik heb ook een script voor deze tutorial geschreven, dus lees dat gerust door als je liever artikelen leest dan video's bekijkt. Het script zal op mijn GitHub staan, naast het Python-document, dus je zou het moeten kunnen volgen als het helpt. Ik heb ook aangepaste ondertitels aan de video toegevoegd in veel verschillende talen, dus kijk daar eens naar als je van ondertitels houdt! Hoe dan ook, ik ga door op dit punt, dus laten we beginnen met coderen.

Het eerste dat we willen doen, is Python installeren. Ik laat een link achter in de beschrijving om het te downloaden. Als je Linux gebruikt zoals ik, gebruik dan gewoon je pakketbeheerder om `python3` te installeren. Download op Windows of MacOS de nieuwste versie op https://python.org. Nadat Python is geïnstalleerd, maakt u een nieuw Python-bestand. Een Python-bestand heeft de extensie `.py`. In mijn programma maak ik het `hello.py`-bestand. Open dit bestand in een teksteditor naar keuze - VS Code, een IDE of gewoon IDLE, de ingebouwde Python IDE.

Geweldig - nu zijn de saaie dingen uit de weg, het is tijd om te beginnen met programmeren! Kopieer in `hello.py` (of hoe je Python-bestand ook heet) de volgende code:

`print("Hallo wereld")`

We kunnen dan onze code uitvoeren met behulp van de terminal. Open een nieuwe terminal en navigeer naar de map met het Python-programma. Gebruik in die map de opdracht `python3` om onze code uit te voeren. In mijn geval zou ik `python3 hello.py` typen. Merk op dat op sommige apparaten - met name Windows-computers - `python3` is geïnstalleerd als `python` of `py`. Probeer alle drie de commando's en gebruik degene die werkt! Wanneer we onze code uitvoeren, krijgen we 'Hallo wereld' afgedrukt op de console!

Nu we onze code met succes hebben geschreven en uitgevoerd, laten we uitleggen wat het allemaal betekent.

Eerst beginnen we met het aanroepen van de functie `print`. Een functie is in feite een codeblok/groep die wordt uitgevoerd wanneer we deze aanroepen. In ons geval, wanneer we de functie `print` aanroepen, drukt Python wat tekst af op het scherm. We kunnen een functie aanroepen met behulp van een paar haakjes `()` aan het einde van een functienaam. In ons geval roepen we de functie `print` aan door `print()` te typen.

Binnen deze haakjes kunnen we gegevens toevoegen, ook wel argumenten genoemd. In ons programma geven we "Hallo wereld" door als argument. "Hallo wereld" is wat we een string noemen, wat eigenlijk gewoon tekst is. Wanneer we `print` aanroepen, zal het de gegeven tekst naar de console (terminal) printen.