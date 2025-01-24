# RealTimeStockDashboard
Developed using Python, Flask, Java, and a finance API, this project gives users a front end application where they can find the current price of stocks, their open price, and percent change with real time data. Also allows users to convert currencies and get automated email notifications for updates on quarterly economic reports.


# Features
- Real time stock prices for many stock tickers
- Automated economic reports emailing, including GDP, QFR, and ECI, to notify users.
- Currency conversion with automated rate updates and ease of access to users.
- A customized and detailed user website


# Installation
### **Steps**


1. Clone the repository
   ```bash
   git clone https://github.com/VedPeesu/RealTimeStockDashboard.git
   ```


2. Set up News API credentials
- Go to News API Wesbite and create an account
- Generate your own News API key


3. Set up Gmail credentials
   ```bash
   apiKey = "NEWS_API_KEY";
   apiUrl = "https://newsapi.org/v2/everything";
   ```


4. Configure applicaion properties
   - Create an application.properties file and add the following
   ```bash
   news.api.key=NEWS_API_KEY
   news.api.url=https://newsapi.org/v2/everything
   spring.mail.host=smtp.gmail.com
   spring.mail.port=587
   spring.mail.username=your_email@gmail.com  
   spring.mail.password=your_email_app_password 
   spring.mail.properties.mail.smtp.auth=true
   spring.mail.properties.mail.smtp.starttls.enable=true
   ```
