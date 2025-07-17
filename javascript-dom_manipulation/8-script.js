const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
			.then(data => {
			document.getElementById('hello').textContent = data.hello;

			})
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });