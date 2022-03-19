# redmine-gchat-bot
A Google Chat bot for logging conversations to Redmine tasks

# Development
1. Install Prerequisites
    * [Azure Functions Core Tools 4,x](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2)
    * [Python 3.8+](https://www.python.org/downloads/)
2. Create and activate virtual environment
    * `python -m venv .venv`
    * `source .venv/bin/activate`
3. Run locally 
    * `func start`

# Deployment
1. Deploy the redmine-gchat-bot to an Azure Function and note the URL
    - (see [.github/workflows/main_pangaeatech-gchat-bot.yml](.github/workflows/main_pangaeatech-gchat-bot.yml)
2. Enable the [Google Chat API](https://console.cloud.google.com/apis/library/chat.googleapis.com)
3. Go to the "Configuration" tab in the [Google API Dashboard](https://console.cloud.google.com/apis/api/chat.googleapis.com/)
4. Set the Configuration as follows:
    - Bot status: `LIVE - available to users`
    - Bot name: `recorder`
    - Avatar URL: (the URL of the image you want to use)
    - Description: `Redmine Issue Updater`
    - Functionality:
        - [x] Bot can be messaged directly
        - [x] Bot works in spaces with multiple users
    - Connection Settings:
        - [x] Bot URL
        - Bot URL: (the URL of the Azure Function deployment)
            - e.g.  `https://pangaeatech-gchat-bot.azurewebsites.net/api/Trigger`
    - Slash commands:
        - (none)
    - Link unfurling:
        - (none)
    - Permissions:
        - [x] Everyone in the Domain

# Additional Resources
* https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python
* https://developers.google.com/chat/how-tos/bots-develop#python
