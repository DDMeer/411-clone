1. Project Name:  
Chicago Restaurant Recommendation  
   
2. Project summary:  
Provide help to people who are not familiar with Chicago restaurants. By setting different preferences for different types of restaurants, dining times, and locations, users can set different weights for preferences to provide personalized recommendation services. And you can make new friends by searching for users who have the same preferences as you on this website.    

3. Detailed description of the project:  
In daily life, the recommendation service of this web application is usually ranked according to the weight provided by the website, but different people have different views on the waiting time and location. That is to say, a restaurant that needs to wait a long time but the dishes are delicious in the eyes of one person, it may not be worth choosing, but in the eyes of another person, it is very worth looking forward to. This project is to avoid website misrecommendations that make users miss out on restaurants that suit them.  
For people who have the same taste preferences and preferences for choosing restaurants, they are likely to have similar interests and hobbies, which is also one of the prerequisites for two people to become friends. This website matches the relevant information of registered users. If users wish, they can provide their own social account informationn. This allows many people with similar interests and hobbies to get to know each other and become friends, especially when some people feel lonely when enjoying food alone. When you are lonely, this website can solve this problem well.  

4. Uses:  
    Usage description: This website provides restaurant recommendation services for people who live or travel in Chicago, allowing users to define the weights of different aspects of their own restaurants, so as to better match user preferences.
After the user registers an account on the website, he needs to fill in the information in his account. The information that must be filled contains the user’s preferences for various aspects of the restaurant and other data. The user can choose to fill in his social account information, such as facebook and ins, etc., in the user If you are willing, you can choose to make your personal information public and match it with other users, so that you can find users with similar preferences and make more friends.   
    The difference: Similar applications usually rank restaurants with the weights set by the website, while ignoring the needs of users themselves, that is, people with different preferences should rank restaurants differently.Moreover, many websites that provide restaurant reviews ignore the social functions of the website. By providing opportunities for further communication with people with similar hobbies, the attractiveness of the website can be improved.  

5. Realness:   
    The information of restaurants in the Chicago is extracted from the public database provided by yelp to ensure the validity of the information. Yelp is the biggest local business review and social networking site. Most restaurants will publish their informations in Yelp website so that it can attract more customers. Customer can write their review based on their experience.  
    Now, there are more than 200 million reviews and more than 40 million unique visitors in their website.The raw dataset will contain lots of unuseful information. We will explore the dataset and desing an algorithm to preprocess the data so that we can filter useful information.

6. Description of the functionalities:  
    1. Describe what data is stored in the database.
    For the business itself, it include the basic information, such as name, address, city, state, postal code, star rating, open hours and so on. 
    For the users, it include the user id, user name, friends, business id, review text, rating star.
    For the dishes, it include the name, category and pictures.
    2. What are the basic functions of your web application?
    Users can search for their favorite restaurants through the search bar. Each restaurant has different dishes. Users can click on the dishes they want to get product pictures. Users can also write their own evaluations of dishes and score them. Users can also fill in their own preferences, and the system will help you select restaurants that meet your tastes.
    3. What would be a good creative component (function) that can improve the functionality of your application?
    Users can make classification requirements according to their different tastes and requirements, and the website will screen out restaurants suitable for users according to their choices. The website can also recommend suitable restaurants and people with the same tastes to users according to their daily choices.
    4. ![image](https://user-images.githubusercontent.com/90111545/132971485-d24a1857-6644-4fb7-88dd-3d75b72b11c8.png)
       ![img2](https://user-images.githubusercontent.com/43330557/132972412-7bad0dce-e229-4823-bc0a-cac8b1de8572.jpg)
       ![img3](https://user-images.githubusercontent.com/43330557/132972405-cf324b28-07ee-42a6-9706-f5f1b6e4c1f3.jpg)


7. Project work distribution:  
Yingjie Zhao is mainly responsible for recommend system and machine learning part. She will apply recommend system algorithm to filter relative restaurants based on user’s query. In addition, as a captain, she will coordinate everyone’s work and make sure everyone finish their part on time.  
Chang Li will focus on data mining and prepossessing part. He will collect the dataset from website. Then he will explore those data to filter useful information.   
Tengjun Jin will develop database. He will make database work efficiently and safely.  
Yunjia Zhang responsible for front-end design and connection with the database.
