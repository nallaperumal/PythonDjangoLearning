function showAlert() {
    alert("Button clicked!");
}

function fetchtop3Movies(){
    fetch('http://127.0.0.1:8000/api/movies/top_3_movies/')
    .then(resp => resp.json())
    .then(movJson => { console.log(movJson); PopulateMovies(movJson); });
}

function PopulateMovies(movies) {
     const movieContainer = document.getElementById('movie-list');
     movieContainer.innerHTML = ''; // Clear previous content

     movies.forEach(movie => {
         const movieCard = document.createElement('div');
          movieCard.innerHTML = `
            <div class="product-title">${movie.name}</div>
            <div class="product-info">Language: ${movie.lang}</div>
            <div class="product-info">Year: ${movie.year_of_release}</div>
            <div class="product-price">IMDB Rating: ${movie.imdb_rating}</div>
            <button class="buy-btn" onclick="showAlert()">Book ticket</button>
        `;
        movieContainer.appendChild(movieCard);
     });
}
