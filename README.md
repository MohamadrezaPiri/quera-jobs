## Quera Jobs Scraper
This script helps you to get aware of the latest job positions on __[Quera.org](https://quera.org)__ as soon as possible.
## How to customize:
- The script is looking for Junior and Intern job positions. To change it, You must change the value of ```URL```. For example":
     #### From:
   ```
   URL = 'https://quera.org/magnet/jobs?level=intern&level=junior'
   ```
    #### To:
   ```
   URL = 'https://quera.org/magnet/jobs/category/senior'
   ```
- You may also want to change the search keywords:

   ```
   python_ = "python"  
   django = "django"
   back_end = "back-end"

   key_words = [python_,django,back_end]
   ```    
- You need two emails for sending and recieving the job position's link
    
