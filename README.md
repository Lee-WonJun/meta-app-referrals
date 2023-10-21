# Meta App Referrals

## Overview

Meta App Referrals is a Python script designed to extract app information from an Oculus store HTML page. The extracted data, including the app name, original link, and referral link, is saved to a CSV file.

---

## Prepare

1. **Log in** to [Oculus Quest's page](https://secure.oculus.com/my/quest/).
2. **Click on `SHOW ALL APPS`**.
   ![Show All Apps](https://github.com/Lee-WonJun/meta-app-referrals/assets/10369528/6ef9a66f-0ca6-4ac8-85be-59e440053661)
3. **Copy the HTML code**. It is recommended to use browser developer tools (F12).
   ![Copy HTML Code 1](https://github.com/Lee-WonJun/meta-app-referrals/assets/10369528/cc98656c-f69b-4b80-bd66-24513da2947a)
   ![Copy HTML Code 2](https://github.com/Lee-WonJun/meta-app-referrals/assets/10369528/958ab8c7-ceee-4b7c-a4d3-0ab3fdb42294)
4. **Overwrite** the example HTML code with the code you've copied.
   ![Overwrite HTML](https://github.com/Lee-WonJun/meta-app-referrals/assets/10369528/3978fb6d-73ca-4dfb-8427-57aefe3b0e9a)

---

## Usage

1. Prepare an HTML file (`apps.html`) in the current directory.
2. Run the script: `python script_name.py`
3. When prompted, input your user ID.
4. Check the generated `apps.csv` file.

(Like this)
```csv
Product Name,Original Link,Referral Link
First Steps,https://www.oculus.com/experiences/quest/1863547050392688/,https://www.oculus.com/appreferrals/dldnjs1013/1863547050392688
SUPERHOT VR,https://www.oculus.com/experiences/quest/1921533091289407/,https://www.oculus.com/appreferrals/dldnjs1013/1921533091289407
Meta Quest TV,https://www.oculus.com/experiences/quest/1931356740318898/,https://www.oculus.com/appreferrals/dldnjs1013/1931356740318898
Eleven Table Tennis,https://www.oculus.com/experiences/quest/1995434190525828/,https://www.oculus.com/appreferrals/dldnjs1013/1995434190525828
YouTube VR,https://www.oculus.com/experiences/quest/2002317119880945/,https://www.oculus.com/appreferrals/dldnjs1013/2002317119880945
Virtual Desktop,https://www.oculus.com/experiences/quest/2017050365004772/,https://www.oculus.com/appreferrals/dldnjs1013/2017050365004772
SKYBOX VR Video Player,https://www.oculus.com/experiences/quest/2063931653705427/,https://www.oculus.com/appreferrals/dldnjs1013/2063931653705427
Shadow Point,https://www.oculus.com/experiences/quest/2088119334554800/,https://www.oculus.com/appreferrals/dldnjs1013/2088119334554800
Mission: ISS: Quest,https://www.oculus.com/experiences/quest/2094303753986147/,https://www.oculus.com/appreferrals/dldnjs1013/2094303753986147
Vader Immortal: Episode I,https://www.oculus.com/experiences/quest/2108775495884888/,https://www.oculus.com/appreferrals/dldnjs1013/2108775495884888
The Room VR: A Dark Matter,https://www.oculus.com/experiences/quest/2124523024270629/,https://www.oculus.com/appreferrals/dldnjs1013/2124523024270629
```

---

## Limitations

1. The process is not automated.
2. The script does not filter out apps that cannot generate referral links, such as Beatsaver or free apps.
