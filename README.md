# Web Scrapping With Selenium


![4dgjph](https://user-images.githubusercontent.com/32064166/91863087-1b1ceb00-ec45-11ea-8ed6-c293da676718.gif)



This project was designed to automate my monthly routine. Every month I have to generate the download of my college's bank slip. 
With what has been done, it is only necessary to run the project and I will have in my "preferential" email the bank slip as
well as the financial history of payments. 
PS: This works for FURB students, only.

## Getting Started

### Running the project 
    * Build a new venv
    * Run  pip install -r requirements.txt inside the new venv
    * Set up your credencials at.env (make sure if you've chrome webdriver, if not, download it)
    * Just run the main.py file

### After Running
   After you run main.py, it will be create new directory called "docs", inside it will contain your bank slip, an 
   image of your history of payments and a csv file with the data of the image manipulable. Like that:
   
   ![pastas](https://user-images.githubusercontent.com/32064166/91867067-9385ab00-ec49-11ea-9acf-ae6255532d8b.JPG)

   
   
## Built With

* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [SMTP](https://docs.python.org/3/library/smtplib.html)

## One Step Forward
   Let's make a .exe file? It's very simple! Go to path of your project and apply this following command:
   ```
   pip install pyinstaller
   pyinstaller --onefile -w file_to_become_executable.py
   ```
   
   Delete the build paste and main.spec file. The .exe will be in dist/file_to_become_executable.exe,
   move this file to project path, delete dist and just RUN the file, be happy :satisfied:
   
   
## Next Step

I intend to make an executable file, by this i can share with my classmates.
Automate to another level, run the script once a month every day pre-defined by the user.

This project looks great, - it's time to merge! :shipit:
