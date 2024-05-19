<h1 align="center">Melon RagGPT</h1>
<p align="center"><i>Loved the project? Please visit CloudMelon's <a href="https://github.com/cloudmelon">Github profile</a></i></p>
<br>

### Introduction

Melon RagGPT is a private AI chatbot, and it can be deployed in Containers and Kubernetes for entreprise-grade scale. This is part of POV (proof of concept) for iMelonArt's AI MVP. 


### Setup Python virtual environment

Set up a virtual environment (optional):

```
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```shell
pip install -r requirements.txt
```

Pull the model you'd like to use:

```
ollama pull llama3
```

### How to use it 

Ingest file in the `source_document` folder

```shell
python ingest.py
```
Lauch `melonRagGPT` using the following command : 

```shell
python melonRagGPT.py
```

## Detailed instructions

Find detailed instructions in this blog post :
[How I built a LLM-based Private AI for FREE in Docker Containers ](https://cloudmelonvision.com/how-i-built-a-llm-based-private-ai-for-free-in-docker-containers/)


## Supported document formats

Put any and all your files into the `source_documents` directory. The sample documents are : 
1. NVIDIA'S cloud-native and AI strategy - video source : https://youtu.be/KrmqURibQB8
2. Will AI Robots take over our jobs in 5 years ? - video source : https://youtu.be/ag-Vgwg1m8I

The supported extensions are:

- `.csv`: CSV,
- `.docx`: Word Document,
- `.doc`: Word Document,
- `.enex`: EverNote,
- `.eml`: Email,
- `.epub`: EPub,
- `.html`: HTML File,
- `.md`: Markdown,
- `.msg`: Outlook Message,
- `.odt`: Open Document Text,
- `.pdf`: Portable Document Format (PDF),
- `.pptx` : PowerPoint Document,
- `.ppt` : PowerPoint Document,
- `.txt`: Text file (UTF-8),

# Authors

Contributors names and contacts

- Github profile [here](https://github.com/cloudmelon)
- Twitter [@MelonyQ](https://twitter.com/melonyq)
- Blog [CloudMelon Vis](https://cloudmelonvision.com)
- Youtube[ CloudMelon Vis](https://www.youtube.com/@CloudMelonVis?sub_confirmation=1)

# Contribute

This is an updated RAG Private GPT version by cloudmelon. Credits for PrivateGPT goes to Iván Martínez who is the original creator, and you can find his GitHub repo [here](https://github.com/imartinez/privateGPT). 


Contributions are always welcome! Please create a PR to add Github Profile.

## License

This project is licensed under [MIT](https://opensource.org/licenses/MIT) license.

## Show your support

Give a ⭐️ if this project helped you!