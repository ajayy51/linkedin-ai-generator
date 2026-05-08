async function generatePost() {

  const topic =
    document.getElementById("topic").value

  if (!topic) {
    alert("Please enter a topic")
    return
  }

  const loading =
    document.getElementById("loading")

  const preview =
    document.getElementById("preview")

  loading.classList.remove("hidden")
  preview.classList.add("hidden")

  setTimeout(() => {

    const fakePost = `
🚀 Understanding ${topic}

${topic} is transforming how AI systems work.

Instead of relying only on model memory,
modern AI applications combine:

✅ Retrieval
✅ Context injection
✅ Semantic search
✅ LLM reasoning

This creates more accurate,
scalable, and production-ready AI systems.

The future of AI apps is RAG-powered.

#AI #RAG #LLM #MachineLearning
`

    const image =
      `https://image.pollinations.ai/prompt/${encodeURIComponent(topic + " AI futuristic linkedin post")}`

    document.getElementById(
      "preview-post"
    ).innerText = fakePost

    document.getElementById(
      "preview-image"
    ).src = image

    loading.classList.add("hidden")
    preview.classList.remove("hidden")

  }, 1500)
}

document
  .getElementById("publish-btn")
  .addEventListener("click", () => {

    alert(
      "LinkedIn publishing will be added next"
    )

})