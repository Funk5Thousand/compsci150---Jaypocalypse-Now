# 🛡️ Project Title
**CompSci 150 - Intro to programming - Python Malware scanner** 🐍

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Course](https://img.shields.io/badge/Course-CompSci%20150-purple.svg)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)
![Security](https://img.shields.io/badge/Security-Malware%20Detection-red.svg)

**🔍 Digital Detective Work • 🎓 Learning by Doing • 💻 Real-World Application**

</div>

---

## 📖 Description

> *"When digital security meets educational excellence..."*

**The Challenge:** 🚨 Jayden has a problem. He engages in nefarious or otherwise disreputable behavior on his work computer, and has thus contracted a virus. Jayden's problem is now a problem for this class to solve in the second half of the course.

**Our Mission:** 🎯
- 🐍 Develop a Python application for malware detection and removal
- 🖥️ Work with either a virtual copy of Jayden's hard drive OR create our own controlled infection
- 📊 Track development progress through each class session
- 🎓 Master real-world software development practices

**Learning Objectives:** 📚
This repository serves as your gateway to understanding:
- ✅ **Git & GitHub** - Version control mastery
- ✅ **CI/CD Pipelines** - Automated development workflows  
- ✅ **Software Development Lifecycle** - Industry-standard practices
- ✅ **Cybersecurity Fundamentals** - Malware analysis and detection

> 💡 **Note:** Each student will maintain a similar repository for final examination purposes.

---

## 📋 Progression
In our first class we set up our github accounts and connected vscode to github for source control, we 
set up our coding environment, created a virtual environment to develop our application, and investigated
yara as an initial means of detecting malware. We looked into what yara is, what it does, what sort of
resources it requires, and decided it was a worthwile implementation based on our own research, and the
number and reputation of the number of security community representatives who also use it. Thus, we
started writing code. That code is now present in this repository. By the end of our first class, we had gathered some yara rules, and written a basic application to scan the file system for malware. We're off to a healthy start.


Class #2 of group project.

So we proved that our project is feasible, something within the realm of our skillset and got some rudimentary function from it using python-yara. Now we want to build out some CLI UI functionality. Add a few options to select from, give some informative feedback to our users as the application is running, and look into scanning the actively loaded and running processes. We will also be able to make our yara rules folder much more robust and likely circumvent the Edge browser virus block notifications we received upon initial attempt to grab these rules.

#End of class 2. We did not get very far thanks to surveys etc. We moved some functions from the main app to the utilities.py file, we added some user interaction, we added process scanning, and we had technological difficulties. I am working on those. We also had a fiery discussion on how to help students learn better, I will take that feed back into account and we will start fresh nexet class with making the application more user friendly. I will also bring a laptop and we will reformat it and attempt to infect it with malware.

Class 2 reset: During class 2 I implemented some major changes to the code during class, which due to our survey guests in and out, I did not explain in depth. I will now explain those here. First, since we implemented a function to scan process ID's, which also requires a compiled list of our rules, we followed the DRY principle, do not repeat yourself. Since we compiled our rules previously when we scanned the file system, I did not rewrite all of that code. I simply broke that code out into a function in the utilities file. As seen here:


def get_compiled_rules():
    if os.path.exists('.//yararules//yara_compiled_rules'):
        compiled_rules = yara.load('.//yararules//yara_compiled_rules')
    

    else:    
        yara_rules_dict = get_yara_rules_paths('.\\yararules')
        compiled_rules = yara.compile(filepaths=yara_rules_dict)
        compiled_rules.save('.//yararules//yara_compiled_rules')
    return compiled_rules

Since we now have two functions which require compiled rules (our function that scans the file system, and now the function that scans processes) in those two functions we can simply call get_compiled_rules and store the result in a variable and we will have our compiled rules. In order facilitate this move, we needed to import yara to our utilities file, and also change our call to the utility functon util.get_yara_rules_paths to simply get_yara_rules_paths since now we are calling it from the same file where the get yara rules paths function is defined. 

Next we added some user interface code, so that we could ask the user, if they want to scan the file system, scan active processes, or run a full system scan. We did this, but first printing out some information about the application, and then we created a variable and assigned it whatever returned from an input function. In the input function we used a here string ''' <uniquely formatted string> ''' to print out a list of options for the user as seen here:

 print("Welcome to CompSci 150 Malware Scanner")
    print(" ")

    user_response = input('''
          Welcome, What would you like to do? Enter the number for your choice.
                          
        1) Scan the file system.
        2) Scan the active running processes.
        3) Scan the entire system.
                          
                        ''')
    if user_response == '1':
            scan_file_system()
    elif user_response == '2':
            scan_processes()
    elif user_response == '3':
            scan_file_system()
            scan_processes()
    else:
            print("That selection does not exist")

We used input and a here string to collect the users desired action and an if else if else if else control flow to figure out which option the user had selected, and thus run that function.

Finally, we defined out scan processes function. We needed a way to get a list of all running process ID's on a system and found the psutil package. Since we looked at the documentation of the psutil package and determined it was cross platform (meaning it would also work on linux) we installed that package as directed in its documentation by pip install psutil.

Obtaining a list of process ID's using psutil was straight forward and so we defined a utility functions to do so here:


def get_process_pids():
    return psutil.pids()

Then we investigated the YARA documentaton to see how to run our yara rules against running processes. This was also straight forward, it was essentially the same as scanning the file system. You take a compiled rules object, and run the .match method against a process id. So we simply looped through our previously acquired list of process id's and scanned each ID with our compiled rules using match as shown below:

def scan_processes():
    compiled_rules = util.get_compiled_rules()
    pids = util.get_process_pids()
    for id in pids:
        matches = compiled_rules.match(pid=id)

further, I was able to recreate the issues we experienced with insatlling python packages at home and found that running
python -m pip install --upgrade pip
and then using pythomn -m pip install psutil
python -m pip install yara-python
resolved the errors and allowed me to install packages into my virtual environment without an issue. This is important, as we will wish to install additional packages and these will all be necessary for each student to complete their project.

Class project class #3. Now we are going to give the user some feedback to let them know what the application is doing. We are going to do this with the halo package, which will give the user clear indication that the application is running and what it is doing.
---

## 🚀 Installation
*Installation instructions will be added as the project develops...*

---

## 💻 Usage
*Usage examples and tutorials coming soon...*

---

## ⭐ Features
*Feature list will be updated as development progresses...*

---

## ⚙️ Configuration
*Configuration options will be documented here...*

---

## 🤝 Contributing
*Guidelines for class collaboration and contributions...*

---

## 🧪 Testing
*Testing procedures and methodologies...*

---

## 📚 Documentation
*Additional documentation and resources...*

---

## 📄 License
*License information...*

---

## 📈 Changelog
*Project history and version updates...*

---

## 🆘 Support
*Getting help and reporting issues...*

---

## 👥 Authors
*Meet the development team...*

---

## 🙏 Acknowledgments
*Special thanks and credits...*