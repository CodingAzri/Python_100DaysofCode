Learned how to apply multiple APIs in a program to fetch data based on specific conditions.

Implemented the following steps:

1. Checked if the stock price increased/decreased by 5% between yesterday and the day before yesterday.
2. Retrieved yesterday's closing stock price.
3. Obtained the day before yesterday's closing stock price.
4. Calculated the positive difference between steps 2 and 3.
5. Determined the percentage difference in price between closing prices of yesterday and the day before yesterday.
6. If the difference calculated in step 4 was larger than 5%, the program fetched news.
7. Instead of printing "Get News", the program got the first 3 news pieces for the COMPANY_NAME.
8. Used the News API to get articles related to the COMPANY_NAME.
9. Utilized Python slice operator to create a list containing the first 3 articles.
10. Created a new list of the first 3 article's headlines and descriptions using list comprehension.
