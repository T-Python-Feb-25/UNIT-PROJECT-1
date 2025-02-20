
def get_season (month, day):
    if month ==3 & day>=21 & day<=31|month==4 & day>=1 & day<=30|month==5 & day>=1 & day<=31|month==6 & day>=1 & day<=20:
        return "Spring"
    elif month ==6 & day>=21 & day<=30|month==7 & day>=1 & day<=31|month==8 & day>=1&day<=31|month==9 & day>=1 & day<=22:
        return "Summer"
    elif month ==9 & day>=23 & day<=30|month==10 & day>=1 & day<=31|month==11 & day>=1&day<=30|month==12 & day>=1 & day<=20:
        return "Autumn"
    elif month ==12 & day>=21& day<=31|month==1 & day>=1 & day<=31|month==2 & day>=1 & day<=29|month==3 & day>=1 & day<=20:
        return "Winter"
    
month_input=input("enter the month")
day_input=input("enter the day")

season=get_season(month_input, day_input)

if season =="Spring":
    print(''' At this time of year, the spring season has arrived, 
          so it is recommended to wear clothes with light
          and cheerful colors such as white, pink, light blue, light green, 
          yellow, light purple and pastel colors.and bright 
          and refreshing colors are suitable for this season.''')
    
    
elif season== "Summer":
    print('''At this time of year, summer has arrived, so it is recommended to
          wear clothes in light and calm colors such as white, beige, sky blue, 
          mint green, light yellow, and light pink, because these colors reflect 
          the sun's rays instead of absorbing them, which reduces the feeling of heat.''')
    
    
elif season=="Autumn":

 print('''At this time of year, autumn has arrived, so it is
        recommended to wear clothes in earthy and warm colors such as orange, 
       brick red, mustard yellow, brown, olive, navy blue, and dark gray,
        because they match the colors of nature in autumn..''')
 
elif season=="Winter":

 print('''At this time of year, winter has arrived, so it is 
          recommended to wear clothes in dark and warm colors such as 
          black, navy, brown, gray, dark green, dark red, and burgundy
           because dark colors absorb more heat than light colors,
           which helps maintain warmth.''')