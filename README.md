# Leonardo

[Link to Devpost](https://devpost.com/software/stonks-6pb8u0)

## Inspiration
One of our team members had just started university. Although coursework and the novel social environment were challenging, what he found most difficult was the transition from a life financially dependent on his parents to one more financially independent, especially concerning shopping. While he did ask his friends about the best places to shop, he was concerned that many of their recommendations were not useful for him due to their different spending patterns. Furthermore, he also found it extremely difficult to decide where to spend most of his money as there was no way to experiment with different spending strategies.

His difficulties in transitioning into a more independent lifestyle are certainly shared among many university students who are transitioning as well. We thought that there should be a tool available for students to find better places to shop and experiment with better spending strategies using their personalized data combined with other customer data with similar spending patterns.

## What it does
To help students transition into independent adulthood, we created a web app where users can input their yearly income, the recommendation types they would like to receive (Food and Dining, Auto and Transport, Entertainment, Home, Shopping, Health and Fitness), and their unique spending strategies based on their priorities. Lastly, they can also input a location to find recommendations within five kilometres

We built a custom Euclidean-based similarity algorithm to identify TD virtual users from the Da Vinci API that have extremely similar spending patterns and priorities. Using this algorithm, we then computed five recommendations, which were displayed on Google Maps for the user to discover nearby locations of business that accommodate their spending strategies.

## How we built it
We used Flask, Jinja, and the Google Maps API to construct the front end and to integrate code from several parts of the project. RESTful API Python scripts were also constructed to scrape 273,000 transactions from the TD Da Vinci API. Lastly, we used NumPy to construct and optimize our algorithm. 

## Challenges we ran into
There were several pressing challenges, but through our resilience and willingness to learn we found our way past them. The first big one was getting the Google Maps API to work in our environment. Since most of our work was done in Python and Google Maps was in JavaScript, we had to learn some new technologies, such as Postman in order to ensure seamless compatibility. 

Another challenge was scraping data from the Da Vinci API and storing it in a usable format. Since none of our team members had experience in this area of data engineering, this was a big obstacle that we managed to overcome. 

We also had to deal with the limited functionality of Flask in making components in our forms displayed on our web app.  

## Accomplishments that we're proud of
We're proud that we integrated several different technologies and languages together and managed to retrieve hundreds of thousands of data points to create a robust recommendation model. Moreover, we’re proud of creating of a custom recommendation algorithm optimized for customer transaction data.  

## What we learned
Given that we're all relatively new to the world of financial APIs and recommendation algorithms, we learned a lot about:
•	How to integrate RESTful principles in pulling and posting data 
•	Scraping financial data into a usable form for algorithms
•	Flask web development
•	Creating a data-efficient recommendation algorithm 

## What's next for Leonardo
We would like to develop Leonardo further with the following additions:
* More granular control over the type of establishment recommended by the algorithm
* Scrape more data points from Da Vinci
* Incorporate cloud computing for more efficient data processing
