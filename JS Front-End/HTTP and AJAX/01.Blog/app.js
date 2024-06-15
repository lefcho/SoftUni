function attachEvents() {
    const postsURL = 'http://localhost:3030/jsonstore/blog/posts';
    const commentsURL = 'http://localhost:3030/jsonstore/blog/comments';

    const postsSelectElement = document.getElementById('posts');
    const getPostsButton = document.getElementById('btnLoadPosts');
    const viewButton = document.getElementById('btnViewPost');
    const postTitleElement = document.getElementById('post-title');
    const postTextElement = document.getElementById('post-body');
    const listCommentElement = document.getElementById('post-comments');

    getPostsButton.addEventListener('click', () => {
        postsSelectElement.innerHTML = '';

        fetch(postsURL)
            .then(response => response.json())
            .then(posts => {
                Object.values(posts)
                    .forEach(post => {
                        const optionElement = document.createElement('option');
                        optionElement.value = post.id;  
                        optionElement.textContent = post.title;

                        postsSelectElement.appendChild(optionElement);
                    })
            })
            .catch(() => console.log('posts not loaded'));
    })

    viewButton.addEventListener('click', () => {
        listCommentElement.innerHTML = '';
        const postID = postsSelectElement.value;
        
        fetch(`${postsURL}/${postID}`)
            .then(res => res.json())
            .then(post => {
                postTitleElement.textContent = post.title;
                postTextElement.textContent = post.body;
            })
            .catch(() => console.log('posts not loaded'));

        fetch(commentsURL)
            .then(response => response.json())
            .then(comments => {
                Object.values(comments)
                    .forEach(comment => {
                        if (comment.postId === postID) {
                            const liElement = document.createElement('li');
                            liElement.id = comment.id;
                            liElement.textContent = comment.text;
                            listCommentElement.appendChild(liElement);
                        }
                    })
            })
            .catch(() => console.log('comments not loading'));
    })
}

attachEvents();