Suppose you wanted to create a chatbot that could determine an outcome based on a Machine Learning model. The chatbot would gather the parameters necessary to use the model's prediction method to determine the outcome.
## Part 1: Create a Machine Learning Model
For example, suppose you want to predict whether a person has diabetes or not. A search on Kaggle finds a few likely candidate datasets. I selected [this one](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset). Imagine you wanted to set this up in a chatbot.

Before you begin, drop to a command prompt for your Pythen environment and do:

```bash
pip list
```

Open the list and make sure you know the versions of pandas, numpy, and scikit-learn, enter those version numbers in the requirements.txt file in the DiabetesDockerContainer folder. If the versions between the environment and the requirements file are different, the pickle save and pickle load will fail because they are mismatched.

See the Python code for the [Machine Learning model here](https://github.com/simonkingaby/AI-BootCamp-Public/blob/main/Diabetes%20Chatbot/diabetes.ipynb).

Now, we have a model that we can load into the chatbot to predict the diabetes outcome from the input variables: Gender, Age, Hypertension, Heart Disease, Smoking History, and BMI.

Next, we need to create a Lex bot that can ask for those variables.
## Part 2: Creating the Lex Bot
If you haven't done so, create an AWS Skill Builder account and take the [Amazon Lex Getting Started (1 hr) class](https://explore.skillbuilder.aws/learn/course/external/view/elearning/17999/amazon-lex-getting-started). This will introduce you to the Lex concepts.
Our bot will be quite simple, with a single Intent, several Slot Types, and a Fulfillment algorithm in Lambda.

==**If you would like to skip ahead to the coding section, you can download the [JSON.zip file here](https://github.com/simonkingaby/AI-BootCamp-Public/blob/main/Diabetes%20Chatbot/DiabetesBot-LexJson.zip). Then, in the Lex console, click on Action, Import, give your bot a name, such as DiabetesBot, select the JSON.zip file, under IAM permissions, select Create a role with basic Amazon Lex permissions, select No in the COPPA section, and click Import. Then skip ahead to Part 3: Creating the Lambda function.**==

When you're ready, follow this procedure to create a blank Lex bot:

1. In the AWS Console, in Amazon Lex, click the Create bot button.
2. Select to Create a blank bot.
3. Give the bot a name, such as DiabetesBot.
4. In IAM permissions, Create a role with basic Amazon Lex permissions.
5. In the COPPA section, select No.
6. Click Next
7. In the Language section, select a language and a Voice.
8. Then click Done to create the bot.
### Setting up the slot values
Now, set up the Slots, these are the values we will collect with the bot.

9. In the left navigation panel, click < Back to intents list.
10. Then click on Slot types.
11. Click Add slot type, then select Add blank slot type.
12. Enter gender for the Slot type name, and click Add.
13. Toggle the Slot value resolution over to Restrict to slot values.
14. Then enter the following Slot type values (case matters):

	a) Female
	b) Male

15. To the right of each option, enter any synonyms, such as woman and man.
16. When you're done, it should look like this:

![Slot Types](<images/Pasted image 20240311124217.png>)

17. Click Save Slot type.
18. You might think we'd use a slot type for Smoking History, but we'll use a pair of Yes/No questions instead to simplify the bot interactions.
19. Next we'll set up the intent.
### Setting up the intent and the slots
20. In the left navigation panel, select Intents.
21. Then click on the NewIntent intent in the list.
22. Change the Intent name to PredictDiabetes.
23. Skip down to Sample utterances.
24. Enter the things a user might say to trigger your intent. In other words, when the user says an utterance, it kicks off the process for predicting diabetes. For example, a user might say, "Do I have diabetes?" Or even just a simple, "Hi."
25. Scroll down to Slots. We need to ask for several slots. Start by clicking the Add slot button.
26. For the Name, enter *age*. In the Slot type, select AMAZON.Number, in the Prompts, enter How old are you? Then click Add.
27. Enter the remaining slots and their prompts. (Note: Everything is case sensitive.)

| Name           | Slot type           | Prompt                                  |
| -------------- | ------------------- | --------------------------------------- |
| age            | AMAZON.Number       | How old are you?                        |
| current_smoker | AMAZON.Confirmation | Do you smoke?                           |
| former_smoker  | AMAZON.Confirmation | Have you ever smoked?                   |
| gender         | gender              | Which gender are you?                   |
| hypertension   | AMAZON.Confirmation | Do you have high blood pressure?        |
| heart_disease  | AMAZON.Confirmation | Do you have a history of heart disease? |
| bmi            | AMAZON.Number       | What's your B.M.I.?                     |

![Slots](<images/Pasted image 20240308155835.png>)

28. Now, that you've entered the slots, go back up to the utterances. Add the following utterance:
      "As a 30 year-old woman with a B.M.I. of 32, do I probably have diabetes?"
29. Now select the number 30, and in the Use available slot prompt select age.
30. Now select the word woman and in the Use available slot prompt select gender.
31. Now select the number 32, and in the Use available slot prompt select bmi. Be sure to leave a space after the {bmi} slot (before the comma), as slots have to be separated from the rest by whitespace.
32. The utterance should now look like this (colors may vary):

![Utterance](<images/Pasted image 20240308182217.png>)

33. Save the intent by clicking the Save intent button at the bottom of the screen.
34. Now click Build and wait for it to complete.
35. Resolve any errors that occur.
36. Now click Test and try out your bot. Say, "Hi" to the bot and answer the questions it asks.
### Configuring the Fulfillment option
37. Scroll down to the Fulfillment section of the Intent.
38. Make the Fulfillment option Active.
39. Save the Intent again.
40. Now click Build and wait for it to complete.
41. Resolve any errors that occur.
42. Now click Test and try out your bot. Say, "Hi" to the bot. It will try to call the fulfillment function (which we have yet to write), and will complain that the fulfillment function is not specified.
43. And that's the Lex side of the bot completed (mostly - we'll come back to it in a bit).
## Part 3: Creating the Lambda function
The backend of a Lex bot is implemented in a Lambda function. We're going to create it twice. Once, for development and testing, without the ML wired in, and once, for deployment, with the ML wired in. We will take very different approaches for these so we'll go through them independently.
### Creating the Dev Lambda function
Start, by navigating to the Lambda console in AWS. Then click on Create function.
In the Create function dialog:

1. Select Author from scratch.
2. Enter a Function name, such as DiabetesLambda.
3. Select the latest Python runtime (3.12).
4. Leave the Architecture at x86_64.
5. Click Create Function.
6. Scroll down to the code window.
7. Replace the contents of the lambda_function.py with the contents of the [diabetes_lambda_start.py](https://github.com/simonkingaby/AI-BootCamp-Public/blob/main/Diabetes%20Chatbot/diabetes_lambda_start.py) file.
8. Click the Deploy button.
9. That's it, you're ready to connect the function to the bot.
### Connecting the Lex bot to the Lambda function
To connect the two, switch back to the Lex bot in the console. Then follow these steps:

10. Expand Deployment in the left navigation panel. 
11. Select Aliases.
12. Select the TestBotAlias.
13. Scroll down to Languages. 
14. Select English (US).
15. This is where you connect the Lambda function.
16. Select the DiabetesLambda as the Source.
17. Click Save.
18. Click on Intents in the left navigation.
19. Click on the Build button at the top right.
20. When the build is complete, click the Test button.
21. Enter Hi.
22. Answer the questions.
23. Regardless of what you enter, at the end it should say, "As a {age} year-old. It is quite likely that you do not have diabetes." This is the hard coded message we will change in the next section.
### Finishing the Lambda function
At this point, we have a Lex bot set up and wired up to a Lambda function. Now we need to get the slot values out of the JSON payload.

Switch over to the Lambda console.

First, we're going to set up a test function so we don't have to toggle back to the Lex bot to test. Follow these steps:

1. Scroll down and select the Test tab.
2. Select to Create a new event.
3. Give the event a name, say "LexTestPayload".
4. Select Private.
5. Replace the Event JSON with the payload from [this JSON file](https://github.com/simonkingaby/AI-BootCamp-Public/blob/main/Diabetes%20Chatbot/diabetes_test.json).
6. Click the Save button (top right).
7. Toggle back to the Code tab.
8. Click the Test button. 
9. Scroll down to see the bot response in the messages section of the JSON. Like this:

```json
  "messages": [
    {
      "contentType": "PlainText",
      "content": "As a 35 year-old. It is quite likely that you do not have diabetes."
    }
  ]
```

Now, toggle back to the lambda_function.py file and locate the line where we parse the age slot:

```python
    age = parse_int(get_slot_value(slots, "age", 0))
```

Add the remaining slots:

```python
    current_smoker = (get_slot_value(slots, "current_smoker", ""))
    former_smoker = (get_slot_value(slots, "former_smoker", ""))
    gender = (get_slot_value(slots, "gender", ""))
    heart_disease = (get_slot_value(slots, "heart_disease", ""))
    hypertension = (get_slot_value(slots, "hypertension", ""))
    bmi = float(get_slot_value(slots, "bmi", 0))
```

Next, convert the smoking columns and binary columns.

```python
    if current_smoker == 'Yes':
        smoking_history = 'current'
    elif former_smoker == 'Yes':
        smoking_history = 'former'
    else:  
        smoking_history = 'never'
    if heart_disease == 'Yes':
        heart_disease = 1
    else:
        heart_disease = 0
    if hypertension == 'Yes':
        hypertension = 1
    else:
        hypertension = 0
```

Now, make a dataframe out of the slot values 

```python
    # make a DataFrame out of the gathered slots 
    # (note: column order matters, it must match the saved model)
    X = pd.DataFrame({"gender": [gender],
                      "age": [age],
                      "hypertension": [hypertension],
                      "heart_disease": [heart_disease],
                      "smoking_history": [smoking_history],
                      "bmi": [bmi]}, index=[0])
```

Next, use the model components that were saved as PKL files.

```python
    try:
        # Now load the OHE
        with open("encoder.pkl", "rb") as f:
            encoder = pickle.load(f)
        # and encode the data
        X = encoder.transform(X)

        # Now load the scaler
        with open("scaler.pkl", "rb") as f:
            scaler = pickle.load(f)
        # and scale the data
        X = scaler.transform(X)

        # Now load the model
        with open("diabetes_model.pkl", "rb") as f:
            model = pickle.load(f)
            # and predict
            y_pred = model.predict(X)
    except Exception as e:
        logging.error(f'An error occurred while processing the request: {e}')
        return {
            'sessionState': {
                'dialogAction': {
                    'type': 'Close'
                },
                'intent': intent
            },
            'requestAttributes': {},
            'messages': [
                {
                    'contentType': 'PlainText',
                    'content': 'An error occurred while processing the request. Please try again later.'
                }
            ]
        }

    if y_pred[0] == 1:
        do_or_do_not = 'do'
    else:
        do_or_do_not = 'do not'
```

Finally, change the message content as follows:

```python
        'messages': [
            {
                'contentType': 'PlainText',
                'content': f'As a {age} year-old {gender} with the indicators you gave, it is likely that you {do_or_do_not} have diabetes.'
            }
        ]
```

Now click Deploy to save and deploy your changes. 

Then click Test to try it out.

You'll see a problem... Pandas is not in the default Lambda build. We will need to add it. 
However, that won't be the only module we need to add. We could add Pandas as a layer in the Lambda function, but we're also missing Scikit-learn, which is too big to fit in a layer.

This necessitates a significant change in direction, as we now have to move the Lambda function code into a Docker container. This is not difficult, but it is an entirely different approach.
It starts by installing Docker Desktop.
## Part 4: Setting up the Docker container
First, install Docker Desktop from here: [Overview of Docker Desktop | Docker Docs](https://docs.docker.com/desktop/). Scroll down and pick the Docker Desktop install for your PC. Follow the steps. If you're on Windows, you will need to enable some BIOS features and Windows features to get Docker Desktop to work. On my machine, the BIOS feature to enable hardware virtualization was a bit of a hunt, but I eventually found it and enabled it. 

Once you've installed Docker Desktop and restarted your machine, you can create your Docker container files.

In VS Code, create a new folder, for example: DiabetesDockerContainer.

In that folder, create three files:
* [app.py](https://github.com/simonkingaby/AI-BootCamp-Public/blob/main/Diabetes%20Chatbot/docker/app.py)
* [Dockerfile](https://github.com/simonkingaby/AI-BootCamp-Public/blob/main/Diabetes%20Chatbot/docker/Dockerfile)
* [requirements.txt](https://github.com/simonkingaby/AI-BootCamp-Public/blob/main/Diabetes%20Chatbot/docker/requirements.txt)

Copy the contents of the files from GitHub at the links above.

Then, into the same folder, copy the three .pkl files you created in the modeling step in Part 1.

Now, within VS Code, right-click on the docker folder (DiabetesDockerContainer) and choose Open in Integrated Terminal. 

Then, from the command line, execute the following commands:

```bash
docker build -t diabetesdockercontainer .   
# (NOTE: Don't miss the dot at the end of that line.)
```

While that's building, in the AWS console, go to IAM. Create a new user called ecr_admin. Assign it the following policies:
* AmazonEC2ContainerRegistryFullAccess
* AmazonElasticContainerRegistryPublicFullAccess
* AWSAppRunnerServicePolicyForECRAccess
* EC2InstanceProfileForImageBuilderECRContainerBuilds
* SecretsManagerReadWrite

After creating the user, go to the Credentials tab, scroll down to Access keys and give it one. Ignore the warning.

With the keys in hand, go back to the VS Code integrated terminal and execute the following command. 

``` bash
aws configure
```

When asked for them, provide your keys.
Once that's done and you're back at the command line, execute the next command.

``` bash
aws ecr create-repository --repository-name diabetes-repo --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
```

Next, tag the docker image with the repo name (replace the account number with yours):

```bash
docker tag diabetesdockercontainer:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/diabetes-repo:latest
```

Now, get an authorization token, again replace the account number:

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
```

Finally, push the image to the container:

```bash
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/diabetes-repo:latest
```

If you see that the image has been pushed, then celebrate, and move on to the last part, hooking up the new image as the lambda function.

## Part 5: Wiring up the final Lambda function
Open the AWS Console, and go to Lambda functions.

Click the Create function button.

Select the Container image radio button.

Give the function a name, such as diabetes-lex-lambda-container.

Browse for the container image we just uploaded.

Click Create function at the bottom.

Once the function is created, go back to Lex in the console.

Open the DiabetesBot.

Go to Aliases.

Select TestBotAlias.

Select the language English.

Change the source to diabetes-lex-lambda-container.

Click Save.

Go to Intents.

Click Build.

When ready, click Test.

Say Hi and answer the questions.

It might take a few seconds to spin up the docker container the first time.

If it makes a prediction, about diabetes, you win! 

The process is complete and you can rest on your laurels.

Woohoo! 

![Homer Simpson says Woohoo](images/woohoo.jpg)

If not, you have a bug to find and fix. Good luck.

![Homer and Maggie Simpson perplexed at a computer](images/screen-shot-2012-06-03-at-1-32-50-pm.png)

You'll want to look at the Cloudwatch logs for the diabetes-lex-lambda-container to see what went wrong.

When you change the code you need to:

```bash
docker build -t diabetesdockercontainer .   
docker tag diabetesdockercontainer:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/diabetes-repo:latest
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/diabetes-repo:latest
```

Then, in Lambda, edit the function and "Deploy new image" to select the latest image from the container.

Then, in Lex, Test again. Then go back to Cloudwatch. Then make adjustments and redeploy the container and update the Lambda function. Then try again. Rinse. Repeat. Each time you will squash one bug, solve one problem, or something. Eventually, you will sort out the root problem and fix it too. Then you too can celebrate with a well-deserved Woohoo!

Bugs fixed so far:
* Lambda function timeout: 3 seconds. Increased to 30 seconds. Increased to 2 minutes 30 seconds.
* Mismatched versions of Scikit-learn in the pickle process.
* Ran out of memory loading the pickle files. Increased to 1024 MB for RAM and Ephemeral storage.
* Looks like OHE was encoding the BMI column too. Oops.
* **ALL BUGS RESOLVED!!!! WOOHOO!!!**

![alt text](images/1566609425888.jpeg)

With apologies to Matt Groening.