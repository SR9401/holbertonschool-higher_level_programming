import re


def generate_invitations(template, attendees):
    # verification type des parametres
    if not isinstance(template, str):
        raise TypeError('template muste be a str')

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict)
                                                  for attendee in attendees):
        raise TypeError('attendees must be a dict')

    if template is None:
        print('template must be not empty')
        return
    if attendees is None:
        print('attendees must be not empty')
        return

    def replace_placeholders(template, attendees):
        templa = template
        placeholders = re.findall(r'\{(\w+)\}', template)
        for key in placeholders:

            value = attendees.get(key, "N/A")
            templa = templa.replace(f"{{{key}}}", value)
            return templa

    for index, attendee in enumerate(attendees, start=1):
        processed_template = replace_placeholders(template, attendee)
        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(processed_template)
