const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                const characterName = data.name;
                document.getElementById('character').textContent = characterName;
            })
            .catch(error => {
                // Gérer les erreurs éventuelles
                console.error('There was a problem with the fetch operation:', error);
            });