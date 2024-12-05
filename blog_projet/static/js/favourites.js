document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.favorite-button');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const postId = button.getAttribute('data-post-id');
            const isFavorite = button.getAttribute('data-favorite') === 'true';

            fetch(`/post/${postId}/toggle_favorite/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json',
                },
            })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'added') {
                        button.textContent = '★';
                        button.setAttribute('data-favorite', 'true');
                    } else if (data.status === 'removed') {
                        button.textContent = '☆';
                        button.setAttribute('data-favorite', 'false');
                    }
                });
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
