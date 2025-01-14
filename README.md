# Chat with PDF using Gemini

Picture this: You’ve got a stack of PDFs. You’re short on time. But you desperately need answers, fast and with as little friction as possible. **Enter this project**—a friendly Streamlit-powered app that lets you upload multiple PDFs, automatically builds a FAISS vector store for semantic search, and then leverages **Google’s Gemini LLM** to answer your burning questions about your documents. No more frantic scrolling or keyword searching!

---

## Why This Project?

Sometimes, you only need that **one golden piece of information** hidden deep in a PDF. Don’t waste hours combing through pages. Let the app do the work for you:

- **Save Time**: Quickly extract and query multiple PDFs in minutes.
- **AI-Powered**: Google’s Gemini LLM delivers context-aware answers.
- **User-Friendly**: Streamlit makes the interface super approachable—no complicated setups.

---

## Why Use a Retrieval-Augmented Generation (RAG) Model?

Simply having access to data isn’t enough—you need to extract meaningful insights efficiently. This is where **Retrieval-Augmented Generation (RAG)** models shine. Here’s why we chose to integrate a RAG model in this application:

- **Enhanced Accuracy**: By combining information retrieval with language generation, RAG models ensure that the answers provided are both relevant and contextually accurate, minimizing the chances of incorrect or hallucinated responses.
  
- **Efficient Handling of Large Documents**: PDFs can be extensive and contain vast amounts of information. RAG leverages FAISS to perform semantic searches, allowing the application to quickly locate and reference the most pertinent sections of the text.
  
- **Context-Aware Responses**: Traditional Q&A systems may struggle with maintaining context over long passages. RAG models maintain a strong understanding of the context, providing more coherent and precise answers.
  
- **Scalability**: As the volume of uploaded PDFs grows, the RAG framework ensures that the system remains scalable, efficiently managing and querying large datasets without compromising performance.

- **Versatility**: Whether you're analyzing academic papers, business reports, or technical documentation, the RAG model adapts to different types of content, providing reliable answers across various domains.

By integrating RAG, this application not only retrieves relevant information from your PDFs but also synthesizes it into meaningful, easy-to-understand responses, making your interaction with documents seamless and productive.

---

## Prerequisite Dependencies

- **Python 3.10+** (recommended for best compatibility)
- **LangChain** + **LangChain-Community** (provides FAISS support)
- **PyPDF2** (grabs text from your uploaded PDFs)
- **Google Generative AI** (`google-generativeai` library)
- **Streamlit** (for a delightful web UI)
- **Docker** (if you’d like to containerize the entire shebang)

Install everything with a single command:

```bash
pip install -r requirements.txt
```

To let Gemini do its magic, you need to supply your Gemini API key. Create a .env file (or set an environment variable) like so:

```bash
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Keep this key safe and private—it’s basically your VIP pass to the model!

## How to Use

1. **Upload PDFs**: Drag-and-drop or select multiple PDFs.
2. **Hit “Submit & Process”**: This step harnesses FAISS to build an index from your PDFs’ text.
3. **Ask Your Question**: Type in a question about the PDFs’ content.
4. **Get Your Answer**: Gemini reads the index, figures out the context, and provides a concise answer.

**Example**:

- Uploaded an eBook on data science? Ask, “What’s the difference between supervised and unsupervised learning?”
- The app fetches the relevant sections from the PDF and seamlessly generates an answer.
- Uploaded an eBook on data science? Ask, “What’s the difference between supervised and unsupervised learning?”
- The app fetches the relevant sections from the PDF and seamlessly generates

## Docker Setup

If you’re a container enthusiast:

1. Build the image:

    ```bash
    docker build -t chat-with-pdf .
    ```

2. Run the container:

    ```bash
    docker run -p 8501:8501 chat-with-pdf
    ```

3. Open your browser: Visit `localhost:8501` and start chatting with your PDFs.

## Main Features

- **PDF Upload & Processing**: Simple interface to upload as many PDFs as you want.
- **FAISS Vector Store**: Embeds and indexes your text for lightning-fast semantic search.
- **Google Gemini Integration**: An advanced LLM that formulates human-like, context-aware answers.
- **User-Friendly UI**: Streamlit ensures minimal friction in usage—no complicated CLI tools required.

## Contribution

We welcome contributors of all backgrounds—whether you’re a seasoned developer or a curious beginner!
1. **Fork this repo**: Make it your own.
2. **Create a new branch**: Work on new features or squash pesky bugs.
3. **Submit a Pull Request**: Share your awesome ideas with the community.
4. **Test, Test, Test**: Please ensure everything runs smoothly before sending in your PR.


## License

We want everyone to benefit from this tool! It’s licensed under the MIT License. Feel free to modify and distribute under the same terms.

Now, enjoy discovering knowledge hidden in your PDFs—without the hassle of sifting through endless pages.

Happy querying!
