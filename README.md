# auto_feedback
This is a script used to complete feedback automatically  for VIPKid classes. Right now, it only provides feedback for regular lessons, not unit assessment lessons. This is a feature that I plan on adding soon. 
## Example
-------


## Installation
------
How do I get this code? You have a few options:

 - **Clone**: You can clone this repo to your local machine using `$ git clone https://github.com/c-smith7/auto_feedback.git`

 - **Download ZIP**: You can also download the zip file straight from Github. 

 - **Copy**: You can also just copy and paste the source code into a new python file on your local machine. Source code is located in "script" file. 

TIP: Once you have cloned/zipped/copied the script onto your local machine, make sure to save it somewhere easily accessible, such as your desktop. Don't bury it in too many folders. 

## Usage
 ------
 1. Once you have the script on your local machine, run the script in your terminal or command prompt. Should look something like this for command prompt: 
    - `py desktop\auto_feedback.py`
    - or whatever path you have to script saved in.

2. You will then be prompted to input a `Student name:` for the lesson you are generating feedback for. Input a student name with no quotes and press enter. 

3. Next, you will be prompted to input a `Feedback template:`. You can find a template to use in the "Feedback Template" tab under the "Materials" section for the lesson. If you have your own template, that's fine too, just go ahead and copy and paste it into the prompt. 
    - With the current version of this script there is only one 'style' of template that will work and not produce any bugs. 
    - The template must use the pronoun "We" and/or "we" throughout the whole feedback template. 
    - There are two teachers that I almost always use because they have this template style: Amber MZC and Tammy PHT.
    - Again, any template will work as long as it **only** uses "We" and/or "we" throughout the entire template. Here's an example template:
    >In this lesson, ***we*** reviewed the words,"move, push, pull, roll, bounce, fast, slow, stop." ***We*** also reviewed the sentence frames "Force makes things move." and "Gravity pulls you down towards the ground." ***We*** practiced the sight words, conjugating verbs, and adding 'ing' to alter tense. ***We*** also practiced the math terms "take away, left, minus, equals."

    - Notice how this template only uses the pronoun "we" to refer to the teacher and student. 
    - The reason this template style is required is because the script will locate the *first* "we" in the feedback template that you supply the script, and replace it with `{student_name} and I`. 
    - Once you have your desired template inputted into the prompt, press enter.
4. Your automated feedback will be outputted and you can copy and paste it into the VIPKid feedback portal. 
5. To run the script the again for the next student feedback, simply press the *up* arrow in the command prompt, which will run the previous command, such as: `py desktop\auto_feedback.py`

## Contribute
-------
To be continued..
