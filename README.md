# FIFAQatar2022-StatsbombFreeEventData
Statsbomb released their free event data from the 'FIFA Qatar World Cup 2022' back in December 2022, and I took this opportunity to apply some of the data analysis skills that i have got to create a report highlighting the top ball progressors in this edition of the world cup, I created this repository to show the techniques used to filter and analyse the event data and visualize the results that were produced.
<br />Check the PDF file of the report here: https://github.com/GoonerMH99/FIFAQatar2022-StatsbombFreeEventData/blob/main/FIFA%20Qatar%20World%20Cup%202022%20Top%20Ball%20Progressors%20Report.pdf

## Table Of Content
* Technologies
* Dataset
* Python Code
* Tableau Figures

## Technologies
* Python 3 (Pycharm).
* Matplotlib, Pandas and Numpy.
* Tableau.
* JSON.

## Dataset
The Dataset source is the Statsbomb free event data that they released for the public and you can access it by downloading the files from this link 'https://github.com/statsbomb/open-data/tree/master/data' or by using the Statsbomb API which enables you to use all the event data files directly into your python code, the event data files are stored in the format of JSON files and it is constructed as shown in the image below in which each event that happens in the game is logged as a JSON containing all the attributes realted to that event, in order to get a better understanding of the attributes related to each event you might want to take a look at this PDF 'https://github.com/statsbomb/open-data/blob/master/doc/StatsBomb%20Open%20Data%20Specification%20v1.1.pdf'.
![image](https://github.com/GoonerMH99/FIFAQatar2022-StatsbombFreeEventData/assets/101012808/9514dd5c-bf3a-4af5-a9b3-16e0f938a2d4)

## Python Code
These image are a snippet from the code that was used to filter out the progressive passes or progressive carries out of all the events that are stored in the JSON files, the location and the end_location attributes were the main attributes used to identify what a progressive pass or carry is.
![GithubCodeSS_1](https://github.com/GoonerMH99/FIFAQatar2022-StatsbombFreeEventData/assets/101012808/c4859cf1-fd3d-4e8f-abaf-2af3855df570)
![GithubCodeSS_2](https://github.com/GoonerMH99/FIFAQatar2022-StatsbombFreeEventData/assets/101012808/7ada9752-58ab-4aff-ae49-cad0d0002843)

This image is a snippet from the code used to create the pitch map and draw the arrows showing the locations of each pass or carry for the selected player.
![GithubCodeSS_3](https://github.com/GoonerMH99/FIFAQatar2022-StatsbombFreeEventData/assets/101012808/629663a1-4743-47f7-97e8-73e3495c0f8f)

## Tableau Figures
Tableau is the data visualization tool used to create the charts of the top player in each category, the top players list was saved as CSV file from the python files that created it and then it was fed uploaded into tableau in order to visualize them by different types of figured or charts.
![Top10PassersOverall](https://github.com/GoonerMH99/FIFAQatar2022-StatsbombFreeEventData/assets/101012808/8417d47d-00bb-42df-893d-ffe1c7701f24)
