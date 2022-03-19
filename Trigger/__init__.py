import logging
import jsons

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        event = req.get_json()
    except:
        logging.exception('Bad Request')
        return func.HttpResponse("Bad Request", status_code=400)
    
    try:
        return func.HttpResponse(jsons.dumpb(handle_event(event)))
    except PermissionError:
        logging.exception('Unauthorized')
        return func.HttpResponse("Unauthorized", status_code=401)
    except:
        logging.exception('Internal Server Error')
        return func.HttpResponse("Internal Server Error", status_code=500)

def handle_event(event: object) -> object:
    """Handles an event from Google Chat."""
    if event['type'] == 'ADDED_TO_SPACE' and not event['space']['singleUserBotDm']:
        text = 'Thanks for adding me to "%s"!' % (event['space']['displayName'] if event['space']['displayName'] else 'this chat')
    elif event['type'] == 'MESSAGE':
        text = 'You said: `%s`' % event['message']['text']
    else:
        return None

    return {'text': text}
