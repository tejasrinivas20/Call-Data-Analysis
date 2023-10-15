# Call Data Analysis

This repository contains a collection of scripts and notebooks for analyzing call data. The call data is collected from a phone using an app named [SMS Backup and Restore](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore) and exported to an XML file. The XML file can be converted to a CSV file using `call_analysis_functions.py` file by `xml_to_csv(xml_filepath,csv_filepath)` function in it.

> The call data in this repository has been anonymized for privacy reasons.

# Sections

- [Introduction](#introduction)
- [How to use](#how-to-use)
- [Further implementations](#further-implementations)
- [Contributions](#contributions)

# Introduction

The time period of the data collected is from April to September. <br>
Once the call data is in CSV format, it can be analyzed using a variety of tools and techniques. For example, you can use the data to answer the following questions:

- ### Number of calls made by month
  ![Image of Calls made by month](./images/calls_made_by_month.png)<br>
  June month has the highest number of calls: **544 calls**
- ### Top 10 callers by Frequency of Calls.
  ![Image of Top 10 Callers by Frequency of Calls](./images/top_10_callers_by_freq.png)<br>
  Mom (understandably) is the highest caller: **604 calls**
- ### Top 10 Callers by Duration
  ![Image of Top 10 Callers by Duration](./images/top_10_callers_by_duration.png)<br>
  Sashank D is the most I've wasted my time on: **81513 seconds**
- ### Time of the day with most calls.
  ![Image of Time of Day with Most Calls](./images/time_of_day_with_most_calls.png)<br>
  I've spent most of my Noon talking: **605 calls**
- Average Duration of Calls.
  ![Average Duration of Calls](./images/avg_dur_of_calls.png)<br>
  My average talktime is **108 seconds** :)
- ### Day of the Week with Most Calls
  ![Image of Day of the Week with Most Calls](./images/day_of_the_week_with_most_callspng.png)<br>
  Monday (understandably, since I have to beg my friends to attend college) is the day I talk the most: **483 calls**
- ### Distribution of Calls by Day of the Week.<br>
  ![Image of Distribution of Calls by Day of the Week](./images/distribution_of_calls_by_day_of_the_week.png)<br>
- This data can also be used to make informed decisions about your mobile plan. For example, if you have purchased an _**x**_ amount unlimited talktime plan and you talk way less than you pay, you might reconsider after viewing it. Of course the plan also include other things like _**x**_ amount of data per day and _**x**_ SMS per day so definitely take the decision based on your needs.
  - For this question, I currently don't know the charge per minute (rupee/min) for my carrier. I've contacted them, so I'll update it when I get a reply from them.

## How to use

To use this repository, follow these steps:

1. Install [SMS Backup and Restore](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore) app on your phone.
1. Go to Settings > Backup Settings > Under Readability section select Readable Date format to `dd/MM/yyyy HH:mm:ss`
2. Backup your call data using the app. The app will create an XML file with the call data.
3. Clone the repository to your local machine.
4. Install the required Python libraries using `pip install pandas matplotlib` 
> _Assuming you have Jupyter installed_.
5. Change the paths in the notebook to the path of the XML file and resultant CSV file.
6. Convert the XML file to CSV file using given function.
7. Run the notebook and see your data.

## Further implementations

This repository can be extended to support additional features, such as:

- Identifying patterns in call data, such as frequent callers or times of day when you are most likely to be called.
- Predicting future call patterns.
- Integrating with other data sources, such as your calendar or contact list, to provide more insights into your calling habits.

## Contributions

Contributions to this repository are welcome. Please feel free to submit pull requests with new features, bug fixes, or documentation improvements.
