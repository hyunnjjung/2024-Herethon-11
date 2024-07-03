// script.js

//localStorage.clear();
let posts = JSON.parse(localStorage.getItem("posts")) || [];
let currentPostId = localStorage.getItem("currentPostId");

function savePosts() {
  localStorage.setItem("posts", JSON.stringify(posts));
}

function addPost() {
  const tag = document.getElementById("new-post-tag").value;
  const title = document.getElementById("new-post-title").value;
  const content = document.getElementById("new-post-content").value;

  if (title && content) {
    const newPost = {
      id: posts.length + 1,
      tag: tag,
      title: title,
      content: content,
      comments: [],
    };

    posts.push(newPost);
    savePosts();
    document.getElementById("new-post-tag").value = "";
    document.getElementById("new-post-title").value = "";
    document.getElementById("new-post-content").value = "";
    localStorage.setItem("currentPostId", newPost.id);
    location.href = "post-detail.html";
  }
}

function renderPostList() {
  const postList = document.getElementById("post-list");
  if (!postList) return;

  postList.innerHTML = "";

  posts.forEach((post) => {
    const postElement = document.createElement("div");
    postElement.className = "post";
    postElement.innerHTML = `
            <h4><strong></strong> ${post.tag}</h4>
            <h2 onclick="viewPost(${post.id})">${post.title}</h2>
            <h5><strong>댓글</strong> ${post.comments.length}</h5>
            <p><strong></strong> ${post.content}</p>
        `;
    postList.appendChild(postElement);
  });
}

function viewPost(id) {
  localStorage.setItem("currentPostId", id);
  location.href = "post-detail.html";
}

function renderPostDetail() {
  if (!currentPostId) return;

  const post = posts.find((p) => p.id === parseInt(currentPostId));

  if (post) {
    document.getElementById("post-tag").innerText = post.tag;
    document.getElementById("post-title").innerText = post.title;
    document.getElementById("post-content").innerText = post.content;

    const commentsDiv = document.getElementById("comments");
    commentsDiv.innerHTML = "";

    post.comments.forEach((comment) => {
      const commentElement = document.createElement("p");
      commentElement.innerText = comment;
      commentsDiv.appendChild(commentElement);
    });
  }
}

function addComment() {
  const commentContent = document.getElementById("new-comment-content").value;

  if (commentContent) {
    const post = posts.find((p) => p.id === parseInt(currentPostId));
    post.comments.push(commentContent);
    savePosts();
    document.getElementById("new-comment-content").value = "";
    renderPostDetail();
  }
}

// 페이지 로드 시 초기화
if (document.getElementById("post-list")) {
  renderPostList();
} else if (document.getElementById("post-title")) {
  renderPostDetail();
}
