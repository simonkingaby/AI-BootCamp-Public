# Some Additional Thoughts
## Time to Shine
This project is the culmination of six months of hard work. Make the most of this opportunity to work with your classmates, TAs, and me to identify and solve a real problem, either from your career experience, or from a novel field you are interested in.

## Presentation
Consider using one or more of the following to make a presentation/user interface layer for your app:
- Gradio
- Streamlit
- GitHub Pages
- Hugging Face
- Flask

Host your app on the web so that potential employers can find it.

https://www.infoworld.com/article/3586120/8-great-little-python-web-frameworks.html

***Make it something you're really proud of.***

## Project Management
Consider using a web-based project management tool:
- Github Teams
- Trello
- Jira by Confluence (be careful not to go down the rabbithole)

## Data
Consider using a database to store your data:
- mySQL
- Postgres
- Airtable

For vector storage, consider:
- Pinecone.io
- Faiss

## Cloud 
Consider using a cloud provider for some or all of your project features:
- Amazon AWS
- Microsoft Azure
- Google Cloud

## Mobile
Consider using a mobile framework for your user interface:
- Kivy
- Beeware

https://www.ongraph.com/definitive-guide-to-python-app-development/

## Chatbot
Consider creating a chatbot for your user interface:
- Amazon Lex (AWS.amazon.com)
- Amazon Alexa (https://developer.amazon.com/en-US/alexa)
- Microsoft CLU (portal.azure.com)
- VoiceFlow.com 
- Rasa.com

## Presentation Tools
Consider using alternatives to Microsoft PowerPoint and Google Slides for your presentation:
- Canva
- Prezi

## Notes
- You've got five classes over two weeks.
- Make the most of it, but don't bite off more than you can chew. Focus on layers of technology. Get the base layer working, then add another layer and get that working, then another, and so on. For example, you might decide to build a mobile app with Scikit-learn, NLU, and Kivy. Don't try to do all three at once. Get Scikit-learn working first, then add the NLU layer, then add the mobile UI. 
- Don't forget that you can use oversampling to build out a larger dataset, and undersampling and filtering to wrangle one that is too large.
- Make sure you are all using the same versions of the modules in your local environment (including Python). You may want to create a new local environment just for the project.
- Be sure to save off your model components (model, preprocessors, etc.) as pickle files. If you build an app with a UI, it should use the model (from the pickle files), and not train the model through the UI. Training the model is a backend task that is done before the UI is built.
- Remember to only Fit the model on the X-Train data, and Transform the X-Train and X-Test data.
- Use the TAs, tutors, instructor, fellow students, and AI tools as resources to help you make this project awesome.
- As this project is going to be part of your Linked-In profile, how much money are you willing to spend to make it awesome? If you decide to use paid resources, make sure you can turn them off after two weeks. Consider recording a video of your solution, potentially with a soundtrack and voiceover.  


