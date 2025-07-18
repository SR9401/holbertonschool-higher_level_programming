import re

def generate_invitations(template, attendees):
    try:
        # Vérification des types des paramètres
        if not isinstance(template, str):
            print('Erreur: template doit être une chaîne de caractères.')
            return

        if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
            print('Erreur: attendees doit être une liste de dictionnaires.')
            return

        if not template.strip():
            print('Template is empty, no output files generated.')
            return

        if not attendees:
            print('No data provided, no output files generated.')
            return

        def replace_placeholders(template, attendee):
            try:
                templa = template
                placeholders = re.findall(r'\{(\w+)\}', template)
                for key in placeholders:
                    value = attendee.get(key, "N/A")
                    templa = templa.replace(f"{{{key}}}", value)
                return templa
            except Exception as e:
                print(f"Une erreur s'est produite lors du remplacement des placeholders : {e}")
                return template  # Retourne le template inchangé en cas d'erreur

        for index, attendee in enumerate(attendees, start=1):
            try:
                processed_template = replace_placeholders(template, attendee)
                filename = f"output_{index}.txt"
                with open(filename, 'w') as file:
                    file.write(processed_template)
            except IOError as e:
                print(f"Erreur lors de l'écriture dans le fichier {filename} : {e}")
            except Exception as e:
                print(f"Une erreur inattendue s'est produite : {e}")

    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
