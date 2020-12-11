#
# voice-skill-sdk
#
# (C) 2020, Florian Lueffe, Deutsche Telekom AG
#
# This file is distributed under the terms of the MIT license.
# For details see the file LICENSE in the top directory.
#
#
from skill_sdk import skill, Response, tell
from skill_sdk.l10n import _

import requests


@skill.intent_handler('TEAM_41_WHISPER')
def handler() -> Response:
    """ Handler for Warehouse Wispher

    :return:        Response
    """
    try:
        # Gets data from SAP Cloud Platform
        response = requests.get('https://mvconnector.cfapps.eu10.hana.ondemand.com/product/Schuhe%20Groesse%2043', timeout=10)
        response.raise_for_status()
        data = response.json()
        # Get the info from json
        # How to dynamically get this?
        amount = data[0]['AMOUNT']
        # output
        if amount >= 1:
            msg = _('WW_AVAILABLE', amount=amount)
        else:
            msg = _('WW_NOT_AVAILABLE')
    except requests.exceptions.RequestException as err:
        msg = _('HELLOAPP_REQUEST_ERROR', err=err)

    # We create a response with either joke or error message
    return tell(msg)
