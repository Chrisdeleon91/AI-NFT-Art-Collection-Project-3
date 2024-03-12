# AI-NFT-Art-Collection-Project-3

## How to use
Follow instructions at bottom of page
##
### Authors: Christopher De Leon, Mike West, Daniyar Mussin

### Introduction

* **System Design & Architecture**: To be led by Christopher, outlining the main components of the NFT marketplace system and how they will interact.

* **Art Development**:  Daniyar will design the NFT's using ChatGPT's API function to create collections of art using prompt engineering.

* **Interface Design**: Mike will take the helm in designing a sleek, intuitive, and interactive interface using Plotty Express, ensuring the system is user-friendly and efficient.

* **Integration & Testing**: The team will collaborate in this final phase to integrate all system components to ensure full functionality.
  
### Research Questions
**Our research questions are as follows**:
* Can we build a local NFT marketplace from what we learned in class?
* How can we enhance the functionality and visual aesthetic over using Streamlit?
* Can we implement Chat GPT's generative image AI into creating an art collection for us?

### Libraries and tools used
We will use the following in our project:
* Remix IDE (to launch smart contract)
* React (Javascript)
* Hardhat (to connect to network)
* Alchemy
* OpenAI library (ChatGPT)
* Flask
* Piñata (to upload your data to IPFS)
* Metamask
* Ganache

### Overview of Tasks
* Generating Images
* Integrating 
* Visualization
* Integration

### Instructions

1. Run DALL_E_3_API.py in a terminal after adding your API key (needs an active subscription) and editing prompts
   
3. Deploy Smart Contract on Remix IDE, follow video, "1. deploying smart contract on remix ide.mp4":
   Connect MetaMask account via "Injected Provider - MetaMask"
[![Video 1](https://github.com/Chrisdeleon91/AI-NFT-Art-Collection-Project-3/assets/22796940/b2300173-20f0-4cd2-998f-891ca57f5609)](https://www.youtube.com/watch?v=4eIgUi2RgRo "Video 1")

2. Launch React Ethereum dapp, follow video, "2. launching react etheruem dApp.mp4":
   - Create a Ganache workspace
   - commands:
   - Git Bash into "NFT Marketplace" folder, or cd into this directory in your terminal of choose
   - activate conda dev environment, "conda activate dev" in terminal
   - Optional: typing in "npx hardhat node " will give test accounts if needed (Skipping this step is okay)
   - type " npx hardhat run scripts/deploy.js --network ganache"
   - type "npm start"
[![Video 2](https://github.com/Chrisdeleon91/AI-NFT-Art-Collection-Project-3/assets/22796940/4eb29299-9d48-4d96-b0c3-ca3b8f6101a6)](https://www.youtube.com/watch?v=0cLeM9Q-NNM "Video 2")


3. Interacting with NFT Marketplace, follow video, "3.NFT Markplace list, sell and buy demo.mp4":
   - Go into your browser of choose and open the local host address (http://localhost:3000/)
[![Video 3](https://github.com/Chrisdeleon91/AI-NFT-Art-Collection-Project-3/assets/22796940/7814ed4b-c5a4-4845-ac5c-f1ba02c8726f)](https://www.youtube.com/watch?v=Xn2e7hKJZdM "Video 3")

4. Optional: Using OpenSea Testnet, follow video, "4. OpenSea testnet demo.mkv":
[![Video 4](https://github.com/Chrisdeleon91/AI-NFT-Art-Collection-Project-3/assets/22796940/53f9c0be-97ae-4db3-a95c-dca4c5057fb7)]([https://www.youtube.com/watch?v=Xn2e7hKJZdM](https://www.youtube.com/watch?v=3nxnQBoH5zE) "Video 4")

hardhat config
https://docs.openzeppelin.com/ for smart contract
-find openzeppelin functions used/ and look in tutorial for further explainatations



![Picture](https://www.columbia.edu/content/themes/custom/columbia/assets/img/cu-header.svg)
