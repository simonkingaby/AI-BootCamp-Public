"""
 This code sample demonstrates an implementation of the Lex Code Hook Interface
 in order to serve a bot which manages dentist appointments.
 Bot, Intent, and Slot models which are compatible with this sample can be found in the Lex Console
 as part of the 'MakeAppointment' template.

 For instructions on how to set up and test this bot, as well as additional samples,
 visit the Lex Getting Started documentation http://docs.aws.amazon.com/lex/latest/dg/getting-started.html.
"""

import json
import dateutil.parser
import datetime
import time
import os
import math
import random
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


""" --- Helpers to build responses which match the structure of the necessary dialog actions --- """


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message, response_card):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message,
            'responseCard': response_card
        }
    }


def confirm_intent(session_attributes, intent_name, slots, message, response_card):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ConfirmIntent',
            'intentName': intent_name,
            'slots': slots,
            'message': message,
            'responseCard': response_card
        }
    }


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response


def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }


def build_response_card(title, subtitle, options):
    """
    Build a responseCard with a title, subtitle, and an optional set of options which should be displayed as buttons.
    """
    buttons = None
    if options is not None:
        buttons = []
        for i in range(min(5, len(options))):
            buttons.append(options[i])

    return {
        'contentType': 'application/vnd.amazonaws.card.generic',
        'version': 1,
        'genericAttachments': [{
            'title': title,
            'subTitle': subtitle,
            'buttons': buttons
        }]
    }


def parse_int(n):
    try:
        return int(n)
    except ValueError:
        return float('nan')


def try_ex(func):
    """
    Call passed in function in try block. If KeyError is encountered return None.
    This function is intended to be used to safely access dictionary.

    Note that this function would have negative impact on performance.
    """

    try:
        return func()
    except KeyError:
        return None


def get_slot_value(slots, slot_name, default_value):
    if slot_name in slots:
        if slots[slot_name] == None:
            return default_value
        else:
            return slots[slot_name]['value']['interpretedValue']
    else:
        raise("Slot Name Incorrect")


""" --- Helper Functions --- """


""" --- Functions that control the bot's behavior --- """


def roll_dice(intent_request):
    """
    Performs dialog management and fulfillment for rolling the dice

    Beyond fulfillment, the implementation for this intent demonstrates the following:
    1) Use of elicitSlot in slot validation and re-prompting
    2) Use of confirmIntent to support the confirmation of inferred slot values, when confirmation is required
    on the bot model and the inferred slot values fully specify the intent.
    """
    
    # Log the entire intent request
    logging.debug(f"Intent:\n{intent_request}")
    
    session = intent_request['sessionState']
    intent = session['intent']
    slots = intent['slots']
    
    # Log the slot values
    logging.debug(f'Slots: {slots}')
    
    # Parse the slot values
    no_of_dice = parse_int(get_slot_value(slots, "NumberOfDice", 1))
    number_of_sides = get_slot_value(slots, "NumberOfSides", 'six')
    plus_minus = get_slot_value(slots, "PlusOrMinus", 'plus')
    modifier = parse_int(get_slot_value(slots, "Modifier", 0))
    
    side_options = {'two':2,'three':3,'four':4,'six':6,'eight':8,'ten':10,'twelve':12,'twenty':20, 'one-hundred':100}
    no_of_sides = side_options[number_of_sides]
    
    
    # Roll the Dice.  In a real bot, this would likely involve a call to a backend service.
    sum_rolls = 0
    rolls = []
    for n in range(no_of_dice):
        roll = random.randrange(no_of_sides)+1
        sum_rolls += roll
        rolls.append(roll)
    if plus_minus == 'plus':
        sum_rolls += modifier
    else:
        sum_rolls -= modifier

    intent['state'] = 'Fulfilled'
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
                'content': f'I rolled {rolls}. For a total of: {sum_rolls}.'
            }
        ]
    }
    

""" --- Intents --- """

def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    # logger.debug('dispatch intentName={}'.format(intent_request['currentIntent']['name']))
    
    logger.debug(f'Intent Request {intent_request}')
    
    intent_name = intent_request['sessionState']['intent']['name']
    
    # Dispatch to your bot's intent handlers
    if intent_name == 'RollDice':
        return roll_dice(intent_request)
    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))

    return dispatch(event)
