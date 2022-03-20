import jsons, logging, sys
from oauth2client import client
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Handle a request from Google Chat

    @param req: The request object
    @return: The response object
    """
    logging.info('Python HTTP trigger function processed a request.')

    try:
        verify_auth(req.headers["authorization"])
    except:
        logging.exception('Unauthorized')
        return func.HttpResponse("Unauthorized", status_code=401)

    try:
        event = req.get_json()
    except:
        logging.exception('Bad Request')
        return func.HttpResponse("Bad Request", status_code=400)
    
    try:
        return func.HttpResponse(jsons.dumpb(handle_event(event)))
    except:
        logging.exception('Internal Server Error')
        return func.HttpResponse("Internal Server Error", status_code=500)

def handle_event(event: object) -> object:
    """
    Handles an event from Google Chat.

    @param event: The event sent from chat.
    @return: The object to respond with
    """
    logging.info('Received an authenticated event: %s' % jsons.dumps(event))

    if event['type'] == 'ADDED_TO_SPACE' and not event['space']['singleUserBotDm']:
        text = 'Thanks for adding me to "%s"!' % (event['space']['displayName'] if event['space']['displayName'] else 'this chat')
    elif event['type'] == 'MESSAGE':
        text = 'You said: `%s`' % event['message']['text']
    else:
        return None

    return {'text': text}

CHAT_ISSUER = 'chat@system.gserviceaccount.com'
PUBLIC_CERT_URL_PREFIX = 'https://www.googleapis.com/service_accounts/v1/metadata/x509/'
AUDIENCE = '{{AUDIENCE}}'

def verify_auth(bearer: str) -> None:
    """
    This method asserts that the specified bearer token matches the expected deployment.  If not, an exception is thrown.
    
    @param bearer: The authorization string
    @raise Error: If authorization fails
    """
    token = client.verify_id_token(bearer.replace("Bearer ", ""), AUDIENCE, cert_uri=PUBLIC_CERT_URL_PREFIX + CHAT_ISSUER)

    if token['iss'] != CHAT_ISSUER:
        raise PermissionError()

