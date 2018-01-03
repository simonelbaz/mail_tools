from icalendar import Calendar, Event, vCalAddress
import icalendar.prop
from datetime import datetime
from pytz import UTC # timezone
import logging, argparse
import logging.handlers, logging.config


parser = argparse.ArgumentParser(description='CSV to VCF')
parser.add_argument('--data')
parser.add_argument('--output')
parser.add_argument('--user')
args = parser.parse_args()

dataProcess=args.data
userMail=args.user
outputDirectory=args.output

g = open(dataProcess + userMail + "@stif.info.ics")
g_idf = open(outputDirectory + userMail + "@iledefrance-mobilites.fr.ics", "w")

gcal = Calendar.from_ical(g.read())
for component in gcal.walk():
    if component.name == "VEVENT":
        #print(component.get('summary'))
        #print(component.get('organizer').property_items())
        #print(component.property_items())
        #print(component.to_ical().splitlines())
        #print(component.to_ical().splitlines())
        #print(component['organizer'].params)
        organizer_params = component['organizer'].params
        #print(organizer_params)
        #print(component.get('organizer').replace('@stif.info','@iledefrance-mobilites.fr'))
        component['organizer'] = vCalAddress(component.get('organizer').replace('@stif.info','@iledefrance-mobilites.fr'))
#	for i in organizer_params.keys():
#		component['organizer'].params[i] = organizer_params[i]
        component['organizer'].params = organizer_params
        #print(component['organizer'])
        #print(component['organizer'].params)
        #print(component['organizer'].params)
        #print(component.get('organizer'))
        #print(component.get('attendee'))
        if type(component.get('attendee')) is list:
		attendees_tab_stif = [] + component['attendee']
	else:
		attendees_tab_stif = [component['attendee']]
	nbAttendees = len(component['attendee'])
	i=0
	#while i < nbAttendees:
	print attendees_tab_stif
	attendees_tab = []
	for aCalAttendee in attendees_tab_stif:
		#print(aCalAttendee)
		#aCalAddress = vCalAddress(component['attendee'][i].replace('@stif.info','@iledefrance-mobilites.fr'))
		#print(aCalAttendee)
		aCalAddress = vCalAddress(aCalAttendee.replace('@stif.info','@iledefrance-mobilites.fr'))
		#if hasattr(component['attendee'][i], 'params'):
		if hasattr(aCalAttendee, 'params'):
			attendees_params = aCalAttendee.params
			#print(attendees_params)
			aCalAddress.params = attendees_params
		attendees_tab.append(aCalAddress)
		i=i+1
	component['attendee'] = attendees_tab
        #print(component.get('attendee'))

g_idf.write(gcal.to_ical())
g_idf.close()
g.close()
