# Strava Dev API 
Playing about with Strava's open API 
- Pulled down all my data into a CSV to play around with
- I have not provided the CSV here but the code for the heatmap is provided just need to drop in some location data with longitude and latitude.
- Medium article written around this here with links to documentation: https://medium.com/p/ae0ad0791f08

# Data & Results
You are now free to browse your data for insights. I exported all my Strava activities to a CSV to play about with. There is a useful tutorial here by CJ Mayes which also covers some of the setup in Postman and additional scopes https://cj-mayes.com/2023/02/08/using-the-strava-api/ from here I used ‘plotly’ and ‘pandas’ python libraries to visualise my data.

The below views are using scatter_map: https://plotly.com/python/mapbox-to-maplibre/

I isolated the longitude and latitude data to build a heatmap of my activites by location. I have provided some of the results below.

![image](https://github.com/user-attachments/assets/eec71fa9-efc5-4d0c-a1e1-a6d7f7ff8830)
Heatmap of runs by location

![image](https://github.com/user-attachments/assets/37e7b56e-9897-4c2b-9680-058a358f0af9)
Global runs view — All Strava activities
I looked at the type of activities completed on Strava, walking and running making up the most of this. I use Huawei Health which utilises the Strava WebHooks to sync my activities so would be interesting to expand on this on the hooks side of things in future.

![image](https://github.com/user-attachments/assets/f2ee2a6e-1c82-4cd6-a708-bc2ef09f1638)
Activity by type as percentage
