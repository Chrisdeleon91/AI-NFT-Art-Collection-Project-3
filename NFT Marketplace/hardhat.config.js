require("@nomiclabs/hardhat-waffle");
require("@nomiclabs/hardhat-ethers");
const fs = require('fs');
// const infuraId = fs.readFileSync(".infuraid").toString().trim() || "";

task("accounts", "Prints the list of accounts", async (taskArgs, hre) => {
  const accounts = await hre.ethers.getSigners();

  for (const account of accounts) {
    console.log(account.address);
  }
});

module.exports = {
  defaultNetwork: "hardhat",
  networks: {
    hardhat: {
      //chainId: 1337
	  chainId: 5777 //copied network id from ganache
    },
    mumbai: {
      url: `https://polygon-mumbai.g.alchemy.com/v2/nAhiCHKvZkhkp4A7PkkCIBON0-BXW26d`,
      //accounts: [process.env.privateKey]
    },
    ganache: {
      url: "HTTP://127.0.0.1:7545",
      accounts: [
        `4271da57a37987aaef759e9fc0e5ec787af1342d4533c0070b69ad162b87cf95`,
      ],
    },
	sepolia: {
      url: "https://eth-sepolia.g.alchemy.com/v2/gpCApOSP6lRt0nterMcmDb50oJTYD20U",
      accounts: [ "4271da57a37987aaef759e9fc0e5ec787af1342d4533c0070b69ad162b87cf95" ],
      chainId: 11155111 //added line
    }
//    goerli: {
//      url: process.env.REACT_APP_ALCHEMY_API_URL,
//      accounts: [ process.env.REACT_APP_PRIVATE_KEY ]
//    }
  },
  solidity: {
    version: "0.8.4",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  }
};