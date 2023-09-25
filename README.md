# Call Data Analysis
## It's a work in progress :)
This repository contains a collection of scripts and notebooks for analyzing call data. The call data is collected from a phone using an app named [SMS Backup and Restore](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore) and exported to an XML file. The XML file is then converted to a CSV file using a Jupyter notebook file named "xml_to_csv.ipynb".

Once the call data is in CSV format, it can be analyzed using a variety of tools and techniques. For example, you can use the data to answer the following questions:

* How many calls do I usually take in a day?
* At which time of day do I talk the most?
* Who do I call the most?
* How long do my calls typically last?
* What is the total duration of my calls in a day/week/month?
* This data can also be used to make informed decisions about your mobile plan. For example, if you have taken a 3-month unlimited talktime plan and you talk way less than you pay, you might reconsider after viewing it. Of course the plan also include other things like x data per day and x SMS per day so definitely take the decision based on your needs.

## Privacy

The call data in this repository has been anonymized for privacy reasons. The contact numbers and names have been changed, but the rest of the data is the same.

## How to use

To use this repository, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python libraries.
3. Open the "xml_to_csv.ipynb" notebook file in Jupyter Notebook.
4. Run the notebook to convert the XML file to a CSV file.
5. Open the CSV file in a data analysis tool of your choice and start analyzing your call data.

## Further implementations

This repository can be extended to support additional features, such as:

* Analyzing call data by contact person or group.
* Identifying patterns in call data, such as frequent callers or times of day when you are most likely to be called.
* Predicting future call patterns.
* Integrating with other data sources, such as your calendar or contact list, to provide more insights into your calling habits.

## Contributions

Contributions to this repository are welcome. Please feel free to submit pull requests with new features, bug fixes, or documentation improvements.
