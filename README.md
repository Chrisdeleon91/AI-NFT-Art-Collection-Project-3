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

### Resources:
- https://docs.openzeppelin.com/
- https://docs.alchemy.com/docs/nft-project-code-templates

### Instructions

1. Run DALL_E_3_API.py in a terminal after adding your API key (needs an active subscription) and editing prompts
   
3. Deploy Smart Contract on Remix IDE, follow video, "1. deploying smart contract on remix ide.mp4":
   - Connect MetaMask account via "Injected Provider - MetaMask"
   
[![Video 1](https://github.com/Chrisdeleon91/AI-NFT-Art-Collection-Project-3/assets/22796940/1eb92477-8945-441b-9404-f5d17fa67dfb)](https://www.youtube.com/watch?v=4eIgUi2RgRo "Video 1")

2. Launch React Ethereum dapp, follow video, "2. launching react etheruem dApp.mp4":
   - Create a Ganache workspace
   - commands:
   - Git Bash into "NFT Marketplace" folder, or cd into this directory in your terminal of choose
   - activate conda dev environment, "conda activate dev" in terminal
   - Optional: typing in "npx hardhat node " will give test accounts if needed (Skipping this step is okay)
   - type " npx hardhat run scripts/deploy.js --network ganache"
   - type "npm start"

[![Video 2](https://github.com/Chrisdeleon91/AI-NFT-Art-Collection-Project-3/assets/22796940/b7183d8f-09a9-4d14-9aae-93e88323e232)](https://www.youtube.com/watch?v=0cLeM9Q-NNM "Video 2")

3. Interacting with NFT Marketplace, follow video, "3.NFT Markplace list, sell and buy demo.mp4":
   - Go into your browser of choose and open the local host address (http://localhost:3000/)
     
[![Video 3](https://github.com/Chrisdeleon91/AI-NFT-Art-Collection-Project-3/assets/22796940/8bd87b2e-55b6-4d48-bebd-3e5ef532002e)](https://www.youtube.com/watch?v=Xn2e7hKJZdM "Video 3")

4. Optional: Using OpenSea Testnet, follow video, "4. OpenSea testnet demo.mkv":

[![Video 4](https://github.com/Chrisdeleon91/AI-NFT-Art-Collection-Project-3/assets/22796940/a0463ee2-f3bc-4a74-88a5-d10e34c24d27)](https://www.youtube.com/watch?v=3nxnQBoH5zE "Video 4")

![Picture](https://www.columbia.edu/content/themes/custom/columbia/assets/img/cu-header.svg)
