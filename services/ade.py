import zoneinfo

import requests
from ics import Calendar


def extract_teacher_name_from_text(text, teacher_list):
    """
    Extract the teacher name from a text
    :param text: text to extract the teacher name from
    :param teacher_list: list of teachers
    :return: the teacher name or ' - - - ' if not found
    """
    for teacher in teacher_list:
        if teacher in text:
            return teacher
    return (' - - - ')


def get_events_from_ade(url, teacher_list, day):
    """
    Get the events from an ics file (at the url) and return a list of events
    :param url: url of the ics file
    :param teacher_list: list of teachers
    :param day: day to get the events from
    :return: list of events for the day (start, end, title, teacher)
    """
    tz_UTC = zoneinfo.ZoneInfo('UTC')
    tz_FR = zoneinfo.ZoneInfo('Europe/Paris')

    calendar = Calendar(requests.get(url).text)
    ade_events = []
    for event in calendar.events:
        if event.begin.date() == day:
            ade_events.append({'start': event.begin.datetime.replace(tzinfo=tz_UTC).astimezone(tz_FR).time().isoformat(
                timespec='minutes'),
                'end': event.end.datetime.replace(tzinfo=tz_UTC).astimezone(tz_FR).time().isoformat(timespec='minutes'),
                'title': event.name, 'teacher': extract_teacher_name_from_text(event.description, teacher_list)})
    ade_events.sort(key=lambda x: x['start'])
    return ade_events
